# 1A2B-
這是用python寫得非常小小小遊戲，主要是想回味童年啦，不過這次的1A2B不限定4個數字
如果是新手可以選擇少一點數字，想挑戰進階的可以選超過4個數字(最多10個)

![剛剛睡著了](https://user-images.githubusercontent.com/91367098/151692056-138b6f74-42de-4c3a-a31c-a90adfdbfd90.png)
***********************************************************
那我們就開始囉！
一開始會有簡單的遊戲說明，加上一隻大恐龍歡迎使用者進到這個小遊戲，我小時候喜歡恐龍，所以選恐龍當作童年守護神

![螢幕擷取畫面 (226)](https://user-images.githubusercontent.com/91367098/151692334-82d71785-b752-40a0-ab40-3642ab0620ad.png)
***********************************************************
接下來進入猜的環節，一開始先選幾個數字，接著是使用者的猜測(注意數字不能重複喔)![螢幕擷取畫面 (227)](https://user-images.githubusercontent.com/91367098/151692599-f0ccd850-bcd1-4941-ace7-8b54a8b83613.png)
***********************************************************
猜對之後又會有小恐龍出來問你要不要繼續，輸入y就可以繼續囉！
![螢幕擷取畫面 (228)](https://user-images.githubusercontent.com/91367098/151692647-8450cf4e-8357-4157-9f19-915806278be9.png)
***********************************************************
除了做玩家猜電腦版，也稍微分析了一下電腦猜玩家版><(詳細程式碼可以看電腦猜.py那個檔案)目前網路上找到的資料都是說電腦最多猜6次可以猜中(最好的演算法是5.21次)
那電腦猜玩家大概是甚麼流程呢？用下圖來看看！
![圖片2](https://user-images.githubusercontent.com/91367098/151729166-a387e9fe-b3a9-4a4b-afb9-d74e0af8739c.png)
```
#這邊是把電腦猜測的四位數的四位數拆成4個位數
def digit4(n):\<br>
    n1 = int(n/1000)
    n2 = int((n - n1*1000)/100)
    n3 = int((n - n1*1000 - n2*100)/10)
    n4 = n - n1*1000 - n2*100 - n3*10
    return (n1, n2, n3, n4)
```
```
#這邊是剔除重複數字，因為我們一開始的答案庫沒有排除所有重複
def isvalid(n):
    d = digit4(n)
    if d[0]==0 or d[1]==0 or d[2]==0 or d[3]==0 or n<1234 or n>9876: return False
    if d[0]==d[1] or d[0]==d[2] or d[0]==d[3] or d[1]==d[2] or d[1]==d[3] or d[2]==d[3]: return False
    return True
 ```
 ```
 #下面三個函數就是開始找下一組答案囉
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

#這是答案庫生成
numlist = []
for i in range(1234, 9877):
    if isvalid(i): numlist.append(i)
```
