
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'gAmErS'
strategy_name = 'Collude 95% unless betrayed within last 5 rounds or have less than -150 points.'
strategy_description = '''\
Betray if they betray in last 5 rounds, or if our score is below -150. Other wise our code will be random with us betraying only 5% of the time
'''

import random 
            
def move(my_history, their_history, my_score, their_score):
    if my_score < -150:
        return 'b'
    else:
        if 'b' in their_history[-5:]:
            return 'b'
        else:
            if random.random()<0.05:
                return 'b'
            else:
                return 'c'
    
    
    
    
