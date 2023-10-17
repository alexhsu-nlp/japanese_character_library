# Original simple and messy code not fit for current use
import re
from pathlib import Path
from typing import List, Set
import itertools


class HuriganaCorpusProcessor:

    def __init__(self, eng_ignore: bool = False) -> None:
        self._pattern = re.compile(
            "行番号: +[0-9]+\t\t\n(.*?)\t\t\[入力文\]\n\t(.*?)\t\[入力 読み\]\n((?:(?!行番号: [0-9]+).+\n)+)", re.MULTILINE)
        self._token_pattern = re.compile(
            "([^\t\n]*)\t([^\t\n]*)\t([^\t\n(:?分かち書き)]*)\t*\n")
        self._encoding = "utf-8"
        self._word_types: Set[str] = set()
        self.eng_ignore = eng_ignore

    def read_file(self, path: Path) -> List[SentenceInfo]:
        print(path)
        sentence_list: List[SentenceInfo] = []
        text = path.read_text(encoding=self._encoding)
        for sentence, sentence_pronunciation, token_text in self._pattern.findall(string=text):
            tokens: List[Word] = []
            prev = ""
            eng_wordtype = False
            for writing, sound, wordtype in self._token_pattern.findall(string=token_text):
                assert wordtype != "分かち書き"
                if self.eng_ignore and wordtype == "英文字":
                    eng_wordtype = True
                    break
                word, bl = self.get_word(writing, sound, wordtype, prev)
                if not bl:
                    print(sentence)
                    print(token_text)
                    print(self._token_pattern.findall(string=token_text))
                tokens.append(word)
                if word.writing == "":
                    prev = ""
                else:
                    prev = word.writing[-1]
            if eng_wordtype:
                continue
            writing = "".join([token.writing if not (token.wordtype == "英文字" and i+1 < len(tokens)
                              and tokens[i+1].wordtype == "英文字") else token.writing + " " for i, token in enumerate(tokens)])
            sentence_list.append(SentenceInfo(writing=writing,
                                              sound=sentence_pronunciation, tokens=tokens))
        return sentence_list

    def get_word(self, writing: str, sound: str, wordtype: str, prev: str):
        self._word_types.add(wordtype)
        if wordtype == "漢字":
            word = KanjiWord(writing=writing, sound=sound,
                             prev=prev, wordtype=wordtype)
            word.set_kanji_dict(KANJIDIC2_DICT)
            return word, True
        elif wordtype in ("ひらがな", "カタカナ"):
            return KanaWord(writing=writing, sound=sound, wordtype=wordtype), True
        else:
            if "-" in writing and wordtype != "記号":
                print("- warning!!!")
                print("writing:", writing)
                print("sound:", sound)
                print("wordtype:", wordtype)
                print("prev:", prev)
                return Word(writing=writing, sound=sound, wordtype=wordtype), False
            return Word(writing=writing, sound="", wordtype=wordtype), True

    def read_files(self, paths: List[Path]) -> List[SentenceInfo]:
        self.sentence_list = list(itertools.chain.from_iterable(
            [self.read_file(path) for path in paths]))
        print(self._word_types)
        return self.sentence_list
