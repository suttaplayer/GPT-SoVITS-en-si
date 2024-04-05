# from https://github.com/dmort27/epitran/blob/master/epitran/data/map/sin-Sinh.csv?plain=1
# https://en.wikipedia.org/wiki/CMU_Pronouncing_Dictionary

CONSTANTS = {
    "a": ["ə", "AH0"], # අ,a
    "ṁ": ["ŋ", "NG"], # ං,ŋ 
    "ḥ": ["h", "HH"], # ඃ,h
}

ANNOTATABLES = {
    "k": ["k", "K"], # ක,kV
    "ṭ": ["ʈ", "T"], # ට,ʈV
    "t": ["θ", "TH"], # ත,tV
    "p": ["p", "P"], # ප,pV
    "g": ["ɡ", "G"], # ග,ɡV
    "ḍ": ["ɖ", "D"], # ඩ,ɖV
    "d": ["ð", "DH"], # ද,dV
    "b": ["b", "B"], # බ,bV
    "s": ["s", "S"], # ස,sV
    "c": ["t͡ʃ", "CH"], # ච,t͡ʃV
    "m": ["m", "M"], # ම,mV
    "l": ["l", "L"], # ල,lV
    "v": ["v", "V"], # ව,vV
    "v": ["w", "W"], # ව,--- added for w support
    "ṇ": ["ɳ", "N"], # ණ,ɳV
    "h": ["h", "H"], # හ,hV
    "j": ["d͡ʒ", "JH"], # ජ,d͡ʒV
    "n": ["n", "N"], # න,nV
    "r": ["ɹ", "R"], # ර,rV
    "y": ["j", "Y"], # ය,jV
    "ḷ": ["ɭ", "L"], # ළ,ɭV
    "kh": ["kʰ", "K"], # ඛ,kV
    "ṭh": ["ʈʰ", "T"], # ඨ,ʈV (same as ṭ)
    "th": ["θ", "TH"], # ථ,tV
    "ph": ["pʰ", "P"], # ඵ,pV
    "gh": ["ɡʰ", "G"], # ඝ,gV
    "ḍh": ["ɖʰ", "D"], # ඪ,ɖV
    "dh": ["ð", "DH"], # ධ,dV
    "bh": ["bʰ", "B"], # භ,bV
    "ś": ["ʃ", "SH"], # ශ,sV
    "ch": ["t͡ʃʰ", "CH"], # ඡ,t͡ʃV
    "ñ": ["ɲ", "N Y"], # ඤ,ɲV (split ARPABET)
    "ng": ["ŋ", "NG"], # ඞ,ŋV
    "ṅ": ["ŋ", "NG"], # ඞ,ŋV (addition)
    "ñj": ["ɲd͡ʒ", "N Y JH"], # ඦ,nd͡ʒV
    "ş": ["ʃ", "SH"], # ෂ,sV
    "jh": ["d͡ʒʰ", "JH"], # ඣ,d͡ʒV
    "jñ": ["jn", "Y N"], # ඥ,d͡ʒɲV
    "f": ["f", "F"], # ෆ,fa
    "p": ["p", "P"], # ප,fa
    "ⁿg": ["ᵑɡ", "NG"], # ඟ,ŋɡV
    "ⁿḍ": ["ɳɖ", "N D"], # ඬ,ɳɖV
    "ⁿd": ["ⁿd", "N D"], # ඳ,ndV
    "n̆d": ["ⁿd", "N D"], # ඳ,ndV (addition)
    "ᵐb": ["ᵐb", "M B"], # ඹ,mbV
    "n̆g": ["ᵑɡ", "NG"], # ඟ,ŋɡV
    "n̆ḍ": ["ɳɖ", "N D"], # ඬ,ɳɖV
    "n̆d": ["ⁿd", "N D"], # ඳ,ndV (addition)
    "m̆b": ["ᵐb", "M B"], # ඹ,mbV
}

ANNOTATIONS = {
    "ai": ["aɪ", "AY"], # ඓ,ai
    "au": ["aʊ", "AW"], # ඖ,au
    # "ru": ["ɪɹu", "IH R UW"], # ඍ,ur
    # "rū": ["ruː", "R UW UW"], # ඎ,ruː
    # "li": "li", # ඏ,li
    # "lī": "liː", # ඐ,liː
    "ā": ["aː", "AA"], # ආ, ɑː
    "æ": ["æ", "AE"], # ඇ,æ
    "i": ["i", "IH"], # ඉ,i
    "u": ["u", "UW"], # උ,u
    "e": ["e", "EY"], # එ,e
    "o": ["o", "OW"], # ඔ,o
    "ǣ": ["æː", "AE"], # ඈ,æː
    "ī": ["iː", "IY"], # ඊ,iː
    "ū": ["uː", "UW"], # ඌ,uː
    "ē": ["eː", "EH"], # ඒ,eː
    "ō": ["oː", "OW"], # ඕ,oː
}

    # "": "ai", # ෛ,ai ???
    # "": "au", # ෞ,au ???
    # "": "ur", # ෘ,ur ???
    # "": "ruː", # ෲ,ruː ???
    # "": "li", # ෟ,li ???
    # "": "liː", # ෳ,liː ???
    # "": "æ", # ැ,æ ???
    # "": "i", # ි,i ???
    # "": "u", # ු,u ???
    # "": "e", # ෙ,e ???
    # "": "o", # ො,o ???
    # "": "aː", # ා,aː ???
    # "": "æː", # ෑ,æː ???
    # "": "iː", # ී,iː ???
    # "": "uː", # ූ,uː ???
    # "": "eː", # ේ,eː ???
    # "": "oː", # ෝ,oː ???
    # "": "", # ් ???

DICT = {}
DICT.update(CONSTANTS)
DICT.update(ANNOTATABLES)
DICT.update(ANNOTATIONS)

sorted_keys = sorted(DICT.keys(), key=len, reverse=True)
# print("Sorted keys:", sorted_keys)

def transcribe_text(text, idx):
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
            transcribed_phonetics.append(text[i])
            i += 1
    
    return transcribed_phonetics
    
trans = transcribe_text('raṭṭhapāla vyañja  dhamma', 1)
# expected output:
# ["ɹ", "ə", "ʈ", "ʈʰ", "ə", "p", "aː", "l", "ə", " ", "ð", "ə", "m", "m", "ə"]
print(trans)