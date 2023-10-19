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
        assert kana_a.dakuon.symbol == 'ヌ'
        assert kana_a.dakuon.pron.symbol == 'ぬ'
        assert kana_a.dan.symbol == 'う'
        assert kana_a.gyou.symbol == 'な'


class TestSuteganas:
    pass
    # TODO: now these should be put into syllables checking
    # NOTE: all the youon's are not sukuonizable except じゅう (十) e.g. in じっぷん [what about 入 sometimes にっ?]
    # NOTE: to consider 歴史的仮名遣い, the previous kana can be affected to have youon!!!
    # def test_sutegana_hira_sha(self):
    #     kana_a = kanas.KANA_DICT['しゃ']
    #     assert kana_a.is_hiragana()
    #     assert not kana_a.is_katakana()
    #     assert kana_a.dakuon.pron.symbol == 'じゃ'
    #     # TODO: is this dan assignment good?
    #     assert kana_a.dan.symbol == 'や'
    #     assert kana_a.gyou.symbol == 'し'
