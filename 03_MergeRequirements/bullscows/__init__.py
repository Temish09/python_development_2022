def bullscows(guess: str, secret: str) -> (int, int):
    import textdistance as td
    
    bulls = td.hamming.similarity(guess, secret)
    cows = 0
    for i in range(len(guess)):
        if guess[i] in secret:
            cows += 1
        if i < len(secret):
            if guess[i] == secret[i]:
                cows -= 1
    
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list) -> int:
    import random
    
    secret = random.choice(words)
    
    tries = 0
    while True:
        tries += 1
        guess = ask('Введите слово: ', words)
        b, c = bullscows(guess, secret)
        inform('Быки: {}, Коровы: {}', b, c)
    
        if b == len(secret):
            break
    
    return tries


def ask(prompt: str, valid: list = None) -> str:
    if not valid:
        return input(prompt)
    
    guess = None
    while guess not in valid:
        guess = input(prompt)
    
    return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
