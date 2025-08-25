# -*- coding: utf-8 -*-

# Magyar ábécé 44 betűvel
HUNGARIAN_ALPHABET = [
    "a", "á", "b", "c", "cs", "d", "dz", "dzs", "e", "é", "f",
    "g", "gy", "h", "i", "í", "j", "k", "l", "ly", "m", "n", "ny",
    "o", "ó", "ö", "ő", "p", "q", "r", "s", "sz", "t", "ty", "u",
    "ú", "ü", "ű", "v", "w", "x", "y", "z", "zs"
]

def decode_file(file_path, codewords, output_path="decoded.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    code = "".join(codewords)
    result = []
    code_index = 0
    i = 0

    while i < len(text):
        matched = False
        # Többjegyű betűk miatt mindig a hosszabbakat nézzük előbb
        for letter in sorted(HUNGARIAN_ALPHABET, key=len, reverse=True):
            if text[i:i+len(letter)].lower() == letter:
                matched = True
                pos_text = HUNGARIAN_ALPHABET.index(letter)
                code_letter = code[code_index % len(code)]
                pos_code = HUNGARIAN_ALPHABET.index(code_letter.lower())

                # --- Itt jön a lényeg: kivonás és határkezelés ---
                new_pos = pos_text - pos_code
                if new_pos < 0:      # ha túlcsúszik 0 alá
                    new_pos += 44
                elif new_pos >= 44:  # elvileg dekódolásnál ritka, de biztonság kedvéért
                    new_pos -= 44

                new_letter = HUNGARIAN_ALPHABET[new_pos]

                # Nagybetű kezelés
                if text[i].isupper():
                    new_letter = new_letter.capitalize()

                result.append(new_letter)
                code_index += 1
                i += len(letter)
                break

        if not matched:
            # nem betű → változatlanul hagyjuk
            result.append(text[i])
            i += 1

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(result))

    print(f"Visszafejtés kész: {output_path}")


# Példa futtatás
if __name__ == "__main__":
    encoded_file = "encoded.txt"
    codewords = ["auto", "lava", "korall"]

    # Dekódolás
    decode_file(encoded_file, codewords, "decoded.txt")
