import cv2
import insightface
import numpy as np

# 載入模型
model = insightface.app.FaceAnalysis()
model.prepare(ctx_id=0, det_thresh=0.5)  # det_thresh可以自己調

# 讀取基準圖片
reference_img = cv2.imread('A.png')
if reference_img is None:
    print("❗ 錯誤：找不到基準圖片，請檢查路徑！")
    exit()

# 轉RGB
reference_rgb = reference_img[:, :, ::-1]
# 偵測基準圖片中的人臉
ref_faces = model.get(reference_rgb)
if len(ref_faces) == 0:
    print("❗ 錯誤：基準圖片中沒有偵測到人臉！")
    exit()

# 取出第一張臉的特徵（embedding）
ref_embedding = ref_faces[0].embedding

# 打開攝影機
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❗ 錯誤：無法開啟攝影機！")
    exit()

print("✅ 開始偵測，按 Q 鍵結束。")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❗ 錯誤：攝影機讀取失敗")
        break

    rgb_frame = frame[:, :, ::-1]
    faces = model.get(rgb_frame)

    for face in faces:
        box = face.bbox.astype(int)
        embedding = face.embedding

        # 比對基準臉和現在這張臉
        distance = np.linalg.norm(ref_embedding - embedding)  # L2距離
        threshold = 1.0  # 這個值可以自己調整，越小越嚴格

        if distance < threshold:
            text = f"Same Person ({distance:.2f})"
            color = (0, 255, 0)  # 綠色
        else:
            text = f"Different ({distance:.2f})"
            color = (0, 0, 255)  # 紅色

        # 畫方框 + 顯示文字
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), color, 2)
        cv2.putText(frame, text, (box[0], box[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # 顯示結果
    cv2.imshow('Face Recognition', frame)

    # 按 Q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 收尾
cap.release()
cv2.destroyAllWindows()
