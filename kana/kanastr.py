from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence
from kana import kanas

# TODO: now we have two types of formation:
# 1. (surface-syllablestr)
# 2. (surface-syllable)s
# It seems that 2 is impossible due to jukujikun (熟字訓)
# TODO: collection of syllablestrs???


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
        if isinstance(key, int):
            return self.syllables[key]
        elif isinstance(key, slice):
            return SyllableStr(syllables=self.syllables.__getitem__(key))
        raise ValueError('invalid key of SyllableStr')

    def add(self, syllable: kanas.Syllable) -> SyllableStr:
        # kana = safetyinnerwrapper_str2kana(kana)
        return SyllableStr(syllable == self.syllables+(syllable,))

    def extend(self, syllablestr: SyllableStr) -> None:
        # TODO: support string?
        return SyllableStr(syllables=self.syllables+syllablestr.syllables)

    @property
    def start_gyou(self) -> kanas.Gyou:
        return self[0].gyou

    @property
    def end_dan(self) -> kanas.Dan:
        return self[-1].dan

    def change_end_dan(self, dan: Union[kanas.Dan, str]):
        # TODO: how to get dan easily
        if len(self) == 0:
            return self  # TODO: should I copy it?
        return self[:-1].add(self[-1].change_dan(dan=dan))

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

    def can_sokuonize(self) -> bool:
        if self.syllables[-1].can_sokuonize():
            if self.kana.symbol in ['う', 'ウ'] and self.sutegana.symbol not in ['ゅ', 'ユ']:
                # TODO: じっ, にっ
                return False
            return True
        return False

    def sokuonize(self) -> SyllableStr:
        # TODO: should I make this a binary stuff?
        assert self.can_sokuonize()
        assert len(self) > 0
        last_syllable = self.syllables[-1]
        if last_syllable.kana.is_hiragana():
            # TODO: remove hardcoding
            return SyllableStr(syllables=self[:-1].add(kanas.Syllable(kanas.KANA_DICT['っ'])))
        elif last_syllable.kana.is_katakana():
            return SyllableStr(syllables=self[:-1].add(kanas.Syllable(kanas.KANA_DICT['ッ'])))
        # if last_kana.sukuonizable():
        #     # TODO: this is only hiragana!!!
        #     return SyllableStr(kanas=self.syllables[:-1] + [kanas.KANA_DICT['っ']])
        # return self
