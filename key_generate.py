import rsa 

(key_public, key_priv) = rsa.newkeys(2048)

key_public = key_public._save_pkcs1_pem()
file_out = open("Key/public.pem", "wb")
file_out.write(key_public)
file_out.close()

key_priv = key_priv._save_pkcs1_pem()
file_out = open("Key/priv.pem", "wb")
file_out.write(key_priv)
file_out.close()