# Bike Sharing Data Analysis Dashboard
Proyek ini bertujuan untuk menganalisis dataset **Bike Sharing** dan menampilkan hasil analisis dalam bentuk **dashboard interaktif menggunakan Streamlit**.

Dataset berisi informasi jumlah penyewaan sepeda berdasarkan waktu, musim, serta kondisi cuaca.

## Struktur Proyek

```
submission
├── dashboard
│   ├── dashboard.py
│   └── main_data.csv
├── data
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Setup Environment

Buat virtual environment

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### MacOS / Linux

```
python -m venv venv
source venv/bin/activate
```

## Install Library

Install semua library yang dibutuhkan menggunakan file `requirements.txt`.

```
pip install -r requirements.txt
```

## Menjalankan Dashboard

Jalankan perintah berikut di terminal:

```
streamlit run dashboard/dashboard.py
```

Dashboard akan berjalan di browser pada alamat:

```
http://localhost:8501
```

## Dataset

Dataset yang digunakan dalam proyek ini adalah **Bike Sharing Dataset** yang berisi informasi penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca.

## Author

Nama: **Rahma Ayu Cindikiawati**
