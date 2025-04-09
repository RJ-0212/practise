牛排=300
豬排=200
套餐=80
主餐=input("主餐:(A)牛排(B)豬排").upper()
升級=input("是否升級為套餐(Y)是(N)否").upper()
if 主餐=="A" and 升級=="Y":
    print(f"餐點費用為{牛排+套餐}元")
elif 主餐=="B"and 升級=="Y":
    print(f"餐點費用為{豬排+套餐}元")
elif 主餐=="A"and 升級=="N":
    print(f"餐點費用為{牛排}元")
else:
    print(f"餐點費用為{豬排}元")

