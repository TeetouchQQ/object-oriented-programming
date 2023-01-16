string_input = input()
def only_english(string1):
    return len([x for x in string1 if x.encode().isalpha()])
print(only_english(string_input))