from kana.const import ITER_SYMBOL_COLLECTION, IterSymbol


class TestConst:

    def test_itersymbol(self):
        for string, symbol in ITER_SYMBOL_COLLECTION.itersymbolstr_dict.items():
            assert isinstance(string, str)
            assert isinstance(symbol, IterSymbol)

        # print(ITER_SYMBOL_COLLECTION.itersymbolstr_dict['ヾ'])
