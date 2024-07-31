'''
Pro archivaci souborů slouží modul `zipfile`. 
V tomto module existuje třída `ZipFile`, 
která je obdobou funkce `open()` pro ostatní soubory. 
Opět můžeme použít módy "r" pro čtení, "w" pro zápis a "a" 
pro přidání. Můžeme použít i kontextový manažer `with` 
abychom se nemuseli starat o zavření souboru.
'''
import zipfile

filename = "examples/mp4s.zip"
archive = zipfile.ZipFile(filename,"r")
archive.printdir()

# allows us to see whats inside

filenames = archive.namelist()
print(filenames)

'''
Informace (metadata) o souboru zjistíme 
pomocí metody `get_info(soubor)`. 
Výsledky pak jsou dostupné v atributech `file_size, 
compress_size, filename, date_time`.
'''

info = archive.getinfo(filenames[1])
print(info.file_size)
print(info.filename)
print(info.date_time)

archive.close()

'''
Extrahovat soubory ze zip souboru můžeme 
pomocí metody `extract()`, druhým argumentem je 
cesta kam chci soubory rozbalit.

'''
with zipfile.ZipFile("examples/mp4s.zip", mode="r") as archive:
    for file in archive.namelist():
        archive.extract(file, "output")

filenames = ["examples/exampleTXT.txt", "examples/exampleJSON.json", "examples/exampleCSV.csv"]

'''
Zabalit pak pomocí metody `write()`. 
'''
with zipfile.ZipFile("examples_backup.zip", mode="w") as archive:
    for filename in filenames:
        archive.write(filename,compress_type = zipfile.ZIP_DEFLATED)