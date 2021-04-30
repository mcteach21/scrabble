from termcolor import colored
from menu import Menu
from onlinedico import dictionary_search
from option import Option
from scrabble import scrabble

msg_color = 'blue'


def print_msg(msg):
    print('*******************************************************')
    print('\t', colored(msg, msg_color))
    print('*******************************************************')



def search():
    word = input('mot recherché : ')
    dictionary_search(word)



if __name__ == '__main__':
    print_msg('Python : Scrabble => Dictionnaire (en ligne)')    
    menu = Menu([
        Option('Scrabble (mots possibles)', scrabble),
        Option('Chercher dans Dictionnaires', search)
        # , Option('Tests', test)
    ])
    while not menu.want_exit:
        menu.show()
    print('*******************************************************')
