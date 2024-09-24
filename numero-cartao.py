import re

def validar_cartao_credito(numero_cartao):
    # Expressão regular corrigida para validar somente espaços OU somente hífens
    padrao = r"^(\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})$"
    
    # Verifica se o número do cartão corresponde ao padrão
    if re.match(padrao, numero_cartao):
        return True
    else:
        return False

# Exemplo de uso
cartoes_teste = [
    "1234 5678 9123 4567",  # Válido
    "1234-5678-9123-4567",  # Válido
    "1234567891234567",      # Inválido
    "1234-5678 9123-4567",   # Inválido (mistura de separadores)
    "1234 5678 9123 456",    # Inválido (um número a menos)
    "1234 5678 9123 45678",    # Inválido (um número a mais)
]

for cartao in cartoes_teste:
    if validar_cartao_credito(cartao):
        print(f"Cartão {cartao} é válido.")
    else:
        print(f"Cartão {cartao} é inválido.")