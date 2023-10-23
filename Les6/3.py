import random
import tkinter as tk
from tkinter import ttk
import pandas as pd



films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])



complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)

for genre in complex_genres:
    film_genres_list.remove(genre)
genres_set = set(film_genres_list)
gen_l = list(genres_set)
Films = list(films['Title'])
def main():
    def Movies(*args):
        try:
            M = []
            for i in range(len(film_genres_list)):
                S = str(film_genres_list[i])
                G = S.split(' | ')
                if G.count(combo.get()) == 1:
                    if i < len(Films):
                        M.append(Films[i])
            film.set(M[random.randint(0, len(M) - 1)])
        except ValueError:
            pass

    root = tk.Tk()
    root.geometry('300x200')
    combo = tk.StringVar()
    Combo_1 = ttk.Combobox(root, values=gen_l, textvariable=combo).pack()
    film = tk.StringVar()
    button = ttk.Button(root, text='Find a movie', command=Movies).pack()
    film_label = tk.Label(root, textvariable=film).pack()


    root.mainloop()
if __name__ == '__main__':
    main()

