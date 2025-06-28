from pyzbar.pyzbar import decode
from PIL import Image

# QRコード画像のパス
image_path = "Image_20250627_235502_375.jpeg"

# 画像を開く
image = Image.open(image_path)

# QRコードをデコード
decoded_objects = decode(image)

# 結果を表示
for obj in decoded_objects:
    print("タイプ:", obj.type)
    print("データ:", obj.data.decode('utf-8'))

