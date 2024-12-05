import unicodedata

from pali_si_transliteration import Roman2PhonemeTransliteration, Roman2SinhalaTransliteration
from sinhala_transliteration import Sinhala2PhonemeTransliteration, Sinhala2RomanTransliteration
from SI_RS_MAPS import SI_PHONEMES, RS_SI_MAPS, SI_RS_MAPS

SIN_ROM_TEST_DATA = [
    "අ ආ ඇ ඈ ඉ ඊ උ ඌ එ ඒ ඓ ඔ ඕ ඖ ඍ ඎ ළ් ඐ",
    "a ā æ ǣ i ī u ū e ē ai o ō au ṛ ṝ ḷ ḹ",
    "ක ඛ ග ඝ ඞ ඟ ච ඡ ජ ඣ ඤ ඥ ඦ ට ඨ ඩ ඪ ණ ඬ ත ථ ද ධ න ඳ ප ඵ බ භ ම ඹ ය ර ල ළ ව හ ශ ෂ ක්‍ෂ ස ෆ",
    "ka kha ga gha ṅa n̆ga ca cha ja jha ña gña ñja ṭa ṭha ḍa ḍha ṇa n̆ḍa ta tha da dha na n̆da pa pha ba bha ma m̆ba ya ra la ḷa va ha śa ṣa kṣa sa fa",
    "ක ක් කා කැ කෑ කි කී කු කූ කෙ කේ කෛ කො කෝ කෞ කෘ කෲ ක්ළ් කෳ ක්‍ය ක්‍ර කං",
    "ka k kā kæ kǣ ki kī ku kū ke kē kai ko kō kau kṛ kṝ kḷ kḹ kya kra kaṁ",
    "බුද්ධ, ධම්ම, සාංග",
    "buddha, dhamma, sāṁga",
    "ශශංක ට්‍රාම්ප්",
    "śaśaṁka ṭrāmp",
    "මංජුලා + මාකස් විමලජීව - ට්‍රඅම්ප්",
    "maṁjulā + mākas vimalajīva - ṭraamp",
    "අනේ මට ගහන්නේ නැත්තම් එළියට එන්නම් යනුවෙන් දිවි රැක ගන්නට ගම්මුන් ඉදිරියේ ඇය බැගෑපත් විය.", 
    "anē maṭa gahannē nættam eḷiyaṭa ennam yanuven divi ræka gannaṭa gammun idiriyē æya bægǣpat viya.", 
    "අන්‍යයන්ට කිසිවකු විසින් ගෞරවයක් සැලකිල්ලක් දක්වන්නේ නැත. මා හට වනාහි දුටු දුටු සැම දෙන ම ගරු කරති", 
    "anyayanṭa kisivaku visin gauravayak sælakillak dakvannē næta. mā haṭa vanāhi duṭu duṭu sæma dena ma garu karati", 
    "අපට හෝ ඔබ වහන්සේට හෝ පින් ඇති නම් හෙට එබඳු ආහාරයක් ලබන්නේ යි මුගලන් ස්වාමි කීයේ ය.", 
    "apaṭa hō oba vahansēṭa hō pin æti nam heṭa eban̆du āhārayak labannē yi mugalan svāmi kīyē ya.", 
    "අවිද්‍යා - තෘෂ්ණා - කර්ම - ස්පර්ශ සමුදයයෙන් සංඥා සමුදය වන්නේයයි ද සංඥාව ගේ නිබ්බත්ති ලක්‍ෂණය ද බලන්නේ යි.", 
    "avidyā - tṛṣṇā - karma - sparśa samudayayen saṁgñā samudaya vannēyayi da saṁgñāva gē nibbatti lakṣaṇaya da balannē yi.", 
    "ඉෆ් පිටුපස ඇති කතාව කිප්ලිං සිය ජීවිත කතාව ලෙස ලියූ සම්තින්ග් ඔෆ් මයි සෙල්ෆ් හි සටහන් කර තිබේ.", 
    "if piṭupasa æti katāva kipliṁ siya jīvita katāva lesa liyū samting of mayi self hi saṭahan kara tibē.", 
    "එ බැවින් පමා නො වවු. නොබෝ කලෙකින් ම තෙපි රහත් බව ලබන්නහු යැ යි වදාළ සේක.", 
    "e bævin pamā no vavu. nobō kalekin ma tepi rahat bava labannahu yæ yi vadāḷa sēka.", 
    "ඒ සදහා ඔබ මනසින් නැඟිටින්න ඕනෑ. ගමේ තරුණයන් ඊට නායකත්වය ගන්න ඕනි. ගැමියන් වට කරගෙන කරූ ජයසුරිය මහතා පැවසීය.", 
    "ē sadahā oba manasin næn̆giṭinna ōnǣ. gamē taruṇayan īṭa nāyakatvaya ganna ōni. gæmiyan vaṭa karagena karū jayasuriya mahatā pævasīya.", 
    "ඔවුහු කොහි වෙසෙත් දැයි දේවිය ඇසුවා ය. හිමාලය වනයෙහි වෙසෙන බව මහාසංඝයා වදාළහ.", 
    "ovuhu kohi veset dæyi dēviya æsuvā ya. himālaya vanayehi vesena bava mahāsaṁghayā vadāḷaha.", 
    "කිමෙක් ද, ස්වාමීනි, වර්තමාන වූ දුක්ඛයාගේ ප්‍රහාණය පිණිස ව්‍යායාම් කරණසේක් දැ? යි කීහ. නැත, මහරජානෙනි යි කීසේක.", 
    "kimek da, svāmīni, vartamāna vū dukkhayāgē prahāṇaya piṇisa vyāyām karaṇasēk dæ? yi kīha. næta, maharajāneni yi kīsēka.",
    "අද අඟහරුවාදා. ඔයාට විශ්වාස ද? ඔයා බැරැරුම් ද! ඔව් ඇත්ත වශයෙන්ම, මෙතන බලන්න දෙයක් නෑ.",
    "ada an̆gaharuvādā. oyāṭa viśvāsa da? oyā bærærum da! ov ætta vaśayenma, metana balanna deyak nǣ.",

    "මජ්ඣිම", "majjhima",
    "කූටෝපක්‍රම", "kūṭōpakrama",   
    "පෘතග්ජන", "pṛtagjana",  
    "ක්‍රමක්‍රමයෙන්", "kramakramayen",  
    "ස්ත්‍රීන්", "strīn",    
    "විද්‍යාඥයා", "vidyāgñayā",  
    "කෘමියා", "kṛmiyā",   
    "පීතෲන්", "pītṝn",
    "සෞභාග්‍ය", "saubhāgya",    
    "කව්‍යෝපදේශය", "kavyōpadēśaya", 
    "අවිද්‍යාව", "avidyāva",  
    "ප්‍රඥාව", "pragñāva",  
    "කොන්ස්තන්තිනෝපලය", "konstantinōpalaya", 
    "ස්වප්න", "svapna",  
    "ශල්‍යකර්ම", "śalyakarma",  
    "පාර්ලිමේන්තුව", "pārlimēntuva",  
    "ද්වන්ද්ව", "dvandva",  
    "හෘදස්පන්දනය", "hṛdaspandanaya",
    "සම්ප්‍රේක්‍ෂණ", "samprēkṣaṇa",
    "ක්‍ෂේත්‍ර", "kṣētra",
    "ප්‍රවෘත්ති", "pravṛtti",
    "ප්‍රව්‍රජ්‍යා", "pravrajyā",
    "ප්‍රශ්‍රබ්ධිය", "praśrabdhiya",
    "සංස්කෘත", "saṁskṛta"
]

