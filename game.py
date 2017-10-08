import random

print('这是我也不知道的python')

time = 3
secret = random.randint(1,10)
guess = 0

print("不妨查一查这是一个什么数字：", end=" ")

while (guess != secret) and (time > 0):
    temp = input()
	guess = int(temp)
	times = times - 1 #用户每输入一次，可用机会减少一次、
	if guess == secret：
	print("牛逼!")
	print("不错")
	else:
	if guess > secret：
	print("哥 ，大了")
	else：
	print("哥 ，小了")
	if times > 0:
		print("再试一次:", end=" ")
		else:
		print("you haven't chances")
		
print("game over ,thanks")