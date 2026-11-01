def decode_string_mapping(text: str, mapping: dict) -> str:
    res = ""
    for char in text:
        res += mapping.get(char, char)


    return res
