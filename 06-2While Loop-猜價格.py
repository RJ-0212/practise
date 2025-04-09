商品價格=1000
玩家A=input(print('請輸入玩家1名稱:'))
玩家B=input(print('請輸入玩家2名稱:'))
回答次數=0
while 回答次數<3:
    A = int(input(f"請{玩家A}輸入商品價格:"))
    B = int(input(f"請{玩家B}輸入商品價格:"))
    if A==商品價格 or B==商品價格:
        break
    else:
        A差=abs(商品價格-A)
        B差=abs(商品價格-B)
        if A差>B差:
            print(f"{玩家B}的答案較接近價格")
        else:
            print(f"{玩家A}的答案較接近價格")
    回答次數 += 1

if B == 商品價格:
    print(f"回答正確,{玩家B}獲勝!")
elif A == 商品價格:
    print(f"回答正確,{玩家A}獲勝!")
elif A==商品價格 and B==商品價格:
    print('都答對了!')
elif A差<B差:
     print(f"遊戲結束,{玩家A}的答案較接近價格,{玩家A}獲勝!")
elif A差>B差:
    print(f"遊戲結束,{玩家B}的答案較接近價格,{玩家B}獲勝!")


