#! /bin/python3

from PIL import Image
from sys import argv

def bigger(*numbers):
    
    m = max(numbers)
    return numbers.index(m), m



scales = [
    ' ',
    '-',
    '+',
    '=',
    '#',
    '█',
    
]

colors = [
    '\33[31m', # red 
    '\33[32m', # green
    '\33[34m', # blue
    '\33[37m', # white
    
    '\33[33m', # yellow
    '\33[35m', # cyan
    '\33[36m', # magenta
]

HELP = 'arguments: <image> --scale [scale (default=1)] --capprox [int (default=5)] [--nocolor] [--fat] --save [out] \
\n\t\t capprox: likelyhood of using secondary colors\
\n\t\t fat: double the width of the output\
\n\t\t save: write output to [out] file. If nocolor is not active, will store ANSII color escape codes as well'


DIVIDE = 1
APPROX = 5
DOCOLOR = 1
DOFAT = 0
SAVE = 0

try:
    img = argv[1]
except: print(HELP); exit(1)

for i in range(len(argv)):
    if argv[i] == '--help':
        print(HELP); exit(1)
    
    if argv[i] == '--scale':
        try:
            DIVIDE = int(argv[i+1])
        except: 0

    if argv[i] == '--capprox':
        try:
            APPROX = int(argv[i+1])
        except: 0
    
    if argv[i] == '--nocolor':
        DOCOLOR = 0
    
    if argv[i] == '--fat':
        DOFAT = 1
    
    if argv[i] == '--save':
        try:
            SAVE = argv[i+1]
        except: 0

if not img:
    print('missing input file'); exit(1)
    
image = Image.open(img)
pixels = image.load()


w, h = int(image.width/DIVIDE), int(image.height/DIVIDE)

to_print = '\33[1;37m'

for y in range(h):
    to_print+=f'\n '
    for x in range(w):
        try:
            r, g, b = pixels[x*DIVIDE, y*DIVIDE]
        except:
            GARBAGE, r, g, b = pixels[x*DIVIDE, y*DIVIDE]

        r = int(r/10)
        g = int(g/10)
        b = int(b/10)
        
        #if y == 38:
        #    print(r, g, b)
        
        bigI, big = bigger(r, g, b)
        
        if big == 0 or (r == g and g == b):
            color = colors[3]

        
        elif abs(r-g) <= APPROX:
            color = colors[4]
            big = r
        
        elif abs(b-g) <= APPROX:
            color = colors[5]
            big = g
        
        elif abs(r-b) <= APPROX:
            color = colors[6]
            big = r

        else:
            color = colors[bigI]
        
        scale = scales[int(big/5)]

        if not DOCOLOR:        
            color = ''
        to_print += color+scale
        for i in range(DOFAT):
            to_print += scale

if SAVE:
    with open(SAVE, 'w') as f:
        f.write(to_print)
else:
    print(to_print)
        
        


