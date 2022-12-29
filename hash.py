import hashlib

email = 'sanjoy@gmail.com'
password = '923sdoiwe293892s'
pass_encode = password.encode()
pass_hash = hashlib.md5(pass_encode).hexdigest()

your_email = 'sanjoy@gmail.com'
your_pass = 'b507b5fbb6314d7d0b3340820069e104'
hashed_your_pass = hashlib.md5(your_pass.encode()).hexdigest()

if email == your_email and pass_hash == hashed_your_pass:
  print('right user!')
else :
  print('wrong password!')

print(pass_hash)
print(hashed_your_pass)