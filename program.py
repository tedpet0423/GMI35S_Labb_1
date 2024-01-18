import modules
import time


loop_running = True
while loop_running:
    print('Choose an option from list below:'
          '\n1. Print numbers between 1-1600 that can be'
          '\n   divided by two numbers of your choice.'
          '\n2. Guessing game! Guess a number between 0-60'
          '\n3. Exit')
    user_input = input()
    if user_input == '1':
        print('You choose 1!')
        user_input_div_1 = int(input('Type a number between 1-1600: '))
        user_input_div_2 = int(input('Type another number between 1-1600: '))
        modules.div_two_numbers(user_input_div_1, user_input_div_2)  # anropar funktionen för att hitta delbara tal
        input('Press enter to continue')
    elif user_input == '2':
        print('You choose 2!')
        modules.guesses_made()  # anropar funktionen för gissningsspelet
        input('Press enter to continue')
    elif user_input == '3':
        print('Exiting...')
        time.sleep(1)
        loop_running = False
    else:
        print('Try a number from the list!')
print('Press enter to exit.')
input()
exit()
