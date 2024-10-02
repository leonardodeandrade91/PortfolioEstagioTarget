def inverterString(s):
    stringInvertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        stringInvertida += s[i]
        
    return stringInvertida

# Exemplo de uso:
entrada = input("Informe uma string: ")
print("String invertida: ", inverterString(entrada))
