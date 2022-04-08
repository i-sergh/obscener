import os
import re
print(os.getlogin())

print(os.getcwd())

print(os.listdir())


os.chdir('test\empty')
print(os.listdir())
"""
#print('Новый текстовый документ*' in os.listdir())
for name in os.listdir():
    if re.search( 'Новый текстовый документ', name):
        os.rename(name, re.sub( 'Новый текстовый документ', '123', name))
#print(re.search( 'Новый текстовый документ',os.listdir()[0] ))
        
#os.rename(os.listdir()[0], re.sub('Новый текстовый документ', '123', os.listdir()[2]))
os.chdir('..')
os.chdir('test/n')
#os.rename('chMe.txt', 'wow.txt')

print(os.listdir())
"""
