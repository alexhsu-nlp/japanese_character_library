import kanas
import kanastr

# TODO: what do i want to achieve for this library?
# 1. a sentence of kana in kana objects
# 2. transform kana strings based on their consonants etc.
# 3. support special reasoning of consonant changes


class TestKanaDict:

    def __init__(self) -> None:
        self.kana_dict = kanas.KANA_DICT

    def test_hiragana_a(self):
        kana_a = self.kana_dict['あ']
        assert kana_a.dakuon.pron == 'あ'
        assert kana_a.dan.pron == 'あ'
        assert kana_a.gyou.pron == 'あ'

    def test_hiragana_ka(self):
        kana_a = self.kana_dict['か']
        assert kana_a.dakuon.pron == 'が'
        assert kana_a.dan.pron == 'あ'
        assert kana_a.gyou.pron == 'か'

    def test_hiragana_ti(self):
        kana_a = self.kana_dict['ち']
        assert kana_a.dakuon.pron == 'じ'
        assert kana_a.dan.pron == 'い'
        assert kana_a.gyou.pron == 'た'

    def test_katakana_su(self):
        pass


class TestKanaStr:
    pass
