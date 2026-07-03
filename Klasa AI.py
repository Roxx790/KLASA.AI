from ultralytics import YOLO
import cv2

# Muat model
model = YOLO("modelKLASA.pt")


def deteksi_gambar(path_gambar):
    hasil = model(path_gambar)

    for r in hasil:
        if len(r.boxes) > 0:
            idx = r.boxes.conf.argmax()
            r.boxes = r.boxes[idx:idx + 1]

        r.show()
        r.save(filename="hasil_deteksi.jpg")

    print("Hasil disimpan sebagai hasil_deteksi.jpg")


def deteksi_webcam(sumber=0):
    cap = cv2.VideoCapture(sumber)

    while cap.isOpened():
        sukses, frame = cap.read()
        if not sukses:
            break

        # Prediksi
        hasil = model(frame, conf=0.5)

        # Ambil hanya 1 objek dengan confidence tertinggi
        for r in hasil:
            if len(r.boxes) > 0:
                idx = r.boxes.conf.argmax()
                r.boxes = r.boxes[idx:idx + 1]

            frame = r.plot()

        cv2.imshow("Deteksi YOLO", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # deteksi_gambar("foto.jpg")
    deteksi_webcam()