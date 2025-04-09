import random
import string
數字=string.digits
字母=string.ascii_letters
素材庫=list(數字+字母)
random.shuffle(素材庫)
位數=int(input(print("想要幾位密碼呢?")))
密碼=素材庫[:位數]
print(f"您的密碼是:{"".join(密碼)}")

