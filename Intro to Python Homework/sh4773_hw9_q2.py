# 2

import random


def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1, name2)
    game1.play()


class Die(object):
    def __init__(self, faces=6):
        self.number_of_faces = faces
        self.curr_face_value = 0

    def __repr__(self):
        return str(self.curr_face_value)

    def roll(self):
        self.curr_face_value = random.randint(1, self.number_of_faces)


class PigGamePlayer(object):
    def __init__(self, name):
        self.name = name
        self.die = Die()
        self.score = 0

    def play_turn(self):
        print("\n", self.name + "'s turn:", sep='')
        temp_points = 0
        while True:
            self.die.roll()
            print("You rolled", self.die.curr_face_value)
            if self.die.curr_face_value == 1:
                temp_points = 0
                break
            else:
                temp_points += self.die.curr_face_value
                print("Your score for this turn is:", temp_points)
                roll_status = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                if roll_status == 'h':
                    break
                elif roll_status == 'r':
                    pass
                else:
                    print("That isn't a valid response, so we'll roll again.")
        self.score += temp_points
        print("You scored", temp_points, "points this turn. Your total score is", self.score)


class PigGame(object):
    def __init__(self, player1_name, player2_name):
        self.player1 = PigGamePlayer(player1_name)
        self.player2 = PigGamePlayer(player2_name)

    def play(self):
        while True:
            self.player1.play_turn()
            if self.player1.score >= 100:
                print(self.player1.name, "won!")
                break
            self.player2.play_turn()
            if self.player2.score >= 100:
                print(self.player2.name, "won!")
                break


main()

