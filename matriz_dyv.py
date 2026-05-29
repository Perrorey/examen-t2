import random
 
n = int(input("Ingrese el tamaño de la matriz (N): "))
 
mat = [[random.randint(99, 999) for j in range(n)] for i in range(n)]
 
print("\nMatriz generada:")
for fila in mat:
    print("  ".join(str(x) for x in fila))
 
def contar_fila(fila, ini, fin):
    if ini == fin:
        return 1 if fila[ini] % 5 == 0 or fila[ini] % 7 == 0 else 0
    mid = (ini + fin) // 2
    return contar_fila(fila, ini, mid) + contar_fila(fila, mid + 1, fin)
 
def contar_mat(ini, fin):
    if ini == fin:
        return contar_fila(mat[ini], 0, n - 1)
    mid = (ini + fin) // 2
    return contar_mat(ini, mid) + contar_mat(mid + 1, fin)
 
total = contar_mat(0, n - 1)
print(f"\nCantidad de multiplos de 5 o 7: {total}")
 
