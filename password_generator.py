import hashlib

def generate_password(site_url, username, algorithm):
  # URL ve kullanıcı adını birleştirin
  data = site_url + username

  # Seçilen algoritma ile veriyi şifreleyin
  if algorithm == "sha1":
    hash_object = hashlib.sha1(data.encode())
  elif algorithm == "sha224":
    hash_object = hashlib.sha224(data.encode())
  elif algorithm == "sha256":
    hash_object = hashlib.sha256(data.encode())
  elif algorithm == "sha384":
    hash_object = hashlib.sha384(data.encode())
  elif algorithm == "sha512":
    hash_object = hashlib.sha512(data.encode())
  elif algorithm == "md5":
    hash_object = hashlib.md5(data.encode())
  else:
    raise ValueError("Geçersiz algoritma seçildi")

  # Şifrelenmiş veriyi hexadecimal biçiminde döndürün
  password = hash_object.hexdigest()

  return password

# Kullanıcıdan site URL'sini, kullanıcı adını ve şifreleme algoritmasını alın
site_url = input("Site URL'sini girin: ")
username = input("Kullanıcı adınızı girin: ")
algorithm = input("Şifreleme algoritmasını seçin (sha1 / sha224 / sha256 / sha384 / sha512 veya md5): ")

# Parolayı oluşturun ve kullanıcıya gösterin
password = generate_password(site_url, username, algorithm)
print("Parolanız:", password)
