import json

# 48 characters total
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# . ? , ( ) ' " - : ; !
# a break character to seperate different words

characters = {
    "a": b"00000000",
    "b": b"00000001",
    "c": b"00000010",
    "d": b"00000011",
    "e": b"00000100",
    "f": b"00000101",
    "g": b"00000110",
    "h": b"00000111",
    "i": b"00001000",
    "j": b"00001001",
    "k": b"00001010",
    "l": b"00001011",
    "m": b"00001100",
    "n": b"00001101",
    "o": b"00001110",
    "p": b"00001111",
    "q": b"00010000",
    "r": b"00010001",
    "s": b"00010010",
    "t": b"00010011",
    "u": b"00010100",
    "v": b"00010101",
    "w": b"00010110",
    "x": b"00010111",
    "y": b"00011000",
    "z": b"00011001",
    ".": b"00011010",
    "?": b"00011011",
    ",": b"00011100",
    "(": b"00011101",
    ")": b"00011110",
    "'": b"00011111",
    "\"": b"00100000",
    "-": b"00100001",
    ";": b"00100010",
    ":": b"00100011",
    " ": b"00100100",
    "0": b"00100101",
    "1": b"00100110",
    "2": b"00100111",
    "3": b"00101000",
    "4": b"00101001",
    "5": b"00101010",
    "6": b"00101011",
    "7": b"00101100",
    "8": b"00101101",
    "9": b"00101110",
    "!": b"00101111"
}

with open("string.json", "r") as file:
    data = json.load(file)
    target_string = data["target_string"]
    target_string = target_string.lower()


with open("output.bin", "ab") as output:
    for char in target_string:
        if char in characters:
            output.write(bytes([int(characters[char], 2)]))

the_8_bytes = b""
pointer = 0
output = b""

with open("output.bin", "rb") as read_output:
    binary = read_output.read()
    for b in binary:
        the_8_bytes += bytes([b])
        pointer += 1

        if pointer == 8:
            pointer = 0
            output += the_8_bytes
            the_8_bytes = b""
    if the_8_bytes:
        output += the_8_bytes

output_string = ""
for k in output:
    k_binary = f"{k:08b}"
    for key, byte in characters.items():
        if k_binary.encode() == byte:
            output_string += key

print(output_string)