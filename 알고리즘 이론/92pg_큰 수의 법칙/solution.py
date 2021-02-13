N, M, K = map(int, input().split())
data = list(map(int,input().split()))

#data.sort(reverse = True) #sort는 본체 정렬
c = sorted(data, reverse=True) #sorted는 정렬한걸 리턴
print(c)

result = 0
tmp = 0
count = 0
while True:
  if tmp == K:
    tmp = 0
    result += c[1]
    #print('TMP=K {}'.format(result))
  else:
    tmp +=1
    result += c[0]
    #print('TMP=!K {}'.format(result))
  count +=1

  if count == M:
    break

print(result)