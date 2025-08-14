def caeser_cipher(text, shift):
    result_str = ""
    for letter in text:
        if str.isalpha(letter):
            letter_position = ord(letter)
            is_upper = Is_upper(letter)
            if is_upper:
                alpha_position = letter_position - 65
            else:
                alpha_position = letter_position - 98
            alpha_position += shift

            while (alpha_position > 25):
                alpha_position -= 25
            if is_upper:
                alpha_position += 65
            else:
                alpha_position += 98
            result_str += chr(alpha_position)
        else:
            result_str += letter
    return result_str

def Is_upper(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return True
    else:
        return False
print(caeser_cipher('cccc', 2))