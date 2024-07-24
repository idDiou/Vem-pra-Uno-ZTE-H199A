import re
import pyperclip

# Função para remover caracteres especiais e espaços em branco
def remover_caracteres(texto):
    # Expressão regular para substituir qualquer caractere que não seja uma letra ou número por uma string vazia
    return re.sub(r'[^a-zA-Z0-9]', '', texto)

# Solicita ao usuário para inserir um texto
entrada = texto_copiado = pyperclip.paste()

# Remove caracteres especiais e espaços
resultado = remover_caracteres(entrada)

print("Texto sem caracteres especiais e espaços:", resultado)


