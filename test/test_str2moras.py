from kana import kanas, morastr
from kana.str2mora import str2morastr
import pytest


class TestStr2Syllables:

    @pytest.mark.parametrize(
        'string,str_result,mora_size',
        [
            ('わたしのことは', 'わたしのことは', 7),
            ('きょうかいせん', 'きょうかいせん', 6),
            ('おしいなぁ', 'おしいなあ', 5),
            ('わぁぁぁあ', 'わああああ', 5),
            ('ウイルスセキュリティがじゅうようだ', 'ウイルスセキュリティがじゅうようだ', 14),
            ('ヴァイスシュヴァルツ', 'ヴァイスシュヴァルツ', 7),
            ('あっ', 'あっ', 2),  # TODO: actually this is not?
            ('バナヽ', 'バナナ', 3),
            ('づゝ', 'づつ', 2),
            ('ハート', 'ハアト', 3),
            ('ファックス', 'ファックス', 4),
            ('つゞく', 'つづく', 3),
            ('たゝく', 'たたく', 3),
        ]

    )
    def test_eval(self, string: str, str_result: str, mora_size: int):
        result = str2morastr(string)
        assert str(result) == str_result
        assert len(result) == mora_size

    def test7(self):
        result = str2morastr('がっこうであったこわいはなし')
        assert len(result) == 14