SI_PHO_TEST_DATA = {
    "බුද්ධ, ධම්ම, සාංග": ["bʊððʰə, ðʰʌmmə, saːŋgə", "B UW0 DH D DH AH0 ,   D DH AA0 M M AH0 ,   S AA1 NG G AH0"]
}

RS_PHO_TEST_DATA = {
    "buddha, dhamma, sāṁga": SI_PHO_TEST_DATA["බුද්ධ, ධම්ම, සාංග"]
}

SI_IPA_ARPA_TEST_DATA = {
    "මජ්ඣිම": ["mʌɟd͡ʒʱimə", "M AA0 JH ZH HH IY0 M AH0"], 
    "කූටෝපක්‍රම": ["kuːʈɔːpʌkrʌmə", "K UW1 T AO1 P AA0 K R AA0 M AH0"], 
    "පෘතග්ජන": ["pruθʌgɟʌnə", "P R UH1 TH AA0 G JH AA0 N AH0"], 
    "ක්‍රමක්‍රමයෙන්": ["krʌmʌkrʌmʌjɛn", "K R AA0 M AA0 K R AA0 M AA0 Y EH0 N"], 
    "ස්ත්‍රීන්": ["sθriːn", "S TH R IY1 N"], 
    "විද්‍යාඥයා": ["viðjaːgɲʌjaː", "V IY0 DH Y AA1 G N Y AA0 Y AA1"],
    "කෘමියා": ["krumijaː", "K R UH1 M IY0 Y AA1"], 
    "පීතෲන්": ["piːθruːn", "P IY1 TH R UW1 N"], 
    "සෞභාග්‍ය": ["saʊbʰaːgjə", "S AW1 B HH AA1 G Y AH0"], 
    "කව්‍යෝපදේශය": ["kʌvjɔːpʌðeːʃʌjə", "K AA0 V Y AO1 P AA0 DH EY1 SH AA0 Y AH0"], 
    "අවිද්‍යාව": ["ʌviðjaːvə", "AA0 V IY0 DH Y AA1 V AH0"], 
    "ප්‍රඥාව": ["prʌgɲaːvə", "P R AA0 G N Y AA1 V AH0"], 
    "කොන්ස්තන්තිනෝපලය": ["konsθʌnθinɔːpʌlʌjə", "K AO0 N S TH AA0 N TH IY0 N AO1 P AA0 L AA0 Y AH0"], 
    "ස්වප්න": ["svʌpnə", "S V AA0 P N AH0"], 
    "ශල්‍යකර්ම": ["ʃʌljʌkʌrmə", "SH AA0 L Y AA0 K AA0 R M AH0"], 
    "පාර්ලිමේන්තුව": ["paːrlimeːnθʊvə", "P AA1 R L IY0 M EY1 N TH UW0 V AH0"], 
    "ද්වන්ද්ව": ["ðvʌnðvə", "DH V AA0 N DH V AH0"], 
    "හෘදස්පන්දනය": ["hurðʌspʌnðʌnʌjə", "HH UW0 R DH AA0 S P AA0 N DH AA0 N AA0 Y AH0"], 
    "සම්ප්‍රේක්‍ෂණ": ["sʌmpreːkʃʌɳə", "S AA0 M P R EY1 K SH AA0 N AH0"], 
    "ක්‍ෂේත්‍ර": ["kʃeːθrə", "K SH EY1 TH R AH0"], 
    "ප්‍රවෘත්ති": ["prʌvurθθi", "P R AA0 V UW0 R TH TH IY0"], 
    "ප්‍රව්‍රජ්‍යා": ["prʌvrʌɟjaː", "P R AA0 V R AA0 JH Y AA1"], 
    "ප්‍රශ්‍රබ්ධිය": ["prʌʃrʌbðʰijə", "P R AA0 SH R AA0 B D DH IY0 Y AH0"], 
    "සංස්කෘත": ["sʌŋskruθə", "S AA0 NG S K R UH1 TH AH0"], 
}

