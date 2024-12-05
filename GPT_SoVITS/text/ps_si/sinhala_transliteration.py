from base_transliteration import BaseTransliteration, LiteralMapElement
from SI_RS_MAPS import SI_RS_MAPS, SI_MODIFIERS_MAP, SI_PHONEMES, CONSO_END_FLAG

_max_key_size = 0
class AbstractS2RTransliteration(BaseTransliteration):

    def __init__(self, src_text: str, base_idx_map: list[dict[str, str]], modifier_map: dict[str, str]):
        super().__init__(src_text, base_idx_map, modifier_map, _max_key_size)

    @staticmethod
    def _calc_max_key_size():
        global _max_key_size
        for map in SI_RS_MAPS:
            for key, _ in map.items():
                _max_key_size = max(_max_key_size, len(key))
        for key, _ in SI_MODIFIERS_MAP.items():
            _max_key_size = max(_max_key_size, len(key))

# Static block execution
AbstractS2RTransliteration._calc_max_key_size()
print(f"AbstractS2RTransliteration._max_key_size={_max_key_size}")


class Sinhala2RomanTransliteration(AbstractS2RTransliteration):
    def __init__(self, src_text: str):
        super().__init__(src_text, SI_RS_MAPS, SI_MODIFIERS_MAP)

    def resolve_value_with_modifier_if_rqd(self, prev: LiteralMapElement, curr: LiteralMapElement, next: LiteralMapElement, is_last: bool) -> str:
        ret = curr['value']
        if curr['index'] > -1:
            if curr['index'] == 1 and next and next['was_modifier_applied']:
                ret = ret[:-1]
        return ret


class Sinhala2PhonemeTransliteration(Sinhala2RomanTransliteration):
    def __init__(self, src_text: str, phoneme_idx=1):
        super().__init__(src_text)
        self._phoneme_idx = phoneme_idx

    def resolve_value_with_modifier_if_rqd(self, prev: LiteralMapElement, curr: LiteralMapElement, next: LiteralMapElement, is_last: bool) -> str:
        ret = curr['value']
        if curr['index'] > -1:
            phos = SI_PHONEMES.get(curr['orig_key']) or SI_PHONEMES.get(curr['key'])
            ret = phos[self._phoneme_idx]
            if curr['index'] == 1:
                modifier_as_phoneme = None
                if not (next and next['was_modifier_applied']):
                    if (next and next['index'] == -1) or is_last:
                        modifier_as_phoneme = CONSO_END_FLAG[self._phoneme_idx]
                    else:
                        modifier_as_phoneme = SI_PHONEMES['අ'][self._phoneme_idx]
                if modifier_as_phoneme:
                    ret += (' ' if self._phoneme_idx == 1 else '') + modifier_as_phoneme
        return ret

    def _write_entry_value(self, entry_value: str, target: list[str]):
        if not entry_value:
            return
        if self._phoneme_idx == 1 and entry_value != " ":
            parts = entry_value.split(" ")
            target.extend(parts)
        else:
            target.append(entry_value)


def g2p(txt: str, phoneme_idx=1):
    app = Sinhala2PhonemeTransliteration(txt, phoneme_idx)
    return app.transliterate()