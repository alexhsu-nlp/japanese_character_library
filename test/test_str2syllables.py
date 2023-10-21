from kana import kanas, kanastr
from kana.str2syllablestr import str2syllablestr
import pytest


class TestStr2Syllables:

    @pytest.mark.parametrize(
        'string,str_result,syllable_size',
        [
            ('わたしのことは', 'わたしのことは', 7),
            ('きょうかいせん', 'きょうかいせん', 6),
            ('おしいなぁ', 'おしいなあ', 5),
            ('わぁぁぁあ', 'わああああ', 5),
            ('ウイルスセキュリティがじゅうようだ', 'ウイルスセキュリティがじゅうようだ', 14),
            ('ヴァイスシュヴァルツ', 'ヴァイスシュヴァルツ', 7),
            ('あっ', 'あっ', 2),  # TODO: actually this is not?
            ('バナヽ', 'バナナ', 3),
            ('づゝ', 'づつ', 2)
        ]

    )
    def test_eval(self, string: str, str_result: str, syllable_size: int):
        result = str2syllablestr(string)
        assert str(result) == str_result
        assert len(result) == syllable_size

    def test7(self):
        result = str2syllablestr('がっこうであったこわいはなし')
        assert len(result) == 14

    def test8(self):
        result = str2syllablestr('ハート')
        assert len(result) == 3
        assert str(result) == 'ハアト'

    def test9(self):
        result = str2syllablestr('ファックス')
        assert len(result) == 4
        assert str(result) == 'ファックス'

    def test10(self):
        result = str2syllablestr('つゞく')
        assert len(result) == 3
        assert str(result) == 'つづく'

    def test10(self):
        result = str2syllablestr('たゝく')
        assert len(result) == 3
        assert str(result) == 'たたく'
