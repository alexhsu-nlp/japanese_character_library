"""
File for generating the kanji dictionary for data cleaning.
This is the original file used in the research project.
"""

from dataclasses import dataclass
from functools import cached_property
from xml.etree.ElementTree import ElementTree
from typing import List
import jaconv
from time import time
from itertools import product


start = time()

KANJIDIC_PATH_STR = "kanjidic2/kanjidic2.xml"

kanjidic_root = ElementTree().parse(KANJIDIC_PATH_STR)


@dataclass
class Yomi:
    body: str

    def __post__init__(self):
        self.romaji = jaconv.kana2nihonshiki(self.body)

    def dakuonize(self):
        PREV_DAKUON_DICT = {
            'ti': ['zi'],
            'tu': ['zu'],
            'ty': ['zy'],
        }
        DAKUON_DICT = {
            'k': ['g'],
            't': ['d'],
            'h': ['p', 'b'],  # TODO: true?
            's': ['z'],
            'o': ['no'],  # TODO: this should be conditional
            'e': ['ne'],
            'i': ['mi'],
        }
        yomis = set()
        romaji = self.body
        if romaji.startswith(tuple(PREV_DAKUON_DICT.keys())):
            for dakuon in PREV_DAKUON_DICT[romaji[:2]]:
                dakuon_romaji = dakuon + romaji[2:]
                yomis.add(jaconv.nihonshiki2kana(dakuon_romaji))
        elif romaji.startswith(tuple(DAKUON_DICT.keys())):
            for dakuon in DAKUON_DICT[romaji[0]]:
                dakuon_romaji = dakuon + romaji[1:]
                yomis.add(jaconv.nihonshiki2kana(dakuon_romaji))
        return yomis

    @cached_property
    def valid_yomis(self):
        # TODO: any better treatment other than set?
        return set([self.body])


class Nanori(Yomi):
    pass


class OnYomi(Yomi):

    def sokuonize(self):
        sokuon_endings = ('く', 'き', 'ち', 'つ')
        if len(self.body) > 1 and self.body.endswith(sokuon_endings):
            return set([self.body[:-1] + 'っ'])

    @cached_property
    def valid_yomis(self):
        return super().valid_yomis().union(self.sokuonize())


@dataclass
class KunYomi(Yomi):
    ending: str
    # NOTE: temporarily they are still alphabet strings rather than kanas

    def __post__init__(self):
        super().__post__init__()
        self.ending_romaji = jaconv.kana2nihonshiki(self.ending)

    def is_adjective(self):
        return self.ending.endswith('い')  # TODO: pure ending

    def is_verb(self):
        return self.ending_romaji.endswith('u')

    def is_godanverb(self):
        return self.is_verb() and not self.is_ichidanverb()

    def is_ichidanverb(self):
        return self.ending_romaji.endswith(('eru', 'iru'))

    def verb_nominalize(self):
        if self.is_godanverb():
            result = self.body + \
                jaconv.nihonshiki2kana(self.ending_romaji[:-1]+"i")
            return set([result])
        elif self.is_ichidanverb():
            # print("TRUE")
            result = self.body + self.ending[:-1]
            return set([result])
        return set([self.body + self.ending])

    @cached_property
    def valid_yomis(self):
        pass


@dataclass
class KanjiYomi:
    kanji: str
    onyomis: List[str]
    kunyomis: List[str]
    nanoris: List[str]

    def __post_init__(self):
        self.valid_onyomis = self._get_valid_onyomis()
        self.valid_kunyomis = self._get_valid_kunyomis()
        self.valid_yomis = self.valid_onyomis.union(self.valid_kunyomis)

    def _get_valid_onyomis(self):
        valid_onyomis = []
        for onyomi in self.onyomis:
            valid_onyomis.append(onyomi)
            if len(onyomi) > 1 and onyomi.endswith(('く', 'き', 'ち', 'つ')):
                valid_onyomis.append(onyomi[:-1]+'っ')
            valid_onyomis.extend(self._dakuonize(onyomi))
        return set(valid_onyomis)

    def _get_valid_kunyomis(self):
        valid_kunyomis = []

        for kunyomi in self.kunyomis:
            kunyomi = kunyomi.replace("-", "")
            if "." in kunyomi:
                assert kunyomi.count(".") == 1
                splits = kunyomi.split('.')
                valid_kunyomis.append(splits[0])
                valid_kunyomis.append(splits[0]+splits[1])
                valid_kunyomis.extend(self._dakuonize(splits[0]))
                full_dakuon = self._dakuonize(splits[0]+splits[1])
                valid_kunyomis.extend(full_dakuon)
                for dakuon in full_dakuon:
                    valid_kunyomis.extend(self._verb_nominalize(dakuon))
                valid_kunyomis.extend(
                    self._verb_nominalize(splits[0]+splits[1]))
            else:
                valid_kunyomis.append(kunyomi)
                valid_kunyomis.extend(self._dakuonize(kunyomi))
        valid_kunyomis.extend(self.nanoris)
        for nanori in self.nanoris:
            valid_kunyomis.extend(self._dakuonize(nanori))
        return set(valid_kunyomis)

    def _dakuonize(self, hiragana: str) -> List[str]:
        # same as pronunciation standard in dataset
        PREV_DAKUON_DICT = {
            'ti': ['zi'],
            'tu': ['zu'],
            'ty': ['zy'],
        }
        DAKUON_DICT = {
            'k': ['g'],
            't': ['d'],
            'h': ['p', 'b'],  # TODO: true?
            's': ['z'],
            'o': ['no'],
            'e': ['ne'],
            'i': ['mi'],
        }
        yomis = []
        romaji = jaconv.kana2nihonshiki(hiragana)
        # if self.kanji == '柱':
        #     print(romaji)
        if romaji.startswith(tuple(PREV_DAKUON_DICT.keys())):
            for dakuon in PREV_DAKUON_DICT[romaji[:2]]:
                dakuon_romaji = dakuon + romaji[2:]
                # if self.kanji == '柱':
                #     print(dakuon_romaji)
                #     print(jaconv.nihonshiki2kana(dakuon_romaji))
                yomis.append(jaconv.nihonshiki2kana(dakuon_romaji))
        elif romaji.startswith(tuple(DAKUON_DICT.keys())):
            for dakuon in DAKUON_DICT[romaji[0]]:
                dakuon_romaji = dakuon + romaji[1:]
                # if self.kanji == '柱':
                #     print(dakuon_romaji)
                #     print(jaconv.nihonshiki2kana(dakuon_romaji))
                yomis.append(jaconv.nihonshiki2kana(dakuon_romaji))
        return yomis

    def _verb_nominalize(self, hiragana: str) -> List[str]:
        """change a wago verb form to its noun form"""
        # print("nomialize:", hiragana)
        romaji = jaconv.kana2nihonshiki(hiragana)
        yomis = []
        if romaji.endswith("u"):
            noun_romaji = romaji[:-1] + "i"
            yomis.append(jaconv.nihonshiki2kana(noun_romaji))
        if romaji.endswith(("eru", "iru")):
            # print("TRUE")
            yomis.append(hiragana[:-1])
        return yomis


