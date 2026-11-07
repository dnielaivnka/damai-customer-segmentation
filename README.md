# DaMai Coffee & Bakery · Tim DaMai

**Kasus:** 05 — Segmentasi Pelanggan UMKM  
**Aplikasi:** https://damai-customer-segmentation.streamlit.app/  
**Repositori:** https://github.com/dnielaivnka/damai-customer-segmentation  
**Video:** Belum tersedia

**Mata Kuliah:** Machine Learning (P4–P5)  
**Program Studi:** Mekatronika dan Kecerdasan Buatan  
**Universitas:** Universitas Pendidikan Indonesia  
**Tahun:** 2026

| Anggota | NIM | Bagian yang Dikerjakan |
|---|---|---|
| Daniela Ivanka Maydina Siringoringo  | 2401148 | Data cleaning, EDA, feature engineering, pemodelan dan evaluasi K-Means, pengembangan aplikasi Streamlit, pengujian sistem, serta dokumentasi |
| Muhamad Nurhidayat  | 2401404 | Data cleaning, EDA, feature engineering, pemodelan dan evaluasi K-Means |

## 1. Masalah dan Pengguna

DaMai Coffee & Bakery merupakan studi kasus UMKM fiktif di Bandung yang memiliki 10.000 pelanggan dengan karakteristik dan perilaku transaksi yang beragam.

Pemilik UMKM membutuhkan sistem untuk memahami perbedaan karakteristik pelanggan agar strategi promosi tidak diberikan secara seragam kepada seluruh pelanggan.

Proyek ini mengembangkan sistem **segmentasi pelanggan menggunakan K-Means Clustering** untuk membantu mengidentifikasi pola pembelian, memahami karakteristik pelanggan, dan menyusun rekomendasi promosi yang lebih relevan berdasarkan hasil analisis data.

## 2. Data dan Pembersihan

Dataset berasal dari **Kasus 05 — Segmentasi Pelanggan UMKM** pada repositori pembelajaran Machine Learning MKB UPI.

**Sumber dataset:** https://github.com/nurhikam/mkb-ml-project/tree/main/kasus/05-segmentasi-umkm

Dataset bersifat sintetis dan mencakup ringkasan aktivitas pelanggan selama enam bulan hingga Juni 2026.

| Informasi | Jumlah |
|---|---:|
| Data mentah | 10.150 baris |
| Jumlah variabel awal | 12 |
| Pelanggan unik | 10.000 |
| Data setelah pembersihan | 10.000 baris |

### Permasalahan Kualitas Data

| Masalah yang Ditemukan | Jumlah | Cara Menangani |
|---|---:|---|
| Baris duplikat identik | 90 | Menghapus menggunakan `drop_duplicates()` |
| ID pelanggan berulang | 150 kemunculan tambahan, termasuk duplikat identik | Menghapus duplikat identik terlebih dahulu, lalu memilih satu rekaman untuk setiap ID berdasarkan aturan recency |
| Umur kosong | 208 | Mempertahankan missing values karena umur tidak digunakan sebagai fitur clustering |
| Rating kosong | 812 | Mempertahankan missing values karena rating tidak digunakan sebagai fitur clustering |
| Format nominal belanja tidak konsisten | Ditemukan pada kolom nominal | Membersihkan format mata uang dan mengonversi menjadi nilai numerik |
| Penulisan kecamatan tidak konsisten | Beberapa variasi penulisan | Standardisasi nama kategori |
| Umur dan nilai transaksi tidak valid | Ditemukan saat validasi | Mengubah nilai tidak valid menjadi missing values |
| Missing values pada fitur clustering | Ditemukan setelah validasi | Menangani menggunakan imputasi median pada pipeline preprocessing |

Pembersihan data dilakukan sebelum pemodelan agar setiap pelanggan hanya direpresentasikan oleh satu baris.

## 3. Metodologi Machine Learning

Proyek menggunakan pendekatan **Unsupervised Learning** dengan algoritma **K-Means Clustering**.

Empat fitur perilaku pelanggan yang digunakan adalah:

