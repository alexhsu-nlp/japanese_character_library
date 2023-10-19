# -*- coding: utf-8 -*-
"""
This is a file for building kana-related classes and functions from scratch aiming to replace the modified jaconv and revising the corresponding code in `kanji.py`.
The number of suteganas in One youon kana is at most one.
"""
from __future__ import annotations
from collections import defaultdict
import numpy as np
from functools import cached_property
from typing import List, Tuple, Dict, Optional
from kana import const
from kana.exceptions import SyllableError
from dataclasses import dataclass
# from const import HIRAGANAS, KATAKANAS, const.DAKUON_MAP, DAKUON_REV_MAP, HIRA_SPECIAL_READINGS, KATA_SPECIAL_READINGS, HIRA_HATSUON


class Character:
    # TODO: this may incorporate characters in other languages?
    pass


class JapaneseCharacter(Character):
    # TODO: this may be combined with Kanji
    # TODO: how to define them? what about e.g. numerals, English words, punctuation marks?
    pass


def is_same_type(kana1: BaseKana, kana2: BaseKana):
    return (kana1.is_hiragana() and kana2.is_hiragana()) or (kana1.is_katakana() and kana2.is_katakana())


@dataclass
class Syllable(JapaneseCharacter):
    # core idea: a syllable consists of a kana and an optional sutegana; if the sutegana is "None", then blablabla
    # TODO: if you adopt this, then you need to face わぁぁぁあ
    # idea:
    # in analyzing sentence, if after taking
    # TODO: check kana dan and sutegana: must be different
    kana: Kana
    sutegana: Sutegana
    # TODO: sutegana needs to have an original
    # TODO: distinguish katakana and hiragana suteganas
    # NOTE: Syllable is ALWAYS SHORT (no long syllables)

    def __post__init__(self):
        if self.kana.dan != self.sutegana:
            raise SyllableError(
                f"Illegal syllable as the main kana\'s dan, '{self.kana.dan}', does not fit with sutegana '{self.sutegana}'.")
        assert is_same_type(self.kana, self.sutegana)

    def __repr__(self):
        return f'Syllable<{str(self)}>'

    def __str__(self):
        return self.kana.symbol + self.sutegana.symbol
    
    @property
    def pron(self):
        # TODO: pron of katakanas and kanjis and etc. together?
        pass

    @property
    def dakuon(self):
        #TODO: I think this is overly costly
        return Syllable(kana=self.kana.dakuon, sutegana=self.sutegana)
    
    def check(self):
        return is_same_type(self.kana, self.sutegana)


class Kanji(JapaneseCharacter):
    pass


class BaseKana:

    def __init__(self, symbol: str):
        self.symbol: str = symbol
        self._is_dakuon = False
        # self.base_romaji = romaji

    @property
    def pron(self) -> Kana:
        raise NotImplementedError

    @property
    def handakuon(self) -> Kana:
        raise NotImplementedError

    @cached_property
    def dakuon_pron(self) -> Kana:
        return self.dakuon.pron

    def __repr__(self) -> str:
        return f"Kana<{self.symbol}>"
    
    def is_hiragana(self) -> bool:
        return False

    def is_katakana(self) -> bool:
        return False
    

    # def to_romaji(self) -> Romaji:
    #     # TODO: 3 kinds
    #     pass


class Sutegana(BaseKana):

    def __init__(self, symbol: str):
        self.symbol = symbol
    
    # TODO: in fact nothing can be done about this?
    # @property
    # def pron(self) -> Kana:
    #     return super().pron

class SuteganaHira(Sutegana):
    
    def is_hiragana(self) -> bool:
        return True

class SuteganaKata(Sutegana):
    
    def is_katakana(self) -> bool:
        return True


