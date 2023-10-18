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

    def test_hiragana_su(self):
        kana_a = self.kana_dict['す']
        assert kana_a.dakuon.pron == 'ず'
        assert kana_a.dan.pron == 'う'
        assert kana_a.gyou.pron == 'さ'

    def test_hiragana_si(self):
        kana_a = self.kana_dict['し']
        assert kana_a.dakuon.pron == 'じ'
        assert kana_a.dan.pron == 'い'
        assert kana_a.gyou.pron == 'さ'

    def test_hiragana_tu(self):
        kana_a = self.kana_dict['つ']
        assert kana_a.dakuon.pron == 'ず'
        assert kana_a.dan.pron == 'う'
        assert kana_a.gyou.pron == 'た'

    def test_hiragana_wo(self):
        kana_a = self.kana_dict['を']
        assert kana_a.dakuon.pron == 'お'
        assert kana_a.dan.pron == 'お'
        assert kana_a.gyou.pron == 'わ'

    def test_hiragana_nn(self):
        kana_a = self.kana_dict['ん']
        # TODO: should I make a pronunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron == 'None'
        assert kana_a.dan.pron == 'None'
        assert kana_a.gyou.pron == 'None'

    def test_sutegana(self):
        kana_a = self.kana_dict['ん']
        # TODO: should I make a pronunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron == 'None'
        assert kana_a.dan.pron == 'None'
        assert kana_a.gyou.pron == 'None'


class TestKanaStr:
    pass
