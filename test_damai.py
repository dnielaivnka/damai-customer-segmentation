
from pathlib import Path
import joblib
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(
    BASE_DIR / "data" / "damai_customer_recommendations.csv"
)

bundle = joblib.load(
    BASE_DIR / "models" / "damai_model_bundle.joblib"
)

baseline = pd.read_csv(
    BASE_DIR / "data" / "damai_baseline_metrics.csv"
)

optimasi = pd.read_csv(
    BASE_DIR / "data" / "damai_optimized_metrics.csv"
)

print("PENGUJIAN SISTEM DAMAI")
print("=" * 48)

assert len(df) == 10000
assert df["id_pelanggan"].is_unique
print("PASS — 10.000 pelanggan unik")

jumlah_segmen = {
    "Loyal Customers": 3025,
    "Inactive Customers": 2990,
    "Occasion Buyers": 1481,
    "Promo Seekers": 2504
}

for segmen, jumlah in jumlah_segmen.items():
    assert int((df["segmen"] == segmen).sum()) == jumlah

print("PASS — Distribusi empat segmen sesuai Colab")

assert int((df["membership"] == "Gold").sum()) == 2973
assert int((df["membership"] == "Green").sum()) == 7027

print("PASS — Membership Green dan Gold sesuai")

assert df["nama_promo"].notna().all()
assert df["rekomendasi_promo"].notna().all()
assert df["syarat_promo"].notna().all()

print("PASS — Seluruh pelanggan memiliki rekomendasi")

prediksi_ulang = bundle["pipeline"].predict(
    df[bundle["fitur"]]
)

assert np.array_equal(
    prediksi_ulang.astype(int),
    df["cluster"].astype(int).to_numpy()
)

print("PASS — Prediksi model cocok dengan hasil Colab")

assert bundle["jumlah_cluster"] == 4
assert np.isclose(bundle["silhouette_score"], 0.5632, atol=0.0001)

print("PASS — Konfigurasi model sesuai")

assert len(baseline) == 7
assert len(optimasi) == 7
assert set(optimasi["k"]) == set(range(2, 9))

print("PASS — Data evaluasi lengkap")

sampel = pd.DataFrame([
    [5, 28, 1300000, 20],
    [108, 3, 100000, 34],
    [30, 4, 1040000, 12],
    [12, 11, 340000, 80]
], columns=bundle["fitur"])

hasil = bundle["pipeline"].predict(sampel)

print("\nHASIL PREDIKSI PELANGGAN CONTOH")

for nomor, cluster in enumerate(hasil, start=1):
    segmen = bundle["nama_segmen"][int(cluster)]
    print(f"Pelanggan {nomor}: {segmen}")

print("\nSELURUH PENGUJIAN BERHASIL")
