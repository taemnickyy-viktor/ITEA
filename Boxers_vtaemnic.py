from random import randint
from colorama import Fore, Style
class Peoples:
    def __init__(self, name):
        self.name = name  #Full name of the person
        #TODO
        # self.age = age  # older boxers lost more health
        # self.weight = weight  # heavy boxers cause more damage


class Boxers(Peoples):
    def set_health(self, health):
        #Set health of boxer
        self.health = health

    def get_health(self):
        #Function for health status check
        return self.health

    def hit_move(self, name, cur_hit):
        #Chose current attach move
        if cur_hit == 1:
            return self.jab(name)
        elif cur_hit == 2:
            return self.cross(name)
        elif cur_hit == 3:
            return self.left_hook(name)
        elif cur_hit == 4:
            return self.right_hook(name)

    def defense_move(self, name, dfnd):
        #Chose current defence move
        if dfnd == 1:
            self.block(name)
        elif dfnd == 2:
            self.left_dodge(name)
        elif dfnd == 3:
            self.right_dodge(name)
        elif dfnd == 4:
            self.left_dive(name)
        elif dfnd == 5:
            self.right_dive(name)
        return dfnd

    #Attach functions
    def jab(self, name):
        #light damage left hand front hit (defence - right_dodge)
        print(name, 'do Jab!')
        return randint(4, 8)
    def cross(self, name):
        #middle damage right hand front hit (defence - left_dodge)
        print(name, 'do Cross!')
        return randint(8, 12)
    def left_hook(self, name):
        #powerful left hand side hit (defence - right_dive)
        print(name, 'do Left hook!')
        return randint(12, 16)
    def right_hook(self, name):
        #powerful right hand side hit (defence - left_dive)
        print(name, 'do Right hook')
        return randint(14, 18)

    #Defend functions
    def block(self, name):
        #defence against cross and right_hit. Reduce damage from hit to 50%
        print(name, 'do Block!')
    def left_dodge(self, name):
        #defence against cross.
        #TODO In case of cross it is counterattack possible - left_hook
        print(name, 'do Left Dodge!')
    def right_dodge(self, name):
        #defence against jab.
        #TODO In case of jab it is counterattack possible - right_hook
        print(name, 'do Right Dodge!')
    def left_dive(self, name):
        #defence against right_hook.
        #TODO Counterattack possible - right_hook
        print(name, 'do Left Dive!')
    def right_dive(self, name):
        #defence against left_hook.
        #TODO Counterattack possible - left_hook
        print(name, 'do Right Dive!')

class Fight():
    def __init__(self):
        print(Fore.RED + '-= The Fight has Begun! =-' + Style.RESET_ALL)

    def player_move(self, boxer1, boxer2):
        #This is the function for Player move
        cur_pl_hit = int(input('%s%s%s attack move: 1. Jab, 2. Cross, 3. Left hook, 4. Right hook: ' % (Fore.GREEN, boxer1.name, Style.RESET_ALL)))
        cur_pl_dmg_whole = boxer1.hit_move(boxer1.name, cur_pl_hit)
        cur_pl_dfnc = boxer2.defense_move(boxer2.name, randint(1, 5))
        self.calculate_damage(cur_pl_hit, cur_pl_dmg_whole, cur_pl_dfnc, boxer1, boxer2)

    def opponent_move(self, boxer1, boxer2):
        #This is the function for computer move
        if boxer2.health <= 0:
            return 1 #opponent in knockout
        cur_op_dfnc = boxer1.defense_move(boxer1.name, int(input('%s%s%s defence move: 1. Block, 2. Left dodge, 3. Right dodge, 4. Left dive, 5. Right dive: ' % (Fore.GREEN, boxer1.name, Style.RESET_ALL))))
        cur_op_hit = (randint(1, 4))
        cur_op_dmg_whole = boxer2.hit_move(boxer2.name, cur_op_hit)
        self.calculate_damage(cur_op_hit, cur_op_dmg_whole, cur_op_dfnc, boxer2, boxer1)
        return 0 #oponent sill have health

    def calculate_damage(self, hit, dmg_whole, dfnc, boxer1, boxer2):
        #This function calculates damage according of defence move
        if dfnc == 1:
            dmg = round(dmg_whole * 0.5, 2)
            boxer2.set_health(round(boxer2.get_health() - dmg, 2))
            print("%s%s%s caused %s%s%s damage (blocked 50%s out of %s). %s health %s[%s]%s" % (Fore.GREEN, boxer1.name, Fore.RESET, Fore.RED, dmg, Style.RESET_ALL, '%', dmg_whole, boxer2.name, Fore.BLUE, boxer2.get_health(), Style.RESET_ALL))
        elif hit == 1 and dfnc == 3:
            print("%s%s%s has missed! %s has dodged from jab! %s health [%s]" % (Fore.GREEN, boxer1.name, Fore.RESET, boxer2.name, boxer2.name, boxer2.get_health()))
        elif hit == 2 and dfnc == 2:
            print("%s%s%s has missed! %s has dodged from cross! %s health [%s]" % (Fore.GREEN, boxer1.name, Fore.RESET, boxer2.name, boxer2.name, boxer2.get_health()))
        elif hit == 3 and dfnc == 5:
            print("%s%s%s has missed! %s has dived from left hook! %s health [%s]" % (Fore.GREEN, boxer1.name, Fore.RESET, boxer2.name, boxer2.name, boxer2.get_health()))
        elif hit == 4 and dfnc == 4:
            print("%s%s%s has missed! %s has dived from right hook! %s health [%s]" % (Fore.GREEN, boxer1.name, Fore.RESET, boxer2.name, boxer2.name, boxer2.get_health()))
        else:
            boxer2.set_health(boxer2.get_health() - dmg_whole)
            print("%s%s%s caused %s damage! %s health [%s]" % (Fore.GREEN, boxer1.name, Fore.RED, dmg_whole, boxer2.name, boxer2.get_health()))

    def check_results(self, boxer1, boxer2):
        if boxer1.health <= 0 and boxer2.health <= 0:
            print('What a fight! Looks like we have a draw! %s and %s knocked out! Unbelievable!' % (boxer1.name, boxer2.name))
        elif boxer1.health <= 0:
            print('Knockout! %s%s%s knocked out! 5..4..3..2..1..%s LOST! The winner is %s%s%s. Congratulations!' % (Fore.GREEN, boxer1.name, Fore.RESET, boxer1.name, Fore.GREEN, boxer2.name, Fore.RESET))
        elif boxer2.health <= 0:
            print('%s%s%s knocked out! 5..4..3..2..1..%s LOST! The winner is %s%s%s. Congratulations!' % (Fore.GREEN, boxer2.name, Fore.RESET, boxer2.name, Fore.GREEN, boxer1.name, Fore.RESET))

def main():
    try:
        boxer1 = Boxers(str(input('Enter player name: ')))
        boxer2 = Boxers(str(input('Enter computer name: ')))
        boxer1.set_health(100)
        boxer2.set_health(100)
        main_fight = Fight()

        while boxer1.health > 0 and boxer2.health > 0:
            main_fight.player_move(boxer1, boxer2)
            if main_fight.opponent_move(boxer1, boxer2):
                print('Knockout!!!')
        main_fight.check_results(boxer1, boxer2)

    except TypeError:
        print('Error: Invalid input data. Exit the program...')


if __name__ == '__main__':
    main()