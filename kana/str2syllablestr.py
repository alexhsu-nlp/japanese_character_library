from kana import kanas, kanastr
from typing import List, Tuple
from dataclasses import dataclass, field

# TODO: add punctuation into consideration?
# TODO: add ー
# NOTE: this is in fact an interface, and therefore indeed you should try to include everything
# TODO: should I add kanji here?


@dataclass
class SyllableConstructionInfo:
    string: str
    syllables: List[kanas.Syllable] = field(default_factory=list)
    index: int = 0  # Note: index != len(syllables)

    @property
    def current_char(self) -> str:
        return self.string[self.index]

    @property
    def next_char(self) -> str:
        return self.string[self.index + 1]

    @property
    def final_syllable(self) -> kanas.Syllable:
        return self.syllables[-1]

    # def append_syllable(self, syllable: kanas.Syllable) -> None:
    #     self.syllables.append(syllable)


def str2syllablestr(string: str) -> kanastr.SyllableStr:
    syllable_info = SyllableConstructionInfo(string=string)
    while syllable_info.index < len(string):
        inc, syllable = get_inc_and_syllable_main(syllable_info=syllable_info)
        syllable_info.syllables.append(syllable)
        syllable_info.index += inc
    return kanastr.SyllableStr(syllables=syllable_info.syllables)


def get_inc_and_syllable_main(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:
    current_char = syllable_info.current_char
    if current_char not in kanas.KANA_DICT:
        return get_inc_and_syllable_case_sutegana(syllable_info=syllable_info)
    # current char in kana dict
    elif syllable_info.index < len(syllable_info.string) - 1:
        return get_inc_and_syllable_case_kana(syllable_info=syllable_info)
    # last char in the string
    return 1, kanas.Syllable(kana=kanas.KANA_DICT[current_char], sutegana=None)


def get_inc_and_syllable_case_sutegana(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:
    current_char = syllable_info.current_char
    assert syllable_info.index >= 1 and current_char in kanas.SUTEGANA_DICT
    # current char is a sutegana
    if current_char in ['っ', 'ッ']:
        return 1, kanas.Syllable(
            kana=None, sutegana=kanas.SUTEGANA_DICT[current_char])
    if syllable_info.final_syllable.sutegana is None:
        assert kanas.SUTEGANA_DICT[current_char].hiragana.symbol == syllable_info.final_syllable.kana.dan.symbol
        return 1, kanas.Syllable(
            kana=kanas.SUTEGANA_DICT[current_char].hiragana, sutegana=None)
    assert current_char == syllable_info.final_syllable.sutegana.symbol
    # TODO: avoid self-normalization?
    return 1, kanas.Syllable(
        kana=syllable_info.final_syllable.sutegana.hiragana, sutegana=None)


def get_inc_and_syllable_case_kana(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:
    if syllable_info.next_char in kanas.SUTEGANA_DICT:
        tentative_syllable = kanas.Syllable(
            kana=kanas.KANA_DICT[syllable_info.current_char], sutegana=kanas.SUTEGANA_DICT[syllable_info.next_char])
        if tentative_syllable.check():
            return 2, tentative_syllable
        return 1, kanas.Syllable(
            kana=kanas.KANA_DICT[syllable_info.current_char], sutegana=None)
    return 1, kanas.Syllable(
        kana=kanas.KANA_DICT[syllable_info.current_char], sutegana=None)
