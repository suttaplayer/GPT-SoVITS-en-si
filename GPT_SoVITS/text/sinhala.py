from .ps_si.base_transliteration import BaseTransliteration
from .ps_si.sinhala_transliteration import g2p as g2p_si

def text_normalize(text):
    return BaseTransliteration.normalize(text)

def g2p(text):
    return g2p_si(text, 1)
    
if __name__ == "__main__":
    trans = g2p('සඦය')
    print(trans)