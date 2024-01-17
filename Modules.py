def take_input(max_value):

    user_input = input('Type a number\n')
    run_loop1 = True
    run_loop2 = True
    while run_loop1:
        try:
            while run_loop2:
                int(user_input)
                if int(user_input) > int(max_value):
                    print('Choose a number between 0-' + str(max_value))

                elif int(user_input) < 0:
                    print('Choose a number between 0-' + str(max_value))

                else:
                    run_loop2 = False


        except:
            print('An exeption occured')


    return (int(user_input))

def div_two_numbers(a, b):

    for number in range(1600):
        if number > 0 and (number % a) == 0 and (number % b) == 0:
            print(str(number))
