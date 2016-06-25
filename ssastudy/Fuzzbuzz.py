for i in range (1,1001):
    if i%15 == 0:
        print('fuzzbuzz')
    elif i%3 == 0:
        print('fuzz')
    elif i%5 == 0:
        print('buzz')
    else:
        print(i)
input()
