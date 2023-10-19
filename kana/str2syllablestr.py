from kana import kanas, kanastr
from typing import List

# TODO: add punctuation into consideration?


def str2syllablestr(string: str) -> kanastr.SyllableStr:
    index = 0
    syllables: List[kanas.Syllable] = []
    while index < len(string):
        current_char = string[index]
        if current_char not in kanas.KANA_DICT:
            print("char not in kanadict")
            if index >= 1 and current_char in kanas.SUTEGANA_DICT:
                # current char is a sutegana

                if syllables[index-1].sutegana is None:
                    if kanas.SUTEGANA_DICT[current_char].hiragana.symbol == syllables[index-1].kana.dan.symbol:
                        print('special none')
                        syllables.append(kanas.Syllable(
                        kana=kanas.SUTEGANA_DICT[current_char].hiragana, sutegana=None))
                    else:
                        raise ValueError
                elif current_char == syllables[index-1].sutegana.symbol:
                    # TODO: avoid self-normalization?
                    syllables.append(kanas.Syllable(
                        kana=syllables[index-1].sutegana.hiragana, sutegana=None))
                else:
                    raise ValueError
            else:
                raise ValueError
        # current char in kana dict
        elif index < len(string) - 1:
            print('char in dict and not final')
            next_char = string[index + 1]
            if next_char in kanas.SUTEGANA_DICT:
                print('next char is a sutegana')
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
            print('char in dict, final')
            syllables.append(kanas.Syllable(
                kana=kanas.KANA_DICT[current_char], sutegana=None))
        index += 1
        print("CURRENT:", syllables)
    return kanastr.SyllableStr(syllables=syllables)
