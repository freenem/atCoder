n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

score = 0
char_list = list(t)
v_list = []
janken = {0:r, 1:s, 2:p}
dp = [[0 for i in range(3)] for j in range(n)]

for i in range(n):
  if char_list[i] == 'r':
    v_list.append(2)
  elif char_list[i] == 's':
    v_list.append(0)
  else:
    v_list.append(1)

for i in range(k):
  dp[i][v_list[i]] = janken[v_list[i]]
  for j in range(i+k, n, k):
    for l in range(3):
      if v_list[j] == l:
        dp[j][l] = max(dp[j-k][(l+1)%3], dp[j-k][(l+2)%3]) + janken[l]
      else:
        dp[j][l] = max(dp[j-k][(l+1)%3], dp[j-k][(l+2)%3])

for i in range(1, k+1):
  score += max(dp[n-i][0], max(dp[n-i][1], dp[n-i][2]))

print(score)
