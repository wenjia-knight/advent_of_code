'''
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
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
    'X': 'loose',
    'Y': 'draw',
    'Z': 'win'
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
    target_outcome = shapes[one_round[2]]

    if (opponent_shape, target_outcome) in [('Rock', 'draw'), ('Paper', 'loose'), ('Scissors', 'win')]:
        return outcome_score[target_outcome] + your_shape_score['Rock']
    elif (opponent_shape, target_outcome) in [('Rock', 'win'), ('Paper', 'draw'), ('Scissors', 'loose')]:
        return outcome_score[target_outcome] + your_shape_score['Paper']
    else:
        return outcome_score[target_outcome] + your_shape_score['Scissors']

def calculate_sum():
    rounds = get_rounds('input.txt')
    sum = 0
    for round in rounds:
        sum += score_per_round(round)
    return sum

print(calculate_sum())