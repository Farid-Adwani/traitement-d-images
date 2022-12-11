import math
from math import *
import numpy as np
import time
from random import randrange, randint


class Image:
    matrix = None
    type = ""
    width = 0
    height = 0
    max_gray = 0


    def decalage(self,decalage):
        # calcul des bornes de l'histogramme
        
        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                dec=self.matrix[h][w]+decalage;
                if(dec>255) :
                    dec=255
                if(dec<0):
                    dec=0
                row.append(dec)
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image


    def etire(self):
        # calcul des bornes de l'histogramme
        his=self.histogram()
        n = len(his)
        imin,imax=0,n-1
        while his[imin] == 0 and imin < n: imin += 1
        while his[imax] == 0 and imax > 0: imax -= 1

        
        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append(math.ceil(255*(self.matrix[h][w]-imin)/(imax-imin)))
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image

    def contrast_morceau(self,x1,y1,x2,y2):
        im=self.etire()
        new_matrix = [[]]
        for h in range(self.height):
            row = []
            for w in range(self.width):
                if im.matrix[h][w] < x1:
                    row.append(math.ceil((y1-0)*(self.matrix[h][w]-0)/(x1-0)+0))
                elif im.matrix[h][w] < x2:
                    row.append(math.ceil((y2-y1)*(self.matrix[h][w]-x1)/(x2-x1)+y1))
                else :
                    row.append(math.ceil((255-y2)*(self.matrix[h][w]-x2)/(255-x2)+y2))
            new_matrix.append(row)
            
        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image
    
              
    def __init__(self, matrix=None, type="", width=0, height=0, max_gray=0):
        self.matrix = matrix
        self.type = type
        self.width = width
        self.height = height
        self.max_gray = max_gray

    def load_from_pgm(self, pgmPath):

        file = open(pgmPath, 'rb')
        self.type = file.readline().decode().strip()
        line = file.readline()
        while chr(line[0]) == '#':
            line = file.readline()
        width_binary, height_binary = line.split()
        self.width, self.height = int(width_binary), int(height_binary)
        self.max_gray = int(file.readline())
        self.matrix = []
        if(self.type == "P5"):
            for i in range(self.height):
                row = list(file.read(self.width))
                self.matrix.append(row)
        elif(self.type == "P2"):
            for i in range(self.height):
                line = file.readline()
                row = line.split()
                row = list(map(int, row))
                self.matrix.append(row)

        file.close()
        
        
    def load_from_ppm(self, pgmPath,r,g,b):
    
        file = open(pgmPath, 'rb')
        self.type = file.readline().decode().strip()
        line = file.readline()
        while chr(line[0]) == '#':
            line = file.readline()
        print(line.split())
        width_binary = line.split()[0]
        height_binary = line.split()[1]
        
        self.width, self.height = int(width_binary), int(height_binary)
        print(self.width)
        print(self.height)
        
        self.max_gray = int(file.readline())
        self.matrix = []
        for i in range(self.height):
            line = file.readline()
            
            row = line.split()
            row2=[]
            x=0
            y=0
            for i in row:
                x=x+1
                if x==1:
                    if int(i)>r:
                        row2.append(255)
                    else:
                        row2.append(0)
                elif x==2:
                    if int(i)>g:
                        row2.append(255)
                    else:
                        row2.append(0)
                elif x==3:
                    if int(i)>b:
                        row2.append(255)
                    else:
                        row2.append(0)
                        
                # y=y+int(i)
                if x==3:
                    x=0
                    # row2.append(y)
                    # y=0
            
            print(row2)
            print("--")
            row2 = list(map(int, row2))
            self.matrix.append(row2)

        file.close()
        
        
    
    def load_from_ppmET(self, pgmPath,r,g,b):
        
        file = open(pgmPath, 'rb')
        self.type = file.readline().decode().strip()
        line = file.readline()
        while chr(line[0]) == '#':
            line = file.readline()
        print(line.split())
        width_binary = line.split()[0]
        height_binary = line.split()[1]
        
        self.width, self.height = int(width_binary), int(height_binary)
        print(self.width)
        print(self.height)
        
        self.max_gray = int(file.readline())
        self.matrix = []
        for i in range(self.height):
            line = file.readline()
            
            row = line.split()
            row2=[]
            x=0
            y=0
            t=0
            c1=0
            c2=0
            c3=0
            for i in row:
                x=x+1
                if x==1:
                    c1=int(i)
                    if int(i)>r:
                        t=t+1
                elif x==2:
                    c2=int(i)
                    
                    if int(i)>g:
                        t=t+1
                elif x==3:
                    c3=int(i)
                    if int(i)>b:
                        t=t+1
                if x==3:
                    x=0
                    if t==3:
                        row2.append(255)
                        row2.append(255)
                        row2.append(255)
                    else:
                        row2.append(0)
                        row2.append(0)
                        row2.append(0)
                        
                        
                    t=0
                    # row2.append(y)
                    # y=0
            
            # x=0
            # y=0
            # for i in row:
            #     x=x+1
            #     if x==1:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
            #     elif x==2:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
            #     elif x==3:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
                            
            #         # y=y+int(i)
                if x==3:
                        x=0
            
            print(row2)
            print("--")
            row2 = list(map(int, row2))
            self.matrix.append(row2)

        file.close()
        
        
    def load_from_ppmOU(self, pgmPath,r,g,b):
        
        file = open(pgmPath, 'rb')
        self.type = file.readline().decode().strip()
        line = file.readline()
        while chr(line[0]) == '#':
            line = file.readline()
        print(line.split())
        width_binary = line.split()[0]
        height_binary = line.split()[1]
        
        self.width, self.height = int(width_binary), int(height_binary)
        print(self.width)
        print(self.height)
        
        self.max_gray = int(file.readline())
        self.matrix = []
        for i in range(self.height):
            line = file.readline()
            
            row = line.split()
            row2=[]
            x=0
            y=0
            t=0
            c1=0
            c2=0
            c3=0
            for i in row:
                x=x+1
                if x==1:
                    c1=int(i)
                    if int(i)>r:
                        t=t+1
                elif x==2:
                    c2=int(i)
                    
                    if int(i)>g:
                        t=t+1
                elif x==3:
                    c3=int(i)
                    if int(i)>b:
                        t=t+1
                if x==3:
                    x=0
                    if t>0:
                        row2.append(255)
                        row2.append(255)
                        row2.append(255)
                    else:
                        row2.append(0)
                        row2.append(0)
                        row2.append(0)
                        
                        
                    t=0
                    # row2.append(y)
                    # y=0
            
            # x=0
            # y=0
            # for i in row:
            #     x=x+1
            #     if x==1:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
            #     elif x==2:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
            #     elif x==3:
            #             if int(i)>r and int(i)>g and int(i)>b:
            #                 row2.append(255)
            #             else:
            #                 row2.append(0)
                            
            #         # y=y+int(i)
                if x==3:
                        x=0
            
            print(row2)
            print("--")
            row2 = list(map(int, row2))
            self.matrix.append(row2)

        file.close()
    
        
    def seuiller(img,r,g,b):
        new_image = np.zeros(img.shape)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # r
                if img[i][j][0] > r:
                    new_image[i][j][0] = 255
                else:
                    new_image[i][j][0] = 0
                # g
                if img[i][j][1] > g:
                    new_image[i][j][1] = 255
                else:
                    new_image[i][j][1] = 0

                #b
                if img[i][j][2] > b:
                    new_image[i][j][2] = 255
                else:
                    new_image[i][j][2] = 0

        return new_image
    
    
    



    def histogram(self):
        histogram = [0] * (self.max_gray + 1)
        for h in range(self.height):
            for w in range(self.width):
                histogram[self.matrix[h][w]] += 1
        return histogram

    def cumulated_histogram(self):
        histogram = self.histogram()
        cumulated_histogram = [0] * (self.max_gray + 1)
        cumulated_histogram[0] = histogram[0]
        for i in range(1, self.max_gray + 1):
             cumulated_histogram[i] = histogram[i] + cumulated_histogram[i - 1]
        return cumulated_histogram

    def save_to_pgm(self, path="samples/output/{0}.pgm".format(round(time.time()))):

        f = open(path, "w")
        f.write("{0}\n{1} {2}\n{3}\n".format(
            self.type, self.width, self.height, self.max_gray))

        for h in range(self.height):
            f.write(' '.join([str(elem) for elem in self.matrix[h]])+'\n')
        f.close()

    def histogram_equalizer(self):

        cumulated_histogram = self.cumulated_histogram()
        LUT = [0] * (self.max_gray + 1)
        print(LUT[0])
        for i in range(self.max_gray + 1):
            LUT[i] = int(self.max_gray * cumulated_histogram[i] /
                         (self.height*self.width))
        
        hist=self.histogram()
        print("Histogramme") 
        print(hist)
        
        
        print("Histogramme cumulé") 
        print(cumulated_histogram)
        print("n1")    
        print(LUT)
        hist_egal=[0] * (self.max_gray + 1)
        
        for i in range(self.max_gray + 1):
            hist_egal[LUT[i]] +=hist[i] 
        print("histogramme égalisé")
        print(hist_egal)
        
        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append(LUT[self.matrix[h][w]])
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        
        print("New Image -------------------------")
        print(new_image.matrix  )
        return new_image

    def bruit(self):
        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                rand=randint(0,21)
                if rand==0:
                    row.append(0)
                elif rand==255:
                    row.append(255)
                else:
                    row.append(self.matrix[h][w])
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image
    
    def average(self, size):
        if (size % 2 == 0):
            raise Exception('filter size must be odd')

        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                pixels = []

                for fh in range(h-size//2, h+size//2):
                    for fw in range(w-size//2, w+size//2):
                        if(fh < 0 or fh >= self.height or fw < 0 or fw >= self.width):
                            continue
                        else:
                            pixels.append(self.matrix[fh][fw])
                average = sum(pixels)/len(pixels)
                row.append(int(average))
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image
    
    def median(self, size):
        if (size % 2 == 0):
            raise Exception('filter size must be odd')

        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                pixels = []

                for fh in range(h-size//2, h+size//2):
                    for fw in range(w-size//2, w+size//2):
                        if(fh < 0 or fh >= self.height or fw < 0 or fw >= self.width):
                            continue
                        else:
                            pixels.append(self.matrix[fh][fw])

                pixels.sort()
                median = pixels[len(pixels)//2]
                row.append(median)
            new_matrix.append(row)

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image
    
    def passeHaut(self):
        size=3
        if (size % 2 == 0):
            raise Exception('filter size must be odd')

        new_matrix = []
        for h in range(self.height):
            row = []
            for w in range(self.width):
                sum=self.matrix[h][w]
                for fh in range(h-size//2, h+size//2):
                    for fw in range(w-size//2, w+size//2):
                        if(fh < 0 or fh >= self.height or fw < 0 or fw >= self.width):
                            ##row.append(self.matrix[h][w])
                            continue
                        else:
                            if fh==h and fw==w:
                                sum+=8*self.matrix[fh][fw]
                            else:
                                sum-=self.matrix[fh][fw]
                if sum <0 :
                    sum=0
                if sum> 255:
                    sum=255
                row.append(sum)
            new_matrix.append(row)
            

        new_image = Image(matrix=new_matrix, type="P2", width=self.width,
                          height=self.height, max_gray=self.max_gray)
        return new_image
    
    def moyenne(self):
        s=0
        for h in range(self.height):
            for w in range(self.width):
                s+=self.matrix[h][w]
        return s/(self.height*self.width)
    
    def variance(self,im):
        bruite=self.bruit()
        moy=bruite.moyenne()
        s=0
        sb=0
        for h in range(bruite.height):
            for w in range(bruite.width):
                s+=(bruite.matrix[h][w]-moy)**2
                sb+=(im.matrix[h][w]-bruite.matrix[h][w])**2
                
        return sqrt(s/sb)
    

        

    
    
    