def es_primo(n: int):
    if n < 2:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("¿El 7 es primo?", es_primo(7))
print("¿El 10 es primo?", es_primo(10))