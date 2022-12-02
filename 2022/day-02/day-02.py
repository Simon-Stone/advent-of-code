import pandas as pd


# Part 1

def match_score(shape):
    loses_vs = {'X': 'C', 'Y': 'A', 'Z': 'B'}  # Value loses against key
    wins_vs = {'X': 'B', 'Y': 'C', 'Z': 'A'}   # Value wins against key

    if shape['opponent'] == wins_vs[shape['me']]:
        return 0

    if shape['opponent'] == loses_vs[shape['me']]:
        return 6

    return 3


rps = pd.read_csv('2022/day-02/input.txt', names=['opponent', 'me'], 
                  header=None, delimiter=' ')

rps['match_score'] = rps.apply(match_score, axis='columns')
rps['shape_score'] = rps.me.map({'X': 1, 'Y': 2, 'Z': 3})

print(rps[['match_score', 'shape_score']].sum().sum())


# Part 2
def find_shape(match):
    loses_vs = {'A': 'C', 'B': 'A', 'C': 'B'}  # Value loses against key
    wins_vs = {'A': 'B', 'B': 'C', 'C': 'A'}   # Value wins against key
    if match.result == 'X':
        return loses_vs[match['opponent']]
    if match.result == 'Y':
        return match['opponent']
    if match.result == 'Z':
        return wins_vs[match['opponent']]


rps = pd.read_csv('2022/day-02/input.txt', names=['opponent', 'result'], 
                  header=None, delimiter=' ')

rps['me'] = rps.apply(find_shape, axis='columns')
rps['match_score'] = rps['result'].map({'X': 0, 'Y': 3, 'Z': 6})
rps['shape_score'] = rps['me'].map({'A': 1, 'B': 2, 'C': 3})
                                   
print(rps[['match_score', 'shape_score']].sum().sum())