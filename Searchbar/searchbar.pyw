import tkinter as tk
import webbrowser
import google_mod
import youtube_mod
import wiki_mod
import define_mod
import translate_mod



root = tk.Tk()
root.title('Search Box')
root.geometry('575x175')
root.maxsize(575 , 175)



def clear():
    entry_box.delete('1.0' , 'end')

def google_search(search=''):
    search = entry_box.get('1.0' , 'end-1c')
    if len(search) > 0:
        google_mod.google_search(search)
        clear()

root.bind('<Return>' , google_search)

def youtube_search(search=''):
    if search == '':
        search = entry_box.get('1.0' , 'end-1c')
    if len(search)   >  0 :
        youtube_mod.youtube_search(search)
        clear()

def wiki_search(search=''):
    if search.strip() == '':
        search = entry_box.get('1.0','end-1c')
        if len(search) > 0:
            search = wiki_mod.get_wiki_link(search)
            webbrowser.open(search)
            clear()
        

def define_word(word=''):
    if word.strip() == '':
        word = entry_box.get('1.0' , 'end-1c')
        if len(word) > 0:
            define_mod.define(word)
            clear()

def translate(term=''):
    if term.strip() == '':
        term = entry_box.get('1.0' , 'end-1c')
        if len(term) > 0:
            translate_mod.translate(term)
            clear()
            

# -----Entry Label/Box
entry_label = tk.Label(root , text='Entry:   ')
entry_label.pack(side='top')

entry_box = tk.Text(root, height='1', width=60, font=('Helvetica' , 12))
entry_box.pack(side='top')




#  --- Buttons:
google_key = tk.Button(root, text='Google', width=10, command =  google_search)
google_key.pack()

youtube_key = tk.Button(root, text='Youtube', width=10 , command = youtube_search)
youtube_key.pack(side='top')

wiki_key = tk.Button(root, text='Wiki', width=10, command = wiki_search)
wiki_key.pack(side='top')

define_key = tk.Button(root, text='Define', width=10 , command = define_word)
define_key.pack(side='top')

trans_key = tk.Button(root, text='Translate', width=10 , command = translate)
trans_key.pack(side='top')


root.mainloop()