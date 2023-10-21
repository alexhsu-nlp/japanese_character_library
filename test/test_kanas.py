from kana import kanas
from kana import kanastr

# TODO: what do i want to achieve for this library?
# 1. a sentence of kana in kana objects
# 2. transform kana strings based on their consonants etc.
# 3. support special reasoning of consonant changes
import pytest


class TestKanaDict:

    @pytest.mark.parametrize(
        argnames='hira_str,hira_str,dakuon_str,dakuon_pron_str,rev_dakuon_str,rev_dakuon_pron_str,dan_str,gyou_str',
        argvalues=[
            ()
        ]
    )
    def test_hiragana(self, hira_str: str, dakuon_str: str, dakuon_pron_str: str, rev_dakuon_str: str, rev_dakuon_pron_str: str, dan_str: str, gyou_str: str):
        kana = kanas.KANA_DICT[hira_str]
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.symbol == dakuon_str
        assert kana.dakuon.pron.symbol == dakuon_pron_str
        assert kana.rev_dakuon.symbol == rev_dakuon_str
        assert kana.rev_dakuon.pron.symbol == rev_dakuon_pron_str
        assert kana.dan.symbol == dan_str
        assert kana.gyou.symbol == gyou_str

    def test_hiragana_a(self):
        kana = kanas.KANA_DICT['あ']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'あ'
        assert kana.rev_dakuon.pron.symbol == 'あ'
        assert kana.dan.symbol == 'あ'
        assert kana.gyou.symbol == 'あ'

    def test_hiragana_ka(self):
        kana = kanas.KANA_DICT['か']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'が'
        assert kana.rev_dakuon.symbol == 'か'
        assert kana.dan.symbol == 'あ'
        assert kana.gyou.symbol == 'か'

    def test_hiragana_ti(self):
        kana = kanas.KANA_DICT['ち']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'じ'
        assert kana.rev_dakuon.pron.symbol == 'ち'
        assert kana.dan.symbol == 'い'
        assert kana.gyou.symbol == 'た'

    def test_hiragana_su(self):
        kana = kanas.KANA_DICT['す']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'ず'
        assert kana.dan.symbol == 'う'
        assert kana.gyou.symbol == 'さ'

    def test_hiragana_si(self):
        kana = kanas.KANA_DICT['し']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'じ'
        assert kana.rev_dakuon.symbol == 'し'
        assert kana.dan.symbol == 'い'
        assert kana.gyou.symbol == 'さ'

    def test_hiragana_tu(self):
        kana = kanas.KANA_DICT['つ']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'ず'
        assert kana.rev_dakuon.pron.symbol == 'つ'
        assert kana.dan.symbol == 'う'
        assert kana.gyou.symbol == 'た'

    def test_hiragana_wo(self):
        kana = kanas.KANA_DICT['を']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        assert kana.dakuon.pron.symbol == 'お'
        assert kana.rev_dakuon.pron.symbol == 'お'
        assert kana.dan.symbol == 'お'
        assert kana.gyou.symbol == 'わ'

    def test_hiragana_nn(self):
        kana = kanas.KANA_DICT['ん']
        assert kana.is_hiragana()
        assert not kana.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana.dakuon.pron.symbol == 'N'
        assert kana.dan.symbol == 'N'
        assert kana.gyou.symbol == 'N'

    def test_katakana_nn(self):
        kana = kanas.KANA_DICT['ン']
        assert not kana.is_hiragana()
        assert kana.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana.dakuon.pron.symbol == 'N'
        assert kana.dan.symbol == 'N'
        assert kana.gyou.symbol == 'N'

    def test_katakana_nu(self):
        kana = kanas.KANA_DICT['ヌ']
        assert not kana.is_hiragana()
        assert kana.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana.dakuon.symbol == 'ヌ'
        assert kana.rev_dakuon.symbol == 'ヌ'
        assert kana.dakuon.pron.symbol == 'ぬ'
        assert kana.dan.symbol == 'う'
        assert kana.gyou.symbol == 'な'

    def test_katakana_nu(self):
        kana = kanas.KANA_DICT['グ']
        assert not kana.is_hiragana()
        assert kana.is_katakana()
        # TODO: should I make a pron.symbolunciation class?
        # TODO: how to treat these Nones
        assert kana.dakuon.symbol == 'グ'
        assert kana.rev_dakuon.symbol == 'ク'
        assert kana.dakuon.pron.symbol == 'ぐ'
        assert kana.dan.symbol == 'う'
        assert kana.gyou.symbol == 'が'


class TestSuteganas:
    pass
    # TODO: now these should be put into syllables checking
    # NOTE: all the youon's are not sukuonizable except じゅう (十) e.g. in じっぷん [what about 入 sometimes にっ?]
    # NOTE: to consider 歴史的仮名遣い, the previous kana can be affected to have youon!!!
    # def test_sutegana_hira_sha(self):
    #     kana = kanas.KANA_DICT['しゃ']
    #     assert kana.is_hiragana()
    #     assert not kana.is_katakana()
    #     assert kana.dakuon.pron.symbol == 'じゃ'
    #     # TODO: is this dan assignment good?
    #     assert kana.dan.symbol == 'や'
    #     assert kana.gyou.symbol == 'し'
