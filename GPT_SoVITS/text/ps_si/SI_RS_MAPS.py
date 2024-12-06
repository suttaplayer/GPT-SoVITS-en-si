SI_RS_MAPS = [
    {
        'අ': 'a', 'ආ': 'ā', 'ඇ': 'æ', 'ඈ': 'ǣ', 'ඉ': 'i', 'ඊ': 'ī', 'උ': 'u', 'ඌ': 'ū',
        'එ': 'e', 'ඒ': 'ē', 'ඓ': 'ai', 'ඔ': 'o', 'ඕ': 'ō', 'ඖ': 'au',
    },
    {
        'ක': 'ka', 'ඛ': 'kha', 'ග': 'ga', 'ඝ': 'gha', 'ඞ': 'ṅa', 'ඟ': 'n̆ga',
        'ච': 'ca', 'ඡ': 'cha', 'ජ': 'ja', 'ඣ': 'jha', 'ඤ': 'ña', 'ඥ': 'gña', 'ඦ': 'ñja',
        'ට': 'ṭa', 'ඨ': 'ṭha', 'ඩ': 'ḍa', 'ඪ': 'ḍha', 'ණ': 'ṇa', 'ඬ': 'n̆ḍa',
        'ත': 'ta', 'ථ': 'tha', 'ද': 'da', 'ධ': 'dha', 'න': 'na', 'ඳ': 'n̆da',
        'ප': 'pa', 'ඵ': 'pha', 'බ': 'ba', 'භ': 'bha', 'ම': 'ma', 'ඹ': 'm̆ba',

        'ය': 'ya', 'ර': 'ra', 'ල': 'la', 'ළ': 'ḷa', 'ව': 'va', 'හ': 'ha',
        'ශ': 'śa', 'ෂ': 'ṣa', 'ක්‍ෂ': 'kṣa', 'ස': 'sa', 'ෆ': 'fa',
    },
    {
        'ඍ': 'ṛ', 'ඎ': 'ṝ', 'ඏ': 'l̥', 'ඐ': 'ḹ',
    },
    {
        "\u0DCA": "",
        # "_a_": "_a_"
    },
    {
        "ං": "ṁ",
        "ඃ": "ḥ"
    },
    {
        "හෘ": "hṛ",
        "මෘ": "mṛ",
        "වෘ": "vṛ",
        "නෘ": "nṛ",
    }
]

SI_MODIFIERS_MAP = {
    "\u0DCA": "\u0DCA",

    "ා": "ආ", # base ā - ū
    "ැ": "ඇ",
    "ෑ": "ඈ",
    "ි": "ඉ",
    "ී": "ඊ",
    "ු": "උ",
    "ූ": "ඌ",
    "ෙ": "එ", # extended e - au
    "ේ": "ඒ",
    "ෛ": "ඓ",
    "ො": "ඔ",
    "ෝ": "ඕ",
    "ෞ": "ඖ",
    "ෘ": "ඍ", # advanced ru - lī
    "ෲ": "ඎ",
    "ෟ": "ඏ",
    "ෳ": "ඐ",

    "්‍ය": "ය", # other ya - ra
    "්‍ර": "ර",
}

