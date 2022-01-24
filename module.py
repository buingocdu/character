from dataclasses import dataclass
from unicodedata import name

@dataclass(order=True)
class Skill:
    """Bộ kỹ năng"""
    damage:int
    tank: int
    name: str
    keyword:str
    mana:int
    def __init__(self,name,damage,tank,mana,keyword) -> None:
        self.name= name
        self.damage = damage
        self.tank = tank
        self.mana = mana
        self.keyword = keyword
        pass

@dataclass(order=True)
class Character:
    """Nhân vật"""
    name: str
    blood:int
    maxblood:int
    mana:int
    maxmana:int
    damage:int
    tank: int
    skills: list
    status=1
    def __init__(self,name,blood,mana,damage,tank, skills:list ) -> None:
        self.name = name
        self.blood = blood
        self.maxblood = blood
        self.maxmana= mana
        self.mana=mana
        self.damage = damage
        self.tank = tank
        self.skills = skills
        pass    
    def used_skill(self,character):
        """Sử dụng bộ kỹ năng"""
        if self.status==0:
            print ("Nhân vật đã chết, k thể sử dụng kỹ năng")
            return character
        print("Sử dụng 1 trong các kỹ năng sau")
        for x in self.skills:
            print(x.name," nhấn [",x.keyword,"]")
        key =input(">>")
        for x in self.skills:
            if key.upper() ==x.keyword:                
                if self.mana >= x.mana:
                    character= self.attack(character,x)
                else:
                    print("Không đủ mana để thực hiện")
                return character
        return character
    def change_status(self):
        if self.blood<=0:
            self.status = 0 
            print("Nhân vật {self.name} đã chết")     
    def attack(self,character, skill: Skill):
        b = skill.damage-character.tank
        if b>0:
            character.blood-=b
        return character
    def heal_every_5_second(self):
        if self.status==1:
            self.blood+=10
            if(self.blood>self.maxblood):
                self.blood = self.maxblood
        
    def mana_every_5_second(self):
        if self.status==1:
            self.mana+=10
            if(self.mana>self.maxmana):
                self.mana = self.maxmana




