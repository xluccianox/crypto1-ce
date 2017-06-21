# Ejercicios Criptografía I
Algunos ejercicios de Criptografía I del Master en Seguridad en Informática en la Universidad de Buenos Aires resueltos en python 3.

## Ejercicios RSA
### Ejercicio 8 :
```> python ej_8.py```

Consideremos la siguiente implementación de RSA. 
Una autoridad confiable elige dos primos grandes p y q y computa n = p * q que será utilizado por todos los usuarios. La autoridad le brinda a cada usuario una clave privada d_i y e_i tal que e_i != e_j si i != j.
1. Probar que si dos usuarios, i y j, para los cuales (e_i, e_j) = 1 reciben el mismo mensaje m, un intruso puede reconstruir m usando n, e_i, e_j, m^e_i, m^e_j.
2. Deducir conclusiones acerca de la seguridad de este sistema.
