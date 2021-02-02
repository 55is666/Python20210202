#2-2
import random
h=random.randint(1,20)
l=1
k=int(input('num?'))
while True:
    
    if l>=5:
        print('loser')
        break
    elif h==k:
        print('666')
        print('猜了'+ str(l+1) +'次')
        break
    elif k<h:
        print('too small')
        l=l+1
    elif k>h:
        print('too big')
    k=int(input('num?'))