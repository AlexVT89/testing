import time
begin=time.time()

true_quest=0
x_1=input("вопрос первый")
if x_1 == "T":
    true_quest+=1
    print("its wrong")
else:
    print("isn wrong")

x_2=input("второй вопрос")
if x_2== "T":
    true_quest+=1
    print("its wrong")
else:
    print("isn wrong")
print(time.time()-begin)
print("over")
print(true_quest)