import re

def createBoard(qr_data):
    # 正規表現で s= の後ろだけ抽出
    match = re.search(r"s=(.+)", qr_data)
    s_qr = None

    if match:
        s_qr = match.group(1)
    else:
        print("有効なQRコードではありません")
        return
    
    w = int(s_qr[3])
    s_qr = s_qr[4:]
    assert(len(s_qr) % w == 0)
    assert(len(s_qr) % 2 == 0)
    hw = len(s_qr)//2
    h = hw // w

    board_type = [[0 for _ in range(w)] for _ in range(h)]
    board_height = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            board_type[i][j] = s_qr[i*w*2+j*2]
            board_height[i][j] = s_qr[i*w*2+j*2+1]
    
    return board_type, board_height

    