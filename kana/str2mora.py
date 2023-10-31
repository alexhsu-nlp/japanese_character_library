from kana import kanas, const, morastr
from typing import List, Tuple
from dataclasses import dataclass, field

# TODO: add punctuation into consideration?
# TODO: add ー
# NOTE: this is in fact an interface, and therefore indeed you should try to include everything
# TODO: should I add kanji here?


@dataclass
class MoraConstructionInfo:
    string: str
    moras: List[kanas.Mora] = field(default_factory=list)
    index: int = 0  # Note: index != len(moras)

    @property
    def current_char(self) -> str:
        return self.string[self.index]

    @property
    def next_char(self) -> str:
        return self.string[self.index + 1]

    @property
    def final_mora(self) -> kanas.Mora:
        return self.moras[-1]


def str2morastr(string: str) -> morastr.MoraStr:
    mora_info = MoraConstructionInfo(string=string)
    while mora_info.index < len(string):
        inc, mora = _get_inc_and_mora_main(mora_info=mora_info)
        mora_info.moras.append(mora)
        mora_info.index += inc
    return morastr.MoraStr(moras=mora_info.moras)


def _get_inc_and_mora_main(mora_info: MoraConstructionInfo) -> Tuple[int, kanas.Mora]:
    current_char = mora_info.current_char
    if mora_info.current_char == const.LONG_KATA_VOWEL_CHAR:
        # TODO: all of bugs
        long_kana = mora_info.final_mora.kana.dan.kana
        # TODO: final mora end sound
        if isinstance(mora_info.final_mora.kana, kanas.Katakana):
            return 1, kanas.Mora(
                kana=long_kana.katakana, sutegana=None)
        return 1, kanas.Mora(
            kana=long_kana, sutegana=None)
    itersymbol = const.ITER_SYMBOL_COLLECTION.itersymbolstr_dict.get(
        mora_info.current_char, None)
    if itersymbol is not None:
        return _get_inc_and_mora_case_itersymbol(mora_info=mora_info, itersymbol=itersymbol)
    if current_char not in kanas.KANA_DICT:
        return _get_inc_and_mora_case_sutegana(mora_info=mora_info)
    # current char in kana dict
    if mora_info.index < len(mora_info.string) - 1:
        return _get_inc_and_mora_case_kana(mora_info=mora_info)
    # last char in the string
    return 1, kanas.Mora(kana=kanas.KANA_DICT[current_char], sutegana=None)


def _get_inc_and_mora_case_itersymbol(mora_info: MoraConstructionInfo, itersymbol: const.IterSymbol) -> Tuple[int, kanas.Mora]:
    assert itersymbol.symbol != '々'  # This is for kanji
    assert mora_info.final_mora.sutegana is None
    assert itersymbol.is_hira == mora_info.final_mora.kana.is_hiragana()
    if itersymbol.voiced:
        return 1, kanas.Mora(
            kana=mora_info.final_mora.kana.dakuon, sutegana=None)
    # TODO: reduce voiceness
    return 1, kanas.Mora(
        kana=mora_info.final_mora.kana.rev_dakuon, sutegana=None)


def _get_inc_and_mora_case_sutegana(mora_info: MoraConstructionInfo) -> Tuple[int, kanas.Mora]:
    current_char = mora_info.current_char
    # TODO: why assert this?
    assert current_char in kanas.SUTEGANA_DICT
    # current char is a sutegana
    if current_char in ['っ', 'ッ']:
        return 1, kanas.Mora(
            kana=None, sutegana=kanas.SUTEGANA_DICT[current_char])
    assert mora_info.index >= 1
    if mora_info.final_mora.sutegana is None:
        assert kanas.SUTEGANA_DICT[current_char].hiragana.symbol == mora_info.final_mora.kana.dan.symbol
        return 1, kanas.Mora(
            kana=kanas.SUTEGANA_DICT[current_char].hiragana, sutegana=None)
    assert current_char == mora_info.final_mora.sutegana.symbol
    # TODO: avoid self-normalization?
    return 1, kanas.Mora(
        kana=mora_info.final_mora.sutegana.hiragana, sutegana=None)


def _get_inc_and_mora_case_kana(mora_info: MoraConstructionInfo) -> Tuple[int, kanas.Mora]:

    if mora_info.next_char in kanas.SUTEGANA_DICT:
        kana = kanas.KANA_DICT[mora_info.current_char]
        sutegana = kanas.SUTEGANA_DICT[mora_info.next_char]
        if kanas.Mora.is_valid_kana_sutegana_pair(kana=kana, sutegana=sutegana):
            return 2, kanas.Mora(kana=kana, sutegana=sutegana)
        return 1, kanas.Mora(
            kana=kanas.KANA_DICT[mora_info.current_char], sutegana=None)
    return 1, kanas.Mora(
        kana=kanas.KANA_DICT[mora_info.current_char], sutegana=None)


def morastr2hira(mora_str: morastr.MoraStr) -> morastr.MoraStr:
    moras: List[kanas.Mora] = []
    for mora in mora_str:
        assert isinstance(mora, kanas.Mora)
        kana = mora.kana.hiragana if mora.kana is not None else None
        sutegana = mora.sutegana.hiragana if mora.sutegana is not None else None
        moras.append(mora)
    return morastr.MoraStr(moras=moras)


def morastr2kata(mora_str: morastr.MoraStr) -> morastr.MoraStr:
    moras = []
    for mora in moras:
        assert isinstance(mora, kanas.Mora)
        kana = mora.kana.katakana if mora.kana is not None else None
        sutegana = mora.sutegana.kata if mora.sutegana is not None else None
        moras.append(mora)
    return morastr.MoraStr(moras=moras)
