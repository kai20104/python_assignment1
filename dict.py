import os
import json

### variables ###

start_dictionary = {"hei": "hello", "maailma": "world", "käsi": "hand", "jalka": "foot"}
dictionary = {}
json_file_name = "json_dictionary.json"
word_not_found_text = "Word not found. Please input a definition in format: finnishword=translation"
user_input_word = ""
translation = ""
ask_word_text = "Please enter a word in English or Finnish:"

welcome_text = """

##########################################################################

You are most welcome to use this excellent English-Finnish dictionary! :-)

##########################################################################

Please enter a word in English or Finnish:
"""



##### functions #####

def find_translation(key_or_value):
    result = "-"
    
    keys = dictionary.keys()
    values = dictionary.values()
    if(key_or_value in keys):
        result = dictionary[key_or_value]

    if(key_or_value in values):
        result = get_key(key_or_value)

    print("result == " + result)

    return result

def print_translation(a, b):
    print("Käännos --> " + a + " = " + b)

def load_json_dictionary(file_name):
    file_handler = open(file_name, "r")
    d = json.load(file_handler)
    file_handler.close()
    return d

def save_json_dictionary(file_name, dictio):
    file_handler = open(file_name, "w")
    json.dump(dictio, file_handler)
    file_handler.close()



# function to return key for any value 
def get_key(val): 
    for key, value in dictionary.items(): 
         if (val == value): 
             return key 
  
    return "-"    


def word_not_found():
    print("word_not_found() dict == ", dictionary)
    print(word_not_found_text)
    key, val = input().split("=")
    print("key == " + key)
    print("val == " + val)
    #print("dictaaaaaaa == ", dictionary)
    dictionary[key] = val # lisää sanapari
    #print("dict == " + dictionary)
    save_json_dictionary(json_file_name, dictionary)
    print("New word added.")
    print(ask_word_text)
    user_input_word = input()
    translation = find_translation(user_input_word)
    print_translation(user_input_word, translation)


##### logic #####

dictionary = load_json_dictionary(json_file_name)
print("dictionary alussa == ", dictionary)
if(not dictionary):
    #print("d on tyhjä............")
    #dictionary = start_dictionary
    save_json_dictionary(json_file_name, start_dictionary)
    dictionary = load_json_dictionary(json_file_name)
    print("ddddddddd == ", dictionary)
else:
    print("Dict ei oo tyhjä --> ", dictionary)

print(welcome_text) 


while(True):
    user_input_word = input()
    if(user_input_word == "q"):
        break
    translation = find_translation(user_input_word)

    if(translation == "-"):
        word_not_found()
    else:
        print_translation(user_input_word, translation)

    print(ask_word_text)




