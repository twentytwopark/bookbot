def get_num_words(text):
    return len(text.split())

def get_num_all_chars(text):
    # Count occurrences of each character
    char_count = {}
    text = text.lower()
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_on(dict):
    alpha_dict = {}
    for key in dict:
        if key.isalpha():
            alpha_dict[key] = dict[key]
    alpha_dict = sorted(alpha_dict.items(), key=lambda item: item[1], reverse=True)
    return alpha_dict


