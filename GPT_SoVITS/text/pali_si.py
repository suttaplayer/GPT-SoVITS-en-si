from .ps_si.base_transliteration import BaseTransliteration
from .ps_si.pali_si_transliteration import g2p as g2p_pi

def text_normalize(text):
    return BaseTransliteration.normalize(text)

def g2p(text):
    return g2p_pi(text, 1)
    
if __name__ == "__main__":
    trans = g2p('sañjaya')
    print(trans)