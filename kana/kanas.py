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
# from const import HIRAGANAS, KATAKANAS, const.DAKUON_MAP, DAKUON_REV_MAP, HIRA_SPECIAL_READINGS, KATA_SPECIAL_READINGS, HIRA_HATSUON


class Character:
    # TODO: this may incorporate characters in other languages?
    pass


class JapaneseCharacter(Character):
    # TODO: this may be combined with Kanji
    # TODO: how to define them? what about e.g. numerals, English words, punctuation marks?
    pass


class Kanji(JapaneseCharacter):
    pass


class BaseKana(JapaneseCharacter):

    def __init__(self, symbol: str):
        self.symbol: str = symbol
        self._is_dakuon = False
        self._has_youon = False
        # self.base_romaji = romaji

    @property
    def pron(self) -> Kana:
        raise NotImplementedError

    @property
    def dakuon(self) -> Kana:
        raise NotImplementedError

    @property
    def handakuon(self) -> Kana:
        raise NotImplementedError

    @cached_property
    def dakuon_pron(self) -> Kana:
        return self.dakuon.pron

    def __repr__(self) -> str:
        return f"Kana<{self.symbol}>"

    # def to_romaji(self) -> Romaji:
    #     # TODO: 3 kinds
    #     pass


class Kana(BaseKana):

    def __init__(self, symbol: str, gyou: Gyou, dan: Dan):
        super().__init__(symbol=symbol)
        self.gyou: Gyou = gyou
        self.dan: Dan = dan
        # the `_pron_str` is to make sure that the `pron` property can be loaded later
        self._pron_str: str = ""
        self._gyoudan_dict_index: Optional[int] = None

    @cached_property
    def pron(self) -> Kana:
        # pron_str = HIRA_SPECIAL_READINGS.get(self.symbol, self.symbol)
        if self._pron_str == "":
            # TODO: this may not be a good idea
            return self
        return kana_dict[self._pron_str]

    @cached_property
    def dakuon(self) -> Kana:
        if self._gyoudan_dict_index is None:
            raise NotImplementedError
        return kana_gyoudan_dict[self.gyou.dakuon.symbol, self.dan.symbol][self._gyoudan_dict_index]

    def is_hiragana(self) -> bool:
        return False

    def is_katakana(self) -> bool:
        return False

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


class Gyou(BaseKana):
    # The default symbol of a Gyou is a hiragana

    def __init__(self, symbol: str) -> None:
        self.symbol: str = symbol
        self._is_dakuon: bool = symbol in const.DAKUON_REV_MAP
        self._has_youon: bool = False
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

# Assign dakuons
for kana in kana_dict.values():
    if kana.gyou.symbol in const.DAKUON_MAP:
        kana._is_dakuon = False
        for dakuon_kana in kana_gyoudan_dict[(const.DAKUON_MAP[kana.gyou.symbol], kana.dan)]:
            if isinstance(dakuon_kana, type(kana)):
                kana._dakuon = dakuon_kana
    elif kana.gyou.symbol in const.DAKUON_REV_MAP:
        kana._is_dakuon = True
        kana._dakuon = kana
    else:
        kana._is_dakuon = False
        kana._dakuon = kana

# Assign 'ん'
NONE_GYOU = Gyou(symbol='N')
NONE_DAN = Dan(symbol='N')

kana_dict[const.HIRA_HATSUON] = Hiragana(
    kana_symbol=const.HIRA_HATSUON, katakana_symbol=const.KATA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

kana_dict[const.KATA_HATSUON] = Katakana(
    kana_symbol=const.KATA_HATSUON, hiragana_symbol=const.HIRA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

NONE_KANA = Kana(symbol="N", gyou=NONE_GYOU, dan=NONE_DAN)

kana_dict["N"] = NONE_KANA

kana_gyoudan_dict['N', 'N'] = [NONE_KANA]

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


def foreign_youon_loading(table_str_tuple: Tuple[str, ...]):
    # TODO: at present it only supports or
    for kana_str in table_str_tuple:
        assert len(kana_str)
        if kana_str[1] in const.KATA_YOUON_MAP:
            gyou = KANA_DICT[kana_str[0]].gyou
        else:
            # TODO: katakana or hiragana
            gyou = Gyou(symbol=kana_str[0])
        dan = Gyou(symbol=kana_str[1])
        KANA_DICT[kana_str] = Katakana(
            kana_symbol=kana_str, hiragana_symbol="", gyou='', dan='')


# def analyze_bikana(bikana_str: str) -> Kana:
#     # In fact the length of kana can be more than 2; consider the case 'わぁぁぁぁあ': it may cause word delimination problems
#     # TODO: what about はっ
#     assert len(bikana_str) == 2
#     head, vowel = bikana_str
#     # TODO: note katakana and hiragana
#     assert head in KANA_DICT
#     head_kana = KANA_DICT[head] if head in const.abnormal_katakanas else KANA_DICT[head].dan
#     return Kana(symbol=bikana_str, gyou=Gyou(symbol=head_kana), dan=Dan(symbol=dan_kana))
