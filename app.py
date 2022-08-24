####################################
# Python Band Name Generator
####################################
import time
import random

if __name__ == "__main__":
    # step 1 - print welcome message
    print('''Welcome to the band name generator!
All talented musicians need a great name for their band.
Lets get you one.....''')

    # step 2 - ask user for the city they grew up in 
    city = input('Can you give me the name of a city you grew up in? ').strip().lower()
    time.sleep(1)
    print('Okay, got it!\n')

    # step 3 - ask user for a pets name
    pet_name = input('Can you give me the name of a pet that either you, a friend or a family member owned? ').strip().lower()
    print('Okay, got it!')

    # step 4 - generate name and ask if they are happy 
    print('\n\nI am thinking of a name for your band......')
    time.sleep(3)
    print('Drum roll please.....')
    time.sleep(1)
    print(f'The name for your band is {city}-{pet_name}')
    user_input = input('Are you happy with my suggestion? Enter N for a new name or Y to exit ').strip().lower() 
    # if yes exit prorgam

    # random words gathered from https://randomwordgenerator.com/ and stored in text file
    # read in random_words.txt     
    random_words = open('random_words.txt','r')
    read_words = random_words.read()
    rand_list = [word for word in read_words.split('\n')]

    # step 5 - if user not happy generate further random names
    while user_input != 'y':
        # if no generate random name from words in text file
        print('\nHmmm sorry about that, let me think of a new name.....')
        print('Generating a new name for your band now....')
        time.sleep(3)
        print(f'{rand_list[random.randint(0,len(rand_list)-1)]}-{rand_list[random.randint(0,len(rand_list)-1)]}')
        user_input = input('Are you happy with my suggestion? Enter N for a new name or Y to exit ').strip().lower()



