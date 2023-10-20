
"""
Python file for gojuuon (五十音) information.
"""
from typing import Tuple, Optional, Dict, List
from dataclasses import dataclass
from inspect import getmembers
from functools import cached_property
# from kana.utils import cached_classproperty

# TODO: also put kanas and suteganas into the `const` directory?

KANA_ORDER = ('a', 'i', 'u', 'e', 'o')

# pay attention to checking "he"
HIRAGANA_DICT: Dict[str, Tuple[Optional[str], ...]] = {
    '':  ('あ', 'い', 'う', 'え', 'お'),
    'k': ('か', 'き', 'く', 'け', 'こ'),
    's': ('さ', 'し', 'す', 'せ', 'そ'),
    't': ('た', 'ち', 'つ', 'て', 'と'),
    'n': ('な', 'に', 'ぬ', 'ね', 'の'),
    'h': ('は', 'ひ', 'ふ', 'へ', 'ほ'),
    'm': ('ま', 'み', 'む', 'め', 'も'),
    'y': ('や', None, 'ゆ', None, 'よ'),
    'r': ('ら', 'り', 'る', 'れ', 'ろ'),
    'w': ('わ', 'ゐ', None, 'ゑ', 'を'),
    'g': ('が', 'ぎ', 'ぐ', 'げ', 'ご'),
    'z': ('ざ', 'じ', 'ず', 'ぜ', 'ぞ'),
    'd': ('だ', 'ぢ', 'づ', 'で', 'ど'),
    'b': ('ば', 'び', 'ぶ', 'べ', 'ぼ'),
    'p': ('ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ'),
}

HIRAGANAS = tuple(HIRAGANA_DICT.values())

KATAKANA_DICT: Dict[str, Tuple[Optional[str], ...]] = {
    '':  ('ア', 'イ', 'ウ', 'エ', 'オ'),
    'k': ('カ', 'キ', 'ク', 'ケ', 'コ'),
    's': ('サ', 'シ', 'ス', 'セ', 'ソ'),
    't': ('タ', 'チ', 'ツ', 'テ', 'ト'),
    'n': ('ナ', 'ニ', 'ヌ', 'ネ', 'ノ'),
    'h': ('ハ', 'ヒ', 'フ', 'ヘ', 'ホ'),
    'm': ('マ', 'ミ', 'ム', 'メ', 'モ'),
    'y': ('ヤ', None, 'ユ', None, 'ヨ'),
    'r': ('ラ', 'リ', 'ル', 'レ', 'ロ'),
    'w': ('ワ', 'ヰ', None, 'ヱ', 'ヲ'),
    'g': ('ガ', 'ギ', 'グ', 'ゲ', 'ゴ'),
    'z': ('ザ', 'ジ', 'ズ', 'ゼ', 'ゾ'),
    'd': ('ダ', 'ヂ', 'ヅ', 'デ', 'ド'),
    'b': ('バ', 'ビ', 'ブ', 'ベ', 'ボ'),
    'p': ('パ', 'ピ', 'プ', 'ペ', 'ポ'),
}

KATAKANAS = tuple(KATAKANA_DICT.values())

SUTEGANA_HIRAS: Dict[str, Tuple[Optional[str], ...]] = {
    '':  ('ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ'),
    'y': ('ゃ', None, 'ゅ', None, 'ょ'),
    'w': ('ゎ'),
    '?': ('っ'),
}

SUTEGANA_KATAS: Dict[str, Tuple[Optional[str], ...]] = {
    '':  ('ァ', 'ィ', 'ゥ', 'ェ', 'ォ'),
    'y': ('ャ', None, 'ュ', None, 'ョ'),
    'm': ('ㇺ',),
    'l': ('ㇽ',),
    'p': ('ㇷ゚',),
    'k': ('ㇰ',),
    'w': ('ヮ',),
    '?': ('ッ',),  # NOTE: this forms a syllable uniquely
}

# TODO: youons
HEPBURN_PRONS: Tuple[Tuple[str, ...]] = (
    ('a', 'i', 'u', 'e', 'o'),
    ('ka', 'ki', 'ku', 'ke', 'ko'),
    ('sa', 'shi', 'su', 'se', 'se'),
)

# Majority reading


HIRA_SPECIAL_READINGS: Dict[str, str] = {
    'ぢ': 'じ',
    'づ': 'ず',
    'ゑ': 'え',
    'ゐ': 'い',
    'を': 'お',  # not always?
}
KATA_SPECIAL_READINGS: Dict[str, str] = {
    'ヂ': 'ジ',
    'ヅ': 'ズ',
    'ヱ': 'エ',
    'ヰ': 'イ',
    'ヲ': 'オ',
}

HIRA_HATSUON = 'ん'
KATA_HATSUON = 'ン'

KATA_VU = 'ヴ'

