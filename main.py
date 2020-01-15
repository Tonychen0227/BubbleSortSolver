import sys
from game_components import Board, Ball, Tube


def main():
    # print command line arguments
    board = Board()
    if not board.initialize(sys.argv[1]):
        print("An error occurred, game will NOW EXIT")
        return

    if not board.verify_integrity():
        print("Board integrity has been violated. Game will NOW EXIT")
        return

    print("Valid beginning board found!")
    board.print()


if __name__ == "__main__":
    main()
