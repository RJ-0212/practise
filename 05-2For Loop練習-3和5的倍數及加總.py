sum=0
for num in range(51):
    if num%3==0 or num%5==0:
        print(num)
        sum+=num
print(sum)
