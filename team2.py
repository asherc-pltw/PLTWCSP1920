####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Pentagofu'
strategy_name = 'Betray, Opposite, and History'
strategy_description = 'Betray first, then do opposite of opponent for 3 moves, then go based off total history.'
    
def move(my_history, their_history, my_score, their_score):
    b_counter = 0
    c_counter = 0
    nomoves = b_counter + c_counter
    if their_history == '':
       return 'b'
    if their_history[-1] == 'b':
        b_counter += 1
    elif their_history[-1] == 'c':
        c_counter += 1
    if their_history[nomoves] == 'b' and nomoves < 5:
        return 'c'
    elif their_history[nomoves] == 'c' and nomoves < 5:
        return 'b'
    elif nomoves >= 5:
        if c_counter > b_counter:
            return 'b'
        elif c_counter < b_counter:
            return 'c'
        else:
            return 'c'
