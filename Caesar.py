def generate_key(n):
  character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  key = {}
  for i in range(len(character_set)):
    key[character_set[i]] = character_set[(i+n) % len(character_set)]
  return key

def generate_decryption_key(key):
  dkey = {}
  for c in key:
    dkey[key[c]] = c
  return dkey

def crypt(message, key):
  encrypted_msg = ""
  for c in message:
    if c in key:
      encrypted_msg += key[c]
    else:
      encrypted_msg += c
  return encrypted_msg

def caesar():
  encryption_key = generate_key(3)
  print(encryption_key)
  message = "YOU ARE AWESOME"
  encrypted_message = crypt(message, encryption_key)
  print(encrypted_message)

  decryption_key = generate_decryption_key(encryption_key)
  decrypted_message = crypt(encrypted_message, decryption_key)
  print(decrypted_message)


def crack_caesar():
  encrypted_message = "BRX DUH DZHVRPH"
  for i in range(26):
    dkey = generate_key(i)
    print(crypt(encrypted_message, dkey))


caesar()
#crack_caesar()