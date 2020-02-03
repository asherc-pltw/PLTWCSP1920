####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

# Started on 1/28/2020
# Current Version Date: 1/28/2020

team_name = 'collusion8' # Only 10 chars displayed
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#version 1/28/30
team_name = 'collusion8' # Only 10 chars displayed
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
justbetrayed = False #boolean for one of the strategy to indicate that we've just betrayed.    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    #return 'c'
    
    
    if(len(my_history) < 3): #Lead with three colludes to fool the enemy into thinking that all is good, then betray for the rest of the game
        return 'c'
    else:
        return 'b'
    #Other possible strategies
    #if(len(my_history) == 1): #Lead with a betray, then drop a collude in order to hopefully fool the person into thinking that the person will stil collude, then betray for the rest of the game 
    #   return 'c'
    #else:
    #   return 'b'
    
    
    #if(len(my_history) == 0): #Lead with a collude, then betray for the rest of the game
    #   return 'c'
    #else:
    #   return 'b'
    
    #if(justbetrayed):     #Complicated algorithm: checks for a point difference. If we're losing or the point difference is zero, betray. If we just betrayed, we can expect a betrayal, so betray again. If we're ahead, collude, since it's probably safe to. 
    #   justbetrayed = False
    #   return 'b'
    #   
    #elif((my_score - their_score) <= 0):
    #   justbetrayed = True
    #   return 'b'
    #elif(my_score - their_score >= 0):
    #   return 'c'
    
    for i in 4: #Use complex algorithm but start off with collude, collude, betray, collude
        if i == 0 or i == 1 or i == 3:
            if justbetrayed:
                justbetrayed = False
            return 'c'
        elif i == 2:
            return 'b'
            justbetrayed = True
    if(justbetrayed):
       return 'b'
    elif((my_score - their_score) <= 0):
       justbetrayed = True
       return 'b'
    elif(my_score - their_score >= 0):
       return 'c'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    
