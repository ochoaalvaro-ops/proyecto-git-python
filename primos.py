def es_primo(n: int):
    if n < 2:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Dime un número: "))
print(f"¿El {numero} es primo?", es_primo(numero))