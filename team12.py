####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cornavirus' # Only 10 chars displayed
strategy_name = 'background check'
strategy_description = 'if the other team has a history of betraying, betray. if they are trustworthy, collude'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # this player does a background check to see if the other player is trustworthy or not.
    if 'b' in their_history[-9:] > 6:
        return 'b'
    else:
        return 'c'
        
        
    
    
