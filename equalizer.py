# -*- coding: utf-8 -*-

from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

def main(filename, r):
    # должна обрабатывать чб файл <filename> в формате PNG, уравнивать гистограмму
    # и записывать результат в <filename>.equalized.png
    img = Image.open(filename)
    img.load()

    a = np.array(img.getdata(), dtype=np.uint8).reshape(img.size[::-1])
    b = np.zeros(img.size[::-1], dtype=np.uint8)
 
   # код сюда ....
    #histo=np.histogram(a)
    hist=[0 for i in range(256)]
    for i in range(h):
        for j in range(w):
            hist[a[i][j]]+=1
    
    for i in range(h):
        for j in range(w):
            b[i][j]=(np.sum(hist[:a[i][j]:])/a.size)*256     
    
    
    newimg = Image.fromarray(b);
    newimg.show()
    newimg.save(filename+'.equalized.png')

    
    newimg = Image.fromarray(b);
    newimg.show()
    newimg.save(filename+'.equalized.png')



if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        main(sys.argv[1], r=3)
    else:
        print("Must give filename.\n")




