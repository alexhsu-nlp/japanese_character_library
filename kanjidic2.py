from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence, Set, Optional
from kana.kanas import KANA_DICT, Hiragana, Katakana, Gyou, Dan, Kana, JapaneseCharacter, SUTEGANAS, JapaneseUnit, Mora
from kana.morastr import MoraStr, SequenceContainer
from kana.str2mora import str2morastr, morastr2hira, morastr2kata, MoraConstructionInfo
from pathlib import Path


# TODO: incorporate Yomis into Kanjis

# Needs refactoring the ideas


@dataclass
class JapaneseCharRecord:
    surface: str
    inner: JapaneseUnit  # JointKanjiJukugo or Mora (normalized)
    pron: MoraStr  # TODO: since JapaneseUnit already has pron this is not needed?
    strict: bool  # whether the pronunciation has basis


class JapaneseCharRecordStr(SequenceContainer):
    # NOTE: a class similar to MoraStr
    # This will be the output of the program
    # TODO: two kanji one yomi??? do I need kanjistr?
    def __init__(self, container: Sequence[JapaneseCharRecord]) -> None:
        super().__init__(container)


@dataclass(frozen=True)
class JointKanjiJukugo(JapaneseUnit):
    # Idea: call the characters (kanas, suteganas, symbols) characters, and call combined ones (moras, etc.) `units`
    kanjis: List[Kanji]
    pron: Optional[MoraStr] = None

    def __str__(self):
        return "".join(map(lambda kanji: kanji.symbol, self.kanjis))


@dataclass
class Kanji(JapaneseCharacter):
    symbol: str
    yomi: Yomi

# def safetyinnerwrapper_str2kana(kana: Union[Kana, str]):
#     if isinstance(kana, str):
#         assert kana in KANA_DICT
#         kana = KANA_DICT[kana]
#     return kana

# TODO: this idea is still not mature


class Yomi:

    @property
    def pron_set(self) -> Set[MoraStr]:
        raise NotImplementedError


@dataclass
class KanjiDic2Yomi(Yomi):
    # TODO: replace these with hiraganas!!!
    # TODO: what about "-"?
    main: MoraStr

    def __str__(self):
        return str(self.main)

    # def gen_dakuonize(self) -> KanjiDic2Yomi:
    #     # TODO: 'gen' not done
    #     # TODO: put prev into sth different?
    #     # TODO: type(self)?
    #     return KanjiDic2Kunyomi(main=self.main.dakuonize(), tail=self.tail)


# def str2kanastr(string: str) -> MoraStr:
#     str_ind = 0
#     len_str = len(string)
#     kanas = []
#     while str_ind < len_str:
#         if str_ind + 1 < len_str and string[str_ind + 1] in SUTEGANAS:
#             kana_str = string[str_ind: str_ind + 2]
#             str_ind += 2
#         else:
#             kana_str = string[str_ind]
#             str_ind += 1
#         kanas.append(KANA_DICT[kana_str])
#     return MoraStr(kanas=kanas)


def kanjidic2_kunyomistr2obj(kunyomi_str: str):
    # TODO: need to redesign
    # this is different
    as_prefix = as_suffix = False
    if kunyomi_str.startswith('-'):
        as_suffix = True
        kunyomi_str = kunyomi_str[1:]
    elif kunyomi_str.endswith('-'):
        as_prefix = True
        kunyomi_str = kunyomi_str[-1:]
    dot_split = kunyomi_str.split('.')
    if len(dot_split) == 1:
        dot_split.append('')
    assert len(dot_split) == 2
    main_kanastr = str2morastr(string=dot_split[0])
    tail_kanastr = str2morastr(string=dot_split[1])
    if len(tail_kanastr) != 0 and tail_kanastr[-1].dan == KANA_DICT['う']:
        return KanjiDic2KunyomiVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)
    return KanjiDic2KunyomiNonVerb(main=main_kanastr, tail=tail_kanastr, as_prefix=as_prefix, as_suffix=as_suffix)


