from kana import kanas


def kanastr2kana(string: str) -> kanas.Kana:
    return kanas.KANA_DICT[string]
