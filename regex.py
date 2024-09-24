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
