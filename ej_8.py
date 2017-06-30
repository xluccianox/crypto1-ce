import sys

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

print ("8) Consideremos la siguiente implementación de RSA. Una autoridad confiable elige dos primos grandes p y q y computa n = p * q que será utilizado por todos los usuarios. La autoridad le brinda a cada usuario una clave privada d_i y e_i tal que e_i != e_j si i != j.")
print ("a) Probar que si dos usuarios, i y j, para los cuales (e_i, e_j) = 1 reciben el mismo mensaje m, un intruso puede reconstruir m usando n, e_i, e_j, m^e_i, m^e_j.")
print ("b) Deducir conclusiones acerca de la seguridad de este sistema.\n")

# Ejemplo:
# n = 179
# e_i = 13
# e_j = 9
# c_i = 32
# c_j = 127
# Solución: m = 10

n = int(input("Ingrese el n (p*q): "))
e_i = int(input("Ingrese e_i (clave pública de i): "))
e_j = int(input("Ingrese e_j (clave pública de j): "))
c_i = int(input("Ingrese c_i (m^e_i, mensaje m cifrado con clave privada d_i): "))
c_j = int(input("Ingrese c_j (m^e_j, mensaje m cifrado con clave privada d_j): "))

print("\nCalculo euclides extendido para e_i, e_j:")
(alpha, beta) = eea(e_i, e_j)

# Hago que alpha sea siempre le positivo
if(alpha < beta):
	aux = alpha
	alpha = beta
	beta = aux

print("alpha: ", alpha)
print("beta: ", beta)

print("\nHallo el inverso multiplicativo de c_i modulo n")
inv_i = find_inverse(c_i , n)
if(inv_i < 0):
	inv_i = n - inv_i
print("inv_i: ",inv_i)

print("\nHallo el inverso multiplicativo de c_j modulo n")
inv_j = find_inverse(c_j , n)
if(inv_j < 0):
	inv_j = n - inv_j
	
print("inv_j: ", inv_j)

print("\nDesencripto utilizando m = c_i^alpha * inv_j^|beta| (mod n)")
m = (pow(c_i, alpha) * pow(inv_j, abs(beta))) % n
print("Mensaje:")
print(m)