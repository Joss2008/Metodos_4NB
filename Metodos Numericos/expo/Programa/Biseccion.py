import sublime, sublime_plugin
import os
import math
import numpy
import numpy as np
import pandas as pd
from scipy import optimize
from scipy.optimize import fsolve
from sympy import *
import sympy as sp 
import sympy as sy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def biseccion():
    print("   **METODO DE BISECCION**")
    x= sp.Symbol('x')
    print("*****************")
    print("Ingreso de datos")
    print("Ejemplo: 0.95x^3 - 5.9x^2 + 10.9x - 6")
    print("Grado mayor: 3")
    print("Ingresar el valor de x^3 -> 0.95")
    print("Ingresar el valor de x^2 -> -5.9")
    print("Ingresar el valor de x^1 -> 10.9")
    print("Ingresar termino independiente -> -6")
    print("*****************")
    num=int(input("Ingrese el mayor grado de la funcion -> "))
    num+=1
    vectorx=[1]*num
    vector=[1]*num
    c=num-1
    for i in range(0,num-1):
        vectorx[i]=float(input("Ingrese el valor de x^"+str(c)+" -> "))
        c-=1
    vectorx[(num-1)]=float(input("Ingrese el numero independiente"+" -> "))
    cc=num-1
    for i in range(0,num-1):
        vector[i]=(x**cc)
        cc-=1
    vector[(num-1)]=1
    funcion=0
    for i in range(0,num):
        funcion+=vectorx[i]*(vector[i])
    funcionx = lambdify(x, funcion)
    def funcion(x):
        fun=funcionx
        return fun(x)
    xini = float(input("Valor de x inicial ->"))
    xfini = float(input("Valor de x final ->"))
    ep = float(input("Valor de epsilon ->"))
    interac = []
    vax1 = []
    vax2 = []
    vax3 = []
    # Este metodo es por el cual se aplica el método de biseccion en donde se pasan los valores de epsilon, x inicial, x final y desde donde comenzara el contador
    def ciclo2 (eps, xo, xf, contador) :
        cont = contador
        # Se procede a encontrar el valor intermedio entre los 2 valores de x
        xmid = (xo + xf)/2
        raiz = 0
        # Se guarda en esta variable el valor absoluto con el cual se realizara un comprobacion
        valorabs = abs(funcion(xo)-funcion(xmid))
        cont += 1
        # Con este if se trata de encontrar si el valor ya cambio de signo
        interac.append(cont)
        vax1.append(xo)
        vax2.append(xf)
        vax3.append(xmid)
        valoresbiseccion = pd.DataFrame(data={"Xinicial":vax1, "Xfinal":vax2, "xmedio":vax3}, index=interac)
        if(funcion(xo)*funcion(xmid)<0):
            # Luego se compruba si el valor absoluto encontrado anteriormente es menor o igual a epsilon, si se cumple se retorna el valor de la raiz
            if (valorabs <=eps):
                # La raiz o el punto donde esta la raiz se debe encontrar con la mitad de la suma del xmedio y el xinicial
                raiz = (xmid+xo)/2
                print("Numero de interacciones: ", cont)
                print(valoresbiseccion)
                return raiz
            else:
                return ciclo2(eps, xo, xmid, cont)
        else:
            valorabs = abs(funcion(xmid)-funcion(xf))
            # Luego se compruba si el valor absoluto encontrado anteriormente es menor o igual a epsilon, si se cumple se retorna el valor de la raiz
            if (valorabs <=eps):
                print("Numero de interacciones: ", cont)
                # La raiz o el punto donde esta la raiz se debe encontrar con la mitad de la suma del xmedio y el xfinal
                raiz = (xmid+xf)/2
                print(valoresbiseccion)
                return raiz
            else:
                return ciclo2(eps, xmid, xf, cont)
    print("El valor de la raíz con el método de bisección: ", ciclo2(ep, xini, xfini, 0))
    py=[1]*200
    px=[1]*200
    xi=0
    # Recorremos la funcion
    for y in range(0,200):
        xi = xi + 0.1
        py[y]=funcion(xi)
        px[y]=xi
    # El espacio que tomara el eje x, en este caso comienza desde el punto 1 hasta el punto 4
    x=np.linspace(1,200)
    plt.plot(px, py, color='b')
    plt.axhline(0,color='red',lw=0.5)
    plt.show()
    print(" ")