GPT_SoVITS_arpa_DICT = [
    "AH0",
    "S",
    "AH1",
    "EY2",
    "AE2",
    "EH0",
    "OW2",
    "UH0",
    "NG",
    "B",
    "G",
    "AY0",
    "M",
    "AA0",
    "F",
    "AO0",
    "ER2",
    "UH1",
    "IY1",
    "AH2",
    "DH",
    "IY0",
    "EY1",
    "IH0",
    "K",
    "N",
    "W",
    "IY2",
    "T",
    "AA1",
    "ER1",
    "EH2",
    "OY0",
    "UH2",
    "UW1",
    "Z",
    "AW2",
    "AW1",
    "V",
    "UW2",
    "AA2",
    "ER",
    "AW0",
    "UW0",
    "R",
    "OW1",
    "EH1",
    "ZH",
    "AE0",
    "IH2",
    "IH",
    "Y",
    "JH",
    "P",
    "AY1",
    "EY0",
    "OY2",
    "TH",
    "HH",
    "D",
    "ER0",
    "CH",
    "AO1",
    "AE1",
    "AO2",
    "OY1",
    "AY2",
    "IH1",
    "OW0",
    "L",
    "SH",
]

DHAMMATALKS_ORG_CHARS = list("abcdeghijklmnoprstuvyñāīūḍḷṁṅṇṭ")

