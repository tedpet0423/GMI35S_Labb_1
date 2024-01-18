import random



def div_two_numbers(a, b):
    """
    Detta är en funktion för att hitta de heltal som både är delbart med a & b.
    Vi vill veta om 'number' är ett heltal som är både jämnt delbart med 'a' och 'b'.
    Om detta är sant innebär det att 'number' uppfyller kriterierna för båda delningarna.
    """
    for number in range(1600):  # Loopar igenom alla heltal från 1-1600#
        if number > 0 and (number % a) == 0 and (number % b) == 0:
            print(str(number))


def guesses_made():
    """
    Funktion för att låta användaren gissa ett slumpmässigt tal mellan 1 & 60#
    Användaren får sex gissningar för att hitta det rätta talet.
    """
    guesses_num = 0
    number = random.randint(1, 60) # slumpmässigt väljer en siffra mellan 1 och 60
    print('Can you guess which number im thinking of? Its a number between 1 and 60.')

    keep_loop_going = True

    while keep_loop_going:
        guess = int(input('Take a guess: '))
        guesses_num += 1 # ökar variabelns värde med 1 tills användaren svarar rätt eller når maxantalet för gissningar
        if guesses_num == 6:
            print(f'Oh bummer. The number I was thinking of was {number}')
            keep_loop_going = False  # Avslutar loopen om användaren gjort sex gissningar
        elif guess < number:
            print('To low! Please try again: ')
        elif guess > number:
            print('To high! Please try again: ')
        elif guess == number:
            print(f'Nice work! You made {guesses_num} guesses to find the right number.')
            keep_loop_going = False  # Avslutar loopen om användaren gissar rätt

