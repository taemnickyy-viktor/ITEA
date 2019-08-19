from random import randint
class Peoples:
    def __init__(self, name, age, weight):
        self.name = name  #Full name of the person
        self.age = age  # older boxers lost more health
        self.weight = weight  # heavy boxers cause more damage


class Boxers(Peoples):
    def set_health(self, health):
        #set health of boxer
        self.health = health

    def get_health(self):
        return self.health

    def hit_move(self, hit):
        if hit == 1:
            return self.jab()
        elif hit == 2:
            return self.cross()
        elif hit == 3:
            return self.left_hook()
        elif hit == 4:
            return self.right_hook()
        return hit

    def defense_move(self, dfnd):
        if dfnd == 1:
            self.left_block()
        elif dfnd == 2:
            self.right_block()
        elif dfnd == 3:
            self.left_dodge()
        elif dfnd == 4:
            self.right_dodge()
        elif dfnd == 5:
            self.left_dive()
        elif dfnd == 6:
            self.right_dive()
        return dfnd

    #Attach functions
    def jab(self):
        #light damage left hand front hit (defence - right_dodge)
        print('jab')
        return randint(4, 8)
    def cross(self):
        #middle damage right hand front hit (defence - left_dodge)
        print('cross')
        return randint(8, 12)
    def left_hook(self):
        #powerful left hand side hit (defence - right_dive)
        print('left_hook')
        return randint(12, 16)
    def right_hook(self):
        #powerful right hand side hit (defence - left_dive)
        print('right_kook')
        return randint(16, 20)

    #Defend functions
    def left_block(self):
        #defence against cross and right_hit. Reduce damage from hit to 20%
        print('left_block')
    def right_block(self):
        # defence against jab and left_hit. Reduce damage from hit to 20%
        print('right_block')
    def left_dodge(self):
        #defence against cross.
        #TODO In case of cross it is counterattack possible - left_hook
        print('left_dodge')
    def right_dodge(self):
        #defence against jab.
        #TODO In case of jab it is counterattack possible - right_hook
        print('right_dodge')
    def left_dive(self):
        #defence against right_hook.
        #TODO Counterattack possible - right_hook
        print('left_dive')
    def right_dive(self):
        #defence against left_hook.
        #TODO Counterattack possible - left_hook
        print('right_dive')

class Fight():
    def __init__(self, boxer1, boxer2):
        # self.boxer1 = boxer1
        # self.boxer2 = boxer2
        print('-= Fight has begun =-!')

    def player_move(self, boxer1, boxer2):
        hit = int(input('1. Jab, 2. Cross, 3. Left hook, 4. Right hook: '))
        dfnc = boxer2.defense_move(randint(1, 4))
        dmg_whole = boxer1.hit_move(hit)
        print(dmg_whole, 'damage caused')
        if 1 <= hit <= 4 and 1 <= dfnc <= 2:
            dmg = round(dmg_whole * 0.8, 2)
            print('Damage caused:', dmg, '(blocked -20% from)', dmg_whole)
            boxer2.set_health(boxer2.get_health() - dmg)
            print(boxer2.get_health())
        elif hit == 1 and dfnc == 4:
            print('jab dodjed!')
        elif hit == 2 and dfnc == 3:
            print('cross dodjed')
        elif hit == 3 and dfnc == 6:
            print('left hook dived!')
        elif hit == 4 and dfnc == 5:
            print('right hook dived!')


def main():
    boxer1 = Boxers('Marco Orlando', 40, 75)
    boxer2 = Boxers('Enrico Polanci', 30, 90)
    boxer1.set_health(100)
    boxer2.set_health(100)
    main_fight = Fight(boxer1, boxer2)

    while boxer1.health > 0 or boxer2.health > 0:
        # cur_hit = boxer1.hit_move(int(input('1. Jab, 2. Cross, 3. Left hook, 4. Right hook: ')))
        # cur_def = boxer2.defense_move(randint(1, 4))
        # main_fight.player_move(cur_hit, cur_def, boxer1)
        # boxer1.defense_move(int(input('1. Left block, 2. Right block, 3. Left dodge, 4. Right dodge, 5. Left dive, 6. Right dive: ')))
        # boxer2.hit_move(randint(1, 4))
        # main_fight.player_move(cur_hit, cur_def)
        # main_fight.test()
        main_fight.player_move(boxer1, boxer2)



if __name__ == '__main__':
    main()