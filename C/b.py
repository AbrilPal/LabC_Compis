import re

# abrir archivo y leer todo el contenido
with open('archivo.yal', 'r') as file:
    contenido = file.read()

# eliminar los comentarios del contenido utilizando una expresión regular
contenido_sin_comentarios = re.sub(r'\(\*.*?\*\)', '', contenido, flags=re.DOTALL)

# reescribir el archivo con el contenido sin comentarios
with open('archivo.yal', 'w') as file:
    file.write(contenido_sin_comentarios)
# Paso 1: Leer el archivo YaLex y eliminar comentarios
with open('archivo.yal', 'r') as f:
    contenido = f.read()

contenido_limpio = re.sub(r'/\*.*?\*/', '', contenido, flags=re.DOTALL)

# Paso 2: Procesar el contenido del archivo
patron_tokens = re.compile(r'\|?\s*(\S+)\s*{.*return\s+(\S+).*}', re.IGNORECASE)
matches_tokens = patron_tokens.findall(contenido_limpio)

tokens_extraidos = {}
for match in matches_tokens:
    tokens_extraidos[match[0]] = match[1]

patron_reglas = re.compile(r'rule\s+(\S+)\s*=\s*([\s\S]*?)\s*(?:\n\s*){2}|(/\*.*?\*/)', re.IGNORECASE|re.DOTALL)
matches_reglas = patron_reglas.findall(contenido_limpio)

reglas_extraidas = {}
for match in matches_reglas:
    if match[0]:
        regla = match[0]
        expresion = match[1].strip()
        expresion = re.sub(r'\s+', ' ', expresion)
        reglas_extraidas[regla] = expresion

# Generar expresión regular a partir de los tokens
expresion_regular = '|'.join(re.escape(token.strip('"') and token.strip("'")) for token in tokens_extraidos.keys())

# Paso 3: Escribir los tokens y las reglas extraídos
with open('ui.txt', 'w') as f:
    f.write("Tokens:\n")
    for token, valor in tokens_extraidos.items():
        f.write(f"{token}: {valor}\n")
    f.write("\nReglas:\n")
    for regla, expresion in reglas_extraidas.items():
        f.write(f"{regla}: {expresion}\n")
    f.write("\nExpresion:\n")
    f.write(expresion_regular)
