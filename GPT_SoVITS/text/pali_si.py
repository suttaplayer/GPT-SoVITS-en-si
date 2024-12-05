# This is a limited roman script pali transliteration 
# based on 
#   https://www.dhammatalks.org/books/ChantingGuide/Section0003.html 
# using only 
#   https://www.dhammatalks.org/suttas/ as reference source (see unique_charset below)
# 
# ash@sariputta-l:~/prj/dhammatalks.org-suttas/tools
#   $ node esm/show_unique_charset.js
#       'abcdeghijklmnoprstuvyñāīūḍḷṁṅṇṭ

# https://en.wiktionary.org/wiki/Appendix:Unicode/Sinhala
# https://www.nongnu.org/sinhala/doc/transliteration/sinhala-transliteration_4.html
# https://github.com/dmort27/epitran/blob/master/epitran/data/map/sin-Sinh.csv?plain=1
# https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary
# file:///home/ash/Downloads/problems/indic_nlp_resources_script_arpabet.pdf
# https://www.antvaset.com/arpabet-to-ipa
# https://www.antvaset.com/ipa-chart-with-audio
# https://www.antvaset.com/ipa-to-speech
# https://github.com/RVC-Boss/GPT-SoVITS/blob/main/GPT_SoVITS/text/english.py#L25
# https://ucsc.cmb.ac.lk/ltrl/downloads/SylTool.zip [User Guide.pdf]
# https://en.wikipedia.org/w/index.php?title=ARPABET
# https://chatgpt.com/c/6725b0e9-c8c8-8011-b36d-51bc036372ba
# https://gemini.google.com/app/40c94231ddea0667

#        abcdeghijklmnoprstuvyñāīūḍḷṁṅṇṭ
#  echo "අබ්ච්දෙඝිජ්ක්ල්ම්නොප්‍ර්ස්තුව්‍ය්ඤාඊඌඩ්ළ්ංඞ්ණ්ට්" | espeak-ng -v si --ipa -x -X -q
#   > ˈɐbtʃdeɡʰˌidʒklmnop rstˈuw jɲˌaːiːuːɖɭˈɐnuʂwˌaːɹəjəŋɳʈ

import re
from builtins import str as unicode

# Refer to symbols2.py for ARPABET scope (arpa = {...})

DICT = {
    "a": ["ʌ", "AH0"],
    "ā": ["aː", "AA1"],
    "æ": ["æ", "AE0"],
    "ǣ": ["æː", "AE1"],
    "i": ["i", "IH1"],
    "ī": ["iː", "IY1"],
    "u": ["u", "UH1"],
    "ū": ["uː", "UW1"],
    "e": ["ɛ", "EH1"],
    "ē": ["eː", "EY1"],
    "ai": ["ai", "AY1"],
    "o": ["o", "AO0"],
    "ō": ["ɔː", "OW1"],
    "au": ["aʊ", "AW1"],
    "k": ["k", "K"],
    "kh": ["kʰ", "K HH"],
    "g": ["g", "G"],
    "gh": ["gʱ", "G HH"],
    "ṅ": ["ŋ", "NG"],
    "ṅg": ["ŋg", "NG G"], # ⁿg = ṅg
    "c": ["tʃ", "CH"],
    "ch": ["tʃʰ", "CH HH"],
    "j": ["dʒ", "JH"],
    "jh": ["dʒʱ", "JH HH"],
    "ñ": ["ɲ", "Y"],
    "jñ": ["dʒɲ", "JH Y"],
    "ñj": ["ñdʒ","N JH"],
    "ṭ": ["ʈ", "T"],
    "ṭh": ["ʈʰ", "T HH"],
    "ḍ": ["ɖ", "D"],
    "ḍh": ["ɖʱ", "D HH"],
    "ṇ": ["ɳ", "N"],
    "t": ["θ", "TH"],
    "th": ["θʰ", "TH HH"],
    "d": ["ð", "DH"],
    "dh": ["ðʱ", "DH HH"],
    "n": ["n", "N"],
    "p": ["p", "P"],
    "ph": ["pʰ", "P HH"],
    "b": ["b", "B"],
    "bh": ["bʱ", "B HH"],
    "m": ["m", "M"],
    "y": ["j", "Y"],
    "r": ["ɾ", "R"],
    "l": ["l", "L"],
    "v": ["ʋ", "V"],
    "ś": ["ʒ", "ZH"],
    "ṣ": ["ʃ", "SH"],
    "s": ["s", "S"],
    "h": ["h", "HH"],
    "ḷ": ["l", "L R"],
    "f": ["f", "F"],
    "ṇḍ": ["ɳɖ","N D"],
    "ⁿd": ["ⁿd","N D HH"],
    "ᵐb": ["ᵐb","M B"],

}

sorted_keys = sorted(DICT.keys(), key=len, reverse=True)
# print("Sorted keys:", sorted_keys)

def text_normalize(text):
    # todo: eng text normalize
    rep_map = {
        "[;:：，；]": ",",
        '["’]': "'",
        "。": ".",
        "！": "!",
        "？": "?",
    }
    for p, r in rep_map.items():
        text = re.sub(p, r, text)
    text = unicode(text)
    return text


def g2p(text, idx=1, pad_start_end=False, remove_white_space = True):
    text = text_normalize(text)
    transcribed_phonetics = []
    i = 0
    while i < len(text):
        found = False
        for key in sorted_keys:
            if text[i:].startswith(key):
                val = DICT[key][idx]
                if (idx == 0):
                    transcribed_phonetics.append(val)
                else:
                    val = val.split(' ')
                    transcribed_phonetics.extend(val)
                i += len(key)
                found = True
                break
        if not found:
            appendChar = True
            if (remove_white_space and text[i] == " "):
                appendChar = False
            if (appendChar):    
                transcribed_phonetics.append(text[i])
            i += 1
    if pad_start_end:
        transcribed_phonetics = ["_"] + transcribed_phonetics + ["_"]
    return transcribed_phonetics
    
if __name__ == "__main__":
    # trans = g2p('rishi shashaṇka mihindu āshini keshā ', 1) # sañjaya
    # trans = g2p('abcdeghijklmnoprstuvyñāīūḍḷṁṅṇṭ', 1) # රිෂි, ෂෂංක, මිහින්දු
    trans = g2p('sañjaya', 1) # 
    print(trans)