import os
import sys
import shutil

header = 'Content-Type: text/x-zim-wiki'

def f(file):
    with open(file, 'r+', encoding='utf8') as f:
        content = f.read()
        if content.startswith(header):
            print('\tNot processed!!! ' + file)
            return
        f.seek(0, 0)
        f.write(header + '\n\n' + content)
        print(file)

if len(sys.argv) > 1:
    d = sys.argv[1]
else:
    d= '.'
if os.path.isdir(d):
    for root,_,files in os.walk(d):
        for file in files:
            full = os.path.join(root, file)
            if not full.endswith('txt'):
                continue
            f(full)
            if ' ' in full:
                print('rename ' + full)
                shutil.move(full, full.replace(' ', '_'))
elif os.path.isfile(d):
    f(d)
    if ' ' in d:
        print('rename ' + file)
        shutil.move(d, d.replace(' ', '_'))

os.system('pause')