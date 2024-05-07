matriz = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]

def fnt_agregar(dato, fila, columna):
    if dato == 'A' and (fila==0 and columna== 0):
        print('Ubicado exelentemente')
        matriz[fila][columna] = 'A' 
    else:
        print('Ubicación no valida')

    if dato == 'B' and (fila==0 and columna== 1):
        print('Ubicado exelentemente')
        matriz[fila][columna] = dato
        fnt_impreaion_matriz
    else:
        print('Ubicación no valida')

    if dato == 'C' and (fila==0 and columna== 2):
        print('Ubicado exelentemente')
        matriz[fila][columna] = dato
        fnt_impreaion_matriz
    else:
        print('Ubicación no valida')

    if dato == 'D' and (fila==0 and columna== 3):
        print('Ubicado exelentemente')
        matriz[fila][columna] = dato
        print (fnt_impreaion_matriz)
    else:
        print('Ubicación no valida')

    if dato == 'E' and (fila==0 and columna== 4):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'F' and (fila==0 and columna== 5):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'G' and (fila==1 and columna== 0):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'H' and (fila==1 and columna== 1):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'I' and (fila==1 and columna== 2):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'J' and (fila==1 and columna== 3):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'K' and (fila==1 and columna== 4):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'L' and (fila==1 and columna== 5):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'M' and (fila==2 and columna== 0):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'N' and (fila==2 and columna== 1):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'O' and (fila==2 and columna== 2):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'P' and (fila==2 and columna== 3):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'Q' and (fila==2 and columna== 4):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'R' and (fila==2 and columna== 5):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'S' and (fila==3 and columna== 0):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'T' and (fila==3 and columna== 1):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'U' and (fila==3 and columna== 2):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'V' and (fila==3 and columna== 3):
        print('Ubicado exelentemente')
    else: 
        print('Ubicación no valida')

    if dato == 'W' and (fila==3 and columna== 4):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'X' and (fila==3 and columna== 5):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    
    if dato == 'Y' and (fila==4 and columna== 0):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'Z' and (fila==4 and columna== 1):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'CH' and (fila==4 and columna== 2):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'LL' and (fila==4 and columna== 3):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')

    if dato == 'RR' and (fila==4 and columna== 4):
        print('Ubicado exelentemente')
    else:
        print('Ubicación no valida')
    



def fnt_impreaion_matriz():
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print(matriz[i][j], end='  ')
        print(matriz)
       

sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impreaion_matriz()
    fnt_agregar(input('Dato: '), int(input('Fila: ')), int(input('Columna: ')))




    




    