@dataclass
class KanjiDic2Kunyomi(KanjiDic2Yomi):
    # NOTE: this is only for one listed kunyomi (a kanji may have multiples), rather than their aggregrates
    as_prefix: bool = False
    as_suffix: bool = False
    tail: Optional[MoraStr] = None  # TODO: None or empty? now empty

    def __str__(self):
        if self.tail is None:
            return str(self.main)
        return str(self.main + self.tail)

    def __str__(self):
        if self.tail is not None:
            # TODO: self.tail should be MoraStr
            tail_part = '.' + str(self.tail)
        else:
            tail_part = ''
        return f"{'-' if self.as_suffix else ''}{self.main}{tail_part}{'-' if self.as_prefix else ''}"

    @property
    def pos(self):
        # TODO: since divide them below into specific classes, no need to do this?
        pass

    @property
    def normal(self) -> MoraStr:
        if self.tail is None:
            return self.main
        return self.main + self.tail

    # @property
    # def pron_set(self) -> Set[MoraStr]:
    #     # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
    #     raise NotImplementedError


@dataclass
class KanjiDic2KunyomiVerb(KanjiDic2Kunyomi):
    # TODO: middle Japanese verbs
    # TODO: put middle and modern under the same verb
    # TODO: how to deal with `as_prefix` and `as_suffix`

    def __post_init__(self):
        assert self.tail is not None

    def is_godan(self) -> bool:
        return not self.is_ichidan()

    def is_ichidan(self) -> bool:
        return len(self.tail) >= 2 and self.tail[-1].sutegana is None and self.tail[-1].kana == KANA_DICT['る'] and self.tail[-2].dan.symbol in ('え', 'い')

    @property
    def renyou(self) -> MoraStr:
        # TODO: make this a yomi?
        # TODO: new idea: make this under MoraStr???
        # Ans: sorry you do not know where is the main where is the others
        if self.is_ichidan():
            return self.main + self.tail[:-1]
        return self.main + self.tail.change_end_dan(dan='い')

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        min_set = {self.normal, self.renyou, self.main}
        for element in list(min_set):
            min_set.add(element.dakuonize())
        return min_set


@dataclass
class KanjiDic2KunyomiNonVerb(KanjiDic2Kunyomi):
    # either 名詞 形容詞(`.い`, `.しい`) or 形容動詞

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        return {self.main,
                self.main.dakuonize(),
                self.normal,
                self.main.dakuonize(),
                self.main.handakuonize(),
                self.normal.handakuonize()}


@dataclass
class KanjiDic2Onyomi(KanjiDic2Yomi):

    def __str__(self):
        return str(self.main)

    @property
    def pron_set(self) -> Set[MoraStr]:
        # NOTE: this is a set of pronunciations derivable from the given yomi, such as たかい => だかい.
        return {self.main,
                self.main.dakuonize(),
                self.main.sokuonize(),
                self.main.dakuonize().sokuonize(),
                self.main.handakuonize(),
                self.main.handakuonize().sokuonize()}


class KanjiDic2Nanori(KanjiDic2Yomi):

    @property
    def pron_set(self) -> Set[MoraStr]:
        return {self.main, self.main.dakuonize(), self.main.handakuonize()}


@dataclass
class KanjiDic2KanjiCollectedYomi(Yomi):
    # TODO: should i get rid of the list?
    # TODO: transform when appropriate or in advance?
    # TODO: set or list?

    # TODO: do you need to distinguish these two? Y?
    kunyomi_verbs: List[KanjiDic2KunyomiVerb]
    kunyomi_nonverbs: List[KanjiDic2KunyomiNonVerb]
    onyomis: List[KanjiDic2Onyomi]
    nanoris: List[KanjiDic2Nanori]

    def __post_init__(self):
        self._yomis_all: List[KanjiDic2Yomi] = self.kunyomi_verbs + \
            self.kunyomi_nonverbs + self.onyomis + self.nanoris

    @property
    def pron_set(self) -> Set[MoraStr]:
        pron_set: Set[MoraStr] = set()
        for verb in self._yomis_all:
            # print('in verb:', verb, verb.pron_set)
            pron_set = pron_set.union(verb.pron_set)
        return pron_set


@dataclass
class KunyomiInfo:
    main: MoraStr
    tail: Optional[MoraStr]

    def is_kunyomi_verb(self) -> bool:
        if self.tail is None:
            return False
        final_mora: Mora = self.tail[-1]
        return final_mora.sutegana is None and final_mora.kana.dan.symbol == 'う'


