from kana import kanas, kanastr
from typing import List

# TODO: add punctuation into consideration?
# TODO: add ー
# NOTE: this is in fact an interface, and therefore indeed you should try to include everything
# TODO: should I add kanji here?


def str2syllablestr(string: str) -> kanastr.SyllableStr:
    index = 0
    syllables: List[kanas.Syllable] = []
    while index < len(string):
        current_char = string[index]
        if current_char not in kanas.KANA_DICT:
            assert index >= 1 and current_char in kanas.SUTEGANA_DICT
            # current char is a sutegana
            if current_char in ['っ', 'ッ']:
                syllables.append(kanas.Syllable(
                    kana=None, sutegana=kanas.SUTEGANA_DICT[current_char]))
            elif syllables[index-1].sutegana is None:
                assert kanas.SUTEGANA_DICT[current_char].hiragana.symbol == syllables[index-1].kana.dan.symbol
                syllables.append(kanas.Syllable(
                    kana=kanas.SUTEGANA_DICT[current_char].hiragana, sutegana=None))
            else:
                assert current_char == syllables[index-1].sutegana.symbol
                # TODO: avoid self-normalization?
                syllables.append(kanas.Syllable(
                    kana=syllables[index-1].sutegana.hiragana, sutegana=None))
        # current char in kana dict
        elif index < len(string) - 1:
            next_char = string[index + 1]
            if next_char in kanas.SUTEGANA_DICT:
                tentative_syllable = kanas.Syllable(
                    kana=kanas.KANA_DICT[current_char], sutegana=kanas.SUTEGANA_DICT[next_char])
                if tentative_syllable.check():
                    syllables.append(tentative_syllable)
                    index += 1
                else:
                    syllables.append(kanas.Syllable(
                        kana=kanas.KANA_DICT[current_char], sutegana=None))
            else:
                syllables.append(kanas.Syllable(
                    kana=kanas.KANA_DICT[current_char], sutegana=None))
        else:  # last char in the string
            syllables.append(kanas.Syllable(
                kana=kanas.KANA_DICT[current_char], sutegana=None))
        index += 1
    return kanastr.SyllableStr(syllables=syllables)
