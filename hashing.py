import hashlib
pwd = input("enter the password:")
p= hashlib.new('md4').hexdigest()
print (p)
