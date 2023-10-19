from kana import kanas
from kana import kanastr


class TestSyllables:

    def test_syllable_sha(self):
        syllable = kanas.char2syllable('しゃ')
        assert syllable.kana == kanas.KANA_DICT['し']
        assert syllable.sutegana == kanas.SUTEGANA_DICT['ゃ']
        # assert not syllable.is_katakana()
        assert syllable.dakuon.kana.pron.symbol == 'じ'
        # TODO: is this dan assignment good?
        assert syllable.kana.gyou.symbol == 'し'

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