SI_PHONEMES = {
    "අ": [
        "ʌ",
        "AA0"
    ],
    "ආ": [
        "aː",
        "AA1"
    ],
    "ඇ": [
        "æ",
        "AE0"
    ],
    "ඈ": [
        "æː",
        "AE1"
    ],
    "ඉ": [
        "i",
        "IY0"
    ],
    "ඊ": [
        "iː",
        "IY1"
    ],
    "උ": [
        "ʊ",
        "UW0"
    ],
    "ඌ": [
        "uː",
        "UW1"
    ],
    "එ": [
        "ɛ",
        "EH0"
    ],
    "ඒ": [
        "eː",
        "EY1"
    ],
    "ඓ": [
        "ai",
        "AY1"
    ],
    "ඔ": [
        "o",
        "AO0"
    ],
    "ඕ": [
        "ɔː",
        "AO1"
    ],
    "ඖ": [
        "aʊ",
        "AW1"
    ],
    "්": [
        "",
        ""
    ],
    "_a_": [
        "ə",
        "AH0"
    ],
    "ඍ": [
        "ɾɨ",
        "R IH"
    ],
    "ඎ": [
        "ɾɨː",
        "R IY1"
    ],
    "ඏ": [
        "ilu",
        "IH1 L UH1"
    ],
    "ඐ": [
        "iluː",
        "IH1 L UW1"
    ],
    "ක": [
        "k",
        "K"
    ],
    "ඛ": [
        "kʰ",
        "K HH"
    ],
    "ග": [
        "g",
        "G"
    ],
    "ඝ": [
        "ɡʱ",
        "G HH"
    ],
    "ඞ": [
        "ŋ",
        "NG"
    ],
    "ඟ": [
        "ŋɡ",
        "NG G"
    ],
    "ච": [
        "tʃ",
        "CH"
    ],
    "ඡ": [
        "t͡ʃʰ",
        "CH HH"
    ],
    "ජ": [
        "ɟ",
        "JH"
    ],
    "ඣ": [
        "d͡ʒʱ",
        "ZH HH"
    ],
    "ඤ": [
        "ɲ",
        "N Y"
    ],
    "ඥ": [
        "gɲ",
        "G N Y"
    ],
    "ඦ": [
        "nɖʒ",
        "N JH"
    ],
    "ට": [
        "ʈ",
        "T"
    ],
    "ඨ": [
        "ʈʰ",
        "T HH"
    ],
    "ඩ": [
        "ɖ",
        "D"
    ],
    "ඪ": [
        "ɖʱ",
        "D HH"
    ],
    "ණ": [
        "ɳ",
        "N"
    ],
    "ඬ": [
        "ɳɖ",
        "N D"
    ],
    "ත": [
        "θ",
        "TH"
    ],
    "ථ": [
        "θh",
        "TH HH"
    ],
    "ද": [
        "ð",
        "DH"
    ],
    "ධ": [
        "ðʰ",
        "D DH"
    ],
    "න": [
        "n",
        "N"
    ],
    "ඳ": [
        "nðh",
        "N DH HH"
    ],
    "ප": [
        "p",
        "P"
    ],
    "ඵ": [
        "pʰ",
        "P HH"
    ],
    "බ": [
        "b",
        "B"
    ],
    "භ": [
        "bʰ",
        "B HH"
    ],
    "ම": [
        "m",
        "M"
    ],
    "ඹ": [
        "ᵐb",
        "M B"
    ],
    "ය": [
        "j",
        "Y"
    ],
    "ර": [
        "r",
        "R"
    ],
    "ල": [
        "l",
        "L"
    ],
    "ළ": [
        "ɭ",
        "L R"
    ],
    "ව": [
        "v",
        "V"
    ],
    "හ": [
        "h",
        "HH"
    ],
    "ශ": [
        "ʃ",
        "SH"
    ],
    "ෂ": [
        "ʃ",
        "SH"
    ],
    "ක්‍ෂ": [
        "kʃ",
        "K SH"
    ],
    "ස": [
        "s",
        "S"
    ],
    "ෆ": [
        "f",
        "F"
    ],
    "ං": [
        "ŋ",
        "NG"
    ],
    "ඃ": [
        "h",
        "HH"
    ],
    "හෘ": [
        "hur",
        "HH UW0 R"
    ],
    "මෘ": [
        "mur",
        "M UW0 R"
    ],
    "වෘ": [
        "vur",
        "V UW0 R"
    ],
    "නෘ": [
        "nur",
        "N UW0 R"
    ],
    "ා": [
        "aː",
        "AA1"
    ],
    "ැ": [
        "æ",
        "AE0"
    ],
    "ෑ": [
        "æː",
        "AE1"
    ],
    "ි": [
        "i",
        "IY0"
    ],
    "ී": [
        "iː",
        "IY1"
    ],
    "ු": [
        "ʊ",
        "UW0"
    ],
    "ූ": [
        "uː",
        "UW1"
    ],
    "ෙ": [
        "ɛ",
        "EH0"
    ],
    "ේ": [
        "eː",
        "EY1"
    ],
    "ෛ": [
        "ai",
        "AY1"
    ],
    "ො": [
        "o",
        "AO0"
    ],
    "ෝ": [
        "ɔː",
        "AO1"
    ],
    "ෞ": [
        "aʊ",
        "AW1"
    ],
    "ෘ": [
        "ru",
        "R UH1"
    ],
    "ෲ": [
        "ruː",
        "R UW1"
    ],
    "ෟ": [
        "ilu",
        "IH1 L UH1"
    ],
    "ෳ": [
        "iluː",
        "IH1 L UW1"
    ],
    "්‍ය": [
        "j",
        "Y"
    ],
    "්‍ර": [
        "r",
        "R"
    ]
};

CONSO_END_FLAG = SI_PHONEMES["_a_"]


RS_SI_MAPS = []
REV_SI_MODIFIERS_MAP = {}

RS_PHONEMES = {}

RS_PHONEME_SWITCHES = {
    "ṛ": "ෘ",
    "ṝ": "ෲ"
}