RS_PWL_IPA_ARPA_TEST_DATA = {"dhamma":["ðʰʌmmə","D DH AA0 M M AH0"],"brahman":["brʌhmʌn","B R AA0 HH M AA0 N"],"deva":["ðɛvə","DH EH0 V AH0"],"tathāgata":["θʌθhaːgʌθə","TH AA0 TH HH AA1 G AA0 TH AH0"],"sutta":["sʊθθə","S UW0 TH TH AH0"],"gotama":["goθʌmə","G AO0 TH AA0 M AH0"],"nikāya":["nikaːjə","N IY0 K AA1 Y AH0"],"ānanda":["aːnʌnðə","AA1 N AA0 N DH AH0"],"jhāna":["d͡ʒʱaːnə","ZH HH AA1 N AH0"],"saṅgha":["sʌŋɡʱə","S AA0 NG G HH AH0"],"sāvatthī":["saːvʌθθhiː","S AA1 V AA0 TH TH HH IY1"],"brahmā":["brʌhmaː","B R AA0 HH M AA1"],"sāriputta":["saːripʊθθə","S AA1 R IY0 P UW0 TH TH AH0"],"māra":["maːrə","M AA1 R AH0"],"saṁyutta":["sʌŋjʊθθə","S AA0 NG Y UW0 TH TH AH0"],"aṅguttara":["ʌŋgʊθθʌrə","AA0 NG G UW0 TH TH AA0 R AH0"],"kamma":["kʌmmə","K AA0 M M AH0"],"buddha":["bʊððʰə","B UW0 DH D DH AH0"],"arahant":["ʌrʌhʌnθ","AA0 R AA0 HH AA0 N TH"],"vinaya":["vinʌjə","V IY0 N AA0 Y AH0"],"anāthapiṇḍika":["ʌnaːθhʌpiɳɖikə","AA0 N AA1 TH HH AA0 P IY0 N D IY0 K AH0"],"mahā":["mʌhaː","M AA0 HH AA1"],"nigaṇṭha":["nigʌɳʈʰə","N IY0 G AA0 N T HH AH0"],"jetas":["ɟɛθʌs","JH EH0 TH AA0 S"],"sakyan":["sʌkjʌn","S AA0 K Y AA0 N"],"rājagaha":["raːɟʌgʌhə","R AA1 JH AA0 G AA0 HH AH0"],"moggallāna":["moggʌllaːnə","M AO0 G G AA0 L L AA1 N AH0"],"kassapa":["kʌssʌpə","K AA0 S S AA0 P AH0"],"pasenadi":["pʌsɛnʌði","P AA0 S EH0 N AA0 DH IY0"],"cunda":["tʃʊnðə","CH UW0 N DH AH0"],"kosala":["kosʌlə","K AO0 S AA0 L AH0"],"itivuttaka":["iθivʊθθʌkə","IY0 TH IY0 V UW0 TH TH AA0 K AH0"],"devatā":["ðɛvʌθaː","DH EH0 V AA0 TH AA1"],"theragāthā":["θhɛrʌgaːθhaː","TH HH EH0 R AA0 G AA1 TH HH AA1"],"majjhima":["mʌɟd͡ʒʱimə","M AA0 JH ZH HH IY0 M AH0"],"raṭṭhapāla":["rʌʈʈʰʌpaːlə","R AA0 T T HH AA0 P AA1 L AH0"],"kaccāna":["kʌtʃtʃaːnə","K AA0 CH CH AA1 N AH0"],"bhāradvāja":["bʰaːrʌðvaːɟə","B HH AA1 R AA0 DH V AA1 JH AH0"],"nāga":["naːgə","N AA1 G AH0"],"udāyin":["ʊðaːjin","UW0 DH AA1 Y IY0 N"],"anuruddha":["ʌnʊrʊððʰə","AA0 N UW0 R UW0 DH D DH AH0"],"asura":["ʌsʊrə","AA0 S UW0 R AH0"],"vesālī":["vɛsaːliː","V EH0 S AA1 L IY1"],"udāna":["ʊðaːnə","UW0 DH AA1 N AH0"],"sakka":["sʌkkə","S AA0 K K AH0"],"nāṭaputta":["naːʈʌpʊθθə","N AA1 T AA0 P UW0 TH TH AH0"],"yakkha":["jʌkkʰə","Y AA0 K K HH AH0"],"bodhisatta":["boðʰisʌθθə","B AO0 D DH IY0 S AA0 TH TH AH0"],"mahānāma":["mʌhaːnaːmə","M AA0 HH AA1 N AA1 M AH0"],"uposatha":["ʊposʌθhə","UW0 P AO0 S AA0 TH HH AH0"],"mallan":["mʌllʌn","M AA0 L L AA0 N"],"nanda":["nʌnðə","N AA0 N DH AH0"],"vajjian":["vʌɟɟiʌn","V AA0 JH JH IY0 AA0 N"],"pāṭimokkha":["paːʈimokkʰə","P AA1 T IY0 M AO0 K K HH AH0"],"licchavi":["litʃt͡ʃʰʌvi","L IY0 CH CH HH AA0 V IY0"],"upāli":["ʊpaːli","UW0 P AA1 L IY0"],"citta":["tʃiθθə","CH IY0 TH TH AH0"],"koṭṭhita":["koʈʈʰiθə","K AO0 T T HH IY0 TH AH0"],"kosalan":["kosʌlʌn","K AO0 S AA0 L AA0 N"],"kusinārā":["kʊsinaːraː","K UW0 S IY0 N AA1 R AA1"],"rāhula":["raːhʊlə","R AA1 HH UW0 L AH0"],"kapilavatthu":["kʌpilʌvʌθθhʊ","K AA0 P IY0 L AA0 V AA0 TH TH HH UW0"],"magadha":["mʌgʌðʰə","M AA0 G AA0 D DH AH0"],"kālāma":["kaːlaːmə","K AA1 L AA1 M AH0"],"arahantship":["ʌrʌhʌnθship","AA0 R AA0 HH AA0 N TH S HH IY0 P"],"aggivessana":["ʌggivɛssʌnə","AA0 G G IY0 V EH0 S S AA0 N AH0"],"dīgha":["ðiːɡʱə","DH IY1 G HH AH0"],"tapassin":["θʌpʌssin","TH AA0 P AA0 S S IY0 N"],"aṅgulimāla":["ʌŋgʊlimaːlə","AA0 NG G UW0 L IY0 M AA1 L AH0"],"sal":["sʌl","S AA0 L"],"poṭṭhapāda":["poʈʈʰʌpaːðə","P AO0 T T HH AA0 P AA1 DH AH0"],"māgaṇḍiya":["maːgʌɳɖijə","M AA1 G AA0 N D IY0 Y AH0"],"dhanañjānin":["ðʰʌnʌnɖʒaːnin","D DH AA0 N AA0 N JH AA1 N IY0 N"],"tissa":["θissə","TH IY0 S S AH0"],"soṇa":["soɳə","S AO0 N AH0"],"saccaka":["sʌtʃtʃʌkə","S AA0 CH CH AA0 K AH0"],"vārāṇasī":["vaːraːɳʌsiː","V AA1 R AA1 N AA0 S IY1"],"kosambī":["kosʌmbiː","K AO0 S AA0 M B IY1"],"mallikā":["mʌllikaː","M AA0 L L IY0 K AA1"],"jīvaka":["ɟiːvʌkə","JH IY1 V AA0 K AH0"],"ajātasattu":["ʌɟaːθʌsʌθθʊ","AA0 JH AA1 TH AA0 S AA0 TH TH UW0"],"khemaka":["kʰɛmʌkə","K HH EH0 M AA0 K AH0"],"icchānaṅgala":["itʃt͡ʃʰaːnʌŋgʌlə","IY0 CH CH HH AA1 N AA0 NG G AA0 L AH0"],"nālandā":["naːlʌnðaː","N AA1 L AA0 N DH AA1"],"bodhi":["boðʰi","B AO0 D DH IY0"],"pāvā":["paːvaː","P AA1 V AA1"],"caṅkī":["tʃʌŋkiː","CH AA0 NG K IY1"],"assalāyana":["ʌssʌlaːjʌnə","AA0 S S AA0 L AA1 Y AA0 N AH0"],"vaccha":["vʌtʃt͡ʃʰə","V AA0 CH CH HH AH0"],"lohicca":["lohitʃtʃə","L AO0 HH IY0 CH CH AH0"],"bhaddiya":["bʰʌððijə","B HH AA0 DH DH IY0 Y AH0"],"kāsi":["kaːsi","K AA1 S IY0"],"migāra":["migaːrə","M IY0 G AA1 R AH0"],"vassakāra":["vʌssʌkaːrə","V AA0 S S AA0 K AA1 R AH0"],"pāṭali":["paːʈʌli","P AA1 T AA0 L IY0"],"therīgāthā":["θhɛriːgaːθhaː","TH HH EH0 R IY1 G AA1 TH HH AA1"],"susima":["sʊsimə","S UW0 S IY0 M AH0"],"suppavāsā":["sʊppʌvaːsaː","S UW0 P P AA0 V AA1 S AA1"],"samiddhi":["sʌmiððʰi","S AA0 M IY0 DH D DH IY0"],"isipatana":["isipʌθʌnə","IY0 S IY0 P AA0 TH AA0 N AH0"]}