#-------------------------------------
def aproximaciones():
    print("   **METODO DE APROXIMACIONES**")
    x= sp.Symbol('x')
    print("*****************")
    print("Ingreso de datos")
    print("Ejemplo: 0.95x^3 - 5.9x^2 + 10.9x - 6")
    print("Grado mayor: 3")
    print("Ingresar el valor de x^3 -> 0.95")
    print("Ingresar el valor de x^2 -> -5.9")
    print("Ingresar el valor de x^1 -> 10.9")
    print("Ingresar termino independiente -> -6")
    print("*****************")
    num=int(input("Ingrese el mayor grado de la funcion -> "))
    num+=1
    vectorx=[1]*num
    vector=[1]*num
    c=num-1
    for i in range(0,num-1):
        vectorx[i]=float(input("Ingrese el valor de x^"+str(c)+" -> "))
        c-=1
    vectorx[(num-1)]=float(input("Ingrese el numero independiente"+" -> "))
    cc=num-1
    for i in range(0,num-1):
        vector[i]=(x**cc)
        cc-=1
    vector[(num-1)]=1
    funcion=0
    for i in range(0,num):
        funcion+=vectorx[i]*(vector[i])
    funcionx = lambdify(x, funcion)
    def funcion(x):
        fun=funcionx
        return fun(x)
    interac = []
    vax1 = []
    vax2 = []
    vax3 = []
    xini = float(input("Valor de x inicial ->"))
    ep = float(input("Valor de epsilon ->"))
    # Este metodo es por el cual se aplica el método de Aprocimaciones
    def ciclo3 (contador, eps, xinicial, deltax) :
        # Se procede a pasar los valores que se definieron
        cont = contador
        e = eps
        xo = xinicial
        deltx = deltax
        # Encontramos el nuevo valor de x
        xnuevo = xo + deltx
        raiz = 0
        cont += 1
        # Debemos encontrar el valor absoluto para poder saber cuando se encontro la raíz
        absoluto = abs(funcion(xo)-funcion(xnuevo))
        # Comprobamos si se produjo un cambio de signo
        interac.append(cont)
        vax1.append(xo)
        vax2.append(deltx)
        vax3.append(absoluto)
        valoresaproxi = pd.DataFrame(data={"Xinicial":vax1, "Delta x":vax2, "error":vax3}, index=interac)
        if((funcion(xnuevo)*funcion(xo))<0):
            # Luego comprobamos si el absoluto es menor que el valor de epsilon
            if (absoluto <= e ):
                # Si se cumple la sentencia anterior lo que se realiza es que el valor de la suma del nuevo valor de x y el de inicial se divide en 2
                raiz = (xnuevo+xo)/2
                print("Numero de interacciones: ", cont)
                print(valoresaproxi)
                return raiz
            else:
                # Si lo anterior no se cumple lo que se realiza es que el valor de delta se divide en 10 esto para poder acercanos al valor de la raiz poco a poco
                deltx = deltx/10
                return(ciclo3(cont,e,xo,deltx))
        return(ciclo3(cont,e, xnuevo, deltx))
    print("El valor de la raíz con el método de aproximacion: ", ciclo3(0, ep, xini, 1))
    py=[1]*200
    px=[1]*200
    xi=0
    # Recorremos la funcion
    for y in range(0,200):
        xi = xi + 0.1
        py[y]=funcion(xi)
        px[y]=xi
    # El espacio que tomara el eje x, en este caso comienza desde el punto 1 hasta el punto 4
    x=np.linspace(1,200)
    plt.plot(px, py, color='b')
    plt.axhline(0,color='red',lw=0.5)
    plt.show()
    print(" ")
    print(" ")