
import pandas as pd

FEATURE_COLUMNS = [
    "hari_sejak_transaksi_terakhir",
    "jumlah_transaksi_6bln",
    "total_belanja_rp",
    "persen_pakai_promo"
]


def prepare_features(data):
    missing_columns = [
        column for column in FEATURE_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Kolom fitur tidak ditemukan: {missing_columns}"
        )

    features = data[FEATURE_COLUMNS].copy()

    for column in FEATURE_COLUMNS:
        features[column] = pd.to_numeric(
            features[column],
            errors="coerce"
        )

    return features
