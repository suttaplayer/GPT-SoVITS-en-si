# import LangSegment

# LangSegment.setfilters(["en", "si", "pi"])
# text = "Hello, 你的名字叫<ja>1. 佐々木？එවං<ja> මෙ සුතං – එකං සමයං භගවා <pi>tathāgata<pi> testing\
#     和三款 2. Apple Watch 3. 等一系列新品，这次的 සුතං《gotama》" 
# langlist = LangSegment.getTexts(text)
# print("=================================")
# for line in langlist:
#     print(line)
# print("=================================")


from text.english import g2p as g2p_e
from text.korean import g2p as g2p_k 
from text.pali_si import g2p as g2p_pi

from text.cleaner import clean_text

# check = g2p_e("Today's Tuesday. Are you sure? Are you serious! Yes, of course; nothing to look at here.")
# print("english", check)


# check = g2p_k('안녕하세요 세상')
# print("korean", check)


# check = g2p_pi('sañjaya')
# print("pali", check)


print("english", clean_text("Today's Tuesday. Are you sure? Are you serious! Yes, of course; nothing to look at here.","en"))
