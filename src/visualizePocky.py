from PIL import Image

def visualizePocky(operations, resize_height=50, margin=0):
    # 操作に対応する画像ファイル名
    image_map = {
        'R': 'figs/right.png',
        'D': 'figs/down.png',
        'L': 'figs/left.png',
        'U': 'figs/up.png'
    }

    # 画像を読み込んでリサイズ
    images = []
    for op in operations:
        img = Image.open(image_map[op])
        ratio = resize_height / img.height
        resized_img = img.resize((int(img.width * ratio), resize_height))
        images.append(resized_img)

    # 合計幅 = 画像幅の合計 + 間のマージン合計
    total_width = sum(img.width for img in images) + margin * (len(images) - 1)
    height = resize_height

    # 空の画像を作成
    result = Image.new("RGBA", (total_width, height), (255, 255, 255, 0))  # 透明背景

    # 貼り付け
    x_offset = 0
    for i, img in enumerate(images):
        result.paste(img, (x_offset, 0))
        x_offset += img.width + margin

    result.show()
    # result.save("pocky_path.png")
