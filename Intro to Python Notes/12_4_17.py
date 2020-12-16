class Scoreboard(object):
    def __init__(self, Team1_name='team1', Team2_name='team2', Team1_score=0, Team2_score=0):
         self.Team1_name = Team1_name
         self.Team2_name = Team2_name
         self.Team1_score = Team1_score
         self.Team2_score = Team2_score

    def winning(self, higher_is_better=True):
        if higher_is_better:
            if self.Team1_score > self.Team2_score:
                return self.Team1_name
            elif self.Team2_score > self.Team1_score:
                return self.Team2_name
            else:
                return "Tied"
        else:
            if self.Team1_score > self.Team2_score:
                return self.Team2_name
            elif self.Team2_score > self.Team1_score:
                return self.Team1_name
            else:
                return "Tied"



    def __repr__(self):
        return self.Team1_name + ":" + str(self.Team1_score) + " " + self.Team2_name + ":" + str(self.Team2_score)


my_scoreboard = Scoreboard(Team1_name="josh", Team2_name="bob", Team1_score=1, Team2_score=2)

print(my_scoreboard)