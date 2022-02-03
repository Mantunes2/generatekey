# Importar a biblioteca
from cryptography.fernet import Fernet

# Gerar a chave
key = Fernet.generate_key()

# nome do arquivo
name = input('nome do arquivo: ')
# Abrindo e salvando a chave no arquivo
with open(name, 'wb') as filekey:
  filekey.write(key)
  filekey.close()
print('Chave salva com sucesso!')
