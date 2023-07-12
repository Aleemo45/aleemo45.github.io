import random
import string


def pass_generation(letGen,numGen,punGen):
    passNum = []

    passLen = letGen + numGen + punGen

    while len(passNum) < passLen:
        count = 0
        if letGen > 0:
            while count < letGen:
                passNum.append(random.choice(string.ascii_letters))
                count += 1
                break
        if numGen > 0:
            while count < numGen:
                passNum.append(random.choice(string.digits))
                count += 1
                break
        if punGen > 0:
            while count < punGen:
                passNum.append(random.choice(string.punctuation))
                count += 1

    random.shuffle(passNum)
    password = ''.join(passNum)
    return password


def ask_question():
    while True:
        try:
            question1 = int(input('How many letters?: '))
            question2 = int(input('How many numbers?: '))
            question3 = int(input('How many special characters? : '))
            break
        except ValueError:
            print('''Please use numbers only.
            Try again.''')

    return question1, question2, question3


t1,t2,t3 = ask_question()
print(pass_generation(t1, t2, t3))


