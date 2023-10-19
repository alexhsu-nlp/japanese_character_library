from kana import kanas
from kana import kanastr


class TestSyllables:

    def test_syllable_sha_hira(self):
        syllable = kanas.char2syllable('しゃ')
        assert syllable.kana == kanas.KANA_DICT['し']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ゃ']
        assert syllable.dakuon.kana.pron.symbol == 'じ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'さ'
        syllable.check()

    def test_syllable_she_kata(self):
        syllable = kanas.char2syllable('シェ')
        assert syllable.kana == kanas.KANA_DICT['シ']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ェ']
        assert syllable.dakuon.kana.pron.symbol == 'じ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'さ'
        syllable.check()

    def test_syllable_kuo_kata(self):
        syllable = kanas.char2syllable('クォ')
        assert syllable.kana == kanas.KANA_DICT['ク']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ォ']
        assert syllable.dakuon.kana.pron.symbol == 'ぐ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'か'
        syllable.check()

    def test_syllable_vu_kata(self):
        syllable = kanas.char2syllable('ヴ')
        assert syllable.kana == kanas.KANA_DICT['ヴ']
        assert syllable.sutegana == None
        assert syllable.dakuon.kana.pron.symbol == 'ヴ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'N'
        syllable.check()

    def test_syllable_va_kata(self):
        syllable = kanas.char2syllable('ヴァ')
        assert syllable.kana == kanas.KANA_DICT['ヴ']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ァ']
        assert syllable.dakuon.kana.pron.symbol == 'ヴ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'N'
        syllable.check()
    
    def test_syllable_deu_kata(self):
        syllable = kanas.char2syllable('デュ')
        assert syllable.kana == kanas.KANA_DICT['デ']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ュ']
        assert syllable.dakuon.kana.pron.symbol == 'で'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'だ'
        syllable.check()
    
    def test_syllable_pyo_hira(self):
        syllable = kanas.char2syllable('ぴょ')
        assert syllable.kana == kanas.KANA_DICT['ぴ']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ょ']
        assert syllable.dakuon.kana.pron.symbol == 'び'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'ぱ'
        syllable.check()

    # def test_sutegana_kata_she(self):
    #     syllable = kanas.KANA_DICT['シェ']
    #     assert not syllable.is_hiragana()
    #     assert syllable.is_katakana()
    #     assert syllable.dakuon.pron.symbol == 'ジェ'
    #     # TODO: is this dan assignment good?
    #     assert syllable.dan.symbol == 'え'
    #     assert syllable.gyou.symbol == 'さ'

    # def test_sutegana_kata_kuo(self):
    #     syllable = kanas.KANA_DICT['クォ']
    #     assert not syllable.is_hiragana()
    #     assert syllable.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert syllable.dakuon.pron.symbol == 'ぐぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     # reasoning: the gyou can distinguish the fact that they are foreign
    #     assert syllable.dan.symbol == 'お'
    #     assert syllable.gyou.symbol == 'く'

    # def test_sutegana_kata_tsuo(self):
    #     syllable = kanas.KANA_DICT['ツォ']
    #     assert not syllable.is_hiragana()
    #     assert syllable.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert syllable.dakuon.pron.symbol == 'つぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert syllable.dan.symbol == 'お'
    #     assert syllable.gyou.symbol == 'つ'

    # def test_sutegana_kata_fo(self):
    #     syllable = kanas.KANA_DICT['フォ']
    #     assert not syllable.is_hiragana()
    #     assert syllable.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert syllable.dakuon.pron.symbol == 'ぶぉ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert syllable.dan.symbol == 'お'
    #     # shouldn't the gyou be ふ?
    #     assert syllable.gyou.symbol == 'ふ'

    # def test_sutegana_kata_deu(self):
    #     syllable = kanas.KANA_DICT['デュ']
    #     assert not syllable.is_hiragana()
    #     assert syllable.is_katakana()
    #     # TODO: actually this dakuon does not exist
    #     assert syllable.dakuon.pron.symbol == 'でゅ'
    #     # TODO: is this dan and gyou assignment good?
    #     assert syllable.dan.symbol == 'ゆ'
    #     assert syllable.gyou.symbol == 'で'