def test_missingPhonemeKeys():
    ret = 0
    for mapCategory in SI_RS_MAPS:
        for key, val in mapCategory.items():
            assert key in SI_PHONEMES, f"missing key[{key}] in SI_PHONEMES"
            ret += 1
    return ret

def test_s2r():
    for i in range(0, len(SIN_ROM_TEST_DATA), 2):
        sin = SIN_ROM_TEST_DATA[i]
        expRom = unicodedata.normalize('NFC', SIN_ROM_TEST_DATA[i + 1])
        app = Sinhala2RomanTransliteration(sin)
        actRom = ''.join(app.transliterate())
        assert expRom == actRom, f"set {i}\n\tE: [{expRom}]\n\tA: [{actRom}]"
    return len(SIN_ROM_TEST_DATA) // 2

def test_GPTSoVITS_arpa_scope():
    uniqueArpa = set()
    count = 0
    for key, val in SI_PHONEMES.items():
        phoComposites = val[1].split(" ")
        for arpa in phoComposites:
            if not arpa:
                continue
            if arpa in uniqueArpa:
                continue
            uniqueArpa.add(arpa)
            assert arpa in GPT_SoVITS_arpa_DICT, f"{arpa} is not supported in GPT_SoVITS_arpa_DICT, sin:{key}/{val}"
        count += 1
    return count, len(uniqueArpa)

