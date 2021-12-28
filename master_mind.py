import random


def check_num(num,guess):
    if num == guess:
        return True
    else :
        num_word = str(num)
        guess_word = str(guess)
        matching_indices = []
        for i in range(len(num_word)):
            if i in matching_indices:
                None
            elif num_word[i] == guess_word[i]:
                matching_indices.append(i)
    return(matching_indices)

def hinter(da_list,da_num):
    hint = 'XXXX'
    num = str(da_num)
    
    for i in da_list:        
        hint = hint[0:i]+str(num[i])+hint[i+1:len(hint)]
    return hint
def player_game():
    #p1_num = random.randint(1000,10000)    
    p1_num = 1234
    p2_guessed = False
    count = 1
    while p2_guessed == False:
        
        p2_guess = int(input('> '))
        if check_num(p1_num,p2_guess) == True:
            print('you gussed in',count,'guess(es)')
            break
        else :
            print(hinter(check_num(p1_num,p2_guess),p1_num))
        count = count+1
    return count



def computer_game(player_guesses):
    player_input = int(input('enter a num for computer guess'))
    computer_guessed = False
    comp_guess = random.randint(1000,10000)
    num_of_comp_guesses = 1
    num1 = player_input
    target_list = list(str(player_input))

    while computer_guessed == False :
        
        if num1 == '':
            print('Computer wins bhaaga')
            break
        elif num_of_comp_guesses == player_guesses:
            print('you are the master mind')
            break
        
        else :
            indices_list = check_num(num1,comp_guess)
            for i in indices_list:
            target_list.remove(target_list[i])
            
            print(comp_guess)
            print(target_list)
            num1 = ''
            for x in target_list:
                num1 = num1+x
            print(num1)
            
            comp_guess = random.randint(int(10**(len(target_list)-1)),int(10**len(target_list)))
            print(comp_guess)
        num_of_comp_guesses += 1


def game():
    player_guesses = player_game()
    computer_game(player_guesses)

game()
