import re
import os


"""
creates:
    test
        |_ test
        |        |_empty
        |        |_empty2
        |        |              |_eeh
        |        |_nonempty
        |        |                  |_empty
        |        |                  |            |_empty
        |        |                  |_lolkek.txt
        |        |                  |_NOTket.txt
        |        |_notempty
        |                        |_owch
        |                        |_nonempty2
        |                        |                   |_empty2
        |                        |_ kekt.txt  
        |_kek1.txt                                           
        |_kek.txt
        |_lolkek1.txt
                              

"""


def folderCreater():
    os.makedirs('test\\empty', exist_ok=True)
    os.makedirs('test\\empty2\\eeh', exist_ok=True)
    os.makedirs('test\\nonempty\\empty\\empty', exist_ok=True)
    os.makedirs('test\\notempty\\owch', exist_ok=True)
    
    os.makedirs('test\\notempty\\nonempty2\\empty2', exist_ok=True)

if not 'test' in os.listdir():
    os.mkdir('test')
    
os.chdir('test')
    
folderCreater()
f = open("kek1.txt", "w+")
f.close()
f = open("kek.txt", "w+")
f.close()
f = open("lolkek1.txt", "w+")
f.close()

os.chdir('test\\nonempty')
f = open("lolkek.txt", "w+")
f.close()
f = open("NOTket.txt", "w+")
f.close()
os.chdir('..')
os.chdir('notempty\\nonempty2')
f = open("kekt.txt", "w+")
f.close()
os.chdir('..\\..\\..')
print(os.listdir())
    
