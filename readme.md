## the Japanese Character Library Project

Current status: Developing (incomplete; a basic version should be done before 2023.10.24 11:30 a.m. CST.) 

This is an extension of my NLP course project done in CUHK(SZ) in 2023.

The aim is to provide a means to analyze Japanese sentences with specialized Japanese character objects (*kana*s and *kanji*s) supported with some known Japanese linguistic rules.

This package/repository uses the [JMdict/EDICT](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) dictionary files. These files are the property of the [Electronic Dictionary Research and Development Group]((https://www.edrdg.org/)), and are used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).

---

[Remark: did not finish the original task plan on 2023.10.17, and the tentative deadline postpones to 2023.10.19 11:00 p.m. CST. One of the reasons of publishing this is, the repository may be never finished in 2023 without a formal publishment as motivation :(]

TODO List: (1-3: best before 2023.10.20)
- [] *youon* (拗音) and *gairaigo*-only syllabaries problem
- [] Settle down design of KanaStr
- [] Settle down design of *kanji*s based on kanjidic2 of the KANJIDIC project
- [] DP save all possible furiganas of words
- [] Treatment for corner cases of pronunciation
- [] Data reader support for the previously used corpus (https://github.com/ndl-lab/huriganacorpus-ndlbib)
- [] A simple and ugly interface
- [] Illustration of application: ruby generation for items of Korean-Japanese dictionary (https://korean.dict.naver.com/kojadict/)
- [] Basic Testings using Pytest

---

Other Reference websites:

https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/index.html

https://r12a.github.io/scripts/jpan/ja.html

https://en.wikipedia.org/wiki/Katakana#Extended_katakana