class Kana(BaseKana):

    def __init__(self, symbol: str, gyou: Gyou, dan: Dan):
        super().__init__(symbol=symbol)
        self.gyou: Gyou = gyou
        self.dan: Dan = dan
        # the `_pron_str` is to make sure that the `pron` property can be loaded later
        self._pron_str: str = ""
        # gyoudan_dict is for searching a kana with Gyou and Dan
        # at present it is only used for dauon [if no other uses, why not delete it?]
        self._gyoudan_dict_index: Optional[int] = None

    @cached_property
    def pron(self) -> Kana:
        # pron_str = HIRA_SPECIAL_READINGS.get(self.symbol, self.symbol)
        if self._pron_str == "":
            # TODO: this may not be a good idea
            # TODO: convert katakana to hiragana
            # thus it seems that suteganas need to be objectized
            return self
        return kana_dict[self._pron_str]

    @cached_property
    def dakuon(self) -> Kana:
        if self._gyoudan_dict_index is None:
            # TODO: this may be erratic
            return self
            # raise NotImplementedError
        return kana_gyoudan_dict[self.gyou.dakuon.symbol, self.dan.symbol][self._gyoudan_dict_index]

    

    # def is_hatsuon(self) -> bool:
    #     return False

    def sukuonizable(self) -> bool:
        return False


class Dan(BaseKana):
    # The default symbol of a dan is a hiragana

    def __init__(self, symbol: str) -> None:
        super().__init__(symbol)

    def __repr__(self) -> str:
        return f"Dan<{self.symbol}>"

    def __eq__(self, other) -> bool:
        # TODO: is this enough? or: self is other?
        return isinstance(other, Dan) and other.symbol == self.symbol


class Gyou(BaseKana):
    # The default symbol of a Gyou is a hiragana

    def __init__(self, symbol: str) -> None:
        self.symbol: str = symbol
        self._is_dakuon: bool = symbol in const.DAKUON_REV_MAP
        self._dakuon: str = const.DAKUON_MAP.get(self.symbol, self.symbol)

    def __repr__(self) -> str:
        return f"Gyou<{self.symbol}>"

    @property
    def dakuon(self) -> Kana:
        return kana_dict[self._dakuon]

    def __eq__(self, other) -> bool:
        # TODO: is this enough? or: self is other?
        return isinstance(other, Gyou) and other.symbol == self.symbol

    # def generate_hiragana(self, hiragana_symbol: str, katakana_symbol: str, dan: Dan) -> Hiragana:
    #     return Hiragana(kana_symbol=hiragana_symbol, katakana_symbol=katakana_symbol, gyou=self, dan=dan)


class Hiragana(Kana):

    def __init__(self, kana_symbol: str, katakana_symbol: str, gyou: Gyou, dan: Dan) -> None:
        super().__init__(kana_symbol, gyou=gyou, dan=dan)
        self._katakana: str = katakana_symbol
        self._pron_str: str = const.HIRA_SPECIAL_READINGS.get(
            self.symbol, self.symbol)
        self._gyoudan_dict_index: Optional[int] = 0

    @property
    def katakana(self) -> Katakana:
        return kana_dict[self._katakana]

    def is_hiragana(self) -> bool:
        return True

    def __eq__(self, other):
        return isinstance(other, Hiragana) and self.symbol == other.symbol


class Katakana(Kana):

    def __init__(self, kana_symbol: str, hiragana_symbol: str, gyou: Gyou, dan: Dan) -> None:
        super().__init__(kana_symbol, gyou=gyou, dan=dan)
        self._hiragana: str = hiragana_symbol
        self._pron_str: str = const.KATA_SPECIAL_READINGS.get(
            self.symbol, self.symbol)
        self._gyoudan_dict_index: Optional[int] = 1

    @property
    def hiragana(self) -> Hiragana:
        return kana_dict[self._hiragana]

    def is_katakana(self) -> bool:
        return True


class KanaParser:
    pass


hiraganas = np.array(const.HIRAGANAS)
katakanas = np.array(const.KATAKANAS)
print(hiraganas.shape)
print(katakanas.shape)
assert hiraganas.shape == katakanas.shape
m, n = hiraganas.shape

# Initialize dictionaries
kana_dict: Dict[str, Kana] = {}
kana_gyoudan_dict: defaultdict[Tuple[str, str], List[Kana]] = defaultdict(list)

