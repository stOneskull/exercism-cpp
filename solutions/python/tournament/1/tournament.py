def tally(tournament_results):
    table = dict(
        titles=['Team', 'MP', 'W', 'D', 'L', 'P']
        )
    title = create_line(table['titles'])
    lines = tournament_results.split('\n')
    for line in lines:
        table = calc(line, table)
    print(table)
    return table_out(table)


def calc(line, table):
    team1, team2, result = line.split(';')

    if team1 not in table:
        table[team1] = [team1, 0, 0, 0, 0, 0]
    if result == 'draw':
        table[team1][1] += 1
        table[team1][3] += 1
        table[team1][5] += 1
    elif result == 'loss':
        table[team1][1] += 1
        table[team1][4] += 1
    else:
        table[team1][1] += 1
        table[team1][2] += 1
        table[team1][5] += 3

    if team2 not in table:
        table[team2] = [team2, 0, 0, 0, 0, 0]
    if result == 'draw':
        table[team2][1] += 1
        table[team2][3] += 1
        table[team2][5] += 1
    elif result == 'win':
        table[team2][1] += 1
        table[team2][4] += 1
    else:
        table[team2][1] += 1
        table[team2][2] += 1
        table[team2][5] += 3

    return table


def create_line(titles):
    team, played, win, draw, loss, points = titles
    line = ' '.join(titles)
    print(line)
    return line


def table_out(table):
    output = (line + '\n' for line in table)
    print(output)
    return output
