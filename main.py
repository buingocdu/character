import threading
import module

print("Khởi tạo game")
print("Nhập tên nhân vật 1")
character1_name = input(">>>")

print("Nhập tên nhân vật 2")
character2_name = input(">>>")

listSkill1=[module.Skill("Tấn công 1",100,0,20,"Q"),module.Skill("Tấn công 2",200,200,50,"W"),module.Skill("Chiêu cuối",500,0,100,"E")]
listSkill2=[module.Skill("Tấn công 1",100,0,20,"Q"),module.Skill("Tấn công 2",200,200,50,"W"),module.Skill("Chiêu cuối",500,0,100,"E")]
character1 = module.Character(character1_name,1000,200,100,50,listSkill1)
character2 = module.Character(character2_name,1000,200,100,50,listSkill2)
turn =1
def call_each_5s():
  threading.Timer(5.0, call_each_5s).start()
  character1.heal_every_5_second()
  character1.mana_every_5_second()
  character2.heal_every_5_second()
  character2.mana_every_5_second()
call_each_5s()
while character1.status!=0 and character2.status!=0:
    threading.Timer(1.0, call_each_5s).start()
    if turn==1:
        print(character1.name," Tấn công ",character2.name)
        character2=character1.used_skill(character2)
        turn=2
        print(character1.name, character1.blood)
        print(character2.name, character2.blood)
    else:
        print(character2.name," Tấn công ",character1.name)
        character1 =character2.used_skill(character1)
        turn=1
        print(character1.name, character1.blood)
        print(character2.name, character2.blood)

if(character1.status==0):
    print(character2.name," chiến thắng!")
if(character2.status==0):
    print(character1.name," chiến thắng!")