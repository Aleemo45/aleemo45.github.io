from random import randint
import random
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

    def cStatusChance(self):
        sChance = random.randint(1, 100)
        if sChance <= 40:
            statusEffect = True
        else:
            statusEffect = False
        return statusEffect

    def mdizzyStatus(self):
        statusEffect = Monster.cStatusChance(Monster)
        if statusEffect:
            print('The Monster dazed you')
            dizzyStatus = 'dizzy'
            return dizzyStatus
        else:
            return None

    def mDamage(self, mSelect, attkPow, monHp, hAction, hStatus):
        if mSelect == 'dodge':
            return monHp
        elif mSelect == 'block':
            battkPow = round(attkPow * .50)
            monHp = monHp - battkPow
            print('It takes ' + Colour.DARKCYAN + f'{battkPow}' + Colour.END + ' of damage')
            return monHp
        elif hAction != 'Attack' and hAction != 'Multi':
            return monHp
        else:
            monHp = monHp - attkPow
            if attkPow > 0:
                print('It takes ' + Colour.RED + f'{attkPow}' + Colour.END + ' of damage')
            return monHp

    def mBuff(self, monAttk, buff):
        if buff == True:
            buff = False
            monAttk = monAttk * .50
        return buff, monAttk

    def mAttack(self, monAttk, hHp, monHp, attkPow, hAction, hStatus):
        monAttksel = ['normal', 'special', 'dodge', 'block', 'buff']
        # aNum = randint(0,4)
        # mSelect = monAttksel[aNum]

        if hStatus == 'dizzy':
            safe = True
        else:
            safe = False

        if hAction == 'Multi' and not safe:
            monAttksel = [None]
        elif (hAction != 'Attack' and hAction != 'Multi') or safe:
            monAttksel = ['normal', 'special', 'buff']
            # mSelect = random.choice(monAttksel)
        elif monHp <= (self.monHp * 5):
            monAttksel = ['special', 'dodge', 'block']
        # elif hAction == 'Multi':
        #     monAttksel = [None]

        mSelect = random.choice(monAttksel)

        if mSelect != 'dodge' and mSelect != 'block':
            monHp = Monster.mDamage(Monster, mSelect, attkPow, monHp, hAction, hStatus)

        if mSelect == 'normal':
            crit = Monster.mCritical(Monster)
            if crit:
                cHit = self.monAttk * 2
                if hAction == 'Defend':
                    cHit = round(cHit - (cHit * .25))
                    hHp -= cHit
                else:
                    hHp -= cHit
                print('The monster attacked you for ' + Colour.RED + f'{cHit}' + Colour.END + ' damage')
            else:
                if hAction == 'Defend':
                    rAttack = round(self.monAttk - (self.monAttk * .25))
                    hHp -= rAttack
                    print('The monster attacked you for ' + Colour.RED + f'{rAttack}' + Colour.END + ' damage')
                else:
                    hHp -= self.monAttk
                    print('The monster attacked you for ' + Colour.RED + f'{self.monAttk}' + Colour.END + ' damage')

            # if self.buff == True:
            #     self.buff = False
            #     self.monAttk = self.monAttk*.50

            buff = Monster.mBuff(Monster, self.monAttk, self.buff)
            self.buff = buff[0]
            self.monAttk = buff[1]

            return hHp, monHp
        elif mSelect == 'special':
            crit = Monster.mCritical(Monster)
            if crit:
                scHit = ((self.monAttk * 1.5) * 2)
                if hAction == 'Defend':
                    scHit = round(scHit - (scHit * .25))
                    hHp -= scHit
                else:
                    hHp -= scHit
                print('The monster used a special attack dealing ' + Colour.RED + f'{scHit}' + Colour.END + ' damage')
            else:
                spHit = self.monAttk * 1.5
                if hAction == 'Defend':
                    spHit = round(spHit - (spHit * .25))
                    hHp -= spHit
                else:
                    hHp -= spHit
                print('The monster used a special attack dealing ' + Colour.RED + f'{spHit}' + Colour.END + ' damage')
            dizzyStatus = Monster.mdizzyStatus(Monster)

            buff = Monster.mBuff(Monster, self.monAttk, self.buff)
            self.buff = buff[0]
            self.monAttk = buff[1]

            return hHp, monHp, dizzyStatus
        elif mSelect == 'dodge':
            print('The Monster dodged the attack')
            monHp = Monster.mDamage(Monster, mSelect, attkPow, monHp, hAction, hStatus)
            return hHp, monHp
        elif mSelect == 'block':
            print('The Monster blocked the attack')
            monHp = Monster.mDamage(Monster, mSelect, attkPow, monHp, hAction, hStatus)
            return hHp, monHp
        elif mSelect == 'buff':
            if self.buff == True:
                print('The Monster attempted to buff')
                time.sleep(2)
                print('But he was already buffed')
            else:
                self.monAttk = self.monAttk * 2
                self.buff = True
                print('The Monster Buffed for 2x Damage')
            return hHp, monHp
        else:
            return hHp, monHp


