# 🧵 Garment Accounting & Production Dashboard

Dashboard analitik berbasis Web yang dirancang khusus untuk manajemen industri garmen. Aplikasi ini membantu memantau kesehatan finansial, efisiensi produksi, dan distribusi biaya secara real-time.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Fitur Utama
* **KPI Metrics**: Pantau Pendapatan, Biaya, dan Profit secara instan dengan indikator performa.
* **Analisis Produksi**: Grafik perbandingan Target vs Realisasi produksi bulanan.
* **Struktur Biaya**: Visualisasi distribusi pengeluaran (Bahan Baku, Gaji, dll) menggunakan Donut Chart.
* **Filter Interaktif**: Filter data berdasarkan bulan untuk analisis yang lebih spesifik.
* **Format Rupiah**: Tabel keuangan yang sudah terformat otomatis dalam mata uang Rupiah.
* **Ekspor Excel**: Unduh data yang telah difilter ke format `.xlsx` dengan satu klik.
* **Dark Mode Support**: Tampilan elegan yang nyaman di mata baik dalam mode terang maupun gelap.

## 🚀 Teknologi yang Digunakan
* **Python**: Bahasa pemrograman utama.
* **Streamlit**: Framework untuk membangun antarmuka web.
* **Pandas**: Untuk pengolahan dan manipulasi data tabel.
* **Plotly**: Library untuk grafik interaktif yang modern.
* **Openpyxl**: Engine untuk pembuatan laporan Excel.

## 🛠️ Instalasi Lokal

1.  **Clone Repositori**
    ```bash
    git clone [https://github.com/username-anda/dashboard-akuntansi-garmen.git](https://github.com/username-anda/dashboard-akuntansi-garmen.git)
    cd dashboard-akuntansi-garmen
    ```

2.  **Buat Virtual Environment (Opsional tapi Disarankan)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
    ```

3.  **Instalasi Library**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi**
    ```bash
    streamlit run app.py
    ```

## 📂 Struktur File
* `app.py`: Kode utama aplikasi Streamlit.
* `requirements.txt`: Daftar pustaka Python yang diperlukan.
* `.streamlit/config.toml`: Konfigurasi tema (Dark Mode default).

## 📊 Tampilan Dashboard
Dark Mode
<img width="1916" height="1070" alt="image" src="https://github.com/user-attachments/assets/afbcdf34-f6c3-4799-a332-12676522bb31" />
Light Mode
<img width="1913" height="1067" alt="image" src="https://github.com/user-attachments/assets/7a35d589-c563-41c1-b877-3c224aa3a3fe" />



## 📝 Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detailnya.

---
Dibuat dengan ❤️ untuk efisiensi industri Garmen.