# Add primitive gojuuons
for i in range(m):
    gyou = Gyou(symbol=hiraganas[i][0])
    for j in range(n):
        dan = Dan(symbol=hiraganas[0][j])
        if hiraganas[i][j] is not None:
            hiragana = Hiragana(
                hiraganas[i][j], katakana_symbol=katakanas[i][j], gyou=gyou, dan=dan)
            kana_dict[hiraganas[i][j]] = hiragana
            kana_gyoudan_dict[(hiragana.gyou.symbol,
                               hiragana.dan.symbol)].append(hiragana)
        if katakanas[i][j] is not None:
            katakana = Katakana(
                katakanas[i][j], hiragana_symbol=katakanas[i][j], gyou=gyou, dan=dan)
            kana_dict[katakanas[i][j]] = katakana
            kana_gyoudan_dict[(katakana.gyou.symbol,
                               katakana.dan.symbol)].append(katakana)


# Assign 'ん'
NONE_GYOU = Gyou(symbol='N')
NONE_DAN = Dan(symbol='N')

kana_dict[const.HIRA_HATSUON] = Hiragana(
    kana_symbol=const.HIRA_HATSUON, katakana_symbol=const.KATA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

kana_dict[const.KATA_HATSUON] = Katakana(
    kana_symbol=const.KATA_HATSUON, hiragana_symbol=const.HIRA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

NONE_KANA = Kana(symbol="N", gyou=NONE_GYOU, dan=NONE_DAN)

kana_dict["N"] = NONE_KANA

kana_gyoudan_dict['N', 'N'] = [NONE_KANA, NONE_KANA]

# final constants needed for other use

KANA_DICT: Dict[str, Kana] = kana_dict
SUTEGANAS = tuple(const.HIRA_YOUON_MAP.keys()) + tuple(const.HIRA_ADD_YOUONS.keys()) + \
    tuple(const.KATA_YOUON_MAP.keys()) + tuple(const.KATA_ADD_YOUONS.keys())

nn = KANA_DICT['ん']


print(nn.dan)
print(nn.gyou)
print(nn.symbol)
print(nn.pron)
# print(nn.hatsuon)


def char2kana(char: str) -> Kana:
    assert len(char) == 1
    return KANA_DICT[char]


def youon_loading(table_str_tuple: Tuple[str, ...], is_kata=True):
    # TODO: at present it only supports or
    for kana_str in table_str_tuple:
        print(kana_str)
        assert len(kana_str) == 2
        if kana_str[1] in const.KATA_YOUON_MAP:
            # the case for true youons
            gyou = KANA_DICT[kana_str[0]].gyou
        else:
            # TODO: katakana or hiragana
            # NOTE: in this case these gyous have the same dakuon, which is true for these special gairaigo syllabaries
            gyou = Gyou(symbol=kana_str[0])
        dan = Dan(symbol=const.KATA_ADD_YOUONS[kana_str[1]])
        KANA_DICT[kana_str] = Katakana(
            kana_symbol=kana_str, hiragana_symbol="", gyou=gyou, dan=dan)


youon_loading(const.KATA_FOREIGN_YOUON_TABLE1)

youon_loading(const.KATA_FOREIGN_YOUON_TABLE2)

# Assign dakuons
for kana in kana_dict.values():
    if kana.gyou.symbol in const.DAKUON_MAP:
        kana._is_dakuon = False
        for dakuon_kana in kana_gyoudan_dict[(const.DAKUON_MAP[kana.gyou.symbol], kana.dan.symbol)]:
            if isinstance(dakuon_kana, type(kana)):
                kana._dakuon = dakuon_kana
    elif kana.gyou.symbol in const.DAKUON_REV_MAP:
        kana._is_dakuon = True
        kana._dakuon = kana
    else:
        kana._is_dakuon = False
        kana._dakuon = kana

# def analyze_bikana(bikana_str: str) -> Kana:
#     # In fact the length of kana can be more than 2; consider the case 'わぁぁぁぁあ': it may cause word delimination problems
#     # TODO: what about はっ
#     assert len(bikana_str) == 2
#     head, vowel = bikana_str
#     # TODO: note katakana and hiragana
#     assert head in KANA_DICT
#     head_kana = KANA_DICT[head] if head in const.abnormal_katakanas else KANA_DICT[head].dan
#     return Kana(symbol=bikana_str, gyou=Gyou(symbol=head_kana), dan=Dan(symbol=dan_kana))
