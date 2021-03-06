####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Seven !' # Only 10 chars displayed.
strategy_name = 'if they nice, we nice'
strategy_description = 'we will only be nice if they are nice two times in a row.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if my_history == '':
        return 'c'
    else: 
        if their_history[-1] == 'b':
            helper(my_score, their_score)
        else:
            if their_history[-2] == 'c' :
                return 'c'
            else:
                'b'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'


def helper(my_score, their_score):
    if int(their_score) - int(my_score) >= 600:
        return 'b'
    else:
        return 'c'