'''
For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
'''

def get_rounds(input):
    with open(input) as file:
        lines = file.readlines()
        rounds = [line.strip() for line in lines]
        return rounds

def score_per_round(one_round):
    shapes = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

    your_shape_score = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3
    }

    outcome_score = {
        'win': 6,
        'loose': 0,
        'draw': 3
    }
    opponent_shape = shapes[one_round[0]]
    your_shape = shapes[one_round[2]]
    if opponent_shape == your_shape:
        return outcome_score['draw'] + your_shape_score[your_shape]
    elif (opponent_shape, your_shape) in [('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors', 'Rock')]:
        return outcome_score['win'] + your_shape_score[your_shape]
    else:
        return outcome_score['loose'] + your_shape_score[your_shape]

def calculate_sum():
    rounds = get_rounds('input.txt')
    sum = 0
    for round in rounds:
        sum += score_per_round(round)
    return sum

print(calculate_sum())