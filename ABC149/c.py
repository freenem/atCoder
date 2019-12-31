x = int(input())

def prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

while True:
  if prime(x):
    print(x)
    break
  x += 1
