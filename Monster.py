from random import randint
from Colour import Colour
import time


class Monster:
    monHp = 30
    monAttk = 10.0
    buff = False

    def __init__(self, monHp, monAttk, buff):
        self.monHp = monHp
        self.monAttk = monAttk
        self.buff = buff

    def mCritical(self):
        cNum = randint(1, 100)
        if cNum > 70:
            print('CRITICAL HIT!!!!')
            crit = True
            return crit
        else:
            crit = False
            return crit

    def mDamage(self, mSelect, attkPow, monHp):
        if mSelect == 'dodge':
            return monHp
        elif mSelect == 'block':
            monHp = monHp - round(attkPow * .50)
            return monHp
        else:
            monHp = monHp - attkPow
            return monHp

    def mAttack(self, monAttk, hHp, monHp, attkPow):
        monAttksel = ['normal', 'special', 'dodge', 'block', 'buff']
        aNum = randint(0, 4)
        mSelect = monAttksel[aNum]

        if self.buff:
            self.monAttk = self.monAttk * 2

        monHp = Monster.mDamage(Monster, mSelect, attkPow, monHp)

        if mSelect == 'normal':
            crit = Monster.mCritical(Monster)
            if crit:
                cHit = self.monAttk * 2
                hHp -= cHit
                print('The monster attacked you for ' + Colour.RED + f'{cHit}' + Colour.END + ' damage')
            else:
                hHp -= self.monAttk
                print('The monster attacked you for ' + Colour.RED + f'{self.monAttk}' + Colour.END + ' damage')

            if self.buff == True:
                self.buff = False
                self.monAttk = self.monAttk / 2

            return hHp, monHp
        elif mSelect == 'special':
            crit = Monster.mCritical(Monster)
            if crit:
                scHit = self.monAttk * 3
                hHp -= scHit
                print('The monster used a special attack dealing ' + Colour.RED + f'{scHit}' + Colour.END + ' damage')
            else:
                spHit = self.monAttk * 1.5
                hHp -= spHit
                print('The monster used a special attack dealing ' + Colour.RED + f'{spHit}' + Colour.END + ' damage')

            if self.buff == True:
                self.buff = False
                self.monAttk = self.monAttk / 2

            return hHp, monHp
        elif mSelect == 'dodge':
            print('The Monster dodged the attack')
            return hHp, monHp
        elif mSelect == 'block':
            print('The Monster blocked the attack')
            return hHp, monHp
        elif mSelect == 'buff':
            if self.buff == True:
                print('The Monster attempted to buff')
                time.sleep(2)
                print('But he was already buffed')
            else:
                self.buff = True
                print('The Monster Buffed for 2x Damage')
            return hHp, monHp

#Monster.mAttack(Monster, Monster.monAttk, 100, Monster.monHp, 5)