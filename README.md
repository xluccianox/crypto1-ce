# Ejercicios Criptografía I
Algunos POC de los ejercicios de Criptografía I del Master en Seguridad en Informática en la Universidad de Buenos Aires hechos en python 3.

## Ejercicios RSA
### Guia 2
#### Ejercicio 7 :
```> python ej_7.py```

Alicia y Pedro suelen comunicarse utilizando RSA y la siguiente clave pública (e, n) = (5, 967331). Por un descuido de Alicia, Oscar se apodera de phi(n) = 965352. Se pide:
1. Mostrar como puede hacer Oscar para hallar la clave privada (d, n)
2. Ahora que Oscar tiene (d, n), qué daños puede ocasionar a Alicia y Pedro, sin que estos se den cuenta.
3. Es claro que se necesita phi(n) para determinar valores válidos de e y de d. ¿Qué tenemos que hacer con phi(n) una vez que ya no lo utilizamos?

#### Ejercicio 8 :
```> python ej_8.py```

Consideremos la siguiente implementación de RSA. 
Una autoridad confiable elige dos primos grandes p y q y computa n = p * q que será utilizado por todos los usuarios. La autoridad le brinda a cada usuario una clave privada d_i y e_i tal que e_i != e_j si i != j.
1. Probar que si dos usuarios, i y j, para los cuales (e_i, e_j) = 1 reciben el mismo mensaje m, un intruso puede reconstruir m usando n, e_i, e_j, m^e_i, m^e_j.
2. Deducir conclusiones acerca de la seguridad de este sistema.
