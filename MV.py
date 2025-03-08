def check(obj):
    if(type(obj)==type(1)):
        return False
    else:
        return True
    
def set_variables(p1,p2):
    global P1,P2;
    P1,P2=p1,p2
    
class movement():
    
    def _init_(self):
        pass

    def isenemy(self,TURN,obj):
        player = TURN%2
        if player==1:
            for x in range(8):
                if P1[x]==obj:
                    return True
        else:
            for x in range(8):
                if P2[x]==obj:
                    return True
        return False

    def enemy(self,TURN,obj):
        player = TURN%2
        if player==1:
            for x in range(8):
                if P1[x]==obj:
                    return P1[x]
        else:
            for x in range(8):
                if P2[x]==obj:
                    return P2[x]
        return 0
        
    def search_tile(self,Tstate,next_pos):
        for x in range(8):
            if(check(P1[x])):
                if(P1[x].axis == next_pos):
                    return x
            if(check(P2[x])):
                if(P2[x].axis == next_pos):
                    return x
        return Tstate
                
    def move_map(self,k,z,obj):
        lst=[]
        if(check(obj)):
            n = obj.stat[2]
            x=k
            x=x-n-1
            for i in range(n+1,(2+2*n)):
                y=z
                for j in range(i):
                    if(k%2!=0):
                        lst+=[[x,y-(i//2)]]
                    else:
                        if(i%2==0):
                            lst+=[[x,y-(i//2)]]
                        else:
                            lst+=[[x,y-(i//2)-1]]
                    y+=1
                x += 1
            for i in range(2*n,n,-1):
                y=z
                for j in range(i):
                    if(k%2!=0):
                        lst+=[[x,y-(i//2)]]
                    else:
                        if(i%2==0):
                            lst+=[[x,y-(i//2)]]
                        else:
                            lst+=[[x,y-(i//2)-1]]
                    y+=1
                    
                x+=1
        return lst

    def is_in_mv_map(self,mv_map,mv_cord,obj):
        i = mv_cord[0]
        j = mv_cord[1]
        if (len(mv_map)>0) and (check(obj)):
            for x in mv_map:
                if([-40,-40]==obj.axis):
                    return True
                if x == [i,j]:
                    return True
            return False
        else:
            return True
