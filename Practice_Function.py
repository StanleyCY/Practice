def fc1(a,b):
    a = 10
    def fc2(a):
        return a+2
    def fc3(b):
        return b+3

    return fc2(a)+fc3(b)

print (fc1(2,5))