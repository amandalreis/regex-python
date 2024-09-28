import re;

# Questão 13
def validar_numero_inteiro_ou_decimal(numero):
    padrao = r'^-?[0-9]+(\.[0-9]+)?$'

    numero_str = str(numero)

    if re.match(padrao, numero_str):
        return f"{numero} é um número inteiro ou decimal VÁLIDO."
    else:
        return f"{numero} é um número inteiro ou decimal INVÁLIDO."

numeros_teste = [
    2.3, #Formato válido.
    "1", #Formato válido.
    0, #Formato válido.
    1000.0, #Formato válido.
    101.26948, #Formato válido.
    -102.34523, #Formato válido.
    "-6", #Formato válido.
    "9,8", #Formato inválido: caractere "," não é correto para definir números decimais.
    "1.", #Formato inválido: caractere "." precisa ser acompanhado de uma casa decimal.
    "2-09", #Formato inválido: caractere "-" não esperado entre os números.
    "Amanda" #Formato inválido: "Amanda" não é um número.
]

for numero in numeros_teste:
    print(validar_numero_inteiro_ou_decimal(numero))

print("-" * 40)

# Questão 6
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

# Questão 7
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

# Questão 2
def validar_cpf(numero_cpf: str) -> str:
    # Expressão regular para validar o formato do CPF
    validacao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

    # Verifica se o CPF corresponde ao padrão especificado
    if re.match(validacao, numero_cpf):
        return f"CPF {numero_cpf} válido."
    else:
        return f"CPF {numero_cpf} inválido."

# Lista de CPFs de teste    
cpf_teste = [
    #CPFs Válidos
    "123.456.789-09",
    "987.654.321-00",
    "456.789.123-45",
    #CPFs Inválidos
    "12a.456.789-09",  #contém uma letra "a
    "123.456.789-0b",  #contém uma letra "b"
    "123.456.78-909",  #formato incorreto: o traço está na posição errada
    "123.456789-09",   #falta o ponto após o sexto dígito
    "123.456.789-091" #contém um dígito extra
]

# Loop para validar cada CPF da lista
for cpf in cpf_teste:
    print(validar_cpf(cpf))

print("-" * 40)


#Questão 11
# Regex para validar o RG brasileiro no formato xx.xxx.xxx-x
rg_pattern = r"^\d{2}\.\d{3}\.\d{3}-\d{1}$"
# Função para validar o RG
def validar_rg(rg):
    return bool(re.match(rg_pattern, rg))
# Array de objetos com RGs para validação
rgs = [
    {"rg": "12.345.678-9", "valido_esperado": True},  # Válido
    {"rg": "12345.678-9", "valido_esperado": False},  # Inválido
    {"rg": "98.765.432-1", "valido_esperado": True},  # Válido
    {"rg": "12.34.5678-9", "valido_esperado": False}, # Inválido
    {"rg": "00.111.222-3", "valido_esperado": True},  # Válido
]
# Validação dos RGs
for rg_obj in rgs:
    rg = rg_obj["rg"]
    valido_esperado = rg_obj["valido_esperado"]
    resultado_validacao = validar_rg(rg)
    print(f"RG: {rg} | Válido esperado: {valido_esperado} | Validação: {resultado_validacao}")


# Resultado esperado
# RG: 12.345.678-9 | Válido esperado: True | Validação: True
# RG: 12345.678-9 | Válido esperado: False | Validação: False
# RG: 98.765.432-1 | Válido esperado: True | Validação: True
# RG: 12.34.5678-9 | Válido esperado: False | Validação: False
# RG: 00.111.222-3 | Válido esperado: True | Validação: True

print("-" * 40)

#Questão 19
def validar_numero_serie(numero_serie: str) -> bool:
    # Regex para validar número de série
    pattern = r'^[A-Za-z0-9]{4}(-?[A-Za-z0-9]{4}){3}$'
    
    # Verifica se o número de série corresponde ao padrão
    if re.match(pattern, numero_serie):
        return True
    return False

# Testando exemplos
test_strings = [
    "123A-B123-BB12-12AZ",  # Válido com hífens
    "123AB123BB1212AZ",     # Válido sem hífens
    "123A-B123-BB12-12A",   # Inválido (menos de 4 caracteres no último bloco)
    "123A-B123-BB12-12AZZ"  # Inválido (mais de 4 caracteres no último bloco)
]

# Validando as strings de teste
for s in test_strings:
    if validar_numero_serie(s):
        print(f"{s} é válido.")
    else:
        print(f"{s} é inválido.")

print("-" * 40)

#Questão 10 
def validar_codigo_postal(codigo_postal):
    # Expressão regular para validar código postal no formato xxxxx ou xxxxx-xxxx
    padrao = r'^\d{4,5}(-\d{3,4})?$'
    
    # Verifica se o código postal corresponde ao padrão
    if re.match(padrao, codigo_postal):
        return True
    else:
        return False

# Testando a função
codigos_test = ['1234', '98765', '54321-1234', '54321-123', '87654321', '56789-', '56789-12345']
for codigo in codigos_test:
    if validar_codigo_postal(codigo):
        print(f"{codigo} é um código postal válido.")
    else:
        print(f"{codigo} é um código postal inválido.")