def test_DhammatalksChars():
    for v in DHAMMATALKS_ORG_CHARS:
        trans = None
        for mapCategory in RS_SI_MAPS:
            trans = mapCategory.get(v)
            if trans:
                break
        assert trans is not None, f"dhammatalks.org char[{v}] is not supported"
    return len(DHAMMATALKS_ORG_CHARS)

def test_s2PHO():
    ret = 0
    for key, val in SI_PHO_TEST_DATA.items():
        for i in range(len(val)):
            ret += 1
            app = Sinhala2PhonemeTransliteration(key, i)
            sep = " " if i == 1 else ""
            res = sep.join(app.transliterate())
            assert val[i] == res, f"g2p[failure]: {res}"
    return ret

def test_s2IPA():
    ret = 0
    for key, val in SI_IPA_ARPA_TEST_DATA.items():
        app = Sinhala2PhonemeTransliteration(key, 0)
        actual = ''.join(app.transliterate())
        assert actual == val[0], f"IPA A: {actual} ; E: {val[0]}"
        ret += 1
    return ret

def test_s2ARPA():
    ret = 0
    for key, val in SI_IPA_ARPA_TEST_DATA.items():
        app = Sinhala2PhonemeTransliteration(key, 1)
        actual = ' '.join(app.transliterate())
        assert actual == val[1], f"ARPA A: {actual} ; E: {val[1]}"
        ret += 1
    return ret

