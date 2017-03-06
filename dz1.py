import random
from math import log2


def create_teamlist(names, teamlist):
    for name in names:
        team = dict.fromkeys(['name', 'opponents', 'scores', 'is_out'])
        team['name'], team['is_out'] = name, 0
        team['opponents'], team['scores'] = list(), list()
        teamlist.append(team)


def make_pairs(teamlist):
    team_amount = len(teamlist)
    for i in range(0, (team_amount - 2)):
        swap_team_idx = random.randint(i, team_amount - 1)
        if(swap_team_idx != i):
            teamlist[i], teamlist[swap_team_idx] = teamlist[swap_team_idx], teamlist[i]


def matchmaking(team1, team2):
    team1_score = random.randint(0, 7)
    team2_score = random.randint(0, 7)
    if(team1_score == team2_score):
        winner = random.randint(0, 1)
        if(winner):
            team2_score += 1
        else:
            team1_score += 1
    team1['opponents'].append(team2['name'])
    team1['scores'].append(team1_score)
    team2['opponents'].append(team1['name'])
    team2['scores'].append(team2_score)


def print_playoff_grid(teamlist, step):
    team_amount = len(teamlist)
    grid_step = (step) * 2
    print('STAGE: 1/%d\n' % int(team_amount / grid_step))
    for i in range(0, team_amount, grid_step):
        print('%s (%d : %d) %s\t' % (teamlist[i]['name'],
                                     teamlist[i]['scores'][-1],
                                     teamlist[i + step]['scores'][-1],
                                     teamlist[i + step]['name']))
    print('--------------------------------------------------------\n')


def playoff(teamlist):
    team_amount = len(teamlist)
    for stage in range(int(log2(team_amount))):
        step = int(pow(2, stage))
        for i in range(0, team_amount, (step * 2)):
            matchmaking(teamlist[i], teamlist[i + step])
            if(teamlist[i + step]['scores'][-1] > teamlist[i]['scores'][-1]):
                teamlist[i], teamlist[i + step] = teamlist[i + step], teamlist[i]
            teamlist[i + step]['is_out'] = step
        print_playoff_grid(teamlist, step)


def print_winner(teamlist):
    for team in teamlist:
        if(team['is_out'] == 0):
            print('THE WINNER IS %s!\n' % team['name'])


if __name__ == '__main__':
    team_names = ['team_A', 'team_B', 'team_C', 'team_D', 'team_E', 'team_F',
                  'team_G', 'team_H', 'team_I', 'team_J', 'team_K', 'team_L',
                  'team_M', 'team_N', 'team_O', 'team_P']
    teams = list()
    create_teamlist(team_names, teams)
    make_pairs(teams)
    playoff(teams)
    print_winner(teams)
