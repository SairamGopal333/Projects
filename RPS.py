import random


def get_player_move():

    while True:
        player_input = input("Choose your move (rock, paper, scissors) or 'q' to quit: ").lower()
        if player_input in ['rock', 'paper', 'scissors', 'q']:
            return player_input
        else:
            print("Invalid move. Please choose rock, paper, scissors, or 'q'.")


def get_ai_move_random():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(player_move, ai_move):

    if player_move == ai_move:
        return "It's a tie!"
    elif (player_move == 'rock' and ai_move == 'scissors') or \
            (player_move == 'paper' and ai_move == 'rock') or \
            (player_move == 'scissors' and ai_move == 'paper'):
        return "You win!"
    else:
        return "AI wins!"


def play_game_with_prediction():

    player_history = []
    patterns = {}

    score_player = 0
    score_ai = 0
    score_ties = 0

    print("--- Welcome to Unbeatable Rock, Paper, Scissors! ---")
    print("Try to beat the AI that learns from your patterns!")

    while True:
        print("\n--- New Round ---")
        player_move = get_player_move()

        if player_move == 'q':
            break

        ai_move = get_ai_move_random()

        if len(player_history) >= 1:
            last_player_move = player_history[-1]


            if last_player_move in patterns:

                possible_next_moves_counts = patterns[last_player_move]

                if possible_next_moves_counts:
                    most_frequent_next_move = max(possible_next_moves_counts,
                                                  key=possible_next_moves_counts.get)


                    if most_frequent_next_move == 'rock':
                        ai_move = 'paper'
                    elif most_frequent_next_move == 'paper':
                        ai_move = 'scissors'
                    elif most_frequent_next_move == 'scissors':
                        ai_move = 'rock'

                    print(f"(AI thinks you'll play {most_frequent_next_move} next!)")

        print(f"You chose: {player_move}")
        print(f"AI chose: {ai_move}")

        result = determine_winner(player_move, ai_move)
        print(result)

        if result == "You win!":
            score_player += 1
        elif result == "AI wins!":
            score_ai += 1
        else:
            score_ties += 1


        if len(player_history) >= 1:

            last_move_for_pattern_update = player_history[-1]

            if last_move_for_pattern_update not in patterns:
                patterns[last_move_for_pattern_update] = {}

            patterns[last_move_for_pattern_update][player_move] = \
                patterns[last_move_for_pattern_update].get(player_move, 0) + 1

        player_history.append(player_move)

        print(f"Score: You {score_player} - AI {score_ai} - Ties {score_ties}")


    print("\n--- Game Over ---")
    print(f"Final Score: You {score_player} - AI {score_ai} - Ties {score_ties}")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_game_with_prediction()