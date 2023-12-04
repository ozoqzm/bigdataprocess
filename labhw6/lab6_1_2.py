human = input("가위, 바위, 보 입력: ")

rps_dic = {1:'가위', 2:'바위', 3:'보'}
match_table = {'가위':'보', '바위':'가위', '보':'바위'}

import random
com = random.randint(1, 3)
print(f"컴퓨터: {rps_dic[com]}")

for i in zip(rps_dic, match_table):
    if human == rps_dic[com]:
        print("비겼습니다!")
        break
    elif match_table[human] == rps_dic[com]:
        print("사람 승!")
        break
else:
    print("컴퓨터 승!")
