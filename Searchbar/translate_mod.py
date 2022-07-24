import webbrowser

def translate(term=''):
    if term == '':
        term = input('Enter A Term To Translate: ')
        
    url1 = 'https://translate.google.com/?sl=auto&tl=en&text='
    url2 = '&op=translate'
    

    webbrowser.open(url1 + term.strip() + url2)

if __name__ == '__main__' :
    translate()