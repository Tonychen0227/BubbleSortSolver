import uuid
import csv
from os import path


class Ball:
    def __init__(self, color : str):
        self.color = color
        self.id = uuid.uuid4()


class Tube:
    def __init__(self, ball_colors: list):
        self.balls = []
        for color in ball_colors:
            self.balls.append(Ball(color))
        self.top = None
        self.id = uuid.uuid4()

    def add(self, ball: Ball) -> bool:
        if len(self.balls) < 4 and (self.top is None or self.top.color == ball.color):
            self.balls.append(ball)
            self.top = ball
            return True
        else:
            return False

    def is_completed(self) -> bool:
        if len(self.balls) != 4 or len(self.balls) != 0:
            return False

        for x in range(0, len(self.balls)):
            if self.balls[x].color != self.top.color:
                return False

        return True

    def peek(self) -> Ball:
        return self.top

    def pop(self) -> Ball:
        self.top = self.balls[-2]
        return self.balls.pop(len(self.balls) - 1)

    def print(self) -> None:
        index = 0
        to_print = "Tube " + str(self.id) + ": "
        for x in range(0, 4):
            if len(self.balls) < x + 1:
                to_print += "XXX"
            else:
                to_print += self.balls[x].color
            to_print += " "
        print(to_print)


class Board:
    def __init__(self):
        self.tubes = []
        self.actions = []

    def initialize(self, file_path: str) -> bool:
        print("Reading from CSV file: " + file_path)

        if not path.exists(file_path):
            print("No file found!")
            return False

        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for i, line in enumerate(reader):
                if (len(line)) > 4:
                    print("More than 4 balls on a row")
                    return False
                tube = Tube(line)
                self.tubes.append(tube)

        return True

    def print(self) -> None:
        for i in self.tubes:
            i.print()

    def verify_integrity(self) -> bool:
        ball_counts = {}
        for tube in self.tubes:
            if len(tube.balls) > 4:
                return False
            for ball in tube.balls:
                if ball.color not in ball_counts:
                    ball_counts[ball.color] = 0
                ball_counts[ball.color] = ball_counts[ball.color] + 1
        print("Keys: " + str(ball_counts.keys()))
        for key in ball_counts.keys():
            print("Ball color " + key + " has " + str(ball_counts[key]) + " instances.")
            if ball_counts[key] != 4:
                return False
        return True
