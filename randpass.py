import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
ans = upper_case + lower_case + num + symbol

length = 20
password = "".join(random.sample(ans,length))
print(password)
