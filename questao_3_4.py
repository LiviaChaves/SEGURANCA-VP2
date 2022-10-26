
import rsa

#Recebendo a chave privada
def key_priv():
        key_privada = input("Insira o caminho da chave PRIVADA: ") #Key/priv.pem
        return key_privada


#Recebendo a chave publica
def key_pub():
        key_publica = input("Insira o caminho da chave PUBLICA: ") #Key/public.pem
        return key_publica
 

#Recebendo o arquivo original 
def arquivoorig():
        arquivo_original = input("Insira o caminho do AQUIVO ORIGINAL: ") #arquivo/arquivo_orig.txt
        return arquivo_original
  

#Carregando a chave privada
with open(key_priv(), mode='rb') as privatefile:  
    keypriv = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keypriv) 

#Carregando a chave publica
with open(key_pub(), mode='rb') as publicfile: #'Key/public.pem'
    keypublic = publicfile.read()
publickey = rsa.PublicKey.load_pkcs1(keypublic)


#Recebendo o Arquivo Original 
with open(arquivoorig(), 'rb') as msgfile:  #Assinatura do arquivo_orig 
    signature = rsa.sign(msgfile, privkey, 'SHA-1')

#print(signature)  #Asinatura 

def arquivoass():
        arquivo_ass = input("Insira o caminho onde você quer salvar o arquivo assinatura e o nome do documento exemplo: caminho/nomearquivo_assinatura: ") #arquivo/arquivo_assinatura.txt
        return arquivo_ass
  

file_out = open(arquivoass(), "wb") # salvando arquivo assinatura  
file_out.write(signature)
file_out.close()


try:
    with open(arquivoorig(), 'rb') as msgfile: #verificando assinatura
        rsa.verify(msgfile, signature, publickey)
    print ("Assinatura é Valida.")
except (ValueError, TypeError,FileNotFoundError):
    print ("Assinatura NÃO Valida.")



