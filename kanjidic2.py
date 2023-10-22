from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence, Set, Optional
from kana.kanas import KANA_DICT, Hiragana, Katakana, Gyou, Dan, Kana, JapaneseCharacter, SUTEGANAS, JapaneseUnit
from kana.morastr import MoraStr, SequenceContainer
from kana.str2mora import str2morastr

# TODO: incorporate Yomis into Kanjis

# Needs refactoring the ideas


@dataclass
class JapaneseCharRecord:
    surface: str
    inner: JapaneseUnit  # JointKanjiJukugo or Mora (normalized)
    pron: MoraStr  # this pron is unique, NOT A SET
    strict: bool  # whether the pronunciation has basis


class JapaneseCharRecordStr(SequenceContainer):
    # NOTE: a class similar to MoraStr
    # This will be the output of the program
    # TODO: two kanji one yomi??? do I need kanjistr?
    def __init__(self, container: Sequence[JapaneseCharRecord]) -> None:
        super().__init__(container)


@dataclass(frozen=True)
class JointKanjiJukugo(JapaneseUnit):
    # Idea: call the characters (kanas, suteganas, symbols) characters, and call combined ones (moras, etc.) `units`
    symbol: str
    pron: MoraStr


@dataclass
class Kanji(JapaneseCharacter):
    symbol: str
    yomi: Yomi

# def safetyinnerwrapper_str2kana(kana: Union[Kana, str]):
#     if isinstance(kana, str):
#         assert kana in KANA_DICT
#         kana = KANA_DICT[kana]
#     return kana

# TODO: this idea is still not mature


class Yomi:

    @property
    def pron_set(self) -> Set[MoraStr]:
        raise NotImplementedError


@dataclass
class KanjiDic2Yomi(Yomi):
    # TODO: replace these with hiraganas!!!
    # TODO: what about "-"?
    main: MoraStr

    def __str__(self):
        return str(self.main)

    # def gen_dakuonize(self) -> KanjiDic2Yomi:
    #     # TODO: 'gen' not done
    #     # TODO: put prev into sth different?
    #     # TODO: type(self)?
    #     return KanjiDic2Kunyomi(main=self.main.dakuonize(), tail=self.tail)


# def str2kanastr(string: str) -> MoraStr:
#     str_ind = 0
#     len_str = len(string)
#     kanas = []
#     while str_ind < len_str:
#         if str_ind + 1 < len_str and string[str_ind + 1] in SUTEGANAS:
#             kana_str = string[str_ind: str_ind + 2]
#             str_ind += 2
#         else:
#             kana_str = string[str_ind]
#             str_ind += 1
#         kanas.append(KANA_DICT[kana_str])
#     return MoraStr(kanas=kanas)


def kanjidic2_kunyomistr2obj(kunyomi_str: str):
    # TODO: need to redesign
    # this is different
    as_prefix = as_suffix = False
    if kunyomi_str.startswith('-'):
        as_suffix = True
        kunyomi_str = kunyomi_str[1:]
    elif kunyomi_str.endswith('-'):
        as_prefix = True
        kunyomi_str = kunyomi_str[-1:]
    dot_split = kunyomi_str.split('.')
    if len(dot_split) == 1:
        dot_split.append('')
    assert len(dot_split) == 2
    main_kanastr = str2morastr(string=dot_split[0])
    tail_kanastr = str2morastr(string=dot_split[1])
    if len(tail_kanastr) != 0 and tail_kanastr[-1].dan == KANA_DICT['う']:
        return KanjiDic2KunyomiVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)
    return KanjiDic2KunyomiNonVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)


@dataclass
class KanjiDic2Kunyomi(KanjiDic2Yomi):
    # NOTE: this is only for one listed kunyomi (a kanji may have multiples), rather than their aggregrates
    as_prefix: bool = False
    as_suffix: bool = False
    tail: Optional[MoraStr] = None  # TODO: None or empty? now empty

    def __str__(self):
        if self.tail is None:
            return str(self.main)
        return str(self.main + self.tail)

    def __str__(self):
        if self.tail is not None:
            # TODO: self.tail should be MoraStr
            tail_part = '.' + self.tail
        else:
            tail_part = ''
        return f"{'-' if self.as_suffix else ''}{self.main}{tail_part}{'-' if self.as_prefix else ''}"

    @property
    def pos(self):
        # TODO: since divide them below into specific classes, no need to do this?
        pass

    @property
    def normal(self) -> MoraStr:
        if self.tail is None:
            return self.main
        return self.main + self.tail

    # @property
    # def pron_set(self) -> Set[MoraStr]:
    #     # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
    #     raise NotImplementedError


@dataclass
class KanjiDic2KunyomiVerb(KanjiDic2Kunyomi):
    # TODO: middle Japanese verbs
    # TODO: put middle and modern under the same verb
    # TODO: how to deal with `as_prefix` and `as_suffix`

    def __post_init__(self):
        assert self.tail is not None

    def is_godan(self) -> bool:
        return not self.is_ichidan()

    def is_ichidan(self) -> bool:
        return len(self.tail) >= 2 and self.tail[-1].sutegana is None and self.tail[-1].kana.symbol == KANA_DICT['る'] and self.tail[-2].dan.symbol in ('え', 'い')

    @property
    def renyou(self) -> MoraStr:
        # TODO: make this a yomi?
        # TODO: new idea: make this under MoraStr???
        # Ans: sorry you do not know where is the main where is the others
        if self.is_ichidan():
            return self.main + self.tail[:-1]
        return self.main + self.tail.change_end_dan(dan='い')

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        min_set = {self.normal, self.renyou, self.main}
        for element in list(min_set):
            min_set.add(element.dakuonize())
        return min_set


@dataclass
class KanjiDic2KunyomiNonVerb(KanjiDic2Kunyomi):
    # either 名詞 形容詞(`.い`, `.しい`) or 形容動詞

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        return {self.main, self.main.dakuonize(), self.normal, self.main.dakuonize(), self.main.handakuonize(), self.normal.handakuonize()}


@dataclass
class KanjiDic2Onyomi(KanjiDic2Yomi):

    def __str__(self):
        return self.main

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        return {self.main, self.main.dakuonize(), self.main.sokuonize(), self.main.dakuonize().sokuonize(), self.main.handakuonize(), self.main.handakuonize().sokuonize()}


class KanjiDic2Nanori(KanjiDic2Yomi):

    @property
    def pron_set(self) -> Set[MoraStr]:
        return {self.main, self.main.dakuonize()}


@dataclass
class KanjiDic2KanjiCollectedYomi(Yomi):
    # TODO: should i get rid of the list?
    # TODO: transform when appropriate or in advance?
    # TODO: set or list?
    kunyomi_verbs: List[KanjiDic2KunyomiVerb]
    kunyomi_nonverbs: List[KanjiDic2KunyomiNonVerb]
    onyomis: List[KanjiDic2Onyomi]
    nanoris: List[KanjiDic2Nanori]

    def __post_init__(self):
        self._yomis_all: List[KanjiDic2Yomi] = self.kunyomi_verbs + \
            self.kunyomi_nonverbs + self.onyomis + self.nanoris

    @property
    def pron_set(self) -> Set[MoraStr]:
        pron_set: Set[MoraStr] = set()
        for verb in self._yomis_all:
            pron_set.union(verb.pron_set)
        return pron_set

# # TODO: 3. problem of changing sound in onyomi [3 possible sounds] [ki.ku.ti.tu] [hatuonbin]
# # TODO: 4. problem of changing sound in kunyomi
