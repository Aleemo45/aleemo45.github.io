from random import randint
import time
from Colour import Colour
from Monster import Monster

hP = 100
attkPow = 5
mHp = 20
mattkPow = 10
buff = False


def current(hHp):
    if hHp > 0:
        return f"Your HP is: {hHp}"
    else:
        return 'You Died'


def textPause():
    time.sleep(2)


def takePotion(hHp):
    potion = 25
    print('You take a potion')
    print(f'you were healed for' + Colour.GREEN + f' {potion} ' + Colour.END + 'HP')
    hHp += potion
    return hHp


def mCurrent(monHp):
    if monHp > 0:
        return f"The Monster's HP is: {monHp}"
    else:
        return 'You killed the monster'


def hAttack(attkpow):
    heroAttks = ['Normal']


def cBuff():
    cNum = randint(0, 3)

    if cNum == 3:
        buff = True
        print('The Monster Buffed')
        return buff
    else:
        buff = False
        return buff


# def mAttack(mattkPow, hHp, buff):
#     monAttks = ['normal', 'special']
#     aNum = randint(0,1)
#     mSelect = monAttks[aNum]

#     if buff:
#         mattkPow = mattkPow = mattkPow * 3
#         buff = False


#     if mSelect == 'normal':
#         if mCritical():
#             mattkPow *= 2
#             hHp -= (mattkPow*2)
#         else:
#             hHp -= mattkPow
#         print(f'The monster attacked you for ' + Colour.RED + f'{mattkPow}' + Colour.END + ' damage')
#         #buff = False
#         return hHp
#     elif mSelect == 'special':
#         if mCritical():
#             mattkPow = mattkPow * 3
#             hHp -= mattkPow
#         else:
#             mattkPow *= 1.5
#             hHp -= (mattkPow)
#         print(f'The monster used a special attack dealing ' + Colour.RED + f'{mattkPow}' + Colour.END + ' damage')
#         #buff = False
#         return hHp
# elif mSelect == 'defend':
#     print('The Monster buffed')
#     buff = True
#     t = []
#     t.append(hHp)
#     t.append(buff)
#     return t


def mCritical():
    cNum = randint(1, 100)
    if cNum > 70:
        print('CRITICAL HIT!!!!')
        crit = True
        return crit
    else:
        crit = False
        return crit


def mMultiAttk(monHp, hHp):
    aNum = randint(2, 4)
    n = 0

    # hHp = mAttack(mattkPow, hHp, buff)
    hpValues = Monster.mAttack(Monster, Monster.monAttk, hHp, monHp, attkPow)
    hHp = hpValues[0]
    monHp = hpValues[1]
    print('Multi-Strike')
    while n < aNum:
        arrows()
        cNum = randint(1, 10)
        if mCritical():
            cNum = cNum * 2
        if monHp <= 0:
            break
        n += 1
        print(f'The Monster takes {cNum} points of damage')
        monHp -= cNum
        print(mCurrent(monHp))
        textPause()
    return hHp, monHp


def arrows():
    print(Colour.PURPLE + '\u2193' * 7 + Colour.END)


def helpMenu():
    print('''Attack
Multi Attack
Buff
Take a Potion
Defend''')


def attRotation():
    hHp = hP
    monHp = Monster.monHp
    bTurn = 0
    print(current(hHp))
    print('A Monster approches')
    while monHp > 0:
        # print(buff)
        if hHp <= 0:
            print('You have died')
            break
        arrows()
        ansPath = input('What will you do: ')
        arrows()
        if ansPath == 'Attack':
            # monHp -= attkPow
            # if bTurn == 0:
            #     buff = cBuff()
            # if buff and bTurn == 1:
            #     bTurn = 0
            #     hHp = mAttack(mattkPow, hHp, buff)
            #     buff = False
            # elif buff == False:
            #     hHp = mAttack(mattkPow, hHp, buff)
            hpValues = Monster.mAttack(Monster, Monster.monAttk, hHp, monHp, attkPow)
            hHp = hpValues[0]
            monHp = hpValues[1]
        elif ansPath == 'Multi':
            multi = mMultiAttk(monHp, hHp)
            hHp = multi[0]
            monHp = multi[1]
            # n = 0
            # hHp = mAttack(mattkPow, hHp, buff)
            # print('Multi-Strike')
            # while n < 3:
            #     monHp = mMultiAttk(monHp)
            #     arrows()
            #     if monHp <= 0:
            #         break
            #     n += 1
        elif ansPath == 'Defend':
            hHp -= mattkPow * .25
            hHp = round(hHp)
        elif ansPath == 'Potion':
            hHp = takePotion(hHp)
            hpValues = Monster.mAttack(Monster, Monster.monAttk, hHp, monHp, attkPow)
            hHp = hpValues[0]
            monHp = hpValues[1]
        elif ansPath == 'Help':
            helpMenu()
        textPause()
        hHp = hHp
        if buff:
            bTurn += 1
        print(current(hHp))
        print(mCurrent(monHp))
        # if monHp <= 0:
        #     print('You have killed the monster!!')


attRotation()