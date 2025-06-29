from readQR import readQR
from createBoard import createBoard

def main():
    qr_data = readQR()
    board_type, board_height = createBoard(qr_data)
    print(board_type)


if __name__ == "__main__":
    main()