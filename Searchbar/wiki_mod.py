def get_wiki_link(text):
    wiki_url = 'https://en.wikipedia.org/wiki/'
    if type(text) == str:
        if text[0:5] == 'https':
            return(text)
            
        
        if text[0:5] != 'https':
            list_of_text = text.split(' ')
            new_text = '_'.join(list_of_text)
            url = wiki_url + new_text
            return str(url)
            
        
    if type(text) != str:
        if type(text) == list:
            if len(text) > 1:
                new_text = '_'.join(text)                
                url = wiki_url + new_text
                return str(url)
            
            if len(text) == 1:
                text = text[0]
                if text[:5] == 'https':
                    return text
                if text[:5] != 'https':
                    return(text)


if __name__ == '__main__':
    get_wiki_link()