class Unit():
    def __init__(self,unit_no,self_obj,stat,weapon,axis,placed):
        self.stat = stat
        self.weapon = weapon
        self.axis = axis
        self.self_obj = self_obj
        self.unit_no = unit_no
        self.placed = placed

    def self_obj(self):
        x = self.self_obj
        return x
    
    def unit_no(self):
        x = unit_no
        return x
    
    def axis(self):
        x = self.axis
        return x
    
    def stat(self):
        x =self.stste
        return x
    
    def wepon(self):
        x = self.weapon
        return x

    def placed(slef):
        x = self.placed
        return x
#----------------------------------------------------------------------
    def setself_obj(self,Obj):
        self.self_obj = Obj

    def setunit_no(self,NO):
        self.unit_no = NO
    
    def setaxis(self,Axis):
        self.axis = Axis
    
    def setstat(self,Stat):
        self.stat = Stat
    
    def setwepon(self,Weapon):
        self.weapon = Weapon

    def setplaced(self,Placed):
        self.placed = Placed


    def damage(self,damage):
        self.stat[0] -= damage
        return self.stat[0]

    def heal(self,heal):
        self.stat[0] += heal
        return self.stat[0]


