# DaMai Coffee & Bakery

### Live Application

**Aplikasi Web:** https://damai-customer-segmentation.streamlit.app/

**Source Code:** https://github.com/dnielaivnka/damai-customer-segmentation

Aplikasi DaMai Coffee & Bakery menggunakan K-Means Clustering untuk segmentasi pelanggan dan rekomendasi promosi berbasis perilaku transaksi.

## Customer Segmentation and Personalized Promotion Using K-Means Clustering

**Proyek Machine Learning — Kasus 05: Segmentasi Pelanggan UMKM**

**Disusun oleh:**
- Daniela Ivanka Maydina Siringoringo — 2401148
- Muhamad Nurhidayat — 2401404

**Program Studi:** Mekatronika dan Kecerdasan Buatan  
**Universitas:** Universitas Pendidikan Indonesia  
**Tahun:** 2026

---

## 1. Deskripsi Proyek

DaMai Coffee & Bakery merupakan studi kasus UMKM fiktif di Bandung yang digunakan untuk mengembangkan sistem segmentasi pelanggan berbasis Machine Learning.

Proyek ini bertujuan memahami perbedaan perilaku belanja pelanggan agar pemilik UMKM dapat menyusun strategi promosi yang lebih relevan.

Algoritma yang digunakan adalah **K-Means Clustering**, dengan indikator Recency, Frequency, Monetary, dan persentase penggunaan promo.

Hasil segmentasi diintegrasikan ke aplikasi web berbasis Streamlit untuk visualisasi data, analisis pelanggan, prediksi segmen, dan rekomendasi promosi.

## 2. Dataset

Dataset mencakup aktivitas pelanggan selama Januari–Juni 2026.

- Data awal: 10.150 baris.
- Data setelah pembersihan: 10.000 pelanggan unik.
- Jumlah variabel awal: 12.
- Sumber: Dataset pembelajaran Kasus 05 — Segmentasi Pelanggan UMKM.

Tahap data cleaning meliputi pemeriksaan duplikasi, missing values, penyesuaian format nominal rupiah, standardisasi kategori, dan validasi nilai tidak wajar.

Dataset bersifat simulasi dan tidak mewakili transaksi nyata DaMai Coffee & Bakery.

## 3. Metodologi Machine Learning

Tahapan pengembangan meliputi:

1. Data Understanding.
2. Data Quality Assessment.
3. Data Cleaning.
4. Exploratory Data Analysis (EDA).
5. Feature Engineering dan Preprocessing.
6. K-Means Baseline.
7. Optimasi K-Means.
8. Evaluasi dan pemilihan jumlah cluster.
9. Customer Profiling.
10. Rekomendasi promo dan implementasi aplikasi.

Model menggunakan empat fitur perilaku pelanggan:

| Fitur | Deskripsi |
|---|---|
| Recency | Hari sejak transaksi terakhir |
| Frequency | Jumlah transaksi dalam enam bulan |
| Monetary | Total belanja dalam enam bulan |
| Promo Usage | Persentase transaksi menggunakan promo |

Model final menggunakan imputasi median, transformasi `log1p` pada fitur Recency, Frequency, dan Monetary, serta `StandardScaler`.

## 4. Hasil Evaluasi Model

| Metrik | Baseline | Optimasi |
|---|---:|---:|
| Jumlah Cluster | 4 | 4 |
| Silhouette Score | 0,5394 | 0,5632 |
| Davies-Bouldin Index | 0,7373 | 0,6295 |

Model optimasi dipilih karena menghasilkan Silhouette Score lebih tinggi dan Davies-Bouldin Index lebih rendah.

Pengujian kestabilan menggunakan tiga random seed (21, 42, dan 123) menghasilkan Adjusted Rand Index sebesar 1,0 terhadap model acuan pada percobaan tersebut.

## 5. Hasil Segmentasi Pelanggan

