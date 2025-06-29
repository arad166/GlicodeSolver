import tkinter as tk

symbol_to_emoji = {
    '0': '🈳',   # 空白（全角スペース）
    '1': '　',   # 平地
    '2': '🐻',   # ハグハグ
    '3': '👦',   # 男の子
    '4': '🪨',   # 岩
    '5': '🌳',   # 木
    '6': '💧',   # 水
    '7': '🌀',   # ジャンプ台
    '8': '⬆️',  # 上コンベア
    '9': '➡️',  # 右コンベア
    'a': '⬇️',  # 下コンベア
    'b': '⬅️',  # 左コンベア
    'c': '🧊',   # 氷
    'd': '🔸',   # 赤スイッチ
    'e': '🔶',   # 赤ブロック(ON)
    'f': '🔶',   # 赤ブロック(OFF)
    'g': '◻️',   # 青スイッチ
    'h': '⬜',   # 青ブロック(ON)
    'i': '⬜',   # 青ブロック(OFF)
    'q': '♈',   # 赤ワープ（ドアで統一）
    'r': '♉',   # 黄ワープ
    's': '♊',   # 緑ワープ
    't': '♋',   # 青ワープ
    'u': '♌',   # 茶ワープ
    'w': '👧'    # 女の子
}

def height_to_color(h):
    # 高さに応じたグレー濃度を返す
    gray = 255 - h * 40
    gray = max(0, min(255, gray))
    return f'#{gray:02x}{gray:02x}{gray:02x}'

def draw_board(board_type, board_height, canvas, cell_size=60):
    for i in range(len(board_height)):
        for j in range(len(board_height[0])):
            h = int(board_height[i][j])
            emoji = symbol_to_emoji[board_type[i][j]]
            color = height_to_color(h)
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # 四角を描画
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

            # 絵文字を中央に描画
            canvas.create_text(
                (x1 + x2) // 2,
                (y1 + y2) // 2,
                text=emoji,
                font=("Arial", int(cell_size * 0.5))
            )

def visualizeBoard(board_type, board_height):
    # ウィンドウとキャンバス
    root = tk.Tk()
    cell_size = 60
    canvas = tk.Canvas(root, width=len(board_type[0]) * cell_size, height=len(board_type) * cell_size)
    canvas.pack()

    draw_board(board_type, board_height, canvas, cell_size)
    root.mainloop()