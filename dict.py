import os
import json

### variables ###

start_dictionary = {"hei": "hello", "maailma": "world", "käsi": "hand", "jalka": "foot"}
dictionary = {}
json_file_name = "json_dictionary.json"
word_not_found_text = "Word not found. Please input a definition."
user_input_word = ""
translation = ""

welcome_text = """

##########################################################################

You are most welcome to use this excellent English-Finnish dictionary! :-)

##########################################################################

Please enter a word in English or Finnish:
"""



### functions ###

def find_translation(key_or_value):
    result = "-"
    keys = dictionary.keys()
    values = dictionary.values()
    if(key_or_value in keys):
        return dictionary[key_or_value]

    if(key_or_value in values):
        return get_key(key_or_value)

    return result

def print_translation():
    print("Käännos sanalle %s = %s") % user_input_word, translation

def get_json_dictionary(file_name):
    file_handler = open(file_name, "r")
    dictionary = json.load(file_handler)
    file_handler.close()
    return dictionary


# function to return key for any value 
def get_key(val): 
    for key, value in dictionary.items(): 
         if (val == value): 
             return key 
  
    return "-"    


def word_not_found():
    print(word_not_found_text)
    user_input_word = input()
    print("Annoit sanan == " + user_input_word)


### logic ###

print(welcome_text)
user_input_word = input()
translation = find_translation(user_input_word)

if(translation == "-"):
    word_not_found()
else:
    print_translation()







#json.dump(dictionary, file_handler)

#question_fi_word = "Anna suomenkielinen sana lisättäväksi sanakirjaan:"
#print(question_fi_word)
#fi_word = input()
#question_en_word = "Anna  englannin kielinen käännös sanalle: % s" % fi_word
#print(question_en_word)
#en_word = input()




#print("Suomisana: % s ja eng sana % s" % (fi_word, en_word))

#file_handler = open(json_file_name, "a")
# väsy!!! json.dump








