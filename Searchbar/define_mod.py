import webbrowser

def define(word=''):
    if word == '':
        term = input('Enter A Word To Define: ')
        
    url = 'https://www.dictionary.com/browse/'
    

    webbrowser.open(url + word.strip())

if __name__ == '__main__' :
    define()