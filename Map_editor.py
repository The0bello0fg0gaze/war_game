import random
def makemap():
    Map = open("maps\\G_MAP.txt","w")
    x=""
    WIDTH = 1000
    HEIGHT = 1000
    Z = 25
    A = Z*(0.750111069)
    B = Z*(0.661311865)
    X_GAP = int(2*(Z+B))
    Y_GAP = int(2*A)
    percent = [2,50]

    for i in range(0,(HEIGHT//X_GAP)+1):
        for j in range(0,(WIDTH//Y_GAP)):
            if (i == 0)or(i ==(HEIGHT//X_GAP)):
                x += str(9)+" "
            else:
                if random.randint(0,100)<percent[0]:
                    x += str(2)+ " "
                elif random.randint(0,100)<percent[0]:
                    x += str(3)+ " "
                elif random.randint(0,100)<percent[0]:
                    x += str(4)+ " "
                else:
                    x += str(random.randint(0,1))+" "
        x += "e\n"
        for k in range(0,(WIDTH//Y_GAP)):
            if (i == (HEIGHT//X_GAP))or(i == 0):
                x += str(9)+" "
            else:
                if random.randint(0,100)<percent[0]:
                    x += str(2)+ " "   
                elif random.randint(0,100)<percent[0]:
                    x += str(3)+ " "
                elif random.randint(0,100)<percent[1]:
                    x += str(4)+ " "
                else:
                    x += str(random.randint(0,1))+" "
        x += "e\n"
    Map.write(x)
    Map.close()
