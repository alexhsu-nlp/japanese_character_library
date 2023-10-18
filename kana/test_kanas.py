from kana import kanas
from kana import kanastr

# TODO: what do i want to achieve for this library?
# 1. a sentence of kana in kana objects
# 2. transform kana strings based on their consonants etc.
# 3. support special reasoning of consonant changes


class TestKanaDict:

    def test_hiragana_a(self):
        kana_a = kanas.KANA_DICT['あ']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'あ'
        assert kana_a.dan.symbol == 'あ'
        assert kana_a.gyou.symbol == 'あ'

    def test_hiragana_ka(self):
        kana_a = kanas.KANA_DICT['か']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'が'
        assert kana_a.dan.symbol == 'あ'
        assert kana_a.gyou.symbol == 'か'

    def test_hiragana_ti(self):
        kana_a = kanas.KANA_DICT['ち']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'じ'
        assert kana_a.dan.symbol == 'い'
        assert kana_a.gyou.symbol == 'た'

    def test_hiragana_su(self):
        kana_a = kanas.KANA_DICT['す']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'ず'
        assert kana_a.dan.symbol == 'う'
        assert kana_a.gyou.symbol == 'さ'

    def test_hiragana_si(self):
        kana_a = kanas.KANA_DICT['し']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'じ'
        assert kana_a.dan.symbol == 'い'
        assert kana_a.gyou.symbol == 'さ'

    def test_hiragana_tu(self):
        kana_a = kanas.KANA_DICT['つ']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'ず'
        assert kana_a.dan.symbol == 'う'
        assert kana_a.gyou.symbol == 'た'

    def test_hiragana_wo(self):
        kana_a = kanas.KANA_DICT['を']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'お'
        assert kana_a.dan.symbol == 'お'
        assert kana_a.gyou.symbol == 'わ'

    def test_hiragana_nn(self):
        kana_a = kanas.KANA_DICT['ん']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron.symbol == 'N'
        assert kana_a.dan.symbol == 'N'
        assert kana_a.gyou.symbol == 'N'

    def test_katakana_nn(self):
        kana_a = kanas.KANA_DICT['ン']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron.symbol == 'N'
        assert kana_a.dan.symbol == 'N'
        assert kana_a.gyou.symbol == 'N'

    def test_katakana_nu(self):
        kana_a = kanas.KANA_DICT['ヌ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron.symbol == 'ヌ'
        assert kana_a.dan.symbol == 'う'
        assert kana_a.gyou.symbol == 'な'

    def test_sutegana_hira_sha(self):
        kana_a = kanas.KANA_DICT['しゃ']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'じゃ'
        # TODO: is this dan assignment good?
        assert kana_a.dan.symbol == 'や'
        assert kana_a.gyou.symbol == 'し'

    def test_sutegana_kata_she(self):
        kana_a = kanas.KANA_DICT['シェ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        assert kana_a.dakuon.pron.symbol == 'ジェ'
        # TODO: is this dan assignment good?
        assert kana_a.dan.symbol == 'え'
        assert kana_a.gyou.symbol == 'さ'

    def test_sutegana_kata_kuo(self):
        kana_a = kanas.KANA_DICT['クォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron.symbol == 'ぐぉ'
        # TODO: is this dan and gyou assignment good?
        # reasoning: the gyou can distinguish the fact that they are foreign
        assert kana_a.dan.symbol == 'お'
        assert kana_a.gyou.symbol == 'く'

    def test_sutegana_kata_tsuo(self):
        kana_a = kanas.KANA_DICT['ツォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron.symbol == 'ずぉ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.symbol == 'お'
        assert kana_a.gyou.symbol == 'つ'

    def test_sutegana_kata_fo(self):
        kana_a = kanas.KANA_DICT['フォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron.symbol == 'ぶぉ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.symbol == 'お'
        # shouldn't the gyou be ふ?
        assert kana_a.gyou.symbol == 'ふ'

    def test_sutegana_kata_deu(self):
        kana_a = kanas.KANA_DICT['デュ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron.symbol == 'でゅ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.symbol == 'ゆ'
        assert kana_a.gyou.symbol == 'で'
