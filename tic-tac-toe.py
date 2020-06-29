def game_name():
    print('\nWelcome to Tic-Tac-Toe!\n')
def player_weapon():
    x = '0'
    while x not in ['X','O']:
        x = input('choose your weapon (X or O):')
        if x not in ['X','O']:
            print('\noops, weapon not available! choose again:')
    return x
def display_board(current_list):
    print(f'| {current_list[0]} | {current_list[1]} | {current_list[2]} |')
    print(f'| {current_list[3]} | {current_list[4]} | {current_list[5]} |')
    print(f'| {current_list[6]} | {current_list[7]} | {current_list[8]} |')
def display_rules():
    sample_list = ['9','8','7','6','5','4','3','2','1']
    print('Tic-Tac-Toe classic rules:\n')
    print('1. first player to capture any one of the 8 lines WINS!')
    print('2. territories are demarkated in the following manner:\n')
    display_board(sample_list)
    print('\nmay the best player win!')
def are_players_ready():
    x = 0
    while x not in ['Y','N']:
        x = input('\nstart?(Y or N):')
        if x not in ['Y','N']:
            print('\nPlease enter Y to start!')
    if x == 'Y':
        current_player = 'PLAYER-1'
        return True
    else:
        return False
def display_progress(current_list):
    print('\ncurrent status:\n')
    display_board(current_list)
def player1_input(current_list,P1_weapon,current_player):
    x = 'WRONG'
    while x not in range(1,10):
        x = int(input('PLAYER-1: enter the teritory you want to mark(1 ~ 9):'))
        if x not in range(1,10):
            print('\nPlease mark a valid teritory(1 ~ 9)!')
    current_list[9-x] = P1_weapon
    current_player = 'PLAYER-1'
    display_progress(current_list)
    return current_list
def player2_input(current_list,P2_weapon,current_player):
    x = 'WRONG'
    while x not in range(1,10):
        x = int(input('PLAYER-2: enter the teritory you want to mark(1 ~ 9):'))
        if x not in range(1,10):
            print('\nPlease mark a valid teritory(1 ~ 9)!')
    current_list[9-x] = P2_weapon
    current_player = 'PLAYER-2'
    display_progress(current_list)
    return current_list
def result_check(current_list):
    def check(LIST):
        check_list = current_list
        current_player = 'PLAYER-1'
        if check_list[LIST[0]] == check_list[LIST[1]] == check_list[LIST[2]] and check_list[LIST[0]] in ['X','O']:
            print(f'{current_player} wins!')
            return True
        elif check_list[LIST[0]] in [' '] or check_list[LIST[1]] in [' '] or check_list[LIST[2]] in [' ']:
            return False
    def counter_check(LIST):
        if not check(LIST):
            return True
    if len(list(filter(check,[[0,4,8],[6,4,2],[2,1,0],[4,3,5],[7,6,8],[3,0,6],[1,4,7],[5,2,8]]))) != 0:
        
        return 'win'
    elif len(list(filter(counter_check,[[0,4,8],[6,4,2],[2,1,0],[4,3,5],[7,6,8],[3,0,6],[1,4,7],[5,2,8]]))) != 0:
        return 'in progress'
    else:
        print ('oops! its a tie, try another round!')
        return 'tie'
def tic_tac_toe():
        response = 'Y'
        while response == 'Y':
            current_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
            x_list = []
            result = 'in progress'
            game_name()
            display_rules()
            print('PLAYER-1: WEAPON SELECTION:')
            P1_weapon = player_weapon()
            if P1_weapon == 'X':
            	P2_weapon = 'Y'
            else:
            	P2_weapon = 'X'
            response = are_players_ready()
            current_player = 'PLAYER-1'
            display_progress(current_list)
            while result == 'in progress':
                current_list = player1_input(current_list,P1_weapon,current_player)
                result = result_check(current_list)
                if result == 'in progress':
                    current_list = player2_input(current_list,P2_weapon,current_player)
                    result = result_check(current_list)
                else:
                    pass
            response = input('would you like to play again?(Y or N):')
            if response == 'N':
                print('thanks for playing!')
            else:
                pass