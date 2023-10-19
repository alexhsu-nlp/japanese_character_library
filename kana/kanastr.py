from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence
from kana import kanas


# def safetyinnerwrapper_str2kana(kana_str: str) -> kanas.Kana:
#     pass


class SyllableStr:
    # TODO: frozen instance?

    def __init__(self, syllables: Sequence[kanas.Syllable]) -> None:
        self.syllables: Tuple[kanas.Syllable] = tuple(syllables)

    def __str__(self) -> str:
        return "".join(map(str, self.syllables))

    def __len__(self) -> int:
        return len(self.syllables)

    def __eq__(self, other) -> bool:
        assert isinstance(other, SyllableStr)
        return self.syllables == other.syllables

    def __getitem__(self, key):
        return self.syllables[key]

    def add(self, syllable: kanas.Syllable) -> SyllableStr:
        # kana = safetyinnerwrapper_str2kana(kana)
        return SyllableStr(syllable == self.syllables+(syllable,))

    def extend(self, kanastr: SyllableStr) -> None:
        # TODO: support string?
        return SyllableStr(kanas=self.syllables+kanastr.syllables)

    # def startswith_kana(self):  # TODO: isn't this a waste word?
    #     pass

    # def endswith_kana(self, kana: Union[kanas.Kana, str]):
    #     # TODO: support SyllableStr and relaxed init
    #     kana = safetyinnerwrapper_str2kana(kana)
    #     return self.syllables[-1] == kana

    def dakuonize(self) -> SyllableStr:
        # TODO: good to be present here? (seems y!)
        assert len(self) > 0
        return SyllableStr(kanas=[self.syllables[0].dakuon]+self.syllables[1:])

    def sukuonize(self) -> SyllableStr:
        assert len(self) > 0
        # TODO: not done yet
        last_syllable = self.syllables[-1]
        # if last_kana.sukuonizable():
        #     # TODO: this is only hiragana!!!
        #     return SyllableStr(kanas=self.syllables[:-1] + [kanas.KANA_DICT['っ']])
        # return self