| Segmen | Jumlah Pelanggan | Persentase |
|---|---:|---:|
| Loyal Customers | 3.025 | 30,25% |
| Inactive Customers | 2.990 | 29,90% |
| Occasion Buyers | 1.481 | 14,81% |
| Promo Seekers | 2.504 | 25,04% |
| **Total** | **10.000** | **100%** |

Nama segmen diberikan berdasarkan interpretasi profil cluster, bukan label yang dipelajari langsung oleh algoritma.

## 6. Loyalty Membership

DaMai menggunakan dua tingkat membership dalam simulasi:

- **Green Member:** Total belanja enam bulan di bawah Rp1.000.000.
- **Gold Member:** Total belanja enam bulan minimal Rp1.000.000.

Hasil pengelompokan membership adalah 7.027 Green Member dan 2.973 Gold Member.

Membership merupakan aturan bisnis terpisah dari algoritma K-Means.

## 7. Fitur Aplikasi

Aplikasi DaMai Coffee & Bakery dibangun menggunakan Python dan Streamlit dengan enam halaman utama:

1. **Dashboard:** Ringkasan KPI, distribusi segmen, dan membership.
2. **Data Pelanggan:** Pencarian, filter, tabel, detail profil, dan ekspor CSV.
3. **Segmentasi Pelanggan:** Analisis karakteristik keempat segmen.
4. **Prediksi Pelanggan:** Pengelompokan pelanggan menggunakan model tersimpan.
5. **Loyalty & Promo:** Membership dan rekomendasi promosi.
6. **Analisis Model:** Evaluasi, grafik, dan metodologi K-Means.

Desain antarmuka menggunakan konsep **Warm Modern Bakery** dengan warna ivory, espresso brown, sage green, dan muted gold.

## 8. Teknologi

- Python
- Google Colab
- Pandas dan NumPy
- Scikit-learn
- Matplotlib dan Seaborn
- Streamlit
- Plotly
- Joblib
- Visual Studio Code

## 9. Cara Menjalankan Aplikasi

Pastikan Python terpasang dan folder proyek sudah dibuka melalui terminal VS Code.

Instal dependensi:

```bash
python -m pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python -m streamlit run app.py
```

Buka alamat berikut pada browser:

`http://localhost:8501`

Model tersimpan di `models/damai_model_bundle.joblib`.

Gunakan versi scikit-learn yang sesuai dengan model tersimpan, sebagaimana ditentukan dalam `requirements.txt`.

## 10. Pengujian

Pengujian otomatis dilakukan menggunakan:

```bash
python test_damai.py
```

Hasil pengujian menunjukkan seluruh pemeriksaan berhasil, meliputi konsistensi jumlah pelanggan, distribusi segmen, membership, rekomendasi promo, kecocokan prediksi model, dan kelengkapan hasil evaluasi.

Keenam halaman aplikasi juga telah melalui pengujian fungsi secara manual.

## 11. Keterbatasan

- Dataset merupakan data simulasi.
- Segmentasi belum diuji pada pelanggan UMKM nyata.
- Keberhasilan clustering tidak otomatis menunjukkan peningkatan penjualan.
- Kebijakan membership dan promo belum divalidasi terhadap biaya operasional maupun margin keuntungan.
- Aplikasi merupakan prototipe akademik dan belum terhubung ke sistem transaksi langsung.

## 12. Kesimpulan

Proyek DaMai Coffee & Bakery berhasil mengembangkan model segmentasi pelanggan menggunakan K-Means dengan empat kelompok yang memiliki karakteristik perilaku berbeda.

Optimasi preprocessing meningkatkan kualitas clustering dibandingkan baseline. Model berhasil diintegrasikan ke aplikasi Streamlit yang menyediakan informasi pelanggan, visualisasi segmentasi, prediksi pelanggan, dan rekomendasi promosi.

Sistem ini menunjukkan potensi pemanfaatan Machine Learning untuk mendukung pengambilan keputusan pemasaran berbasis data pada UMKM.
