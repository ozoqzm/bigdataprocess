sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원래 리스트: {sample}")

hol = lambda x : x % 2 == 0
result1 = list(filter(hol, sample))
print(f"짝수 리스트: {result1}")

jjak = lambda x : x % 2 != 0
result2 = list(filter(jjak, sample))
print(f"홀수 리스트: {result2}")
    
