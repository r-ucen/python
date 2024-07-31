# importing our own module:
'''
import module39 as msg

msg.hello()
msg.bye()
'''

# or you can directly import the fuunctions like this:


from module39 import hello, bye

# now we dont need to precede the function with the msg

hello()
bye()

# ---------------------------

import random
print(random.__file__) # we can get the path to the module like this

# ------------------------------------------------------------------
'''
Protože modul je soubor s koncovky *.py je možné ho spustit 
jako jakýkoliv jiný skript. Moduly jsou často vytvářeny tak, 
aby jejich výstup byl jiný, pokud jsou spuštěny samostatně nebo 
importovány. Proto je dobré v modulu oddělit co se má provádět 
při importu a co při spuštění. K tomu slouží proměnná `__name__`, 
která má hodnotu jména modulu pokud 
importujeme a hodnotu `"__main__"`, 
pokud je modul volán přímo. Proto část kódu, kterou chceme 
spustit v případě přímého spuštění uvádíme za podmínku:
`if __name__ == "__main__":`
'''

import example_module

# Call the hello function from the imported module
example_module.hello()

'''
IF WE RUN THIS FILE THE OUTPUT WILL BE:

---------------------

Hello from the module!
'''

'''
Pokud máme opravdu velkou aplikaci s mnoho moduly je dobré 
je hierarchicky organizovat do balíčků (packages). 
Balíčky nám umožňují snadnou organizaci těchto modulů v 
balíčku pomocí symbolu `.` - např. balíček.modul. 
Balíček vytvoříme jednoduše jako adresář, do kterého umístíme 
moduly, které chceme aby byly součástí balíčku. 

adresář utils  
    - modul printing.py  
    - modul functions.py  

Import pak provádíme pomocí:    
`import utils.printing, utils.functions` 
Pokud adresář obsahuje soubor `__init__.py`, tak ten je 
puštěn při importu modulu. Tento soubor může obsahovat různé 
instrukce pro inicializaci nebo zde můžeme přímo umístit import 
jednotlivých modulů balíčku:  

`__init__.py`  
import utils.printing  
import utils.functions  
'''
