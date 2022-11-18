def CantidadOperaciones(m,s):
    for d in range(1,n):
        for i in range(1, longitud - d):
            j=i+d
            min=float('inf')
            for k in range(i,j):
                costo=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if (costo<min):
                    min=costo
                    s[i][j]=k
            m[i][j]=min

def Parentesis(s,inicio,final):
    if inicio == final:
        print('A[{}]'.format(inicio), end='')
        return
    k=s[inicio][final]
    print('(',end='')
    Parentesis(s, inicio, k)
    Parentesis(s, k + 1, final)
    print(')',end='')

if __name__ == '__main__':
    n = int(input('Ingrese numero de matrices: '))
    p = []
    for i in range(n):
        temp = int(input('Ingrese el número de filas de la matriz {}: '.format(i + 1)))
        p.append(temp)
    temp = int(input('Ingrese el número de columnas de la matriz {}: '.format(n)))
    p.append(temp)
    longitud=len(p)
    m = [[0] * longitud for i in range(longitud)]
    s = [[0] * longitud for i in range(longitud)]
    CantidadOperaciones(m,s)
    print('Número total de multipicaciones necesitadas:', m[1][n])
    Parentesis(s,1,n)
