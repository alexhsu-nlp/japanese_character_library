# -*- coding: utf-8 -*-
"""
This is a file for building kana-related classes and functions from scratch aiming to replace the modified jaconv and revising the corresponding code in `kanji.py`.
The number of suteganas in One youon kana is at most one.
"""
from __future__ import annotations
from collections import defaultdict
import numpy as np
from functools import cached_property
from typing import List, Tuple, Dict
# from kana_const import HIRAGANAS, KATAKANAS, DAKUON_MAP, DAKUON_REV_MAP

HIRAGANAS = (
    ('あ', 'い', 'う', 'え', 'お'),
    ('か', 'き', 'く', 'け', 'こ'),
    ('さ', 'し', 'す', 'せ', 'そ'),
    ('た', 'ち', 'つ', 'て', 'と'),
    ('な', 'に', 'ぬ', 'ね', 'の'),
    ('は', 'ひ', 'ふ', 'へ', 'ほ'),
    ('ま', 'み', 'む', 'め', 'も'),
    ('や', None, 'ゆ', None, 'よ'),
    ('ら', 'り', 'る', 'れ', 'ろ'),
    ('わ', 'ゐ', None, 'ゑ', 'を'),
    ('が', 'ぎ', 'ぐ', 'げ', 'ご'),
    ('ざ', 'じ', 'ず', 'ぜ', 'ぞ'),
    ('だ', 'ぢ', 'づ', 'で', 'ど'),
    ('ば', 'び', 'ぶ', 'べ', 'ぼ'),
    ('ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'),
)

HIRA_SPECIAL_READINGS = {
    'ぢ': 'じ',
    'づ': 'ず',
}
KATA_SPECIAL_READINGS = {
    'ヂ': 'ジ',
    'ヅ': 'ズ',
}

HIRA_HATSUON = 'ん'
KATA_HATSUON = 'ン'

KATAKANAS = (
    ('ア', 'イ', 'ウ', 'エ', 'オ'),
    ('カ', 'キ', 'ク', 'ケ', 'コ'),
    ('サ', 'シ', 'ス', 'セ', 'ソ'),
    ('タ', 'チ', 'ツ', 'テ', 'ト'),
    ('ナ', 'ニ', 'ヌ', 'ネ', 'ノ'),
    ('ハ', 'ヒ', 'フ', 'ヘ', 'ホ'),
    ('マ', 'ミ', 'ム', 'メ', 'モ'),
    ('ヤ', None, 'ユ', None, 'ヨ'),
    ('ラ', 'リ', 'ル', 'レ', 'ロ'),
    ('ワ', 'ヰ', None, 'ヱ', 'ヲ'),
    ('ガ', 'ギ', 'グ', 'ゲ', 'ゴ'),
    ('ザ', 'ジ', 'ズ', 'ゼ', 'ゾ'),
    ('ダ', 'ヂ', 'ヅ', 'デ', 'ド'),
    ('バ', 'ビ', 'ブ', 'ベ', 'ボ'),
    ('パ', 'ピ', 'プ', 'ペ', 'ポ'),
)


HIRA_YOUON_MAP = {
    'ゃ': 'や', 
    'ゅ': 'ゆ', 
    'ょ': 'よ',
}
KATA_YOUON_MAP = {
    'ャ': 'や', 
    'ュ': 'ゆ', 
    'ョ': 'よ',
}
HIRA_ADD_YOUONS = ('ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ')
KATA_ADD_YOUONS = ('ァ', 'ィ', 'ゥ', 'ェ', 'ォ')
HIRA_SOKUON = 'っ'
KATA_SOKUON = 'ッ'


DAKUON_MAP = {
    'か': 'が',
    'さ': 'ざ',
    'た': 'だ',
    'は': 'ば',
}
DAKUON_REV_MAP = dict(map(reversed, DAKUON_MAP.items()))

HANDAKUON_MAP = {
    'は': 'ぱ'
}
HanDAKUON_REV_MAP = dict(map(reversed, HANDAKUON_MAP.items()))


class JapaneseCharacter:
    # TODO: this may be combined with Kanji
    pass


