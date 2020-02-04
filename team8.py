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
    
global justbetrayed #boolean for one of the strategy to indicate that we've just betrayed.   
justbetrayed = False 
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    global justbetrayed
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    #return 'c'
    
    
    #if(len(my_history) < 3):
     #   return 'c'
    #else:
    #    return 'b'
    #Other possible strategies
    #if(len(my_history) == 1):
    #   return 'c'
    #else:
    #   return 'b'
    
    
    '''if(len(my_history) == 0):
       return 'c'
    else:
       return 'b'
    '''
    #if(justbetrayed):
    #   justbetrayed = False
    #   return 'b'
    #   
    #elif((my_score - their_score) <= 0):
    #   justbetrayed = True
    #   return 'b'
    #elif(my_score - their_score >= 0):
    #   return 'c'
    
      
    for i in range(0,4): #Use complex algorithm but start off with collude, collude, betray, collude
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
