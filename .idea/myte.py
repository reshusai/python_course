def bas(num,b):
    a = 0
    num = ",".join(num)
    print(num)
    for i in range(0,len(num),2):
        print(a,int(num[i]))
        a += int(num[i])*b

    return a
def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]

if __name__ == "__main__":
    re = conv(35,36)
    print(re)