# TODO: do I need to distinguish these two?
# TODO: seems that these are not needed anymore
# TODO: pronunciation changes
HIRA_YOUON_MAP: Dict[str, str] = {
    'ゃ': 'や',
    'ゅ': 'ゆ',
    'ょ': 'よ',
}
KATA_YOUON_MAP: Dict[str, str] = {
    'ャ': 'や',
    'ュ': 'ゆ',
    'ョ': 'よ',
}
HIRA_ADD_YOUONS: Dict[str, str] = {
    'ぁ': 'あ',
    'ぃ': 'い',
    'ぅ': 'う',
    'ぇ': 'え',
    'ぉ': 'お',
}
# ('ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ')
KATA_ADD_YOUONS: Dict[str, str] = {
    'ァ': 'あ',
    'ィ': 'い',
    'ゥ': 'う',
    'ェ': 'え',
    'ォ': 'お',
}
# ('ァ', 'ィ', 'ゥ', 'ェ', 'ォ')
# HIRA_SOKUON: str = 'っ'
# KATA_SOKUON: str = 'ッ'

# TODO: change these to romajis?
DAKUON_MAP: Dict[str, str] = {
    'か': 'が',
    'さ': 'ざ',
    'た': 'だ',
    'は': 'ば',
    'ぱ': 'ば',
}


DAKUON_REV_MAP: Dict[str, str] = dict(map(reversed, DAKUON_MAP.items()))

HANDAKUON_MAP: Dict[str, str] = {
    'は': 'ぱ'
}
HanDAKUON_REV_MAP: Dict[str, str] = dict(map(reversed, HANDAKUON_MAP.items()))

# https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/honbun01.html, retrieved 2023.09.01
# directly copied from the to avoid any misconstruction
# TODO: mark specialty of ち, し, つ, ふ
KATA_FOREIGN_YOUON_TABLE1: Tuple[str, ...] = ('シェ',
                                              'チェ',
                                              'ツァ', 'ツェ', 'ツォ',
                                                    'ティ',
                                                    'ファ', 'フィ', 'フェ', 'フォ',
                                                    'ジェ',
                                                    # 'ディ', 'デュ',
                                              )
KATA_FOREIGN_YOUON_TABLE2: Tuple[str, ...] = ('イェ',
                                              'ウィ', 'ウェ', 'ウォ',
                                                    'クァ', 'クィ', 'クェ', 'クォ',
                                                    'ツィ',
                                                    'トゥ',
                                                    'グァ',
                                                    'ドゥ',
                                                    'ヴァ', 'ヴィ',
                                                    # 'ヴ',
                                              'ヴェ', 'ヴォ',
                                                    # 'テュ', 'フュ', 'ヴュ'
                                              )

# TODO: why did I pull these out?
abnormal_katakanas: Tuple[str, ...] = ('ヴ', 'ツ', 'フ', 'イ', 'ウ')

# for 促音化
SUKUON_KANAS = ('き', 'く', 'ち', 'つ', 'キ', 'ク', 'チ', 'ツ')

# seems that this needs a case-by-case treatment
SPECIAL_SYMBOLS = ('ー', '々', 'ゝ', 'ゞ', 'ヽ', 'ヾ')

LONG_KATA_VOWEL_CHAR = 'ー'


@dataclass(frozen=True)
class IterSymbol:
    symbol: str
    is_hira: bool
    voiced: bool


class _IterSymbolCollection:
    # in fact it *can* be voiced for kanji sometimes
    kanji = IterSymbol(symbol='々', is_hira=False, voiced=False)
    hira_unvoiced = IterSymbol(symbol='ゝ', is_hira=True, voiced=False)
    hira_voiced = IterSymbol(symbol='ゞ', is_hira=True, voiced=True)
    kata_unvoiced = IterSymbol(symbol='ヽ', is_hira=False, voiced=False)
    kata_voiced = IterSymbol(symbol='ヾ', is_hira=False, voiced=False)

    def __init__(self):
        self.itersymbolstr_dict: Dict[str, IterSymbol] = dict([(getattr(self, itersymbol_varname).symbol, getattr(self, itersymbol_varname))
                            for itersymbol_varname in get_obj_varnames_with_specified_type(self, var_type=IterSymbol)])

    # @cached_property
    # def itersymbolstr_dict(self) -> Dict[str, IterSymbol]:
    #     return


def get_obj_varnames_with_specified_type(obj: object, var_type) -> List[str]:
    print([f for f in dir(obj) if isinstance(getattr(obj, f), var_type)])
    return [f for f in dir(obj) if isinstance(getattr(obj, f), var_type)]

    # @classmethod
    # def get_matched_odoroji(cls, string: str) -> Optional[IterSymbol]:
    #     for _, odoriji in getmembers(cls):
    #         if isinstance(odoriji, IterSymbol) and odoriji.symbol == string:
    #             return odoriji


ITER_SYMBOL_COLLECTION = _IterSymbolCollection()
