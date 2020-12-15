N = int(input())
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += N//coin #소숫점 이하를 버리는 나눗셈 //
  #print('coin : {}, count : {}'.format(coin,count))
  N %= coin
  #print('N : {}'.format(N))

print(count)
