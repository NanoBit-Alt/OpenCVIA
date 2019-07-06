    #cv2 é BGR

#Reconhecimento de Imagem
import cv2
from sklearn import tree
#import numpy as np
#from matplotlib import pyplot as plt
#from time import sleep
arquivo = open('arq.txt', 'w')

iJ = cv2.imread("soccer-1.jpg")
print(iJ.shape)
eixox = int(iJ.shape[1] // 2)  #Divide o eixo x
eixoy = int(iJ.shape[0] // 2)  #Divide o eixo y
print(eixox)
print(eixoy)
print('=======')

def pintar (x, y, cR, cG, cB):
    for q in range(7):          #Pinta 8 em 8
        for w in range(7):      #Pinta 8 em 8
            iJ.itemset((y+w, x+q, 2), cR)    #Vermelho
            iJ.itemset((y+w, x+q, 1), cG)    #Verde
            iJ.itemset((y+w, x+q, 0), cB)    #Azul
def salvar (nome):
    cv2.imwrite(f'{nome}.jpg', iJ)
#vermelho = 0
#verde = 1
#azul = 2
#amarelo = 3
#rosa = 4
#branco = 5
#preto = 6
#verde menta = 7
#verde menta claro = 8
#verde lima = 9
#cinza prata = 10
#azul marinho = 11
#rosa pink fraco = 12
#laranja = 13
#marrom = 14
#cinza escuro = 15
#fe = []
#def chama_lista (a, b, c,):
#    (f'{a}, {b}, {c}, ')

##Tentando algo novo

#for x in range(10):
#    for y in range(10):
#        for z in range(1):
#            fe = [(x, y, z) +  chama_lista(x, y, z,)]
#print(fe)

#la = list(range(100))
#print(la)

#IA
feature = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (255, 255, 255), (0, 0, 0), (0, 255, 150), (150, 255, 150), (150, 255, 0), (125, 125, 125), (0, 125, 125), (0, 0, 125), (220, 120, 120), (255, 125, 0), (110, 62, 0), (35, 35, 35)]     # [46, 102, 115], [157, 152, 24]]
labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 12, 13, 14, 15]
nnt = tree.DecisionTreeClassifier()
nnt = nnt.fit(feature , labels)

for i in range(0, eixox, 8):        #x,x,step
    for u in range(0, eixoy, 8):    #y,y,step
        print (i)
        print (u)
        r = iJ.item(u, i, 2)
        g = iJ.item(u, i, 1)
        b = iJ.item(u, i, 0)

        if(nnt.predict([[r, g, b]])) == 0:
            print("Vermelho")
            pintar(u, i, 255, 0, 0)
        elif(nnt.predict([[r, g, b]])) == 1:
            print("Verde")
            pintar(u, i, 0, 255, 0)
        elif (nnt.predict([[r, g, b]])) == 2:
            print("Azul")
            pintar(u, i, 0, 0, 255)
        elif (nnt.predict([[r, g, b]])) == 3:
            print("Amarelo")
            pintar(u, i, 255, 255, 0)
        elif (nnt.predict([[r, g, b]])) == 4:
            print("Rosa")
            pintar(u, i, 255, 0, 255)
        elif (nnt.predict([[r, g, b]])) == 5:
            print("Branco")
            pintar(u, i, 255, 255, 255)
        elif (nnt.predict([[r, g, b]])) == 6:
            print("Preto")
            pintar(u, i, 0, 0, 0)
        elif (nnt.predict([[r, g, b]])) == 7:
            print("Verde menta")
            pintar(u, i, 0, 255, 150)
        elif (nnt.predict([[r, g, b]])) == 8:
            print("Verde menta claro")
            pintar(u, i, 150, 255, 150)
        elif (nnt.predict([[r, g, b]])) == 9:
            print("Verde lima")
            pintar(u, i, 150, 255, 0)
        elif (nnt.predict([[r, g, b]])) == 10:
            print("Cinza prata")
            pintar(u, i, 125, 125, 125)
        elif (nnt.predict([[r, g, b]])) == 11:
            print("Azul marinho")
            pintar(u, i, 0, 0, 125)
        elif (nnt.predict([[r, g, b]])) == 12:
            print("Rosa pink")
            pintar(u, i, 220, 120, 120)
        elif (nnt.predict([[r, g, b]])) == 13:
            print("Laranja")
            pintar(u, i, 255, 125, 0)
        elif (nnt.predict([[r, g, b]])) == 14:
            print("Marrom")
            pintar(u, i, 145, 90, 20)
        elif (nnt.predict([[r, g, b]])) == 15:
            print("Cinza escuro")
            pintar(u, i, 35, 35, 35)
        else:
            print("Error")
        salvar('soccer-2')
        print('=========== \n')

#print (iJ.item(u, i, 2)) #R
#print (iJ.item(u, i, 1)) #G
#print (iJ.item(u, i, 0)) #B
arquivo.write('R: \n' + str(iJ.item(u, i, 2)) +'\n'+ 'G: \n'  + str(iJ.item(u, i, 1)) +'\n'+ 'B: \n' + str(iJ.item(u, i, 0)) +'\n'+  '\n'+'========='+ '\n')
arquivo.close()

#0 = Red     /vermelho
#1 = Green   /verde
#2 = Blue    /azul

#a = 0
#IA
#b = map(a, 0, 255, 0, 10)

#vermelho = 0
#verde = 1
#azul = 2
#ciano = 3
#amarelo = 4