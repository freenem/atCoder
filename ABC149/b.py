a, b, k = map(int, input().split())

if k - a > 0:
  k -= a
  a = 0
  if k - b > 0:
    b = 0
    print(str(a) + " " + str(b))
  else:
    b -= k
    print(str(a) + " " + str(b))
else:
  a -= k
  print(str(a) + " " + str(b))
