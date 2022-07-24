import sys
import webbrowser

def youtube_search(query=''):
    youtube_url = 'https://www.youtube.com/results?search_query='
    if query == '':
        if len(sys.argv) > 1:
            query = sys.argv[1:]
            query = '+'.join(query)
            url =  youtube_url + query
            webbrowser.open(url)
        
    if query != '':
        query = query.split(' ')
        query = '+'.join(query)
        url = youtube_url + query
        webbrowser.open(url)
    
if __name__ == '__main__':
    youtube_search()