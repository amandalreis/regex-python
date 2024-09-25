import re
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
