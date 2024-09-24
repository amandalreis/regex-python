import re;

# Questão 13
def validar_numero_inteiro_ou_decimal(numero):
    padrao = r'^[0-9]+(\.[0-9]+)?$'

    numero_str = str(numero)

    if re.match(padrao, numero_str):
        return f"{numero} é um número inteiro ou decimal válido."
    else:
        return f"{numero} não é um número inteiro ou decimal válido."
    
print(validar_numero_inteiro_ou_decimal(2.3))

print("-" * 40)

def validar_cartao_credito(numero_cartao):
    # Expressão regular para validar somente espaços OU somente hífens
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

print("-" * 40)

def validar_senha(senha: str) -> str:
    
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'

    if re.match(regex, senha):
        return f'A senha {senha} é forte!'
    return f'A senha {senha} é fraca'

casos_teste = [
    "Senha@123",
    "Exemplo#462",
    "S@12aB",
    "senha@123"
]

for senha in casos_teste:
    print(validar_senha(senha))

print("-" * 40)

