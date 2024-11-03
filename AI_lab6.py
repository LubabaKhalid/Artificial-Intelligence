class AlphaBetaPruning:
    def __init__(self, depth, game_state, player):
        self.depth = depth
        self.game_state = game_state
        self.player = player  

    def is_terminal(self, state):
        winning_conditions = [
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],
            [state[2], state[4], state[6]],
        ]
        if ['X', 'X', 'X'] in winning_conditions:
            return True, 1  
        elif ['O', 'O', 'O'] in winning_conditions:
            return True, -1  
        elif ' ' not in state:
            return True, 0  
        return False, None  

    def utility(self, state):
        terminal, value = self.is_terminal(state)
        if terminal:
            return value
        return None  

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        score = self.utility(state)
        if score is not None:  
            return score

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(len(state)):
                if state[i] == ' ':
                    state[i] = 'X'  
                    eval = self.alphabeta(state, depth - 1, alpha, beta, False)
                    state[i] = ' '  
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(len(state)):
                if state[i] == ' ':
                    state[i] = 'O'  
                    eval = self.alphabeta(state, depth - 1, alpha, beta, True)
                    state[i] = ' '  
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  
            return min_eval

    def best_move(self, state):
        best_eval = float('-inf')
        move = -1
        alpha = float('-inf')
        beta = float('inf')
        for i in range(len(state)):
            if state[i] == ' ':
                eval = self.alphabeta(state, self.depth - 1, alpha, beta, False)
                state[i] = ' '  
                if eval > best_eval:
                    best_eval = eval
                    move = i
        return move

def play_game():
    state = [' '] * 9  
    player = 'X'  
    ai = AlphaBetaPruning(depth=5, game_state=state, player=player)

    while True:
        if player == 'X':
            move = ai.best_move(state)
            state[move] = 'X'
        else:
            move = int(input("Enter your move (0-8): "))
            if state[move] == ' ':
                state[move] = 'O'
            else:
                print("Invalid move! Try again.")
                continue

        terminal, score = ai.is_terminal(state)
        if terminal:
            if score == 1:
                print("AI wins!")
            elif score == -1:
                print("You win!")
            else:
                print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'
        print("Current Board:")
        print(state[:3])
        print(state[3:6])
        print(state[6:])

play_game()
