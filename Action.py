from random import randint
import time
from Colour import Colour
from Monster import Monster
from Monster import Wizard
import random


# hP = 100
# attkPow = 5
# #mHp = 20
# #mattkPow = 10
# buff = False
# hAction = None

class Hero:
    hP = 100
    attkPow = 5
    # mHp = 20
    # mattkPow = 10
    buff = False
    hAction = None
    hStatus = None
    potionCnt = 5

    def __init__(self, hP, attkPow, buff, hAction, hStatus):
        self.hP = hP
        self.attkPow = attkPow
        self.buff = buff
        self.hAction = hAction
        self.hStatus = hStatus

    def current(self, hHp):
        if hHp > 30:
            return f"Your HP is: {hHp}"
        elif hHp <= 30 and hHp > 0:
            # print('Your HP is' + Colour.RED + ' critical' + Colour.END)
            return 'Your HP is: ' + Colour.RED + f'{hHp} (critical)' + Colour.END
        else:
            return 'You Died'

    def textPause(self):
        time.sleep(2)

    def takePotion(self, hHp):
        if self.potionCnt > 0:
            self.potionCnt -= 1
            potion = 25
            print('You take a potion')
            print(f'you were healed for' + Colour.GREEN + f' {potion} ' + Colour.END + 'HP')
            print(f'You have {self.potionCnt} potions left')
            hHp += potion
            if hHp > self.hP:
                print('Your HP is maxed out')
                hHp = self.hP
            Hero.arrows(Hero)
        else:
            print('You do not have anymore potions')
        return hHp

    def mCurrent(self, monHp, enemyType):
        if monHp > 0:
            return f"The Monster's HP is: {monHp}"
        else:
            return f'You killed the {enemyType}'

    def hAttack(self, attkpow):
        pass

    def hStatusChance(self, hStatus, hHp):
        hMove = True
        if hStatus == 'paralyzed' or hStatus == 'dizzy':
            moveChance = randint(1, 100)
            print(f'''You are {hStatus}.
You attempt to move.''')
            Hero.arrows(Hero)
            if moveChance <= 50:
                print('You can not move')
                hMove = False
            else:
                print('You can move')
                hMove = True
        elif hStatus == 'frozen':
            print('You are frozen and can not move')
            hMove = False
        elif hStatus == 'burn':
            print('You took' + Colour.RED + ' 5 ' + Colour.END + 'damage from your burn')
            hHp -= 5
            hMove = True
        self.hStatus = None
        Hero.textPause(Hero)
        return hHp, hMove

    def hBuff(self, attkPow, buff):
        if buff == False:
            self.buff = True
            self.attkPow = attkPow * 2
        elif self.hAction == 'Buff' and buff == True:
            print('You are already buffed')
        else:
            self.buff = False
            self.attkPow = attkPow * .50

    # def mAttack(mattkPow, self.hHp, buff):
    #     monAttks = ['normal', 'special']
    #     aNum = randint(0,1)
    #     mSelect = monAttks[aNum]

    #     if buff:
    #         mattkPow = mattkPow = mattkPow * 3
    #         buff = False

    #     if mSelect == 'normal':
    #         if mCritical():
    #             mattkPow *= 2
    #             self.hHp -= (mattkPow*2)
    #         else:
    #             self.hHp -= mattkPow
    #         print(f'The monster attacked you for ' + Colour.RED + f'{mattkPow}' + Colour.END + ' damage')
    #         #buff = False
    #         return self.hHp
    #     elif mSelect == 'special':
    #         if mCritical():
    #             mattkPow = mattkPow * 3
    #             self.hHp -= mattkPow
    #         else:
    #             mattkPow *= 1.5
    #             self.hHp -= (mattkPow)
    #         print(f'The monster used a special attack dealing ' + Colour.RED + f'{mattkPow}' + Colour.END + ' damage')
    #         #buff = False
    #         return self.hHp
    # elif mSelect == 'defend':
    #     print('The Monster buffed')
    #     buff = True
    #     t = []
    #     t.append(self.hHp)
    #     t.append(buff)
    #     return t

    def mCritical(self):
        cNum = randint(1, 100)
        if cNum > 70:
            # print('CRITICAL HIT!!!!')
            crit = True
            return crit
        else:
            crit = False
            return crit

    def mMultiAttk(self, monHp, hHp, attkPow, enemyType):
        aNum = randint(2, 4)
        n = 0

        # self.hHp = mAttack(mattkPow, self.hHp, buff)
        hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, attkPow, 'multi1', self.hStatus)
        hHp = hpValues[0]
        monHp = hpValues[1]
        Hero.arrows(Hero)
        print(Colour.CYAN + 'Multi-Strike' + Colour.END)
        while n < aNum:
            Hero.arrows(Hero)
            cNum = randint(3, attkPow)
            if Hero.mCritical(Hero):
                cNum = cNum * 2
            if monHp <= 0:
                break
            n += 1
            # print('You deal'  + Colour.RED + f' {cNum} ' + Colour.END + 'points of damage')
            # monHp -= cNum
            hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, cNum, self.hAction, self.hStatus)
            hHp = hpValues[0]
            monHp = hpValues[1]
            print(Hero.mCurrent(Hero, monHp, enemyType))
            Hero.textPause(Hero)
        Hero.arrows(Hero)
        print(f'The {enemyType} was attacked {n} times')
        return hHp, monHp

    def arrows(self):
        print(Colour.PURPLE + '\u2193' * 12 + Colour.END)

    def mChoice(self):
        enemyCall = ['monster', 'wizard']
        # enemyCall = ['wizard']
        randomEnemy = random.choice(enemyCall)

        return randomEnemy

    def moveCall(self, hHp, enemyType, rAttk):
        move = Hero.hStatusChance(Hero, self.hStatus, hHp)
        hHp = move[0]
        moveChance = move[1]
        if moveChance:
            hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction, self.hStatus)
            hHp = hpValues[0]
            monHp = hpValues[1]
        else:
            rAttk = 0
            hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction, self.hStatus)
            hHp = hpValues[0]
            monHp = hpValues[1]

    def mCall(self, enemyType, Attk, hHp, monHp, rAttk, hAction, hStatus):
        if enemyType == 'monster':
            hpValues = Monster.mAttack(Monster, Attk, hHp, monHp, rAttk, hAction, hStatus)
            hHp = hpValues[0]
            monHp = hpValues[1]
            if len(hpValues) > 2:
                hStatus = hpValues[2]
                return hHp, monHp, hStatus
            else:
                return hHp, monHp
        else:
            hpValues = Wizard.wAttack(Wizard, Attk, hHp, monHp, rAttk, hAction, hStatus)
            hHp = hpValues[0]
            monHp = hpValues[1]
            hStatus = hpValues[2]
            return hHp, monHp, hStatus

    def helpMenu(self):
        print('''Attack
Multi Attack
Buff
Take a Potion
Defend''')

    def inputCheck(self, ansPath):
        acptAnsPath = ['Attack', 'Multi', 'Buff', 'Potion', 'Defend', 'Help']
        if ansPath not in acptAnsPath:
            print('''That option is not available. 
Please try again.''')

    def attRotation(self):
        # playAgain = True
        # while playAgain == True:
        hHp = self.hP
        monHp = Monster.monHp
        moveChance = True
        rAttk = self.attkPow
        self.hStatus = None

        print(Hero.current(Hero, hHp))
        enemyType = Hero.mChoice(Hero)
        print(f'A {enemyType} approches')

        while monHp > 0:
            # print(buff)
            if hHp <= 0:
                # print('You have died')
                break
            Hero.arrows(Hero)
            ansPath = input('What will you do? (Type "Help" for options): ')
            Hero.inputCheck(Hero, ansPath)
            Hero.arrows(Hero)
            self.hAction = ansPath
            if ansPath.lower() == 'attack':
                # monHp -= attkPow
                # if bTurn == 0:
                #     buff = cBuff()
                # if buff and bTurn == 1:
                #     bTurn = 0
                #     self.hHp = mAttack(mattkPow, self.hHp, buff)
                #     buff = False
                # elif buff == False:
                #     self.hHp = mAttack(mattkPow, self.hHp, buff)
                move = Hero.hStatusChance(Hero, self.hStatus, hHp)
                hHp = move[0]
                moveChance = move[1]
                if moveChance:
                    rAttk = self.attkPow
                    if Hero.mCritical(Hero):
                        rAttk = self.attkPow * 2
                        print(f'''You attack the {enemyType} 
Critical hit!!!''')
                    else:
                        print(f'You attack the {enemyType}')
                    if self.buff == True:
                        Hero.hBuff(Hero, self.attkPow, self.buff)
                else:
                    rAttk = 0
                hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction, self.hStatus)
                hHp = hpValues[0]
                monHp = hpValues[1]
                if len(hpValues) > 2:
                    self.hStatus = hpValues[2]
            elif ansPath.lower() == 'multi':
                move = Hero.hStatusChance(Hero, self.hStatus, hHp)
                hHp = move[0]
                moveChance = move[1]
                if moveChance:
                    multi = Hero.mMultiAttk(Hero, monHp, hHp, self.attkPow, enemyType)
                    hHp = multi[0]
                    monHp = multi[1]
                    if self.buff == True:
                        Hero.hBuff(Hero, self.attkPow, self.buff)
                else:
                    rAttk = 0
                    hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction,
                                          self.hStatus)
                    hHp = hpValues[0]
                    monHp = hpValues[1]
                    if len(hpValues) > 2:
                        self.hStatus = hpValues[2]
                # n = 0
                # self.hHp = mAttack(mattkPow, self.hHp, buff)
                # print('Multi-Strike')
                # while n < 3:
                #     monHp = mMultiAttk(monHp)
                #     arrows()
                #     if monHp <= 0:
                #         break
                #     n += 1
            elif ansPath.lower() == 'defend':
                move = Hero.hStatusChance(Hero, self.hStatus, hHp)
                hHp = move[0]
                moveChance = move[1]
                if moveChance:
                    hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction,
                                          self.hStatus)
                    hHp = hpValues[0]
                    monHp = hpValues[1]
                    if len(hpValues) > 2:
                        self.hStatus = hpValues[2]
            elif ansPath.lower() == 'potion':
                move = Hero.hStatusChance(Hero, self.hStatus, hHp)
                hHp = move[0]
                moveChance = move[1]
                if moveChance:
                    hHp = Hero.takePotion(Hero, hHp)
                hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction, self.hStatus)
                hHp = hpValues[0]
                monHp = hpValues[1]
                if len(hpValues) > 2:
                    self.hStatus = hpValues[2]
            elif ansPath.lower() == 'buff':
                move = Hero.hStatusChance(Hero, self.hStatus, hHp)
                hHp = move[0]
                moveChance = move[1]
                # print(moveChance)
                if moveChance:
                    Hero.hBuff(Hero, self.attkPow, self.buff)
                hpValues = Hero.mCall(Hero, enemyType, Monster.monAttk, hHp, monHp, rAttk, self.hAction, self.hStatus)
                hHp = hpValues[0]
                monHp = hpValues[1]
                if len(hpValues) > 2:
                    self.hStatus = hpValues[2]
            elif ansPath.lower() == 'help':
                Hero.helpMenu(Hero)
            Hero.textPause(Hero)
            hHp = hHp
            # if self.buff:
            #     bTurn += 1
            print(Hero.current(Hero, hHp))
            print(Hero.mCurrent(Hero, monHp, enemyType))

        Hero.arrows(Hero)
        if hHp <= 0:
            print(Colour.RED + Colour.BOLD + 'You Lose' + Colour.END)
        else:
            print(Colour.YELLOW + Colour.BOLD + 'You Win' + Colour.END)
            # if monHp <= 0:
            #     print('You have killed the monster!!')

            # answer = input('Play Again? (Y or N): ')
            # if answer == 'Y':
            #     playAgain = True
            # else:
            #     playAgain = False

# Hero.attRotation(Hero)