class Wizard(Monster):
    def __init__(self, monster):
        Monster.__init__(self, Monster.monHp, Monster.monAttk, Monster.buff)
        wAttk = (Monster.monAttk * .50)

    def cStatusChance(self):
        sChance = random.randint(1, 100)
        if sChance <= 70:
            statusEffect = True
        else:
            statusEffect = False
        return statusEffect

    def mDamage(self, wSelect, attkPow, monHp, hAction, hStatus):
        test = Monster.mDamage(Monster, wSelect, attkPow, monHp, hAction, hStatus)
        return test

    def wStatus(self, sCast, statusEffect):
        if sCast == 'Lighting':
            print('you are paralyzed')
            statusEffect = 'paralyzed'
        elif sCast == 'Blizzard':
            print('You are frozen')
            statusEffect = 'frozen'
        elif sCast == 'Fire':
            print('You are burning')
            statusEffect = 'burn'
        return statusEffect

    def wSpellDamage(self, wAttack, sCast, statusEffect):
        if sCast == 'Lighting':
            tColor = Colour.YELLOW
        elif sCast == 'Blizzard':
            tColor = Colour.BLUE
        else:
            tColor = Colour.RED

        print(
            'The Wizard casts' + tColor + f' {sCast} ' + Colour.END + 'on you for' + Colour.RED + f' {wAttack} ' + Colour.END + 'damage')
        # if sCast == 'Lighting':
        #     print('The Wizard casts' + Colour.YELLOW + f' {sCast} ' + Colour.END + 'on you for' + Colour.RED + f' {wAttack} ' + Colour.END + 'damage')
        # elif sCast == 'Blizzard':
        #     print('The Wizard casts' + Colour.BLUE + ' Blizzard ' + Colour.END + 'on you for' + Colour.RED + f' {wAttack} ' + Colour.END + 'damage')
        # elif sCast == 'Fire':
        #     print('The Wizard casts' + Colour.RED + ' Fire ' + Colour.END + 'on you for' + Colour.RED + f' {wAttack} ' + Colour.END + 'damage')
        if Wizard.cStatusChance(Wizard):
            statusEffect = Wizard.wStatus(Wizard, sCast, statusEffect)
        return statusEffect

    def wAttack(self, monAttk, hHp, monHp, attkPow, hAction, hStatus):
        wAttk = Monster.monAttk * .50
        monAttksel = ['normal', 'cast', 'multi-cast', 'dodge', 'heal']
        spell = ['Lighting', 'Blizzard', 'Fire']
        statusEffect = None

        if (hStatus == 'frozen' or hStatus == 'paralyzed'):
            safe = True
        else:
            safe = False

        if hAction == 'Multi' and not safe:
            monAttksel = [None]
        elif monHp <= (self.monHp * .5) and ((hAction == 'Attack' or hAction == 'Multi') and not safe):
            monAttksel = ['multi-cast', 'dodge', 'heal']
            # wSelect = random.choice(monAttksel)
        elif hAction != 'Attack' or hAction != 'Multi' or safe:
            monAttksel = ['normal', 'cast', 'multi-cast', 'heal']
            # wSelect = random.choice(monAttksel)
        # elif hAction == 'Multi':
        #     monAttksel = [None]
        # else:
        # wSelect = random.choice(monAttksel)
        wSelect = random.choice(monAttksel)

        monHp = Wizard.mDamage(Wizard, wSelect, attkPow, monHp, hAction, hStatus)

        if wSelect == 'normal':
            crit = Wizard.mCritical(Wizard)
            if crit:
                cHit = wAttk * 2
                if hAction == 'Defend':
                    cHit = round(cHit - (cHit * .25))
                    hHp -= cHit
                else:
                    hHp -= cHit
                print('The Wizard attacked you for ' + Colour.RED + f'{cHit}' + Colour.END + ' damage')
            else:
                if hAction == 'Defend':
                    rAttack = round(wAttk - (wAttk * .25))
                    hHp -= rAttack
                    print('The Wizard attacked you for ' + Colour.RED + f'{rAttack}' + Colour.END + ' damage')
                else:
                    hHp -= wAttk
                    print('The Wizard attacked you for ' + Colour.RED + f'{wAttk}' + Colour.END + ' damage')
        elif wSelect == 'cast':
            sCast = random.choice(spell)
            if hAction == 'Defend':
                rAttack = round(wAttk - (wAttk * .25))
            else:
                rAttack = 10
            hHp -= rAttack
            statusEffect = Wizard.wSpellDamage(Wizard, rAttack, sCast, statusEffect)
            # return hHp, monHp, statusEffect
        elif wSelect == 'multi-cast':
            print('The wizard casts multiple spells')
            sCast = random.choice(spell)
            if hAction == 'Defend':
                rAttack = round(wAttk - (wAttk * .25))
            else:
                rAttack = wAttk * 2
            for _ in range(random.randint(2, 4)):
                sCast = random.choice(spell)
                statusEffect = Wizard.wSpellDamage(Wizard, rAttack, sCast, statusEffect)
                time.sleep(1)
                hHp -= rAttack
            # return hHp, monHp, statusEffect
        elif wSelect == 'dodge':
            print('The Wizard dodged the attack')
        elif wSelect == 'heal':
            print('The Wizard healed for' + Colour.GREEN + ' 10 ' + Colour.END + 'HP')
            if monHp >= self.monHp:
                print("The Wizard's HP is maxed out")
                monHp = self.monHp
            else:
                monHp += 10
        return hHp, monHp, statusEffect

# Monster.mAttack(Monster, Monster.monAttk, 100, Monster.monHp, 5, 'Attack', None)
# test = Wizard.wAttack(Wizard, Monster.monAttk, 100, Monster.monHp, 5, 'Attack', None)
# print(test[0])
# print(test[1])
# print(test[2])
