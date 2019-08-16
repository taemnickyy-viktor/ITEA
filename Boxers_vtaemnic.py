class Peoples:
    def __init__(self, name, age, weight):
        self.name = name  #Full name of the person
        self.age = age  # older boxers lost more health
        self.weight = weight  # heavy boxers cause more damage


class Boxers(Peoples):
    def set_health(self, health):
        #set health of boxer
        self.health = health

    def hit(self, hit):
        if hit == 1:
            self.jab()
        elif hit == 2:
            self.cross()
        elif hit == 3:
            self.left_hook()
        elif hit == 4:
            self.right_hook()

    def jab(self):
        #light damage left hand front hit
        print('jab')
    def cross(self):
        #middle damage right hand front hit
        print('cross')
    def left_hook(self):
        #powerful left hand side hit
        print('left_hook')
    def right_hook(self):
        #powerful right hand side hit
        print('right_kook')
    def left_block(self):
        #defence against cross and right_hit. Reduce damage from hit to 20%
        print('left_block')
    def right_block(self):
        # defence against jab and left_hit. Reduce damage from hit to 20%
        print('right_block')
    def left_dodge(self):
        #defence against cross and jab. In case of cross it is counterattack possible - left_hook
        print('left_dodge')
    def right_dodge(self):
        #defence against cross and jab. In case of jab it is counterattack possible - right_hook
        print('right_dodge')
    def left_dive(self):
        #defence against right_hook. Counterattack possible - right_hook
        print('left_dive')
    def right_dive(self):
        #defence against left_hook. Counterattack possible - left_hook
        print('right_dive')

class Fight:
    def __init__(self, place, char1, char2):
        self.place = place
        self.char1 = char1
        self.char2 = char2


def main():
    import random
    boxer1 = Boxers('Marco Orlando', 40, 75)
    boxer2 = Boxers('Enrico Polanci', 30, 90)
    boxer1.set_health(100)
    boxer2.set_health(100)

    while boxer1.health > 0 or boxer2.health > 0:
        boxer1.hit(int(input('1. Jab, 2. Cross, 3. Left hook, 4. Right hook')))
        boxer2.hit(random.randint(1,4))




if __name__ == '__main__':
    main()