def kunyomistr2yomi(kunyomi_str: str) -> KanjiDic2Kunyomi:
    as_prefix = (kunyomi_str[0] == '-')
    as_suffix = (kunyomi_str[-1] == '-')
    kunyomi_str_strip = kunyomi_str.strip('-')
    if '.' not in kunyomi_str_strip:
        # TODO: did not pay attention to `as_prefix` and `as_suffix` in pron_set?
        return KanjiDic2KunyomiNonVerb(main=str2morastr(kunyomi_str_strip), as_prefix=as_prefix, as_suffix=as_suffix, tail=None)
    parts = kunyomi_str_strip.split('.')
    assert len(parts) == 2
    main_str, tail_str = parts
    main = str2morastr(main_str)
    tail = str2morastr(tail_str)
    kunyomi_info = KunyomiInfo(main=main, tail=tail)
    if kunyomi_info.is_kunyomi_verb():
        return KanjiDic2KunyomiVerb(main=kunyomi_info.main, as_prefix=as_prefix, as_suffix=as_suffix, tail=kunyomi_info.tail)
    return KanjiDic2KunyomiNonVerb(main=kunyomi_info.main, as_prefix=as_prefix, as_suffix=as_suffix, tail=kunyomi_info.tail)


def _get_kanjidic2_dict() -> Dict[str, Kanji]:
    import time
    from xml.etree.ElementTree import ElementTree

    start = time.time()

    kanji_dict: Dict[str, Kanji] = {}
    KANJIDIC_PATH_STR = Path("kanjidic2/kanjidic2.xml")

    kanjidic_root = ElementTree().parse(KANJIDIC_PATH_STR)
    for character in kanjidic_root.findall("character"):
        kanji_str = character.find("literal").text
        assert kanji_str is not None
        kanji_str

        # 2. identify verb or n verb for `.` items
        # NOTE: kuns are hiraganas, ons are katakanas
        onyomis = [KanjiDic2Onyomi(main=morastr2hira(str2morastr(onyomi_element.text.strip('-')))) for onyomi_element in character.findall(
            './/reading[@r_type="ja_on"]')]
        # TODO: sth special for kunyomi
        kunyomis = [kunyomistr2yomi(kunyomi.text) for kunyomi in character.findall(
            './/reading[@r_type="ja_kun"]')]
        kunyomi_verbs = list(filter(lambda kunyomi: isinstance(
            kunyomi, KanjiDic2KunyomiVerb), kunyomis))
        kunyomi_nonverbs = list(filter(lambda kunyomi: isinstance(
            kunyomi, KanjiDic2KunyomiNonVerb), kunyomis))

        nanoris = [KanjiDic2Nanori(main=str2morastr(nanori.text.replace('.', ''))) for nanori in character.findall(
            './/nanori')]
        full_yomi = KanjiDic2KanjiCollectedYomi(
            kunyomi_verbs=kunyomi_verbs, kunyomi_nonverbs=kunyomi_nonverbs,
            onyomis=onyomis,
            nanoris=nanoris
        )
        kanji_dict[kanji_str] = Kanji(symbol=kanji_str, yomi=full_yomi)

    end = time.time()
    time_lapse = round(end-start, 2)
    print(f"KanjiDict2 loading done. Time taken: {time_lapse}s.")
    # kanji_yomi = KanjiDic2KanjiCollectedYomi(kanji=kanji, onyomis=onyomis,
    #                                          kunyomis=kunyomis, nanoris=nanoris)
    # char_dict[kanji] = kanji_yomi
    return kanji_dict


KANJI_DICT = _get_kanjidic2_dict()

print('testing')
print(KANJI_DICT['長'].yomi.pron_set)
print(KANJI_DICT['引'].yomi.pron_set)
print(KANJI_DICT['暗'].yomi.pron_set)
print(KANJI_DICT['白'].yomi.pron_set)
print(KANJI_DICT['翔'].yomi.pron_set)

# # TODO: 3. problem of changing sound in onyomi [3 possible sounds] [ki.ku.ti.tu] [hatuonbin]
# # TODO: 4. problem of changing sound in kunyomi


@dataclass
class StrWithPron:
    str: str
    pron: str


def str2record(string: StrWithPron) -> JapaneseCharRecord:
    # TODO: dynamic programming
    # Tentative pesudocoode Algorithm:
    # for each character:
    #     if it is a kanji:
    #        include it in present kanji flow
    #
    MoraConstructionInfo(string=string)
    pass
