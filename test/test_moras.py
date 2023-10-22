from kana import kanas
from kana import morastr


class TestMoras:

    def test_mora_sha_hira(self):
        mora = kanas.char2mora('しゃ')
        assert str(mora) == 'しゃ'
        assert mora.__repr__() == 'Mora<しゃ>'
        assert mora.kana == kanas.KANA_DICT['し']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ゃ']
        assert mora.dakuon.kana.pron.symbol == 'じ'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'さ'
        # mora.check()

    def test_mora_she_kata(self):
        mora = kanas.char2mora('シェ')
        assert mora.kana == kanas.KANA_DICT['シ']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ェ']
        assert mora.dakuon.kana.pron.symbol == 'じ'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'さ'
        # mora.check()

    def test_mora_kuo_kata(self):
        mora = kanas.char2mora('クォ')
        assert mora.kana == kanas.KANA_DICT['ク']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ォ']
        assert mora.dakuon.kana.pron.symbol == 'ぐ'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'か'
        # assert mora.check() is True

    def test_mora_vu_kata(self):
        mora = kanas.char2mora('ヴ')
        assert str(mora) == 'ヴ'
        assert mora.__repr__() == 'Mora<ヴ>'
        assert mora.kana == kanas.KANA_DICT['ヴ']
        assert mora.sutegana == None
        assert mora.dakuon.kana.pron.symbol == 'ヴ'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'N'
        # assert mora.check() is True

    def test_mora_va_kata(self):
        mora = kanas.char2mora('ヴァ')
        assert mora.kana == kanas.KANA_DICT['ヴ']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ァ']
        assert mora.dakuon.kana.pron.symbol == 'ヴ'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'N'
        # mora.check()

    def test_mora_deu_kata(self):
        mora = kanas.char2mora('デュ')
        assert mora.kana == kanas.KANA_DICT['デ']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ュ']
        assert mora.dakuon.kana.pron.symbol == 'で'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'だ'
        # mora.check()

    def test_mora_pyo_hira(self):
        mora = kanas.char2mora('ぴょ')
        assert mora.kana == kanas.KANA_DICT['ぴ']
        assert mora.sutegana == kanas.SUTEGANA_DICT['ょ']
        assert mora.dakuon.kana.pron.symbol == 'び'
        # TODO: is this dan assignment good?
        assert mora.kana.gyou.symbol == 'ぱ'
        # mora.check()

    # def test_sutegana_kata_she(self):
    #     mora = kanas.KANA_DICT['シェ']
    #     assert not mora.is_hiragana()
    #     assert mora.is_katakana()
    #     assert mora.dakuon.pron.symbol == 'ジェ'
    #     # TODO: is this dan assignment good?
    #     assert mora.dan.symbol == 'え'
    #     assert mora.gyou.symbol == 'さ'

    # def test_sutegana_kata_kuo(self):
    #     mora = kanas.KANA_DICT['クォ']
    #     assert not mora.is_hiragana()
    #     assert mora.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert mora.dakuon.pron.symbol == 'ぐぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     # reasoning: the gyou can distinguish the fact that they are foreign
    #     assert mora.dan.symbol == 'お'
    #     assert mora.gyou.symbol == 'く'

    # def test_sutegana_kata_tsuo(self):
    #     mora = kanas.KANA_DICT['ツォ']
    #     assert not mora.is_hiragana()
    #     assert mora.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert mora.dakuon.pron.symbol == 'つぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert mora.dan.symbol == 'お'
    #     assert mora.gyou.symbol == 'つ'

    # def test_sutegana_kata_fo(self):
    #     mora = kanas.KANA_DICT['フォ']
    #     assert not mora.is_hiragana()
    #     assert mora.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert mora.dakuon.pron.symbol == 'ぶぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert mora.dan.symbol == 'お'
    #     # shouldn't the gyou be ふ?
    #     assert mora.gyou.symbol == 'ふ'

    # def test_sutegana_kata_deu(self):
    #     mora = kanas.KANA_DICT['デュ']
    #     assert not mora.is_hiragana()
    #     assert mora.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert mora.dakuon.pron.symbol == 'でゅ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert mora.dan.symbol == 'ゆ'
    #     assert mora.gyou.symbol == 'で'
