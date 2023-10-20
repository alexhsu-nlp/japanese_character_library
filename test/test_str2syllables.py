from kana import kanas, kanastr
from kana.str2syllablestr import str2syllablestr


class TestStr2Syllables:

    def test1(self):
        result = str2syllablestr('わたしのことは')
        assert str(result) == 'わたしのことは'
        assert len(result) == 7

    def test2(self):
        result = str2syllablestr('きょうかいせん')
        assert str(result) == 'きょうかいせん'
        assert len(result) == 6

    def test3(self):
        result = str2syllablestr('おしいなぁ')
        print(result[-1].check())
        assert str(result) == 'おしいなあ'
        assert len(result) == 5

    def test4(self):
        result = str2syllablestr('わぁぁぁあ')
        assert len(result) == 5

    def test5(self):
        result = str2syllablestr('ウイルスセキュリティがじゅうようだ')

    def test6(self):
        result = str2syllablestr('ヴァイスシュヴァルツ')

    def test7(self):
        result = str2syllablestr('がっこうであったこわいはなし')
        assert len(result) == 14
