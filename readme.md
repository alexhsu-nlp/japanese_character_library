## the Japanese Character Library Project

Current status: Developing (incomplete; a basic version should be done before 2023.10.24 11:30 a.m. CST.) 

This is an extension of my NLP course project done in CUHK(SZ) in 2023.

The aim is to provide a means to analyze Japanese sentences with specialized Japanese character objects (*kana*s and *kanji*s) supported with some known Japanese linguistic rules.

This package/repository uses the [JMdict/EDICT](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) dictionary files. These files are the property of the [Electronic Dictionary Research and Development Group]((https://www.edrdg.org/)), and are used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).

---

TODO List:
- [x] *youon* (拗音) and *gairaigo*-only syllabaries problem (*sutegana* problem)
- [ ] Treatment of "half-voiced" sounds (半濁音) (ぱぴぷぺぽ)
- [x] Convertor considering edge cases of *sutegana*s as the basis for SyllableStr
- [ ] Refactor the convertor above, add 'ー' (long vowel sound) treatment (how to deal with surface and real?)
- [ ] Settle down design of JapaneseStr: including primitive *kanji*s
- [ ] Settle down design of *kanji*s based on kanjidic2 of the KANJIDIC project
- [ ] DP save all possible furiganas of words
- [ ] Treatment for corner cases of pronunciation
- [ ] Data reader support for the previously used corpus (https://github.com/ndl-lab/huriganacorpus-ndlbib)
- [ ] A simple demo using jupyter notebook
- [ ] Illustration of application: ruby generation for items of Korean-Japanese dictionary (https://korean.dict.naver.com/kojadict/)
- [ ] Basic Testings using Pytest
- [ ] Incorporate the old Japanese *kana* style (歴史的仮名遣い)
- [ ] Iteration marks (踊り字): 々, ゝ, ゞ, ヽ, ヾ 
- [ ] List of common special symbols: 〆 (しめ), ゟ (より), ヿ (こと), 〇 (れい), and the problem of ヵ/ヶ.
---

Other reference websites:

- https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/index.html
- https://r12a.github.io/scripts/jpan/ja.html
- https://en.wikipedia.org/wiki/Katakana#Extended_katakana
- https://ja.wikipedia.org/wiki/%E6%8D%A8%E3%81%A6%E4%BB%AE%E5%90%8D
- https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97
- https://www.youtube.com/watch?v=A-zL6VuJbjc
- https://nihon5kyoushi.com/2018/05/29/%E4%BF%83%E9%9F%B3%E4%BE%BF%E3%81%AE%E5%95%8F%E9%A1%8C/
- https://ja.wikipedia.org/wiki/%E8%B8%8A%E3%82%8A%E5%AD%97#%E3%82%9D%E3%81%A8%E3%83%BD%EF%BC%88%E4%B8%80%E3%81%AE%E5%AD%97%E7%82%B9%EF%BC%89