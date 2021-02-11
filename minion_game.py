def minion_game(string):
    vowels = [65, 69, 73, 79, 85]
    pointS = 0
    pointK = 0

    word_length = len(string)
    for index, character in enumerate(string):
        if(ord(character) < 91 and ord(character) > 64):
            if ord(character) not in vowels:
                pointS += word_length - index
            else:
                pointK += word_length - index

    if pointS > pointK:
        print("Stuart {}".format(pointS))
    elif pointS < pointK:
        print("Kevin {}".format(pointK))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
