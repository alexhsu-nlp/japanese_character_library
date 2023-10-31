from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Union, List, Tuple, Dict, Sequence, TypeVar, Generic, Iterable
from typing_extensions import Self
from kana import kanas


# TODO: now we have two types of formation:
# 1. (surface-morastr)
# 2. (surface-mora)s
# It seems that 2 is impossible due to jukujikun (熟字訓)
# TODO: collection of morastrs???

T = TypeVar('T')


class SequenceContainer(Generic[T]):

    def __init__(self, container: Sequence[T]) -> None:
        self._container: Tuple[T] = tuple(container)

    def __len__(self) -> int:
        return len(self._container)

    def __eq__(self, other) -> bool:
        assert isinstance(other, self.__class__)
        return self._container == other._container

    def __getitem__(self, key) -> T:
        if isinstance(key, int):
            return self._container[key]
        elif isinstance(key, slice):
            # TODO: this may be buggy in the future
            return self.__class__(self._container.__getitem__(key))
        raise NotImplementedError

    def add(self, element: T) -> Self:
        # assert isinstance(element, T)
        # kana = safetyinnerwrapper_str2kana(kana)
        return self.__class__(self._container + (element,))

    def __add__(self, other) -> Self:
        # TODO: support string?
        assert isinstance(other, self.__class__)
        return self.__class__(self._container + other._container)

    def __iter__(self) -> Iterable[T]:
        return self._container.__iter__()


class MoraStr(SequenceContainer):
    # TODO: frozen instance?

    def __init__(self, moras: Sequence[kanas.Mora]) -> None:
        super().__init__(container=moras)
        # self.moras: Tuple[kanas.Mora] = tuple(moras)

    def __repr__(self) -> str:
        return f"MoraStr<{self}>"

    def __str__(self) -> str:
        return "".join(map(str, self._container))

    def __hash__(self) -> int:
        return hash(tuple(self._container))

    @property
    def start_gyou(self) -> kanas.Gyou:
        return self[0].gyou

    @property
    def end_dan(self) -> kanas.Dan:
        return self[-1].dan

    def change_end_dan(self, dan: Union[kanas.Dan, str]) -> MoraStr:
        # TODO: how to get dan easily
        if len(self) == 0:
            return self  # TODO: should I copy it?
        return self[:-1].add(self[-1].change_dan(dan=dan))

    def dakuonize(self) -> MoraStr:
        # TODO: good to be present here? (seems y!)
        assert len(self) > 0
        return MoraStr(moras=[self[0].dakuon]+list(self[1:]))

    def handakuonize(self) -> MoraStr:
        # TODO: good to be present here? (seems y!)
        assert len(self) > 0
        return MoraStr(moras=[self[0].handakuon]+list(self[1:]))

    def can_sokuonize(self) -> bool:
        if self[-1].can_sokuonize():
            if len(self) >= 2 and self[-1].kana.symbol in ['う', 'ウ'] and self[-2].sutegana.symbol not in ['ゅ', 'ユ']:
                # TODO: じっ, にっ
                return False
            return True
        return False

    def sokuonize(self) -> MoraStr:
        # TODO: should I make this a binary stuff?
        # assert self.can_sokuonize()
        if not self.can_sokuonize():
            return self
        assert len(self) > 0
        last_mora: kanas.Mora = self[-1]
        if last_mora.kana.is_hiragana():
            # TODO: remove hardcoding
            return MoraStr(moras=self[:-1].add(kanas.Mora(kanas.KANA_DICT['っ'])))
        elif last_mora.kana.is_katakana():
            return MoraStr(moras=self[:-1].add(kanas.Mora(kanas.KANA_DICT['ッ'])))
