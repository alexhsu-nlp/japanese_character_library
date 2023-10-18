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
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'あ'
        assert kana_a.dan.pron == 'あ'
        assert kana_a.gyou.pron == 'あ'

    def test_hiragana_ka(self):
        kana_a = self.kana_dict['か']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'が'
        assert kana_a.dan.pron == 'あ'
        assert kana_a.gyou.pron == 'か'

    def test_hiragana_ti(self):
        kana_a = self.kana_dict['ち']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'じ'
        assert kana_a.dan.pron == 'い'
        assert kana_a.gyou.pron == 'た'

    def test_hiragana_su(self):
        kana_a = self.kana_dict['す']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'ず'
        assert kana_a.dan.pron == 'う'
        assert kana_a.gyou.pron == 'さ'

    def test_hiragana_si(self):
        kana_a = self.kana_dict['し']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'じ'
        assert kana_a.dan.pron == 'い'
        assert kana_a.gyou.pron == 'さ'

    def test_hiragana_tu(self):
        kana_a = self.kana_dict['つ']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'ず'
        assert kana_a.dan.pron == 'う'
        assert kana_a.gyou.pron == 'た'

    def test_hiragana_wo(self):
        kana_a = self.kana_dict['を']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'お'
        assert kana_a.dan.pron == 'お'
        assert kana_a.gyou.pron == 'わ'

    def test_hiragana_nn(self):
        kana_a = self.kana_dict['ん']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        # TODO: should I make a pronunciation class?
        # TODO: how to treat these Nones
        assert kana_a.dakuon.pron == 'None'
        assert kana_a.dan.pron == 'None'
        assert kana_a.gyou.pron == 'None'

    def test_sutegana_hira_sha(self):
        kana_a = self.kana_dict['しゃ']
        assert kana_a.is_hiragana()
        assert not kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'じゃ'
        # TODO: is this dan assignment good?
        assert kana_a.dan.pron == 'や'
        assert kana_a.gyou.pron == 'し'

    def test_sutegana_kata_she(self):
        kana_a = self.kana_dict['シェ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        assert kana_a.dakuon.pron == 'ジェ'
        # TODO: is this dan assignment good?
        assert kana_a.dan.pron == 'え'
        assert kana_a.gyou.pron == 'さ'

    def test_sutegana_kata_kuo(self):
        kana_a = self.kana_dict['クォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron == 'ぐぉ'
        # TODO: is this dan and gyou assignment good?
        # reasoning: the gyou can distinguish the fact that they are foreign
        assert kana_a.dan.pron == 'お'
        assert kana_a.gyou.pron == 'く'

    def test_sutegana_kata_tsuo(self):
        kana_a = self.kana_dict['ツォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron == 'ずぉ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.pron == 'お'
        assert kana_a.gyou.pron == 'つ'

    def test_sutegana_kata_fo(self):
        kana_a = self.kana_dict['フォ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron == 'ずぉ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.pron == 'お'
        # shouldn't the gyou be ふ?
        assert kana_a.gyou.pron == 'ふ'

    def test_sutegana_kata_deu(self):
        kana_a = self.kana_dict['デュ']
        assert not kana_a.is_hiragana()
        assert kana_a.is_katakana()
        # TODO: actually this dakuon does not exist
        assert kana_a.dakuon.pron == 'でゅ'
        # TODO: is this dan and gyou assignment good?
        assert kana_a.dan.pron == 'ゆ'
        assert kana_a.gyou.pron == 'で'
