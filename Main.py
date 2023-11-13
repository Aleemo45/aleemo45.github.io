from Action import Hero
from Monster import Monster

class Main:
    #object = Foo.method2(Foo.method2)

    #print(object)
    playAgain = True

    while playAgain:
        Hero.attRotation(Hero)

        answer = input('Play Again? (Y or N): ')
        if answer == 'Y':
            playAgain = True
        else:
            playAgain = False