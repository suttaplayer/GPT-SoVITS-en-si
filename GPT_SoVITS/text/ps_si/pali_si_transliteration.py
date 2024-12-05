from base_transliteration import BaseTransliteration, LiteralMapElement
from SI_RS_MAPS import CONSO_END_FLAG, REV_SI_MODIFIERS_MAP, RS_PHONEME_SWITCHES, RS_PHONEMES, RS_SI_MAPS, SI_MODIFIERS_MAP, SI_PHONEMES, SI_RS_MAPS

_max_key_size = 0

class AbstractR2STransliteration(BaseTransliteration):
    def __init__(self, src_text: str, base_idx_map: list[dict[str, str]], modifier_map: dict[str, str]):
        super().__init__(src_text, base_idx_map, modifier_map, _max_key_size)

    @staticmethod
    def _build_roman_sinhala_map():
        global _max_key_size
        for i in range(len(SI_RS_MAPS)):
            transposed_map = {}
            for key, val in SI_RS_MAPS[i].items():
                if i == 1:
                    val = val[:-1]
                transposed_map[val] = key
                _max_key_size = max(_max_key_size, len(val))
            RS_SI_MAPS.append(transposed_map)

    @staticmethod
    def _build_reverse_sinhala_modifier_map():
        for key, val in SI_MODIFIERS_MAP.items():
            REV_SI_MODIFIERS_MAP[val] = key

# Build the maps
AbstractR2STransliteration._build_roman_sinhala_map()
AbstractR2STransliteration._build_reverse_sinhala_modifier_map()
print(f"AbstractR2STransliteration._max_key_size={_max_key_size}")


class Roman2SinhalaTransliteration(AbstractR2STransliteration):
    def __init__(self, src_text: str):
        super().__init__(src_text, RS_SI_MAPS, {})

    def resolve_value_with_modifier_if_rqd(self, prev: LiteralMapElement, curr: LiteralMapElement, next: LiteralMapElement, is_last: bool) -> str:
        ret = curr['value']
        if prev and prev['index'] == 1:
            if curr['key'] == 'a':
                ret = ''
            else:
                rev_modifier = REV_SI_MODIFIERS_MAP.get(curr['value'])
                if rev_modifier:
                    ret = rev_modifier
                else:
                    ret = "\u0DCA" + ret
        if curr['index'] == 1 and is_last:
            ret += "\u0DCA"
        return ret


class Roman2PhonemeTransliteration(Roman2SinhalaTransliteration):
    def __init__(self, src_text: str, phoneme_idx=1):
        super().__init__(src_text)
        self._phoneme_idx = phoneme_idx

    def resolve_value_with_modifier_if_rqd(self, prev: LiteralMapElement, curr: LiteralMapElement, next: LiteralMapElement, is_last: bool) -> str:
        ret = curr['value']
        if curr['index'] > -1:
            if curr['key'] == 'a' and ((next and next['index'] == -1) or is_last):
                ret = CONSO_END_FLAG[self._phoneme_idx]
            else:
                rev_modifier = RS_PHONEME_SWITCHES.get(curr['key'])
                if rev_modifier and not (prev == None or prev['index'] == -1):
                    ret = SI_PHONEMES[rev_modifier][self._phoneme_idx]
                else:
                    ret = RS_PHONEMES[curr['key']][self._phoneme_idx]
        return ret

    @staticmethod
    def _build_phoneme_map():
        for i in range(len(RS_SI_MAPS)):
            for key, val in RS_SI_MAPS[i].items():
                RS_PHONEMES[key] = SI_PHONEMES[val]

    # Build the phoneme map
    _build_phoneme_map()

def g2p(txt: str, phoneme_idx=1):
    app = Roman2PhonemeTransliteration(txt, phoneme_idx)
    return app.transliterate()