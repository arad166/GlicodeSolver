import tkinter as tk

# 高さデータ
height_map = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
]

# マスごとの絵文字（同じサイズ）
emoji_map = [
    ["🌱", "🌿", "🌳", "🌲"],
    ["🐛", "🐞", "🐝", "🦋"],
    ["🐌", "🪲", "🪳", "🦗"],
    ["🐍", "🦎", "🐢", "🐊"]
]

def height_to_color(h):
    # 高さに応じたグレー濃度を返す
    gray = 255 - h * 30
    gray = max(0, min(255, gray))
    return f'#{gray:02x}{gray:02x}{gray:02x}'

def draw_board(canvas, cell_size=60):
    for i in range(len(height_map)):
        for j in range(len(height_map[0])):
            h = height_map[i][j]
            emoji = emoji_map[i][j]
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

# ウィンドウとキャンバス
root = tk.Tk()
canvas_size = 4 * 60
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

draw_board(canvas)
root.mainloop()
