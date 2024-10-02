def fibonacciSequence(n):
    a, b = 0, 1
    sequence = [a]  # Inicia a sequência com 0

    while b <= n:
        sequence.append(b)
        a, b = b, a + b

    return sequence

# Solicitar entrada do usuário
numero = int(input("Informe um número: "))

# Calcular a sequência de Fibonacci
sequencia = fibonacciSequence(numero)

# Verificar se o número está na sequência
if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
    print("Sequência de Fibonacci gerada: ", sequencia)
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