| Fitur | Keterangan |
|---|---|
| Recency | Hari sejak transaksi terakhir |
| Frequency | Jumlah transaksi selama enam bulan |
| Monetary | Total belanja selama enam bulan |
| Promo Usage | Persentase transaksi yang menggunakan promo |

Tahapan pengembangan meliputi:

1. Data Understanding dan Data Quality Assessment.
2. Data Cleaning.
3. Exploratory Data Analysis (EDA).
4. Feature Engineering.
5. Preprocessing.
6. Pemodelan K-Means baseline.
7. Optimasi preprocessing.
8. Evaluasi jumlah cluster.
9. Customer Profiling.
10. Perancangan rekomendasi promo.
11. Integrasi model ke aplikasi Streamlit.
12. Pengujian dan dokumentasi.

### Model Baseline

Model baseline menerapkan:

- Imputasi median pada missing values.
- StandardScaler untuk standardisasi fitur.
- K-Means Clustering.
- Pengujian jumlah cluster k=2 hingga k=8.

### Model Optimasi

Model optimasi menerapkan:

- Imputasi median pada missing values.
- Transformasi `log1p` pada Recency, Frequency, dan Monetary.
- StandardScaler untuk standardisasi fitur.
- K-Means Clustering.
- Pengujian jumlah cluster k=2 hingga k=8.

Model final disimpan bersama pipeline preprocessing agar dapat digunakan kembali untuk mengelompokkan pelanggan baru secara konsisten.

## 4. Hasil dan Evaluasi Model

### Perbandingan Baseline dan Model Final

| Model | Silhouette Score (Evaluasi Internal) | Davies-Bouldin Index |
|---|---:|---:|
| Baseline — K-Means + StandardScaler | 0,5394 | 0,7373 |
| Final — K-Means + Log1p + StandardScaler | **0,5632** | **0,6295** |

Model final menggunakan **empat cluster (k=4)** karena memperoleh Silhouette Score tertinggi pada eksperimen optimasi dan menghasilkan kelompok pelanggan dengan karakteristik bisnis yang dapat diinterpretasikan.

Silhouette Score dihitung menggunakan sampel acak 1.800 pelanggan dari data pemodelan, sedangkan model K-Means dilatih menggunakan seluruh 10.000 pelanggan.

**Validation dan Test:** Evaluasi yang dilakukan merupakan evaluasi internal clustering. Skor validation dan test dari subset independen belum tersedia, sehingga hasil tersebut tidak diklaim sebagai skor test.

**Threshold model:** Tidak digunakan karena K-Means bukan algoritma klasifikasi probabilistik.

Pengujian kestabilan menggunakan random seed 21, 42, dan 123 menghasilkan Adjusted Rand Index (ARI) sebesar 1,0 terhadap pengelompokan acuan dalam percobaan tersebut.

### Hasil Segmentasi Pelanggan

| Cluster | Nama Segmen | Jumlah Pelanggan | Persentase |
|---|---|---:|---:|
| 0 | Loyal Customers | 3.025 | 30,25% |
| 1 | Inactive Customers | 2.990 | 29,90% |
| 2 | Occasion Buyers | 1.481 | 14,81% |
| 3 | Promo Seekers | 2.504 | 25,04% |
| **Total** | | **10.000** | **100%** |

Karakteristik masing-masing segmen:

**Loyal Customers:** Pelanggan dengan frekuensi transaksi tinggi, nilai belanja besar, dan aktivitas pembelian yang relatif konsisten.

**Inactive Customers:** Pelanggan dengan frekuensi transaksi rendah dan waktu yang relatif panjang sejak transaksi terakhir.

**Occasion Buyers:** Pelanggan dengan frekuensi pembelian rendah, tetapi nilai transaksi tinggi serta preferensi terhadap produk untuk kebutuhan acara.

**Promo Seekers:** Pelanggan dengan penggunaan promo tinggi dan kecenderungan menggunakan platform pemesanan makanan daring.

Nama segmen diberikan berdasarkan interpretasi karakteristik cluster, bukan label yang dipelajari langsung oleh algoritma.

## 5. Loyalty Membership dan Rekomendasi Promo

