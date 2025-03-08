n = 2
x=4
y=4
def move_map(self,x,y,n=1):
    x=x-(n//2)
    lst=[]
    for i in range(n+1,(1+2*n)+1):
        for j in range(i):
            print((x-1,y-(n//2)+j-1),end='')
            lst+=[(x-1,y-(n//2)+j-1)]
        print()
        x+=1
    for i in range((1+2*n)-1,n,-1):
        for j in range(i):
            print((x-1,y-(n//2)+j-1),end='')
            lst+=[(x-1,y-(n//2)+j-1)]
        print()
        x+=1
    return lst

def check_over(main,given):
    if(main[0]<given[0]):
        given[0] = main[0] - given[0]
    elif(main[1]<given[1]):
        given[1] = main[1] - given[1]
    else:
        return given
    given = check_over(main,given)
    return given
main = [5,6]
given = [4,7]
print(check_over(main,given))
