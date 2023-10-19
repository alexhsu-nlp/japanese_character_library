from kana import kanas, kanastr


def str2syllablestr(string: str) -> kanastr.SyllableStr:
    index = 0
    syllables = []
    while True:
        if index < len(string) - 1:
            current_char, next_char = string[index], string[index+1]
            if current_char not in kanas.KANA_DICT:
                if True:
                    pass
                else:
                    raise ValueError
            if next_char in kanas.SUTEGANA_DICT:
                tentative_syllable = kanas.Syllable(kana=kanas.KANA_DICT[current_char], sutegana=kanas.SUTEGANA_DICT[next_char])
