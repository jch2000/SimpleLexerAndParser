import re


def lexer(file_content):
    file_content = file_content.replace("\n", " ")
    key_words = ["VOID", "MAIN", "switch", "for", "while", "do", "if", "return"]
    two_char_ops = ["!=", "++", "--", ">=", "<=", "=="]
    one_char_ops = ["+", "-", "*", "/", "=", ">", "<"]
    punct = ["(", ")", "{", "}", ",", ";"]
    ids = []
    lexical_units = []
    curr_lexeme = ""

    white_space = " "
    file_length = len(file_content)
    curr = 0

    while curr < file_length:
        curr_char = file_content[curr]
        if curr < file_length - 1:
            with_next_char = curr_char + file_content[curr+1]
        else:
            with_next_char = ""

        # Process string
        if curr_char == "\"":
            curr += 1
            if curr == file_length:
                error()
            curr_char = file_content[curr]
            if curr_lexeme != "":
                lexical_units.append(process_lexeme(curr_lexeme, key_words))
                if check_id(lexical_units, curr_lexeme, ids):
                    ids.append(curr_lexeme)
                curr_lexeme = ""
            while curr_char != "\"":
                curr_lexeme += curr_char
                curr += 1
                if curr == file_length:
                    error()
                curr_char = file_content[curr]
            lexical_units.append([curr_lexeme, "STRING_LIT"])
            curr_lexeme = ""
        # Process operator that contains two characters
        elif with_next_char in two_char_ops:
            if curr_lexeme != "":
                lexical_units.append(process_lexeme(curr_lexeme, key_words))
                if check_id(lexical_units, curr_lexeme, ids):
                    ids.append(curr_lexeme)
                curr_lexeme = ""
            lexical_units.append(["OPERATOR", with_next_char])
            curr += 1
        # Process operator that contains one character
        elif curr_char in one_char_ops:
            if curr_lexeme != "":
                lexical_units.append(process_lexeme(curr_lexeme, key_words))
                curr_lexeme = ""
            lexical_units.append(["OPERATOR", curr_char])
        # Process punctuation
        elif curr_char in punct:
            if curr_lexeme != "":
                lexical_units.append(process_lexeme(curr_lexeme, key_words))
                if check_id(lexical_units, curr_lexeme, ids):
                    ids.append(curr_lexeme)
                curr_lexeme = ""
            lexical_units.append(["PUNCT", curr_char])
        # Process current lexeme if at whitespace
        elif curr_char == white_space:
            if curr_lexeme != "":
                lexical_units.append(process_lexeme(curr_lexeme, key_words))
                if check_id(lexical_units, curr_lexeme, ids):
                    ids.append(curr_lexeme)
                curr_lexeme = ""
        else:
            curr_lexeme += curr_char
        curr += 1
        # End of while loop
    # Process last lexeme if anything is there
    if curr_lexeme != "":
        lexical_units.append(process_lexeme(curr_lexeme, key_words))
        if check_id(lexical_units, curr_lexeme, ids):
            ids.append(curr_lexeme)
    print("Lexical Units:")
    print(lexical_units)
    print("IDs: ")
    print(ids)
    return lexical_units, key_words, two_char_ops, one_char_ops, punct, ids


def process_lexeme(curr_lexeme, key_words):
    if curr_lexeme in key_words:
        return ["KEY_WORD", curr_lexeme]
    elif re.fullmatch("[A-Za-z_].*", curr_lexeme):
        return ["ID", curr_lexeme]
    elif re.fullmatch("([1-9]\d*(\.\d*[1-9])?|0\.\d*[1-9]+)|\d+(\.\d*[1-9])?|\.[0-9]+", curr_lexeme):
        return ["NUM_LIT", curr_lexeme]
    else:
        error()


def check_id(lexical_units, curr_lexeme, ids):
    if len(lexical_units) < 1:
        return False
    elif lexical_units[-1][0] == "ID":
        if curr_lexeme not in ids:
            return True
    return False


def error():
    print("Lexical Error")
    exit()
