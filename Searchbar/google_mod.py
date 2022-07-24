import sys
import webbrowser

def google_search(query=''):
    google = 'https://www.google.com/search?q='
    if query == '':
        if len(sys.argv) > 1:
            query = sys.argv[1:]
            query = '+'.join(query)
            url =  google + query
            webbrowser.open(url)
        
    if query != '':
        query = query.split(' ')
        query = '+'.join(query)
        url = google + query
        webbrowser.open(url)
    
if __name__ == '__main__':
    google_search()