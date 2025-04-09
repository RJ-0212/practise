正確密碼=1234
for 次數 in range(5):
    密碼 = int(input('請輸入密碼:'))
    if 密碼==正確密碼:
        print('密碼正確')
        break
    elif 密碼!=正確密碼 and 4-次數>0:
        print('密碼錯誤')
        print(f'剩餘機會:{4-次數}')
    else:
        print('帳號已鎖定')