def test_r2s():
    for i in range(0, len(SIN_ROM_TEST_DATA), 2):
        exp_sin = unicodedata.normalize('NFC', SIN_ROM_TEST_DATA[i])
        rom = SIN_ROM_TEST_DATA[i + 1]
        app = Roman2SinhalaTransliteration(rom)
        act_sin = ''.join(app.transliterate())
        assert exp_sin == act_sin, f'set {i}\n\tE: [{exp_sin}]\n\tA: [{act_sin}]'
    return len(SIN_ROM_TEST_DATA) // 2

def test_r2PHO():
    ret = 0
    for key, val in RS_PHO_TEST_DATA.items():
        for i in range(len(val)):
            ret += 1
            app = Roman2PhonemeTransliteration(key, i)
            res = ''.join(app.transliterate()) if i != 1 else ' '.join(app.transliterate())
            assert val[i] == res, f'g2p[failure]: {res}'
    return ret

def test_r2IPA():
    ret = 0
    for key, val in SI_IPA_ARPA_TEST_DATA.items():
        rom_key = SIN_ROM_TEST_DATA[SIN_ROM_TEST_DATA.index(key) + 1]
        app = Roman2PhonemeTransliteration(rom_key, 0)
        actual = ''.join(app.transliterate())
        assert actual == val[0], f'IPA A: {actual} ; E: {val[0]}'
        ret += 1
    return ret

def test_rPWL():
    ret = 0
    for key, val in RS_PWL_IPA_ARPA_TEST_DATA.items():
        for i in range(len(val)):
            ret += 1
            app = Roman2PhonemeTransliteration(key, i)
            res = ''.join(app.transliterate()) if i != 1 else ' '.join(app.transliterate())
            assert val[i] == res, f'pwl[failure]: {res}'
            if val[i] != res:
                val[i] = res
    return ret

print('From Sinhala')
print(f'processed {test_missingPhonemeKeys()} missingPhonemeKeys tests')
print(f'processed {test_s2r()} s2r tests')
pho_test_info = test_GPTSoVITS_arpa_scope()
print(f'processed {pho_test_info[0]} sinhala, {pho_test_info[1]} unique arpa codes')
print(f'processed {test_s2PHO()} s2PHO tests')
print(f'processed {test_s2IPA()} s2IPA tests')
print(f'processed {test_s2ARPA()} s2ARPA tests')

print('From Roman')
print(f'processed {test_r2s()} r2s tests')
print(f'processed {test_DhammatalksChars()} dhammatalks tests')
print(f'processed {test_r2PHO()} r2PHO tests')
print(f'processed {test_r2IPA()} r2IPA tests')
print(f'processed {test_rPWL()} rPWL tests')

