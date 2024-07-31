'''
Pokud chceme uložit pouze textové data,
můžeme je uložit do textového souboru txt nebo json.
Pokud chceme ale ukládat proměnné složitějších datových 
typů nebo objekty vlastních tříd můžeme využít modulu `pickle`,
který je součástí instalace Pythonu. Ten umí ukládat do binárních
souboru veškeré interní datové typy Pythonu a také většinu instancí
uživatelských tříd. Knihovnu `pickle` musíme ale nejprve 
naimportovat.   

'''
import pickle

'''
Pokud máme např. proměnné datového typu `dict` a 
druhou proměnnou datového typu `float`, můžeme je uložit 
pomocí metody `pickle.dump()`. Tato metoda používá jako první 
proměnnou seznam objektů a jako druhý parametr referenci na soubor.

'''
a_float = 3.1415
b_dict = {"model":"Octavia", "znacka":"Skoda"}

with open("examples/mydata.dat","wb") as outfile:
    pickle.dump([a_float,b_dict],outfile)

del a_float, b_dict

'''
Nyní můžeme znovu soubor s daty otevřít pro čtení a pomocí metody
`pickle.load()` data načíst. Musíme však zachovat stejné pořadí, 
v jakém jsme proměnné ukládali. 

'''

with open("examples/mydata.dat","rb") as outfile:
    a,b = pickle.load(outfile)

print(type(b)) # output: dict

'''
Pomocí módu 'ab' můžeme postupně přidávat další objekty 
do binárního souboru.

'''
with open("examples/pokemon_cards.dat","ab") as file:
    pickle.dump(["Pikachu", 75], file)

with open("examples/pokemon_cards.dat","ab") as file:
    pickle.dump(["Charmander", 175], file)

with open("examples/pokemon_cards.dat","rb") as file:
    while True:
        try:
            card = pickle.load(file)
        except EOFError:
            break

        print(card)

# output:
'''
['Pikachu', 75]
['Charmander', 175]
['Pikachu', 75]
['Charmander', 175]
'''