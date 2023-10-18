def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value

def str_to_hex(string):
    byte_data = string.encode('utf-8')
    hex_value = byte_data.hex()
    hex_with_prefix = "0x" + hex_value

    return hex_with_prefix
