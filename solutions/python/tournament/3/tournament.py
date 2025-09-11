class Team:
    titles = ['Team', 'MP', 'W', 'D', 'L', 'P']
    teams = {}

    def __init__(self, name):
        Team.teams[name] = self
        self.name = name
        self.played, self.points = 0, 0
        self.won, self.drawn, self.lost = 0, 0, 0
        

def create_line(entries):
    form = '{:<31}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'
    return form.format(*entries)


def tally(results):
    output = []
    output.append(create_line(Team.titles))
    if not results: return output

    for line in results: calc(line)

    sorted_teams = sorted(
        [(name, team_ob, team_ob.points)
        for name, team_ob in Team.teams.items()]
    )
    
    sorted_teams = [
        v[1] for v in sorted(
        sorted_teams, key=lambda v: v[2], reverse=True
        )
    ]

    for team in sorted_teams:
        entries = [team.name, team.played, team.won,
            team.drawn, team.lost, team.points]
        output.append(create_line(entries))

    Team.teams = {}

    return output


def calc(line):
    team1, team2, result = line.split(';')

    for team in team1, team2:
        if team not in Team.teams:
            Team(team)

    for team in team1, team2:
        team = Team.teams[team]
        team.played += 1

        if result == 'draw':
            team.drawn += 1
            team.points += 1

        elif team.name == team1:
            if result == 'win':
                    team.won += 1
                    team.points += 3
                    Team.teams[team2].lost += 1
            elif result == 'loss':
                    team.lost += 1
                    Team.teams[team2].won += 1
                    Team.teams[team2].points += 3
