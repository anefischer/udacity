
from sample_players import DataPlayer
from isolation import Isolation, DebugState

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
            
    
        #self.queue.put(random.choice(state.actions()))
        # code from sample_players.py
        # 1: 
        # 2:  
        # 3: 54%        ID: 52%
        # 4: 56%        ID: 48%
        # 5: 59%        ID: 59%
        # 6: 57.0%      ID; 68%
        # 7:            ID: 77%
        # 8:            ID: 73%
        # 9:                        ID+OB: 76%
        
        #self.data = []
        if state.ply_count <= 4 and state.board in self.data:
            self.queue.put(self.data[state.board])
        elif state.ply_count <= 2:           
            self.queue.put(random.choice(state.actions()))
        else:
            # Turns out "iterative deepening" is just a for loop...
            depth_limit = 12
            for depth in range(1, depth_limit+1):
                self.queue.put(self.alpha_beta_search(state, depth=depth))

    # from sample_players.py wodified for alpha and beta accourding to lectures
    def alpha_beta_search(self, state, depth):
 
        # pseudocode refactored to duplicade the min/max from sample_players.py
        
        def min_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:   
                    break # (* α cutoff *)
            return value

        def max_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)
            if depth <= 0: return self.score(state)
            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break # (* β cutoff *)
            return value

        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1,float("-inf"),float("inf")))
    
    # evaluation function
    # from sample_players.py
    def score(self, state):
        #my_moves - #opponent_moves
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        return len(own_liberties) - len(opp_liberties)
    