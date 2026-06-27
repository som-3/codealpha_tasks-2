import hashlib

username = input("Username: ")
password = input("Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Username:", username)
print("Hashed Password:", hashed_password)
