def myFun(arg1,*args,**kwargs):
    print(arg1)
    for arg in args:
        print (arg)
    for key,value in kwargs.items():
        print(key,value)


# myFun(1,2,3,a1='4',a2='5')