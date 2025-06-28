import cv2
from pyzbar.pyzbar import decode

def readQR():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("カメラが見つかりません")
        return None

    window_name = "QR Reader"
    cv2.namedWindow(window_name)

    print("QRコードを読み取っています。QRコードをかざしてください...")

    qr_data = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # QRコードの検出と描画
        decoded_objects = decode(frame)
        if decoded_objects:
            obj = decoded_objects[0]
            qr_data = obj.data.decode("utf-8")
            print(f"検出されたQRコード: {qr_data}")

            # 四角形を描く
            points = obj.polygon
            if len(points) == 4:
                pts = [(p.x, p.y) for p in points]
                for i in range(4):
                    cv2.line(frame, pts[i], pts[(i+1)%4], (0, 255, 0), 2)

            cv2.imshow(window_name, frame)
            cv2.waitKey(1000)
            break

        # ウィンドウの表示と状態確認
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF

        # 'q' キーで終了
        if key == ord("q"):
            break

        # ウィンドウが閉じられたら終了（-1は閉じられた状態）
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            print("ウィンドウが閉じられました")
            break

    cap.release()
    cv2.destroyAllWindows()
    return qr_data

if __name__ == "__main__":
    readQR()
