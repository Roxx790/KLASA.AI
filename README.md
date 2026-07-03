# 🗑️ KLASA.AI
### Smart Waste Classifier untuk Pemilahan Sampah Otomatis

## 📖 Deskripsi

KLASA.AI merupakan sistem berbasis Artificial Intelligence (AI) yang dikembangkan untuk mendeteksi dan mengklasifikasikan jenis sampah secara otomatis menggunakan metode Object Detection YOLO. Sistem ini membantu proses pemilahan sampah agar lebih cepat, akurat, dan efisien.

---

## ✨ Fitur

- Deteksi objek sampah menggunakan AI.
- Klasifikasi berbagai jenis sampah.
- Deteksi melalui gambar.
- Deteksi secara real-time menggunakan webcam.
- Menggunakan model hasil training YOLO.

---

## 🛠️ Teknologi

- Python 3.12
- PyTorch
- Ultralytics YOLO
- OpenCV
- Roboflow
- Google Colab
- Visual Studio Code

---

# 🚀 Instalasi

## 1. Clone Repository

```bash
git clone https://github.com/Roox790/KLASA.AI.git
```

Masuk ke folder proyek

```bash
cd KLASA.AI
```

---

## 2. Membuat Virtual Environment

Windows

```bash
python -m venv yolo
```

Aktifkan Virtual Environment

Command Prompt

```bash
yolo\Scripts\activate
```

PowerShell

```bash
.\yolo\Scripts\Activate.ps1
```

Jika berhasil akan muncul

```bash
(yolo)
```

di awal terminal.

---

## 3. Upgrade Pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install PyTorch

### CPU

```bash
pip install torch torchvision torchaudio
```

### NVIDIA GPU (CUDA)

Silakan sesuaikan dengan versi CUDA yang digunakan. Contoh:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

---

## 5. Install Library Lainnya

```bash
pip install ultralytics opencv-python numpy
```

Atau jika tersedia

```bash
pip install -r requirements.txt
```

---

# ▶️ Menjalankan Program

Pastikan file model

```
KLASA.pt
```

berada di dalam folder proyek.

### Menjalankan Deteksi

```bash
python main.py
```

Apabila menggunakan webcam, kamera akan terbuka secara otomatis.

Tekan tombol berikut:

- **Q** → Keluar dari program.
- **S** *(jika tersedia pada program)* → Menyimpan hasil deteksi.

---

# 📁 Struktur Folder

```
KLASA.AI
│
├── model/
│   └── KLASA.pt
│
├── dataset/
│
├── hasil/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset diperoleh dari Roboflow kemudian melalui tahapan:

- Pengumpulan data
- Labeling
- Data preprocessing
- Training menggunakan YOLO
- Validasi model
- Pengujian model

---

# 🤖 Model AI

Model dilatih menggunakan Ultralytics YOLO dan menghasilkan file:

```
KLASA.pt
```

Model digunakan untuk mendeteksi objek sampah sesuai kelas yang telah dilatih.

---

# 👨‍💻 Pengembang

**Invictus Team**  
**LKS Artificial Intelligence**  
**SMK Swadhipa 2 Natar**

KLASA.AI dikembangkan oleh **Invictus Team** dari **SMK Swadhipa 2 Natar** sebagai implementasi teknologi Artificial Intelligence berbasis YOLO untuk mendeteksi dan mengklasifikasikan sampah secara otomatis guna mendukung pengelolaan sampah yang lebih efektif dan efisien.
---

# 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran, penelitian, dan pengembangan.
