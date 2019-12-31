n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

tmp = ''
score = 0
char_list = list(t)
v_list = []

def judge(hand):
  global score
  if hand == 'r':
    if tmp == 'p':
      v_list.append('r')
    else:
      v_list.append('p')
      score += p
  elif hand == 's':
    if tmp == 'r':
      v_list.append('s')
    else:
      v_list.append('r')
      score += r
  else:
    if tmp == 's':
      v_list.append('p')
    else:
      v_list.append('s')
      score += s

for i in range(n): 
  if i >= k:
    tmp = v_list[i-k]

  judge(char_list[i])

print(score)
