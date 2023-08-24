adade_1 = int(input("adade aval ra vared konid: "))
adade_2 = int(input("adade dovom ra vared konid: "))
adade_3 = int(input("adade sevom ra vared konid: "))
if adade_1 >= adade_2 >= adade_3:
    print("biggest number is: ",adade_1)
elif adade_1 >= adade_3 >= adade_2: 
    print("biggest number is: ",adade_1)
elif adade_2 >= adade_1 >= adade_3:
    print("biggest number is: ",adade_2)
elif adade_2 >= adade_3 >= adade_1:
    print("biggest number is: ",adade_2)
elif adade_3 >= adade_1 >= adade_2:
    print("biggest number is: ",adade_3)
elif adade_3 >= adade_2 >= adade_1:
    print("biggest number is: ",adade_3)