import re
import os

#print(os.listdir())

def creater():
    os.makedirs('test\empty', exist_ok=True)
    os.makedirs('test\empty2\eeh', exist_ok=True)

if not 'test' in os.listdir():
    os.mkdir('test')
else:
    os.chdir('test')
    
    creater()
    print(os.listdir())
    
