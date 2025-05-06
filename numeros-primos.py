numeros_primos = [] 

for numero_actual in range(1, 1001): 
    
   
    if numero_actual < 2:
        es_primo = False
    else:
        es_primo = True
        
        for divisor in range(2, numero_actual):
            if numero_actual % divisor == 0:
               
                es_primo = False
                
        
    if es_primo:
        numeros_primos.append(numero_actual)
        
print(f"Los numeros primos encontrados son: {numeros_primos}")
