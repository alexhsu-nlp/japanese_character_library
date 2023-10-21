from kana import kanas, kanastr, const
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


def str2syllablestr(string: str) -> kanastr.SyllableStr:
    syllable_info = SyllableConstructionInfo(string=string)
    while syllable_info.index < len(string):
        inc, syllable = _get_inc_and_syllable_main(syllable_info=syllable_info)
        syllable_info.syllables.append(syllable)
        syllable_info.index += inc
    return kanastr.SyllableStr(syllables=syllable_info.syllables)


def _get_inc_and_syllable_main(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:
    current_char = syllable_info.current_char
    if syllable_info.current_char == const.LONG_KATA_VOWEL_CHAR:
        # TODO: all of bugs
        long_kana = syllable_info.final_syllable.kana.dan.kana
        # TODO: final syllable end sound
        if isinstance(syllable_info.final_syllable.kana, kanas.Katakana):
            return 1, kanas.Syllable(
                kana=long_kana.katakana, sutegana=None)
        return 1, kanas.Syllable(
            kana=long_kana, sutegana=None)
    itersymbol = const.ITER_SYMBOL_COLLECTION.itersymbolstr_dict.get(
        syllable_info.current_char, None)
    if itersymbol is not None:
        return _get_inc_and_syllable_case_itersymbol(syllable_info=syllable_info, itersymbol=itersymbol)
    if current_char not in kanas.KANA_DICT:
        return _get_inc_and_syllable_case_sutegana(syllable_info=syllable_info)
    # current char in kana dict
    if syllable_info.index < len(syllable_info.string) - 1:
        return _get_inc_and_syllable_case_kana(syllable_info=syllable_info)
    # last char in the string
    return 1, kanas.Syllable(kana=kanas.KANA_DICT[current_char], sutegana=None)


def _get_inc_and_syllable_case_itersymbol(syllable_info: SyllableConstructionInfo, itersymbol: const.IterSymbol) -> Tuple[int, kanas.Syllable]:
    assert itersymbol.symbol != '々'  # This is for kanji
    assert syllable_info.final_syllable.sutegana is None
    assert itersymbol.is_hira == syllable_info.final_syllable.kana.is_hiragana()
    if itersymbol.voiced:
        return 1, kanas.Syllable(
            kana=syllable_info.final_syllable.kana.dakuon, sutegana=None)
    # TODO: reduce voiceness
    return 1, kanas.Syllable(
        kana=syllable_info.final_syllable.kana.rev_dakuon, sutegana=None)


def _get_inc_and_syllable_case_sutegana(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:
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


def _get_inc_and_syllable_case_kana(syllable_info: SyllableConstructionInfo) -> Tuple[int, kanas.Syllable]:

    if syllable_info.next_char in kanas.SUTEGANA_DICT:
        kana = kanas.KANA_DICT[syllable_info.current_char]
        sutegana = kanas.SUTEGANA_DICT[syllable_info.next_char]
        if kanas.Syllable.is_valid_kana_sutegana_pair(kana=kana, sutegana=sutegana):
            return 2, kanas.Syllable(kana=kana, sutegana=sutegana)
        return 1, kanas.Syllable(
            kana=kanas.KANA_DICT[syllable_info.current_char], sutegana=None)
    return 1, kanas.Syllable(
        kana=kanas.KANA_DICT[syllable_info.current_char], sutegana=None)
