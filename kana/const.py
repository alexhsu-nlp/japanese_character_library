
"""
Python file for gojuuon (五十音) information.
"""
from typing import Tuple, Optional, Dict

# pay attention to checking "he"
HIRAGANAS: Tuple[Tuple[Optional[str], ...]] = (
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

KATAKANAS: Tuple[Tuple[Optional[str], ...]] = (
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


# TODO: do I need to distinguish these two?
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
HIRA_SOKUON: str = 'っ'
KATA_SOKUON: str = 'ッ'


DAKUON_MAP: Dict[str, str] = {
    'か': 'が',
    # 'き': 'ぎ',
    # 'く': 'ぐ',
    # 'け': 'げ',
    # 'こ': 'ご',
    'さ': 'ざ',
    # 'し': 'じ',
    # 'す': 'ず',
    # 'せ': 'ぜ',
    # 'そ': 'ぞ',
    'た': 'だ',
    # 'ち': 'ぢ',
    # 'つ': 'づ',
    # 'て': 'で',
    # 'と': 'ど',
    'は': 'ば',
    # 'ひ': 'び',
    # 'ふ': 'ぶ',
    # 'へ': 'べ',
    # 'ほ': 'ぼ',
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

# logic of construction: ???
