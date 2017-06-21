import sys
import math

# Algoritmo Extendido de Euclides
# Fuente: https://gist.github.com/tylerl/1239116
# Ver: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def eea(a,b):
	if b==0:return (1,0)
	(q,r) = (a//b,a%b)
	(s,t) = eea(b,r)
	return (t, s-(q*t) )

# Encuentra el inverso multiplicativo de x (mod y)
# Fuente: https://gist.github.com/tylerl/1239116
# Ver: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def find_inverse(x,y):
	inv = eea(x,y)[0]
	#if inv < 1: inv += y #we only want positive values
	return inv

print ("7) Alicia y Pedro suelen comunicarse utilizando RSA y la siguiente clave pública (e, n) = (5, 967331). Por un descuido de Alicia, Oscar se apodera de phi(n) = 965352. Se pide:")
print ("a) Mostrar como puede hacer Oscar para hallar la clave privada (d, n)")
print ("b) Ahora que Oscar tiene (d, n), qué daños puede ocasionar a Alicia y Pedro, sin que estos se den cuenta.")
print ("c) Es claro que se necesita phi(n) para determinar valores válidos de e y de d. ¿Qué tenemos que hacer con phi(n) una vez que ya no lo utilizamos?\n")

n = int(input("Ingrese el n (p*q): "))
e = int(input("Ingrese e (clave pública): "))
phi = int(input("Ingrese phi(n): "))

print("\nParte a):")
print("Sabemos phi(n) = (p - 1)*(q - 1)")
print("Entonces phi(n) = (n + 1) - (p + q)")
print("(n + 1) - phi(n) = p + q")
print("I) (n + 1) - phi(n) - p = q")
print("II) Y sabemos que n = p*q \n")

print("Reemplazo I) en II):")
print("n = p*((n + 1) - phi(n) - p)")
print("n = p*n + p -p*phi(n) - p^2 ")
print("n = -p^2 + p(n + 1 - phi(n))\n")

print("Igualo a 0 y tengo una ecuación cuadrática:")
print("p^2 - p(n + 1 - phi(n)) + n = 0\n")

print("Resuelvo la ecuación usando la fórmula de Bhaskara:")
a = 1
b = -(n + 1 - phi)
c = n

p = int(abs((-b + math.sqrt(b*b -4*a*c)) / 2*a))

print("Nuestro primo p es: ")
print(p)
print("Nuestro primo q es: ")
q = int(n/p)
print(q)

print("\nObtención la clave privada d:")
print("Sabemos que d*e = 1 (mod phi(n))")
print("Entonces: d = e^-1 (mod(phi(n)))")
print("Hallo el inverso multiplicativo de e módulo phi(n):")

inv_e = find_inverse(e , phi)
print(inv_e)

print("Calculo la clave privada d:")
d = inv_e % phi
print(d)

print("\nParte b):")
print("Teniendo la clave privada de Alicia, Oscar puede descifrar todos los mensajes que envía Pedro a Alicia (cifrados con la cláve pública de Alicia).")

print("\nParte c):")
print("Una vez que ya lo utilizamos al phi(n) es necesario eliminarlo de la memoria.")



