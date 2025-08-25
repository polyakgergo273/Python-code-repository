# -*- coding: utf-8 -*-

# Magyar ábécé 44 betűvel
HUNGARIAN_ALPHABET = [
    "a", "á", "b", "c", "cs", "d", "dz", "dzs", "e", "é", "f",
    "g", "gy", "h", "i", "í", "j", "k", "l", "ly", "m", "n", "ny",
    "o", "ó", "ö", "ő", "p", "q", "r", "s", "sz", "t", "ty", "u",
    "ú", "ü", "ű", "v", "w", "x", "y", "z", "zs"
]

def encode_file(file_path, codewords, output_path="encoded.txt"):
    # Szöveg beolvasása
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Kódszavak összefűzése (egy hosszú kulcssorrá)
    code = "".join(codewords)

    # Kimeneti szöveg
    encoded = []
    code_index = 0  # mutató a kódszó betűire

    # végigmegyünk a szövegen
    i = 0
    while i < len(text):
        matched = False
        # Megnézzük, hogy az aktuális helyen kezdődik-e egy magyar többjegyű betű
        for letter in sorted(HUNGARIAN_ALPHABET, key=len, reverse=True):
            if text[i:i+len(letter)].lower() == letter:
                matched = True
                # Számoljuk az aktuális betű pozícióját az abc-ben
                pos_text = HUNGARIAN_ALPHABET.index(letter)

                # Soron következő kód betű
                code_letter = code[code_index % len(code)]
                pos_code = HUNGARIAN_ALPHABET.index(code_letter.lower())

                # Eltolás
                new_pos = pos_text + pos_code
                if new_pos >= 44:
                    new_pos -= 44

                new_letter = HUNGARIAN_ALPHABET[new_pos]

                # Nagybetű kezelés
                if text[i].isupper():
                    new_letter = new_letter.capitalize()

                encoded.append(new_letter)

                # Lépjünk a kódban előre
                code_index += 1
                # Ugorjunk a megfelelő hossznyit (pl. "dzs" → 3 karakter)
                i += len(letter)
                break

        if not matched:
            # Ha nem betű, csak másoljuk
            encoded.append(text[i])
            i += 1

    # Eredmény kiírása fájlba
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(encoded))

    print(f"Kódolás kész: {output_path}")


# Példa futtatás
if __name__ == "__main__":
    input_file = "input.txt"   # ide írd a beolvasandó file-t
    codewords = ["auto", "lava", "korall"]  # itt add meg a kódszavakat
    encode_file(input_file, codewords, "encoded.txt")
