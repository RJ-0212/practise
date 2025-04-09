學生=['Amy',90,'Brian',85,'Cindy',80]
操作=input("請輸入操作指令：(A)查詢(B)新增(C)刪除(D)修改").upper()
if 操作=='A':
    姓名=input("請輸入要查詢的姓名:")
    if 姓名 not in 學生:
        print("查無此人")
    else:
        編號=學生.index(姓名)
        print(f"{姓名}的成績為{學生[編號+1]}分")
elif 操作=='B':
    新增資料=input("請輸入要新增的姓名:")
    新增成績=input("請輸入成績:")
    學生.extend([新增資料,新增成績])
    print(f"已登錄成績資料{int(len(學生)/2)}筆")
    print(學生)
elif 操作=='C':
    刪除資料=input("要刪除的學生姓名:")
    list(刪除資料)
    if 刪除資料 not in 學生:
        print('查無此人')
    else:
        刪除編號=學生.index(刪除資料)
        #學生.pop(刪除編號,刪除編號+1)
        學生.remove(刪除資料)
        學生.pop(刪除編號)
        print(f"已登錄成績資料{int(len(學生) / 2)}筆")
        print(學生)
elif 操作=="D":
    修改姓名=input('請輸入要修改的學生姓名:')
    if 修改姓名 not in 學生:
        print('查無此人')
    else:
        編號=int(學生.index(修改姓名))+1
        修改成績=input('請輸入新成績:')
        學生[編號]=修改成績
        print(學生[編號])
        print(學生)