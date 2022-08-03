def parse(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids):
    curr = 0
    curr = program(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr)
    if curr != len(lexical_units):
        error("Tokens located after end of program")


def program(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr):
    pattern = ["VOID", "MAIN", "(", ")"]
    for i, token in enumerate(pattern):
        this_token, token_type = get_token(lexical_units, i), get_token_type(lexical_units, i)
        if this_token != token or token_type != "PUNCT" and token_type != "KEY_WORD":
            error("at token " + this_token)
    curr += 4
    return block(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr)


def block(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr):
    this_token, token_type = get_token(lexical_units, curr), get_token_type(lexical_units, curr)
    if this_token != "{" or token_type != "PUNCT":
        error("at token " + this_token)
    curr += 1
    curr = statement(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr)
    this_token, token_type = get_token(lexical_units, curr), get_token_type(lexical_units, curr)
    print(this_token)
    if this_token != "}" or token_type != "PUNCT":
        error("at token " + this_token)
    return curr + 1


def statement(lexical_units, key_words, two_char_ops, one_char_ops, punct, ids, curr):
    this_token, token_type = get_token(lexical_units, curr), get_token_type(lexical_units, curr)
    while this_token != "{" and token_type != "PUNCT":
        curr += 1
        this_token, token_type = get_token(lexical_units, curr), get_token_type(lexical_units, curr)
        print("Statement goes here!")
    return curr


def get_token(lexical_units, curr):
    if curr < len(lexical_units):
        return lexical_units[curr][1]
    error("Reached end of file without program closing")


def get_token_type(lexical_units, curr):
    if curr < len(lexical_units):
        return lexical_units[curr][0]
    error("")


def error(token):
    print("Syntax Error: " + token)
    exit()
