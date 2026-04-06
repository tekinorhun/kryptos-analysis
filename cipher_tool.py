# ============================================
# Cipher Tool V2
# Author: OrhunTekin
# Description: Cipher analysis tool (Caesar, Reverse, Frequency)
# ============================================

VERSION = "2.0"
AUTHOR = "OrhunTekin"


def signature():
    return "Cipher Tool by " + AUTHOR + " | v" + VERSION


def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                result += chr(shifted)
            else:
                if shifted < ord('A'):
                    shifted += 26
                result += chr(shifted)
        else:
            result += char
    return result


def reverse_text(text):
    return text[::-1]


def score_text(text):
    common_words = ["THE", "AND", "HELLO", "YOU", "IS"]
    score = 0
    for word in common_words:
        if word in text.upper():
            score += 1
    return score


def frequency_analysis(text):
    freq = {}

    for char in text:
        if char.isalpha():
            char = char.upper()
            freq[char] = freq.get(char, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("\n--- Harf Frekansları ---")
    for char, count in sorted_freq:
        print(char + ": " + str(count))


def main():
    print(signature())

    while True:
        print("\n=== CIPHER TOOL V2 ===")
        print("1 - Caesar Decrypt (Auto)")
        print("2 - Reverse Text")
        print("3 - Frequency Analysis")
        print("0 - Exit")

        choice = input("Seçim: ").strip()

        if choice == "1":
            cipher = input("Şifreli metin: ")

            best_score = 0
            best_result = ""

            for i in range(26):
                result = caesar_decrypt(cipher, i)
                score = score_text(result)

                print("Shift " + str(i) + ": " + result + " (Score: " + str(score) + ")")

                if score > best_score:
                    best_score = score
                    best_result = result

            print("\n>>> EN IYI TAHMIN: " + best_result)

        elif choice == "2":
            text = input("Metin: ")
            print("Sonuç: " + reverse_text(text))

        elif choice == "3":
            text = input("Metin: ")
            frequency_analysis(text)

        elif choice == "0":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
