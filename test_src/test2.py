import cv2
from pyzbar.pyzbar import decode

def main():
    # カメラを起動（通常はデバイスID 0）
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("カメラが見つかりません")
        return

    print("QRコードを読み取っています。'q'を押すと終了します。")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # QRコードを検出・デコード
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # デコードされたデータを表示
            qr_data = obj.data.decode("utf-8")
            print(f"検出されたQRコード: {qr_data}")

            # 四角形を描画
            points = obj.polygon
            if len(points) == 4:
                pts = [(p.x, p.y) for p in points]
                for i in range(4):
                    cv2.line(frame, pts[i], pts[(i+1)%4], (0, 255, 0), 2)

        # 映像を表示
        cv2.imshow("QRコードリーダー", frame)

        # 'q'で終了
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