# TODO: should I provide a way to list all?
@dataclass
class Yomi:
    main: str
    attribute: str = ""

    @cached_property
    def complete(self):
        return self.main + self.attribute


char_dict = {}
# special cases
char_dict["ヶ"] = KanjiYomi(kanji="ヶ", onyomis=[], kunyomis=['か'], nanoris=[])
char_dict["ヵ"] = KanjiYomi(kanji="ヵ", onyomis=[], kunyomis=['か'], nanoris=[])
char_dict["〆"] = KanjiYomi(kanji="〆", onyomis=[], kunyomis=['しめ'], nanoris=[])
char_dict["-"] = KanjiYomi(kanji="-", onyomis=[], kunyomis=[], nanoris=[])
char_dict["-"].valid_yomis.add("-")
char_dict["〇"] = KanjiYomi(kanji="〇", onyomis=['じゅう'],
                           kunyomis=['まる'], nanoris=[])
char_dict["别"] = KanjiYomi(kanji="别", onyomis=['べつ'], kunyomis=[], nanoris=[])
char_dict["宫"] = KanjiYomi(kanji="宫", onyomis=['きゅう'], kunyomis=[], nanoris=[])
char_dict["边"] = KanjiYomi(kanji="边", onyomis=['へん'], kunyomis=[], nanoris=[])
# ['が', 'か']
for character in kanjidic_root.findall("character"):
    kanji = character.find("literal").text
    onyomis = [jaconv.kata2hira(onyomi.text) for onyomi in character.findall(
        './/reading[@r_type="ja_on"]')]
    kunyomis = [kunyomi.text for kunyomi in character.findall(
        './/reading[@r_type="ja_kun"]')]
    nanoris = [nanori.text for nanori in character.findall(
        './/nanori')]
    kanji_yomi = KanjiYomi(kanji=kanji, onyomis=onyomis,
                           kunyomis=kunyomis, nanoris=nanoris)
    char_dict[kanji] = kanji_yomi

# special cases
char_dict["芽"].valid_yomis.add("げ")
char_dict["藍"].valid_yomis.add("あお")
# not sure whether necessary
char_dict["引"].valid_yomis.add("ひっ")
char_dict["突"].valid_yomis.add("つっ")
char_dict["吹"].valid_yomis.add("ふっ")
char_dict["三"].valid_yomis.add("しゃ")

# 猛: たけ.る

print(time()-start)
print(len(char_dict))


def fit(kanjis: str, hiragana: str):
    # if kanjis == "手引書":
    #     print("wow")
    yomis = [list(char_dict[kanji].valid_yomis) for kanji in kanjis]
    # print(yomis)
    # print(list(product(*yomis)))
    combos = list(map("".join, product(*yomis)))
    indices = list(product(*[range(len(x)) for x in yomis]))
    # print(combos)
    for combo in combos:
        if combo.startswith('とりか'):
            print(combo)
    if hiragana in combos:
        # print("YES!!!")
        # TODO: assert there is only one possible index arrangement
        idxs = indices[combos.index(hiragana)]
        # print(idxs)
        correct_yomis = [kanji_yomis[idx]
                         for kanji_yomis, idx in zip(yomis, idxs)]
        # print([correct_yomis])
        print(correct_yomis)
        return correct_yomis
# print(indices[idx])

# print(char_dict["柱"].valid_yomis)

# fit("友情", "ゆうじょう")
# fit("手数料", "てすうりょう")
# fit("旅行", "りょこう")
# fit("中国", "ちゅうごく")
# fit("立派", "りっぱ")
# fit("大雨", "おおあめ")
# fit("一匹", "いっぴき")
# fit("委託会社", "いたくがいしゃ")
# fit("本音", "ほんね")
# fit("一本道", "いっぽんみち")
# fit("手引書", "てびきしょ")
# fit("白葉枯病", "しらはがれびょう")
# fit("枯葉色", "かれはいろ")
# fit("橋橋", "はしばし")
# fit("切手", "きって")
# fit("御柱祭", "おんばしらさい")
# fit("法論", "ほうろん")
# fit("打合", "うちあわ")

# TODO: those containing "の" but not written in words!!!
# TODO: some rare number representations e.g. "八五"=="はちじゅうご"
