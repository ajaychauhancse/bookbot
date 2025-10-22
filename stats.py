def get_num_words(path_to_file):
    file_contents = get_book_text(path_to_file)
    num_words = file_contents.split()
    return len(num_words)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_character_count(path_to_file):
    file_contents = get_book_text(path_to_file)
    char_count={}
    for i in file_contents.lower():
        if i in [' ', '\n', '\t']:
            continue
        if i in char_count:
            char_count[i] = int(char_count[i]) + 1
        else:
            char_count[i] = 1
    #print(char_count)
    
    return dict_to_list_char(char_count)

def dict_to_list_char(char_dict):
    new_list=[]
    tmp_var={}
    for k,v in char_dict.items():
        tmp_var["char"]=k
        tmp_var["num"]=v
        new_list.append(tmp_var)
        tmp_var={}
    return new_list