Selain segmentasi, DaMai menerapkan dua tingkatan membership berdasarkan total belanja selama enam bulan.

| Membership | Aturan | Jumlah Pelanggan |
|---|---|---:|
| Green | Total belanja di bawah Rp1.000.000 | 7.027 |
| Gold | Total belanja minimal Rp1.000.000 | 2.973 |

Batas Rp1.000.000 merupakan **threshold kebijakan bisnis simulasi**, bukan threshold model K-Means.

Setiap segmen memperoleh rekomendasi promo yang berbeda:

| Segmen | Strategi Promo |
|---|---|
| Loyal Customers | DaMai Loyalty Boost |
| Inactive Customers | DaMai Welcome Back |
| Occasion Buyers | DaMai Celebration Pack |
| Promo Seekers | DaMai Smart Bundle |

Rekomendasi promo ditentukan melalui aturan bisnis berdasarkan hasil segmentasi. Seluruh penawaran merupakan simulasi akademik dan belum divalidasi menggunakan biaya promosi, margin keuntungan, atau eksperimen penjualan nyata.

## 6. Aplikasi Web DaMai

**Live Application:** https://damai-customer-segmentation.streamlit.app/

Aplikasi dikembangkan menggunakan Python dan Streamlit dengan konsep antarmuka **Warm Modern Bakery**, menggunakan warna ivory, espresso brown, sage green, dan muted gold.

Terdapat enam halaman utama:

1. **Dashboard:** Menampilkan statistik pelanggan, distribusi segmen, membership, dan insight bisnis.
2. **Data Pelanggan:** Menyediakan pencarian pelanggan, filter, tabel interaktif, detail profil, rekomendasi, dan ekspor CSV.
3. **Segmentasi Pelanggan:** Menampilkan karakteristik empat segmen beserta visualisasi dan strategi bisnis.
4. **Prediksi Pelanggan:** Mengelompokkan pelanggan berdasarkan empat fitur transaksi menggunakan model K-Means tersimpan.
5. **Loyalty & Promo:** Menampilkan tingkat keanggotaan dan strategi promosi setiap segmen.
6. **Analisis Model:** Menampilkan evaluasi jumlah cluster, perbandingan baseline dan optimasi, serta metodologi.

Aplikasi merupakan prototipe akademik yang belum terhubung langsung dengan sistem transaksi operasional UMKM.

## 7. Cara Menjalankan

### Persyaratan

- Python 3.13.
- Library sesuai `requirements.txt`.
- Model tersimpan pada folder `models`.

### Instalasi

```bash
python -m pip install -r requirements.txt
```

### Menjalankan Aplikasi

```bash
python -m streamlit run app.py
```

Buka alamat:

`http://localhost:8501`

### Menjalankan Pengujian

```bash
python test_damai.py
```

Model tersimpan pada:

`models/damai_model_bundle.joblib`

Model menggunakan scikit-learn versi **1.6.1**, sesuai versi yang dicatat dalam `models/metadata.json` dan `requirements.txt`.

Notebook `DaMai_Customer_Segmentation.ipynb` memuat seluruh tahapan analisis, mulai dari pembacaan data, pembersihan, EDA, pemodelan, evaluasi, hingga penyimpanan model.

Dataset mentah tersedia dalam `data/raw.csv` dan juga dapat diakses melalui repositori GitHub.

## 8. Struktur Repositori

```text
damai-customer-segmentation/
├── .streamlit/
│   └── config.toml
├── assets/
│   ├── damai_customer_segmentation.png
│   └── damai_membership_distribution.png
├── data/
│   ├── raw.csv
│   ├── damai_customer_recommendations.csv
│   ├── damai_promotion_strategy.csv
│   ├── damai_segment_profiles.csv
│   ├── damai_baseline_metrics.csv
│   └── damai_optimized_metrics.csv
├── models/
│   ├── damai_model_bundle.joblib
│   └── metadata.json
├── src/
│   └── features.py
├── DaMai_Customer_Segmentation.ipynb
├── app.py
├── test_damai.py
├── requirements.txt
└── README.md
```

`src/features.py` digunakan untuk menyiapkan fitur input yang konsisten pada proses pelatihan dan prediksi.

