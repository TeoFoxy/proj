import rsa
mess = 'Hello, Codeby!'
(pubkey, privkey) = rsa.newkeys(512) # Генерируем 2 ключа
cipher = rsa.encrypt(mess, pubkey) # Шифруем
print(cipher)
mess = rsa.decrypt(crypto, privkey) # Расшифровываем
print(mess)