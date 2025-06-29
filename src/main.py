from readQR import readQR
from createBoard import createBoard
from visualizeBoard import visualizeBoard
from findPath import findPath

def main():
    qr_data = readQR()
    board_type, board_height = createBoard(qr_data)
    visualizeBoard(board_type, board_height)
    path = findPath(board_type, board_height)
    print(path)


if __name__ == "__main__":
    main()