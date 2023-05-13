from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence
from kana import KANA_DICT, Hiragana, Katakana, Gyou, Dan, Kana, JapaneseCharacter, SUTEGANAS


def safetyinnerwrapper_str2kana(kana: Union[Kana, str]):
    if isinstance(kana, str):
        assert kana in KANA_DICT
        kana = KANA_DICT[kana]
    return kana


class KanaStr:
    # TODO: frozen instance?

    def __init__(self, kanas: Sequence[Kana]) -> None:
        self.kanas = tuple(kanas)

    def __str__(self) -> str:
        return "".join(map(lambda kana: kana.symbol, self.kanas))

    def __len__(self) -> int:
        return len(self.kanas)

    def __eq__(self, other) -> bool:
        assert isinstance(other, KanaStr)
        return self.kanas == other.kanas

    def __getitem__(self, key):
        return self.kanas[key]

    def add(self, kana: Union[Kana, str]) -> KanaStr:
        kana = safetyinnerwrapper_str2kana(kana)
        return KanaStr(kanas=self.kanas+(kana,))

    def extend(self, kanastr: KanaStr) -> None:
        # TODO: support string?
        return KanaStr(kanas=self.kanas+kanastr.kanas)

    def startswith_kana(self):
        pass

    def endswith_kana(self, kana: Union[Kana, str]):
        # TODO: support KanaStr and relaxed init
        kana = safetyinnerwrapper_str2kana(kana)
        return self.kanas[-1] == kana

    def dakuonize(self) -> KanaStr:
        # TODO: good to be present here? (seems y!)
        assert len(self) > 0
        return KanaStr(kanas=[self.kanas[0].dakuon]+self.kanas[1:])

    def sukuonize(self) -> KanaStr:
        assert len(self) > 0
        # TODO: not done yet
        last_kana = self.kanas[-1]
        if last_kana.sukuonizable():
            # TODO: this is only hiragana!!!
            return KanaStr(kanas=self.kanas[:-1] + [KANA_DICT['っ']])
        return self


# @dataclass
# class KanjiDic2KanjiYomi:
#     kanji: str
#     onyomis: List[KanaStr]
#     kunyomis: List[KanaStr] # TODO: error!!!
#     nanoris: List[KanaStr]

#     def __post_init__(self):
#         self.valid_onyomis = self._get_valid_onyomis()
#         self.valid_kunyomis = self._get_valid_kunyomis()
#         self.valid_yomis = self.valid_onyomis.union(self.valid_kunyomis)

#     def _get_valid_onyomis(self):
#         valid_onyomis = []
#         for onyomi in self.onyomis:
#             valid_onyomis.append(onyomi)
#             if len(onyomi) > 1 and onyomi.endswith(('く', 'き', 'ち', 'つ')):
#                 valid_onyomis.append(onyomi[:-1]+'っ')
#             valid_onyomis.extend(self._dakuonize(onyomi))
#         return set(valid_onyomis)

#     def _get_valid_kunyomis(self):
#         valid_kunyomis = []

#         for kunyomi in self.kunyomis:
#             kunyomi = kunyomi.replace("-", "")
#             if "." in kunyomi:
#                 assert kunyomi.count(".") == 1
#                 splits = kunyomi.split('.')
#                 valid_kunyomis.append(splits[0])
#                 valid_kunyomis.append(splits[0]+splits[1])
#                 valid_kunyomis.extend(self._dakuonize(splits[0]))
#                 full_dakuon = self._dakuonize(splits[0]+splits[1])
#                 valid_kunyomis.extend(full_dakuon)
#                 for dakuon in full_dakuon:
#                     valid_kunyomis.extend(self._verb_nominalize(dakuon))
#                 valid_kunyomis.extend(
#                     self._verb_nominalize(splits[0]+splits[1]))
#             else:
#                 valid_kunyomis.append(kunyomi)
#                 valid_kunyomis.extend(self._dakuonize(kunyomi))
#         valid_kunyomis.extend(self.nanoris)
#         for nanori in self.nanoris:
#             valid_kunyomis.extend(self._dakuonize(nanori))
#         return set(valid_kunyomis)

