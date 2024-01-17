import Modules
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
        #div_input_1 = Modules.take_input(1600)
        #div_input_2 = Modules.take_input(1600)
        #print( str(div_input_1)+'/'+str(div_input_2))
        Modules.div_two_numbers(7,11)
        input('Press any key to continue')
    elif user_input == '2':
        print('You choose 2!')
        Modules.take_input(60)
        input('Press any key to continue')
    elif user_input == '3':
        print('Exiting...')
        loop_running = False
    else:
        print('Try a number from the list!')
print('Close program Y/N')
