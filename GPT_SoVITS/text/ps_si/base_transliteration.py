import re
import unicodedata

class LiteralMapElement:
    def __init__(self, index: int = -1, key: str = None, value: str = None, orig_key: str = None, 
                 was_modifier_applied: bool = False, tail_sequence: list[str] = None):
        self.index = index
        self.key = key
        self.value = value
        self.orig_key = orig_key
        self.was_modifier_applied = was_modifier_applied
        self.tail_sequence = tail_sequence or []

class BaseTransliteration:
    def __init__(self, src_text: str, base_idx_map: list[dict[str, str]], modifier_map: dict[str, str], next_char_seq_size: int = 1):
        self._orig_source = self._normalize(src_text)
        self._remaining_text = list(self._orig_source)
        self._base_idx_map = base_idx_map
        self._modifier_map = modifier_map
        self._next_char_seq_size = next_char_seq_size
        self._entries = []

    def transliterate(self) -> list[str]:
        while self._remaining_text:
            start_seq = self._query_next_sequence(self._next_char_seq_size)
            next_literal_map_element = self._read_next_literal_map_element(start_seq)
            self._entries.append(next_literal_map_element)
            self._skip_ahead(len(next_literal_map_element['orig_key']))

        return self._render()

    def _set_index_and_value_for_key_if_found(self, lme: dict) -> bool:
        for i in range(len(self._base_idx_map)):
            lme['value'] = self._base_idx_map[i].get(lme['key'])
            if lme['value'] is not None:
                lme['index'] = i
                return True
        return False

    def _read_next_literal_map_element(self, start_seq: list[str]) -> dict:
        ret = {'index': -1, 'key': None, 'value': None, 'orig_key': None, 'was_modifier_applied': False, 'tail_sequence': []}
        stream = start_seq.copy()

        while stream:
            ret['key'] = ''.join(stream)
            ret['orig_key'] = ret['key']
            modified_key = self._modifier_map.get(ret['key'])
            if modified_key:
                ret['was_modifier_applied'] = True
                ret['orig_key'] = ret['key']
                ret['key'] = modified_key
                if not self._set_index_and_value_for_key_if_found(ret):
                    raise ValueError(f"IllegalStateException; [{modified_key}] was not found in base index maps")
                return ret
            if self._set_index_and_value_for_key_if_found(ret):
                return ret
            ret['tail_sequence'].insert(0, stream.pop())

        ret['index'] = -1
        ret['key'] = None
        ret['value'] = start_seq[0]
        ret['orig_key'] = start_seq[0]
        ret['tail_sequence'] = start_seq
        return ret

    def _render(self) -> list[str]:
        ret = []
        for i, curr in enumerate(self._entries):
            prev = self._entries[i - 1] if i > 0 else None
            next = self._entries[i + 1] if i < len(self._entries) - 1 else None
            entry_value = self.resolve_value_with_modifier_if_rqd(prev, curr, next, i == len(self._entries) - 1)
            self._write_entry_value(entry_value, ret)
        return ret

    def _write_entry_value(self, entry_value: str, target: list[str]):
        target.append(entry_value)

    def resolve_value_with_modifier_if_rqd(self, prev: dict, curr: dict, next: dict, is_last: bool) -> str:
        return curr['value']

    def _query_next_sequence(self, size: int = 1) -> list[str]:
        return self._remaining_text[:size]

    def _skip_ahead(self, len: int):
        del self._remaining_text[:len]

    def _normalize(self, text: str) -> str:
        text = unicodedata.normalize('NFC', text) # text.normalize('NFC')
        rep_map = {
            "[;:：，；]": ",",
            '[\'"’]': "",
            "。": ".",
            "！": "!",
            "？": "?",
        }
        for pattern, replacement in rep_map.items():
            text = re.sub(pattern, replacement, text)
        return text.lower()