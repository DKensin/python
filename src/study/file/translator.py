# translate language
# pip3 install translate

from translate import Translator

# set language to translation
translator = Translator(to_lang="ja")   # maybe vi, ko

try:
    with open("data.txt", mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("check file path silly!")