`models/metadata.json` memuat identitas model, versi, fitur masukan, konfigurasi preprocessing, hasil evaluasi, dan pemetaan cluster.

## 9. Pengujian Sistem

Pengujian otomatis dilakukan menggunakan `test_damai.py`, meliputi:

1. Validasi 10.000 pelanggan unik.
2. Konsistensi distribusi empat segmen.
3. Validasi jumlah Green dan Gold Member.
4. Kelengkapan rekomendasi promo.
5. Kecocokan prediksi model tersimpan dengan hasil clustering.
6. Validasi konfigurasi K-Means.
7. Kelengkapan data evaluasi.

**Hasil:** Seluruh tujuh pemeriksaan otomatis berhasil.

Pengujian manual juga telah dilakukan pada enam halaman aplikasi.

Selain itu, aplikasi yang telah di-deploy berhasil memproses input pelanggan dengan hasil:

- Segmen: Loyal Customers.
- Membership: Gold.
- Rekomendasi: DaMai Loyalty Boost.

## 10. Keterbatasan

1. Dataset merupakan data sintetis, sehingga belum mencerminkan karakteristik pelanggan UMKM yang sebenarnya.
2. Model hanya menggunakan empat indikator perilaku transaksi.
3. Imputasi median dapat mengurangi informasi pada pelanggan yang memiliki data tidak lengkap.
4. Evaluasi clustering masih bersifat internal dan belum mengukur kemampuan generalisasi pada dataset independen.
5. Silhouette Score dan Davies-Bouldin Index mengukur kualitas cluster, bukan dampak terhadap peningkatan penjualan.
6. Strategi promo dan membership belum diuji berdasarkan harga pokok produk, margin keuntungan, atau eksperimen pemasaran.
7. Aplikasi belum terintegrasi dengan basis data transaksi secara langsung.
8. Perubahan pola belanja pelanggan pada masa mendatang dapat memerlukan evaluasi dan pelatihan ulang model.

## 11. Daftar Periksa Sebelum Pengumpulan

- [x] Repositori GitHub bersifat publik.
- [x] Dataset mentah dan hasil pengolahan tersedia.
- [x] Notebook berhasil dijalankan ulang dari awal sampai akhir.
- [x] Data cleaning dan EDA telah dilakukan.
- [x] Model baseline dibandingkan dengan model final.
- [x] Hasil clustering memiliki profil dan interpretasi bisnis.
- [x] Pipeline model dan metadata tersedia.
- [x] `src/features.py` digunakan pada notebook dan aplikasi.
- [x] Aplikasi dapat diakses melalui tautan publik.
- [x] Pengujian otomatis berhasil.
- [x] Prediksi pada aplikasi daring berhasil diuji.
- [ ] Kontribusi setiap anggota pada riwayat commit GitHub dilengkapi.
- [ ] Pengujian input tidak wajar pada aplikasi daring didokumentasikan.
- [ ] Laporan akhir maksimal 6 halaman selesai.
- [ ] Video demo maksimal 5 menit selesai.

## 12. Kesimpulan

Proyek DaMai Coffee & Bakery berhasil mengembangkan sistem segmentasi pelanggan UMKM menggunakan algoritma K-Means Clustering berdasarkan perilaku transaksi pelanggan.

Optimasi preprocessing meningkatkan Silhouette Score dari 0,5394 menjadi 0,5632 dan menurunkan Davies-Bouldin Index dari 0,7373 menjadi 0,6295.

Hasil segmentasi menghasilkan empat kelompok pelanggan dengan karakteristik berbeda, yaitu Loyal Customers, Inactive Customers, Occasion Buyers, dan Promo Seekers.

Model telah diintegrasikan ke dalam aplikasi Streamlit untuk mendukung visualisasi data, analisis profil pelanggan, prediksi segmen, membership, dan rekomendasi promosi.

Sistem ini menunjukkan potensi penerapan Machine Learning sebagai alat bantu pengambilan keputusan pemasaran berbasis data, dengan tetap memerlukan pengujian dan validasi lebih lanjut sebelum digunakan dalam operasional UMKM nyata.