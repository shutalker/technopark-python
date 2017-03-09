import random
from math import log2


def check_team_amount(team_amount):
    if log2(team_amount) - int(log2(team_amount)) != 0.0:
        print('Для проведения плэй-офф выбрано'\
              + 'недопустимое количество команд!')
        exit()


def create_teamlist(names, teamlist):
    for name in names:
        team = dict.fromkeys(['name', 'opponents', 'scores', 'is_out'])
        team['name'], team['is_out'] = name, 0
        team['opponents'], team['scores'] = list(), list()
        teamlist.append(team)


def make_pairs(teamlist, team_amount):
    for i in range(0, (team_amount - 2)):
        swap_team_idx = random.randint(i, team_amount - 1)
        if swap_team_idx != i:
            teamlist[i], teamlist[swap_team_idx] = teamlist[swap_team_idx], teamlist[i]


def matchmaking(team1, team2):
    team1_score = random.randint(0, 7)
    team2_score = random.randint(0, 7)
    if team1_score == team2_score:
        winner = random.randint(0, 1)
        if winner:
            team2_score += 1
        else:
            team1_score += 1
    team1['opponents'].append(team2['name'])
    team1['scores'].append((team1_score, team2_score))
    team2['opponents'].append(team1['name'])
    team2['scores'].append((team2_score, team1_score))


def print_playoff_grid(teamlist, step, team_amount):
    grid_step = (step) * 2
    print('Стадия плэй-офф: 1/%d\n' % int(team_amount / grid_step))
    for i in range(0, team_amount, grid_step):
        print('%s (%d : %d) %s' % (teamlist[i]['name'],
                                   teamlist[i]['scores'][-1][0],
                                   teamlist[i + step]['scores'][-1][0],
                                   teamlist[i + step]['name']))
    print('------------------------\n')


def playoff(teamlist, team_amount):
    for stage in range(int(log2(team_amount))):
        step = int(pow(2, stage))
        for i in range(0, team_amount, (step * 2)):
            matchmaking(teamlist[i], teamlist[i + step])
            if teamlist[i + step]['scores'][-1][0] > teamlist[i]['scores'][-1][0]:
                teamlist[i], teamlist[i + step] = teamlist[i + step], teamlist[i]
            teamlist[i + step]['is_out'] = step
        print_playoff_grid(teamlist, step, team_amount)


def show_playoff_winner(winner_team):
    print('Победитель - %s!\n' % winner_team['name'])


def show_team_names(teamlist):
    for idx, team in enumerate(teamlist):
        print('%d - %s' % ((idx + 1), team['name']))


def show_team_stat(team, team_amount):
    match_amount = len(team['opponents'])
    print('Название команды: %s\nКоманда сыграла %d раз(а)\nСоперники:' %
          (team['name'], match_amount))
    for match in range(match_amount):
        match_result = ''
        self_score = team['scores'][match][0]
        opponent_score = team['scores'][match][1]
        if self_score > opponent_score:
            match_result += 'победа'
        else:
            match_result += 'поражение'
        print('%s (%d : %d) - %s' % (team['opponents'][match],
                                     self_score, opponent_score, match_result))
    if team['is_out'] == 0:
        print('Эта команда - победитель турнира!')
    else:
        out_stage = int(team_amount / (team['is_out'] * 2))
        print('Эта команда выбыла на этапе: 1/%d' % out_stage)


def request_for_team_stats(teamlist, team_amount):
    replies = ['y', 'yes', 'n', 'no']
    request = ''
    teamlist_is_sorted = False
    while request.lower().strip() not in replies[2:]:
        request = input('Желаете ли вы просмотреть статистику команд? (y/n): ')
        if request not in replies[0:2]:
            continue
        if not teamlist_is_sorted:
            teamlist = sorted(teamlist, key=lambda team: team['name'])
            teamlist_is_sorted = True
        show_team_names(teamlist)
        choosen_team = int(input('Укажите номер команды, статистику которой'\
                                 + 'вы желаете просмотреть: ').strip())
        if choosen_team not in range(1, (team_amount + 1)):
            print('Выбранный Вами номер не соответсвует\
                  ни одной команде из списка! Повторите попытку выбора')
            continue
        show_team_stat(teamlist[choosen_team - 1], team_amount)


if __name__ == '__main__':
    team_names = ['team_A', 'team_B', 'team_C', 'team_D', 'team_E', 'team_F',
                  'team_G', 'team_H', 'team_I', 'team_J', 'team_K', 'team_L',
                  'team_M', 'team_N', 'team_O', 'team_P']
    team_amount = len(team_names)
    teams = list()
    check_team_amount(team_amount)
    create_teamlist(team_names, teams)
    make_pairs(teams, team_amount)
    playoff(teams, team_amount)
    show_playoff_winner(teams[0])
    request_for_team_stats(teams, team_amount)