class BaseKana(JapaneseCharacter):

    def __init__(self, symbol: str):
        self.symbol = symbol
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
        self.gyou = gyou
        self.dan = dan
        self._pron_str = ""
        self._gyoudan_dict_index = None

    @cached_property
    def pron(self) -> Kana:
        # pron_str = HIRA_SPECIAL_READINGS.get(self.symbol, self.symbol)
        if self._pron_str == "":
            raise NotImplementedError
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

    def is_hatsuon(self) -> bool:
        return False

    def sukuonizable(self) -> bool:
        return False


class Dan(BaseKana):

    def __init__(self, symbol: str) -> None:
        super().__init__(symbol)

    def __repr__(self) -> str:
        return f"Dan<{self.symbol}>"


class Gyou(BaseKana):

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self._is_dakuon = symbol in DAKUON_REV_MAP
        self._has_youon = False
        self._dakuon = DAKUON_MAP.get(self.symbol, self.symbol)

    def __repr__(self) -> str:
        return f"Gyou<{self.symbol}>"

    @property
    def dakuon(self) -> Kana:
        return kana_dict[self._dakuon]

    # def generate_hiragana(self, hiragana_symbol: str, katakana_symbol: str, dan: Dan) -> Hiragana:
    #     return Hiragana(kana_symbol=hiragana_symbol, katakana_symbol=katakana_symbol, gyou=self, dan=dan)


class Hiragana(Kana):

    def __init__(self, kana_symbol: str, katakana_symbol: str, gyou: Gyou, dan: Dan) -> None:
        super().__init__(kana_symbol, gyou=gyou, dan=dan)
        self._katakana = katakana_symbol
        self._pron_str = HIRA_SPECIAL_READINGS.get(self.symbol, self.symbol)
        self._gyoudan_dict_index = 0

    @property
    def katakana(self) -> Katakana:
        return kana_dict[self._katakana]

    def is_hiragana(self) -> bool:
        return True


class Katakana(Kana):

    def __init__(self, kana_symbol: str, hiragana_symbol: str, gyou: Gyou, dan: Dan) -> None:
        super().__init__(kana_symbol, gyou=gyou, dan=dan)
        self._hiragana = hiragana_symbol
        self._pron_str = KATA_SPECIAL_READINGS.get(self.symbol, self.symbol)
        self._gyoudan_dict_index = 1

    @property
    def hiragana(self) -> Hiragana:
        return kana_dict[self._hiragana]

    def is_katakana(self) -> bool:
        return True


class KanaParser:
    pass


hiraganas = np.array(HIRAGANAS)
katakanas = np.array(KATAKANAS)
print(hiraganas.shape)
print(katakanas.shape)
assert hiraganas.shape == katakanas.shape
m, n = hiraganas.shape


kana_dict: Dict[str, Kana] = {}
kana_gyoudan_dict: defaultdict[Tuple[str, str], List[Kana]] = defaultdict(list)

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

for kana in kana_dict.values():
    if kana.gyou in DAKUON_MAP:
        kana._is_dakuon = False
        for dakuon_kana in kana_gyoudan_dict[(DAKUON_MAP[kana.gyou], kana.dan)]:
            if isinstance(dakuon_kana, type(kana)):
                kana._dakuon = dakuon_kana
    elif kana.gyou in DAKUON_REV_MAP:
        kana._is_dakuon = True
        kana._dakuon = kana
    else:
        kana._is_dakuon = False
        kana._dakuon = kana

# print(kana_dict)
# for kana_str, kana in kana_dict.items():
#     print(kana_str, kana)
#     print(kana.gyou, kana.dan, kana.dakuon, kana.pron, kana.is_hiragana(), kana.is_katakana())

NONE_GYOU = Gyou(symbol='None')
NONE_DAN = Dan(symbol='None')

kana_dict[HIRA_HATSUON] = Hiragana(
    kana_symbol=HIRA_HATSUON, katakana_symbol=KATA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

kana_dict[KATA_HATSUON] = Katakana(
    kana_symbol=KATA_HATSUON, hiragana_symbol=HIRA_HATSUON, gyou=NONE_GYOU, dan=NONE_DAN)

# final constants needed for other use

KANA_DICT = kana_dict
SUTEGANAS = tuple(HIRA_YOUON_MAP.keys()) + HIRA_ADD_YOUONS + tuple(KATA_YOUON_MAP.keys()) + KATA_ADD_YOUONS

def str2kana(string: str) -> Kana:
    # TODO: protect dict
    pass