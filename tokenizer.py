"""
script for developing tokenizer-related functions and classes
"""

from pathlib import Path
from konoha import WordTokenizer
from konoha.word_tokenizers.mecab_tokenizer import parse_feature_for_unidic
from konoha.word_tokenizers.tokenizer import BaseTokenizer
from konoha.data.token import Token
from flair.embeddings import OneHotEmbeddings
import fugashi
from typing import List, Tuple
import jaconv

COMMON_EXCEPTIONS = {
    "ハ": "ワ",
    "ヲ": "オ",
    "ヘ": "エ",
}


def unidic_pron_transform(feature):
    # print("in transform")
    pron = feature.pron
    form = feature.form
    # if pron == form == "*":
    #     # print("****success")
    #     return ""
    if pron is None and form is None:
        return None
    elif not (pron is not None and form is not None):
        raise ValueError(f"unknown case in transform: {pron}, {form}")
    # print(pron, form)
    new_pron = ""
    for char1, char2 in zip(pron, form):
        # print(char1, char2)
        if char1 == char2 or char2 in ('ヅ', 'ヂ') or char2 in COMMON_EXCEPTIONS:
            # print('first case')
            new_pron += char1
        elif (char1 == "ー" and char2 != "ー"):
            # print('second case')
            new_pron += char2
        else:
            print(f"unknown case in transform: {pron}, {form}")
            with open('errors.txt', 'a', encoding='utf-8') as f:
                f.write(
                    f"P: {feature}\n")
            return None
            # raise ValueError(f"unknown case in transform: {pron}, {form}")
    # print("new:", new_pron)
    return jaconv.kata2hira(new_pron)


def parse_fugashi_node(node: fugashi.fugashi.UnidicNode):
    """Convert fugashi node to konoha Token form"""
    feature = node.feature
    # print(feature)
    return Token(
        surface=node.surface,
        postag=feature.pos1,
        postag2=feature.pos2,
        postag3=feature.pos3,
        postag4=feature.pos4,
        inflection=feature.cType,
        conjugation=feature.cForm,
        # to make same as hurigana standard!
        pron=unidic_pron_transform(feature)
    )


class MecabUnidicTokenizer(BaseTokenizer):
    """konoha WordTokenizer utilizing fugashi tokenizer (wrapper for MeCab)"""

    def __init__(self) -> None:
        super().__init__(name="mecab_fugashi")
        self.tagger = fugashi.Tagger()

    def tokenize(self, text: str) -> List[Token]:
        raw_tokens = self.tagger(text)
        tokens = [parse_fugashi_node(raw_token)
                  for raw_token in raw_tokens]
        return tokens


class NagisaTokenizer(BaseTokenizer):

    def __init__(self) -> None:
        super().__init__(name="nagisa")
        self.tagger = WordTokenizer(tokenizer="nagisa")

    def tokenize(self, text: str) -> List[Token]:
        return self.tagger.tokenize(text=text)
        # return super().tokenize(text)


def unzip_token_fields(tokens: List[Token]) -> Tuple[List[str]]:
    # TODO: maintain inflection and conjucation???
    # print('token list:', tokens)
    return (
        [token.surface for token in tokens],
        [token.postag if token.postag is not None else '*' for token in tokens],
        [token.postag2 if token.postag2 is not None else '*' for token in tokens],
        [token.postag3 if token.postag3 is not None else '*' for token in tokens],
        [token.postag4 if token.postag4 is not None else '*' for token in tokens],
        [token.pron if token.pron is not None else '*' for token in tokens],
        # [token.inflection for token in tokens],
        # [token.conjugation for token in tokens],
    )


FUGASHI_FEATURE_FILE_PATH = Path("./fugashi_feature_corpus.txt")


def get_fugashi_features(path: Path, encoding='utf-8'):
    # TODO: seems not needed
    text = path.read_text(encoding=encoding)
    for line in text.split('\n'):
        pos_list = line.split()[0].split('-')
        print(pos_list)