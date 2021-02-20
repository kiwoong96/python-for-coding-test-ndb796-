[Tip]  
조합을 통해 구하는 방식  
따로 리스트를 만들어서 조합을 만들기 보단 치킨집들만 모은 리스트 자체를 조합을 넣는데
from itertools import combinations

combination = list(combinations(chicken_list(표본),개수))
