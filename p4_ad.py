n = list(range(2, 101))

primes = []

for p in n:
  is_prime = True
  for i in range(2,int(p**0.5))+1): #một số nguyên dương n nếu có ước lớn hơn 1 thì chắc chắn tồn tại một ước của n mà nhỏ hơn n^1/2.
    if n % i == 0:
      is_prime = False
      break
    if is_prime: 
      primes.append(p)
print(primes)

