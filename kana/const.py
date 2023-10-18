
"""
Python file for gojuuon (五十音) information.
"""
# pay attention to checking "he"
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

# TODO: youons
HEPBURN_PRONS = (
    ('a', 'i', 'u', 'e', 'o'),
    ('ka', 'ki', 'ku', 'ke', 'ko'),
    ('sa', 'shi', 'su', 'se', 'se'),
)

# Majority reading
HIRA_SPECIAL_READINGS = {
    'ぢ': 'じ',
    'づ': 'ず',
    'ゑ': 'え',
    'ゐ': 'い',
    'を': 'お',  # not always?
}
KATA_SPECIAL_READINGS = {
    'ヂ': 'ジ',
    'ヅ': 'ズ',
    'ヱ': 'エ',
    'ヰ': 'イ',
    'ヲ': 'オ',
}

HIRA_HATSUON = 'ん'
KATA_HATSUON = 'ン'


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


DAKUON_REV_MAP = dict(map(reversed, DAKUON_MAP.items()))

HANDAKUON_MAP = {
    'は': 'ぱ'
}
HanDAKUON_REV_MAP = dict(map(reversed, HANDAKUON_MAP.items()))

# https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/honbun01.html, retrieved 2023.09.01
# directly copied from the to avoid any misconstruction
# TODO: mark specialty of ち, し, つ, ふ
KATA_FOREIGN_YOUONS_TABLE1 = ('シェ',
                              'チェ',
                              'ツァ', 'ツェ', 'ツォ',
                              'ティ',
                              'ファ', 'フィ', 'フェ', 'フォ',
                              'ジェ',
                              'ディ', 'デュ')
KATA_FOREIGN_YOUONS_TABLE2 = ('イェ',
                              'ウィ', 'ウェ', 'ウォ',
                              'クァ', 'クィ', 'クェ', 'クォ',
                              'ツィ',
                              'トゥ',
                              'グァ',
                              'ドゥ',
                              'ヴァ', 'ヴィ', 'ヴ', 'ヴぇ', 'ヴォ',
                              'テュ', 'フュ', 'ヴュ')

abnormal_katakanas = ('ヴ', 'ツ', 'フ', 'イ', 'ウ')

# logic of construction: ???
