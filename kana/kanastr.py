from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence
import kanas


def safetyinnerwrapper_str2kana(kana_str: str) -> kanas.Kana:
    pass


class KanaStr:
    # TODO: frozen instance?

    def __init__(self, kanas: Sequence[kanas.Kana]) -> None:
        self.kanas: Tuple[kanas.Kana] = tuple(kanas)

    def __str__(self) -> str:
        return "".join(map(lambda kana: kana.symbol, self.kanas))

    def __len__(self) -> int:
        return len(self.kanas)

    def __eq__(self, other) -> bool:
        assert isinstance(other, KanaStr)
        return self.kanas == other.kanas

    def __getitem__(self, key):
        return self.kanas[key]

    def add(self, kana: Union[kanas.Kana, str]) -> KanaStr:
        if type(kana) == str:
            assert len(kana) == 1
        kana = safetyinnerwrapper_str2kana(kana)
        return KanaStr(kanas=self.kanas+(kana,))

    def extend(self, kanastr: KanaStr) -> None:
        # TODO: support string?
        return KanaStr(kanas=self.kanas+kanastr.kanas)

    def startswith_kana(self):
        pass

    def endswith_kana(self, kana: Union[kanas.Kana, str]):
        # TODO: support KanaStr and relaxed init
        kana = safetyinnerwrapper_str2kana(kana)
        return self.kanas[-1] == kana

    def dakuonize(self) -> KanaStr:
        # TODO: good to be present here? (seems y!)
        assert len(self) > 0
        return KanaStr(kanas=[self.kanas[0].dakuon]+self.kanas[1:])

    def sukuonize(self) -> KanaStr:
        assert len(self) > 0
        # TODO: not done yet
        last_kana = self.kanas[-1]
        if last_kana.sukuonizable():
            # TODO: this is only hiragana!!!
            return KanaStr(kanas=self.kanas[:-1] + [kanas.KANA_DICT['っ']])
        return self