#     def _dakuonize(self, hiragana: str) -> List[str]:
#         # same as pronunciation standard in dataset
#         PREV_DAKUON_DICT = {
#             'ti': ['zi'],
#             'tu': ['zu'],
#             'ty': ['zy'],
#         }
#         DAKUON_DICT = {
#             'k': ['g'],
#             't': ['d'],
#             'h': ['p', 'b'],  # TODO: true?
#             's': ['z'],
#             'o': ['no'],
#             'e': ['ne'],
#             'i': ['mi'],
#         }
#         yomis = []
#         romaji = jaconv.kana2nihonshiki(hiragana)
#         # if self.kanji == '柱':
#         #     print(romaji)
#         if romaji.startswith(tuple(PREV_DAKUON_DICT.keys())):
#             for dakuon in PREV_DAKUON_DICT[romaji[:2]]:
#                 dakuon_romaji = dakuon + romaji[2:]
#                 # if self.kanji == '柱':
#                 #     print(dakuon_romaji)
#                 #     print(jaconv.nihonshiki2kana(dakuon_romaji))
#                 yomis.append(jaconv.nihonshiki2kana(dakuon_romaji))
#         elif romaji.startswith(tuple(DAKUON_DICT.keys())):
#             for dakuon in DAKUON_DICT[romaji[0]]:
#                 dakuon_romaji = dakuon + romaji[1:]
#                 # if self.kanji == '柱':
#                 #     print(dakuon_romaji)
#                 #     print(jaconv.nihonshiki2kana(dakuon_romaji))
#                 yomis.append(jaconv.nihonshiki2kana(dakuon_romaji))
#         return yomis

#     def _verb_nominalize(self, hiragana: str) -> List[str]:
#         """change a wago verb form to its noun form"""
#         # print("nomialize:", hiragana)
#         romaji = jaconv.kana2nihonshiki(hiragana)
#         yomis = []
#         if romaji.endswith("u"):
#             noun_romaji = romaji[:-1] + "i"
#             yomis.append(jaconv.nihonshiki2kana(noun_romaji))
#         if romaji.endswith(("eru", "iru")):
#             # print("TRUE")
#             yomis.append(hiragana[:-1])
#         return yomis

# TODO: this idea is still not mature


@dataclass
class KanjiDic2Yomi:
    # TODO: replace these with hiraganas!!!
    # TODO: what about "-"?
    main: KanaStr
    tail: KanaStr

    def __str__(self):
        return self.main + self.tail

    @property
    def pron(self):
        return self.main + self.tail

    def gen_dakuonize(self) -> KanjiDic2Yomi:
        # TODO: 'gen' not done
        # TODO: put prev into sth different?
        # TODO: type(self)?
        return KanjiDic2Kunyomi(main=self.main.dakuonize(), tail=self.tail)


def str2kanastr(string: str) -> KanaStr:
    str_ind = 0
    len_str = len(string)
    kanas = []
    while str_ind < len_str:
        if str_ind + 1 < len_str and string[str_ind + 1] in SUTEGANAS:
            kana_str = string[str_ind: str_ind + 2]
            str_ind += 2
        else:
            kana_str = string[str_ind]
            str_ind += 1
        kanas.append(KANA_DICT[kana_str])
    return KanaStr(kanas=kanas)


def kanjidic2_kunyomistr2obj(kunyomi_str: str):
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
    main_kanastr = str2kanastr(string=dot_split[0])
    tail_kanastr = str2kanastr(string=dot_split[1])
    if len(tail_kanastr) != 0 and tail_kanastr[-1].dan == KANA_DICT['う']:
        return KanjiDic2KunyomiVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)
    return KanjiDic2KunyomiNonVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)


@dataclass
class KanjiDic2Kunyomi(KanjiDic2Yomi):
    as_prefix: bool = False
    as_suffix: bool = False

    def __str__(self):
        if self.tail:
            tail_part = '.' + self.tail
        else:
            tail_part = ''
        return f"{'-' if self.prev_hyphen else ''}{self.main}{tail_part}{'-' if self.post_hyphen else ''}"

    def pos(self):
        pass

    @property
    def pron_set(self) -> set:
        pass


class KanjiDic2KunyomiVerb(KanjiDic2Kunyomi):

    def is_godan(self) -> bool:
        return not self.is_ichidan()

    def is_ichidan(self) -> bool:
        return len(self.tail) >= 2 and self.tail[-1] == KANA_DICT['る'] and self.tail[-2].dan in (KANA_DICT['え'], KANA_DICT['い'])

    def noun(self):
        pass


class KanjiDic2KunyomiNonVerb(KanjiDic2Kunyomi):
    pass


class KanjiDic2Onyomi(KanjiDic2Yomi):

    def __str__(self):
        return self.main + self.tail

    def sukuonize(self):
        pass


class KanjiDic2Nanori(KanjiDic2Yomi):
    pass


@dataclass
class KanjiDic2KanjiYomiInfo:
    # TODO: should i get rid of the list?
    # TODO: transform when appropriate or in advance?
    # TODO: set or list?
    kunyomis: List[KanjiDic2Kunyomi]
    onyomis: List[KanjiDic2Onyomi]
    nanoris: List[KanjiDic2Nanori]

# # TODO: 3. problem of changing sound in onyomi [3 possible sounds] [ki.ku.ti.tu] [hatuonbin]
# # TODO: 4. problem of changing sound in kunyomi
