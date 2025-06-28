from readQR import readQR
from createBoard import createBoard

def main():
    qr_data = readQR()
    board_type, board_height = createBoard(qr_data)

if __name__ == "__main__":
    main()