

import rsa 

#Maria
#Joana 

(KEY_Publica,JOANA_Privada) = rsa.newkeys(384) # Gerando o Par de Chaves , uma chave publica e privada aleatoria


texto = "Olá tudo bem?".encode('utf8') 

texto_encrypt = rsa.encrypt(texto,KEY_Publica)  #Maria Encripitada Sua Mensagem a chave publica


print('Mensagem encrypt Maria:') # Mensagem Encripitada Por Maria 
print(texto_encrypt)

texto_descrpy = rsa.decrypt(texto_encrypt,JOANA_Privada) # Joana Recebe a mensagem encripitada por Maria e Descripita utilizando a chave privada 

print('Mensagem decrypt Joana:') # Mensagem Descripitada por Joana 
print(texto_descrpy.decode('utf8'))


