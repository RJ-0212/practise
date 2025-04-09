def 加(x,y):
    return x+y
def 減(x,y):
    return x-y
def 乘(x,y):
    return x*y
def 除(x,y):
    return x//y,x%y
while True:
    操作=input("(1)加(2)減(3)乘(4)除")
    if 操作 in ['1','2','3','4']:
        num1=int(input("請輸入第一個數："))
        num2=int(input("請輸入第二個數："))
        if 操作=="1":
            print(f"{num1}+{num2}={加(num1,num2)}")
        if 操作=="2":
            print(f"{num1}-{num2}={減(num1,num2)}")
        if 操作=="3":
            print(f"{num1}x{num2}={乘(num1,num2)}")
        if 操作=="4":
            if num1%num2==0:
                print(f"{num1}÷{num2}={除(num1,num2)[0]}")
            else:
                print(f"{num1}÷{num2}={除(num1,num2)[0]}...{除(num1,num2)[1]}")

    else:
        print('關機了掰掰:D')
        break



