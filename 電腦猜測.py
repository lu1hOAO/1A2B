#
# Guess Number Game (Master Mind or 1A2B Game)
#
def digit4(n):
    n1 = int(n/1000)
    n2 = int((n - n1*1000)/100)
    n3 = int((n - n1*1000 - n2*100)/10)
    n4 = n - n1*1000 - n2*100 - n3*10
    return (n1, n2, n3, n4)


def isvalid(n):
    d = digit4(n)
    if d[0]==0 or d[1]==0 or d[2]==0 or d[3]==0 or n<1234 or n>9876: return False
    if d[0]==d[1] or d[0]==d[2] or d[0]==d[3] or d[1]==d[2] or d[1]==d[3] or d[2]==d[3]: return False
    return True


def checkab(m, n):
    a, b = 0, 0
    c, d = digit4(m), digit4(n)
    if c[0]==d[0]: a = a + 1
    if c[1]==d[1]: a = a + 1
    if c[2]==d[2]: a = a + 1
    if c[3]==d[3]: a = a + 1
    if c[0]==d[1] or c[0]==d[2] or c[0]==d[3]: b = b + 1
    if c[1]==d[0] or c[1]==d[2] or c[1]==d[3]: b = b + 1
    if c[2]==d[0] or c[2]==d[1] or c[2]==d[3]: b = b + 1
    if c[3]==d[0] or c[3]==d[1] or c[3]==d[2]: b = b + 1
    return (a, b)


def rand(a, b):
    rb = uos.urandom(2)
    c = rb[1]*256+rb[0]
    c %= (b-a+1)
    return a+c


def numfilter(n, a, b):
    for i in range(len(numlist)-1, -1, -1):
         x = checkab(n, numlist[i])
         if x[0]!=a or x[1]!=b: del numlist[i]


numlist = []
for i in range(1234, 9877):
    if isvalid(i): numlist.append(i)


while True:
    guessnum = numlist[rand(0,len(numlist)-1)]
    print("I guess the number in your mind is: %d" % guessnum)
    xa = input('a?(0..4) = ')
    xb = input('b?(0..4) = ')
    numfilter(guessnum, int(xa), int(xb))
    if len(numlist)==1:
        print("Thanks! The answer is %d!" % numlist[0])
        break
    elif len(numlist)==0:
        print("Oops, something is wrong!")
        break

