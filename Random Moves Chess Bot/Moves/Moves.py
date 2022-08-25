def Moves():
    
    import random

    pieces = ['','N','B','R','Q','K']
    letters = ['a','b','c','d','e','f','g','h']
    numbers = ['1','2','3','4','5','6','7','8']

    piece = random.choice(pieces)
    letter = random.choice(letters)
    number = random.choice(numbers)
    move = piece + letter + number
    #Random combination of the chess move that consists in piece and square
    # (letter + number).
    
    return move

