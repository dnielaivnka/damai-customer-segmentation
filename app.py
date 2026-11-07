
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="DaMai | Customer Intelligence",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

COLORS = {
    "espresso": "#4B3428",
    "coffee": "#795540",
    "sage": "#8DA796",
    "gold": "#C9A45C",
    "terracotta": "#C98D71",
    "ivory": "#FBF8F4"
}

SEGMENT_COLORS = {
    "Loyal Customers": COLORS["coffee"],
    "Promo Seekers": COLORS["sage"],
    "Inactive Customers": COLORS["terracotta"],
    "Occasion Buyers": COLORS["gold"]
}

SEGMENT_ORDER = [
    "Loyal Customers",
    "Promo Seekers",
    "Inactive Customers",
    "Occasion Buyers"
]


@st.cache_data
def load_data():
    customers = pd.read_csv(
        DATA_DIR / "damai_customer_recommendations.csv"
    )
    profiles = pd.read_csv(
        DATA_DIR / "damai_segment_profiles.csv"
    )
    promotions = pd.read_csv(
        DATA_DIR / "damai_promotion_strategy.csv"
    )
    return customers, profiles, promotions


st.markdown("""
<style>
    .stApp {
        background-color: #FBF8F4;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }

    section[data-testid="stSidebar"] {
        background-color: #F0EAE1;
        border-right: 1px solid #E4D8CB;
    }

    h1, h2, h3 {
        color: #4B3428;
    }

    h1 {
        font-family: Georgia, serif;
        font-size: 2.7rem !important;
        font-weight: 600;
    }

    div[data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E9DED2;
        border-radius: 16px;
        padding: 18px 20px;
    }

    div[data-testid="stMetricLabel"] {
        color: #806C5F;
    }

    div[data-testid="stMetricValue"] {
        color: #4B3428;
        font-size: 1.8rem;
    }

    .damai-brand {
        font-family: Georgia, serif;
        color: #4B3428;
        font-size: 2.4rem;
        font-weight: 700;
        letter-spacing: -1px;
    }

    .damai-subtitle {
        color: #8D796B;
        font-size: 0.8rem;
        letter-spacing: 2px;
    }

    .hero {
        background: linear-gradient(120deg, #EFE5D8, #F8F2EA);
        border: 1px solid #E8DCCF;
        border-radius: 22px;
        padding: 30px 36px;
        margin-bottom: 26px;
    }

    .hero-label {
        color: #967B65;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 2px;
    }

    .hero-title {
        color: #4B3428;
        font-family: Georgia, serif;
        font-size: 2.2rem;
        line-height: 1.3;
        margin: 12px 0;
    }

    .hero-description {
        color: #765F50;
        font-size: 0.95rem;
        line-height: 1.7;
    }

    .section-heading {
        color: #4B3428;
        font-family: Georgia, serif;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 22px 0 12px;
    }

/* DAMAI — WARM MODERN BAKERY */

.stApp {
    background: #FBF8F4;
    color: #3D2B22;
}

.block-container {
    max-width: 1380px;
    padding-top: 1.8rem;
    padding-bottom: 2.5rem;
}

section[data-testid="stSidebar"] {
    background: #4B3428 !important;
    border-right: none;
}

section[data-testid="stSidebar"] .damai-brand {
    color: #FFF8EF !important;
    font-size: 2.8rem;
    letter-spacing: -1.5px;
}

section[data-testid="stSidebar"] .damai-subtitle {
    color: #D9BFA5 !important;
    letter-spacing: 2.5px;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: #F4E9DD !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #D5C1B0 !important;
}

section[data-testid="stSidebar"] hr {
    border-color: #806452;
}

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 7px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    padding: 11px 13px;
    border-radius: 11px;
    border: 1px solid transparent;
    transition: background 0.2s ease;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #654B3A;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: #806044;
    border-color: #AD8B70;
}

h1, h2, h3 {
    color: #4B3428;
    letter-spacing: -0.5px;
}

h1 {
    font-family: Georgia, serif;
    font-size: 2.35rem !important;
    font-weight: 600;
}

h2 {
    font-family: Georgia, serif;
}

.section-heading {
    font-family: Georgia, serif;
    color: #4B3428;
    font-size: 1.4rem;
    margin: 18px 0 10px;
}

.hero {
    background: linear-gradient(125deg, #EDE0CF 0%, #F7EEE3 60%, #FBF8F4 100%);
    border: 1px solid #E7D8C7;
    border-radius: 20px;
    padding: 27px 32px;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 2rem;
    line-height: 1.3;
}

div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E9DFD5;
    border-radius: 15px;
    padding: 17px;
    box-shadow: 0 3px 12px rgba(75, 52, 40, 0.035);
}

div[data-testid="stMetricValue"] {
    font-size: 1.65rem;
    color: #4B3428;
    overflow-wrap: anywhere;
}

div[data-testid="stMetricLabel"] {
    color: #796759;
}

div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #EAE0D6;
    border-radius: 15px;
    overflow: hidden;
}

div[data-testid="stDataFrame"] {
    border: 1px solid #E8DED3;
    border-radius: 13px;
    overflow: hidden;
}

div[data-testid="stForm"] {
    background: #FFFFFF;
    border: 1px solid #E8DED3;
    border-radius: 16px;
    padding: 20px;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    border-bottom: 1px solid #E8DED3;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 9px 9px 0 0;
    padding: 12px 18px;
    color: #806C5F;
}

.stTabs [aria-selected="true"] {
    color: #4B3428 !important;
    font-weight: 600;
    background: #F0E8DE;
}

.stButton button[kind="primary"],
.stFormSubmitButton button[kind="primary"] {
    background: #795540;
    border-color: #795540;
    border-radius: 10px;
    font-weight: 600;
}

.stButton button[kind="primary"]:hover,
.stFormSubmitButton button[kind="primary"]:hover {
    background: #5D3E2E;
    border-color: #5D3E2E;
}

    </style>
""", unsafe_allow_html=True)


try:
    df, df_profiles, df_promotions = load_data()
except (FileNotFoundError, ValueError) as error:
    st.error(f"Gagal memuat dataset: {error}")
    st.stop()


with st.sidebar:
    st.markdown(
        '<div class="damai-brand">DaMai.</div>'
        '<div class="damai-subtitle">COFFEE & BAKERY</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.caption("CUSTOMER INTELLIGENCE")
    st.divider()

    halaman = st.radio(
        "Navigasi",
        [
            "Dashboard",
            "Data Pelanggan",
            "Segmentasi Pelanggan",
            "Prediksi Pelanggan",
            "Loyalty & Promo",
            "Analisis Model"
        ],
        label_visibility="collapsed"
    )

    st.divider()
    st.caption("Data transaksi: Januari–Juni 2026")
    st.caption("Model: K-Means Clustering")
    st.caption("DaMai • Academic Simulation")


if halaman == "Dashboard":
    st.markdown("""
    <div class="hero">
        <div class="hero-label">WELCOME TO DAMAI</div>
        <div class="hero-title">Kenali pelanggan.<br>Bangun hubungan yang lebih bermakna.</div>
        <div class="hero-description">
            Temukan pola belanja, pahami karakteristik pelanggan,
            dan rancang strategi promosi yang lebih relevan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    total_pelanggan = df["id_pelanggan"].nunique()
    total_segmen = df["segmen"].nunique()
    gold_count = (df["membership"] == "Gold").sum()
    gold_percentage = gold_count / total_pelanggan * 100
    median_belanja = df["total_belanja_rp"].median()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Pelanggan", f"{total_pelanggan:,}")

    with col2:
        st.metric("Segmen Pelanggan", total_segmen)

    with col3:
        st.metric("Gold Member", f"{gold_percentage:.1f}%")

    with col4:
        st.metric(
            "Median Belanja / 6 Bulan",
            f"Rp{median_belanja / 1000:,.0f} rb"
        )

    st.markdown(
        '<div class="section-heading">Customer Overview</div>',
        unsafe_allow_html=True
    )

    chart1, chart2 = st.columns([1.5, 1])

    segment_counts = (
        df["segmen"]
        .value_counts()
        .reindex(SEGMENT_ORDER)
        .fillna(0)
        .astype(int)
    )

    segment_fig = go.Figure()

    segment_fig.add_trace(
        go.Bar(
            x=segment_counts.values,
            y=segment_counts.index,
            orientation="h",
            marker_color=[
                SEGMENT_COLORS[s]
                for s in segment_counts.index
            ],
            
text=[
    f"{n:,}"
    for n in segment_counts.values
],
textposition="inside",
insidetextanchor="middle",
textfont=dict(color="white", size=13),

            hovertemplate="%{y}: %{x:,} pelanggan<extra></extra>"
        )
    )

    segment_fig.update_layout(
        title="Distribusi Segmen Pelanggan",
        height=350,
        margin=dict(l=20, r=70, t=60, b=30),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color=COLORS["espresso"]),
        xaxis=dict(
            title="Jumlah Pelanggan",
            showgrid=True,
            gridcolor="#F0EAE1"
        ),
        yaxis=dict(
            title="",
            autorange="reversed"
        ),
        showlegend=False
    )

    membership_counts = (
        df["membership"]
        .value_counts()
        .reindex(["Green", "Gold"])
        .fillna(0)
    )

    membership_fig = go.Figure(
        data=[
            go.Pie(
                labels=membership_counts.index,
                values=membership_counts.values,
                hole=0.68,
                marker=dict(
                    colors=[COLORS["sage"], COLORS["gold"]]
                ),
                textinfo="label+percent",
                hovertemplate="%{label}: %{value:,}<extra></extra>"
            )
        ]
    )

    membership_fig.update_layout(
        title="Komposisi Membership",
        height=350,
        margin=dict(l=20, r=20, t=60, b=30),
        paper_bgcolor="white",
        font=dict(color=COLORS["espresso"]),
        showlegend=False,
        annotations=[
            dict(
                text=f"{total_pelanggan:,}",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(
                    size=23,
                    color=COLORS["espresso"]
                )
            )
        ]
    )

    with chart1:
        st.plotly_chart(
            segment_fig,
            use_container_width=True
        )

    with chart2:
        st.plotly_chart(
            membership_fig,
            use_container_width=True
        )

    st.markdown(
        '<div class="section-heading">Business Insights</div>',
        unsafe_allow_html=True
    )

    inactive_count = int(
        segment_counts.get("Inactive Customers", 0)
    )

    inactive_percentage = (
        inactive_count / total_pelanggan * 100
    )

    insight1, insight2 = st.columns(2)

    with insight1:
        st.info(
            f"**Peluang Retensi**\n\n"
            f"{inactive_count:,} pelanggan "
            f"({inactive_percentage:.1f}%) berada dalam "
            f"segmen Inactive Customers. "
            f"Kelompok ini dapat diprioritaskan untuk "
            f"program aktivasi kembali."
        )

    with insight2:
        st.success(
            f"**Pelanggan Bernilai Tinggi**\n\n"
            f"{gold_count:,} pelanggan masuk kategori "
            f"Gold Member. Program loyalitas dapat "
            f"digunakan untuk mempertahankan hubungan "
            f"dengan kelompok ini."
        )

    st.divider()
    st.caption(
        "DaMai Coffee & Bakery • "
        "Customer Segmentation Dashboard • 2026"
    )



elif halaman == "Data Pelanggan":
    st.title("Data Pelanggan")
    st.caption(
        "Jelajahi profil, aktivitas pembelian, dan rekomendasi "
        "untuk pelanggan DaMai Coffee & Bakery."
    )

    st.markdown(
        '<div class="section-heading">Customer Directory</div>',
        unsafe_allow_html=True
    )

    pencarian = st.text_input(
        "Cari ID Pelanggan",
        placeholder="Contoh: PLG-00001"
    )

    with st.expander("Filter Pelanggan", expanded=False):
        f1, f2, f3 = st.columns(3)

        with f1:
            pilihan_segmen = st.multiselect(
                "Segmen",
                options=SEGMENT_ORDER,
                default=SEGMENT_ORDER
            )

        with f2:
            pilihan_membership = st.multiselect(
                "Membership",
                options=["Green", "Gold"],
                default=["Green", "Gold"]
            )

        with f3:
            semua_channel = sorted(
                df["channel_utama"].dropna().unique().tolist()
            )

            pilihan_channel = st.multiselect(
                "Channel Pembelian",
                options=semua_channel,
                default=semua_channel
            )

    df_filtered = df[
        df["segmen"].isin(pilihan_segmen)
        & df["membership"].isin(pilihan_membership)
        & df["channel_utama"].isin(pilihan_channel)
    ].copy()

    if pencarian.strip():
        df_filtered = df_filtered[
            df_filtered["id_pelanggan"]
            .astype(str)
            .str.contains(
                pencarian.strip(),
                case=False,
                regex=False,
                na=False
            )
        ]

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric(
            "Total Pelanggan",
            f"{len(df_filtered):,}"
        )

    with m2:
        st.metric(
            "Gold Member",
            f"{(df_filtered['membership'] == 'Gold').sum():,}"
        )

    with m3:
        st.metric(
            "Green Member",
            f"{(df_filtered['membership'] == 'Green').sum():,}"
        )

    with m4:
        st.metric(
            "Segmen",
            df_filtered["segmen"].nunique()
        )

    st.write("")

    tab1, tab2, tab3 = st.tabs([
        "Daftar Pelanggan",
        "Profil Pelanggan",
        "Rekomendasi Promo"
    ])

    with tab1:
        st.markdown("#### Customer List")

        kolom_tabel = [
            "id_pelanggan",
            "umur",
            "kecamatan",
            "kategori_favorit",
            "jumlah_transaksi_6bln",
            "total_belanja_rp",
            "hari_sejak_transaksi_terakhir",
            "segmen",
            "membership"
        ]

        nama_kolom = {
            "id_pelanggan": "ID Pelanggan",
            "umur": "Umur",
            "kecamatan": "Kecamatan",
            "kategori_favorit": "Produk Favorit",
            "jumlah_transaksi_6bln": "Transaksi",
            "total_belanja_rp": "Total Belanja (Rp)",
            "hari_sejak_transaksi_terakhir": "Recency (Hari)",
            "segmen": "Segmen",
            "membership": "Membership"
        }

        tabel_tampil = df_filtered[kolom_tabel].rename(
            columns=nama_kolom
        )

        st.dataframe(
            tabel_tampil,
            width="stretch",
            hide_index=True,
            height=420
        )

        if not df_filtered.empty:
            st.download_button(
                "Unduh Data Pelanggan (CSV)",
                data=df_filtered.to_csv(index=False).encode("utf-8-sig"),
                file_name="damai_filtered_customers.csv",
                mime="text/csv"
            )

        st.caption(
            f"Menampilkan {len(df_filtered):,} pelanggan "
            "sesuai pencarian dan filter."
        )

    pelanggan = None

    with tab2:
        st.markdown("#### Customer Profile")

        if df_filtered.empty:
            st.warning(
                "Tidak ditemukan pelanggan yang sesuai dengan filter."
            )
        else:
            pilihan_id = st.selectbox(
                "Pilih pelanggan",
                options=df_filtered["id_pelanggan"].astype(str).tolist(),
                key="damai_profil_pelanggan"
            )

            pelanggan = df_filtered[
                df_filtered["id_pelanggan"].astype(str) == pilihan_id
            ].iloc[0]

            c1, c2 = st.columns(2)

            with c1:
                with st.container(border=True):
                    st.markdown("##### Informasi Pelanggan")

                    st.write(f"**ID:** {pelanggan['id_pelanggan']}")
                    st.write(f"**Kecamatan:** {pelanggan['kecamatan']}")
                    st.write(f"**Umur:** {pelanggan['umur']}")
                    st.write(
                        f"**Produk Favorit:** "
                        f"{str(pelanggan['kategori_favorit']).replace('_', ' ').title()}"
                    )
                    st.write(
                        f"**Channel Utama:** {pelanggan['channel_utama']}"
                    )
                    st.write(
                        f"**Metode Pembayaran:** {pelanggan['metode_bayar']}"
                    )

            with c2:
                with st.container(border=True):
                    st.markdown("##### Perilaku Transaksi")

                    st.write(
                        f"**Frekuensi:** "
                        f"{pelanggan['jumlah_transaksi_6bln']:,.0f} transaksi"
                    )

                    st.write(
                        f"**Total Belanja:** "
                        f"Rp{pelanggan['total_belanja_rp']:,.0f}"
                    )

                    recency = pelanggan["hari_sejak_transaksi_terakhir"]

                    st.write(
                        f"**Transaksi Terakhir:** "
                        f"{recency:,.0f} hari lalu"
                        if pd.notna(recency)
                        else "**Transaksi Terakhir:** Data tidak tersedia"
                    )

                    st.write(
                        f"**Penggunaan Promo:** "
                        f"{pelanggan['persen_pakai_promo']:.0f}%"
                    )

            s1, s2 = st.columns(2)

            with s1:
                st.metric(
                    "Customer Segment",
                    pelanggan["segmen"]
                )

            with s2:
                st.metric(
                    "Membership Level",
                    pelanggan["membership"]
                )

    with tab3:
        st.markdown("#### Personalized Promotion")

        if pelanggan is None:
            st.warning(
                "Pilih filter yang menghasilkan pelanggan "
                "untuk melihat rekomendasi."
            )
        else:
            st.caption(
                f"Rekomendasi untuk pelanggan {pelanggan['id_pelanggan']}"
            )

            with st.container(border=True):
                st.caption("DAMAI EXCLUSIVE OFFER")

                st.subheader(pelanggan["nama_promo"])

                st.markdown("**Penawaran**")
                st.write(pelanggan["rekomendasi_promo"])

                st.markdown("**Syarat dan Ketentuan**")
                st.write(pelanggan["syarat_promo"])

                st.markdown("**Membership Benefit**")
                st.write(pelanggan["benefit_membership"])

            st.info(
                "Rekomendasi disesuaikan berdasarkan segmen "
                "pelanggan. Penawaran ini masih berupa simulasi bisnis."
            )


elif halaman == "Segmentasi Pelanggan":
    st.title("Segmentasi Pelanggan")
    st.caption(
        "Kenali empat kelompok pelanggan DaMai berdasarkan "
        "aktivitas pembelian, nilai belanja, dan penggunaan promo."
    )

    informasi_segmen = {
        "Loyal Customers": {
            "deskripsi": "Pelanggan setia dengan frekuensi transaksi dan nilai belanja tinggi.",
            "strategi": "Pertahankan loyalitas melalui bonus poin dan penghargaan pelanggan.",
            "warna": COLORS["coffee"]
        },
        "Promo Seekers": {
            "deskripsi": "Pelanggan yang aktif memanfaatkan promosi dan penawaran harga.",
            "strategi": "Tawarkan bundling produk dengan batas diskon terkendali.",
            "warna": COLORS["sage"]
        },
        "Inactive Customers": {
            "deskripsi": "Pelanggan dengan frekuensi rendah dan jeda transaksi panjang.",
            "strategi": "Prioritaskan program aktivasi kembali melalui voucher bersyarat.",
            "warna": COLORS["terracotta"]
        },
        "Occasion Buyers": {
            "deskripsi": "Pelanggan yang cenderung berbelanja untuk kebutuhan acara.",
            "strategi": "Tawarkan paket kue, snack, dan layanan preorder.",
            "warna": COLORS["gold"]
        }
    }

    st.markdown(
        '<div class="section-heading">Customer Segments</div>',
        unsafe_allow_html=True
    )

    jumlah_per_segmen = (
        df["segmen"]
        .value_counts()
        .reindex(SEGMENT_ORDER)
        .fillna(0)
        .astype(int)
    )

    kolom_kartu = st.columns(4)

    for kolom, segmen in zip(kolom_kartu, SEGMENT_ORDER):
        with kolom:
            jumlah = int(jumlah_per_segmen[segmen])
            persentase = jumlah / len(df) * 100

            st.metric(
                segmen,
                f"{jumlah:,}",
                f"{persentase:.2f}% dari pelanggan",
                delta_color="off"
            )

    st.markdown(
        '<div class="section-heading">Distribusi Segmen</div>',
        unsafe_allow_html=True
    )

    grafik_distribusi = go.Figure()

    grafik_distribusi.add_trace(
        go.Bar(
            x=jumlah_per_segmen.values,
            y=jumlah_per_segmen.index,
            orientation="h",
            marker_color=[
                SEGMENT_COLORS[s] for s in SEGMENT_ORDER
            ],
            text=[
                f"{n:,}" for n in jumlah_per_segmen.values
            ],
            textposition="inside",
            insidetextanchor="middle",
            textfont=dict(color="white", size=13),
            hovertemplate="%{y}: %{x:,} pelanggan<extra></extra>"
        )
    )

    grafik_distribusi.update_layout(
        height=340,
        margin=dict(l=30, r=30, t=25, b=35),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color=COLORS["espresso"]),
        xaxis=dict(
            title="Jumlah Pelanggan",
            gridcolor="#EEE5DB"
        ),
        yaxis=dict(autorange="reversed"),
        showlegend=False
    )

    st.plotly_chart(
        grafik_distribusi,
        use_container_width=True
    )

    st.markdown(
        '<div class="section-heading">Profil dan Karakteristik</div>',
        unsafe_allow_html=True
    )

    pilihan_segmen_detail = st.selectbox(
        "Pilih segmen untuk dianalisis",
        SEGMENT_ORDER
    )

    data_segmen = df[
        df["segmen"] == pilihan_segmen_detail
    ].copy()

    info = informasi_segmen[pilihan_segmen_detail]

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border-left:5px solid {info['warna']};
            border-radius:12px;
            padding:20px 24px;
            margin:12px 0 22px;
        ">
            <div style="
                font-family:Georgia,serif;
                font-size:24px;
                color:#4B3428;
                margin-bottom:8px;
            ">
                {pilihan_segmen_detail}
            </div>
            <div style="color:#765F50;line-height:1.7;">
                {info['deskripsi']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.metric(
            "Median Transaksi",
            f"{data_segmen['jumlah_transaksi_6bln'].median():.0f} kali"
        )

    with p2:
        st.metric(
            "Median Belanja",
            f"Rp{data_segmen['total_belanja_rp'].median()/1000:,.0f} rb"
        )

    with p3:
        st.metric(
            "Median Recency",
            f"{data_segmen['hari_sejak_transaksi_terakhir'].median():.0f} hari"
        )

    with p4:
        st.metric(
            "Median Penggunaan Promo",
            f"{data_segmen['persen_pakai_promo'].median():.0f}%"
        )

    grafik1, grafik2 = st.columns(2)

    kategori = (
        data_segmen["kategori_favorit"]
        .value_counts(normalize=True)
        .mul(100)
        .sort_values()
    )

    fig_kategori = go.Figure(
        go.Bar(
            x=kategori.values,
            y=kategori.index,
            orientation="h",
            marker_color=info["warna"],
            hovertemplate="%{y}: %{x:.1f}%<extra></extra>"
        )
    )

    fig_kategori.update_layout(
        title="Kategori Produk Favorit",
        height=320,
        margin=dict(l=20, r=20, t=60, b=30),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color=COLORS["espresso"]),
        xaxis_title="Persentase (%)",
        yaxis_title=""
    )

    channel = (
        data_segmen["channel_utama"]
        .value_counts(normalize=True)
        .mul(100)
        .sort_values()
    )

    fig_channel = go.Figure(
        go.Bar(
            x=channel.values,
            y=channel.index,
            orientation="h",
            marker_color=COLORS["sage"],
            hovertemplate="%{y}: %{x:.1f}%<extra></extra>"
        )
    )

    fig_channel.update_layout(
        title="Channel Pembelian",
        height=320,
        margin=dict(l=20, r=20, t=60, b=30),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color=COLORS["espresso"]),
        xaxis_title="Persentase (%)",
        yaxis_title=""
    )

    with grafik1:
        st.plotly_chart(fig_kategori, use_container_width=True)

    with grafik2:
        st.plotly_chart(fig_channel, use_container_width=True)

    st.markdown(
        '<div class="section-heading">Recommended Business Action</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background:#F0EAE1;
            border:1px solid #E3D5C6;
            border-radius:14px;
            padding:22px;
            color:#4B3428;
            line-height:1.8;
        ">
            <strong>Strategi yang Disarankan</strong><br>
            {info['strategi']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">Perbandingan Semua Segmen</div>',
        unsafe_allow_html=True
    )

    tabel_perbandingan = (
        df.groupby("segmen")
        .agg(
            Pelanggan=("id_pelanggan", "count"),
            Median_Transaksi=("jumlah_transaksi_6bln", "median"),
            Median_Belanja=("total_belanja_rp", "median"),
            Median_Recency=("hari_sejak_transaksi_terakhir", "median"),
            Median_Promo=("persen_pakai_promo", "median")
        )
        .reindex(SEGMENT_ORDER)
        .reset_index()
    )

    tabel_perbandingan.columns = [
        "Segmen",
        "Jumlah Pelanggan",
        "Median Transaksi",
        "Median Belanja (Rp)",
        "Median Recency (Hari)",
        "Median Promo (%)"
    ]

    st.dataframe(
        tabel_perbandingan,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Segmen merupakan hasil interpretasi empat cluster K-Means. "
        "Rekomendasi strategi masih berupa simulasi bisnis."
    )


elif halaman == "Prediksi Pelanggan":
    import joblib

    st.title("Prediksi Pelanggan")
    st.caption(
        "Analisis perilaku belanja pelanggan dan temukan "
        "rekomendasi promosi yang sesuai."
    )

    @st.cache_resource
    def load_model_bundle():
        return joblib.load(
            BASE_DIR / "models" / "damai_model_bundle.joblib"
        )

    try:
        model_bundle = load_model_bundle()
    except Exception as error:
        st.error(f"Model belum dapat dimuat: {error}")
        st.stop()

    st.markdown("""
    <div style="
        background:linear-gradient(120deg,#EFE5D8,#F8F2EA);
        border:1px solid #E7D8C8;
        border-radius:18px;
        padding:26px 30px;
        margin:18px 0 24px;
    ">
        <div style="
            color:#967B65;
            font-size:12px;
            font-weight:600;
            letter-spacing:2px;
        ">
            DAMAI CUSTOMER INTELLIGENCE
        </div>
        <div style="
            color:#4B3428;
            font-family:Georgia,serif;
            font-size:27px;
            margin:10px 0;
        ">
            Every customer has a story.
        </div>
        <div style="color:#765F50;line-height:1.7;">
            Masukkan ringkasan transaksi selama enam bulan
            untuk mengenali karakteristik pelanggan dan
            menentukan strategi promosi yang relevan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">Customer Information</div>',
        unsafe_allow_html=True
    )

    with st.form("form_prediksi_damai"):
        c1, c2 = st.columns(2)

        with c1:
            jumlah_transaksi = st.number_input(
                "Jumlah Transaksi / 6 Bulan",
                min_value=1,
                max_value=10000,
                value=28,
                step=1
            )

            total_belanja = st.number_input(
                "Total Belanja / 6 Bulan (Rp)",
                min_value=1,
                max_value=1000000000,
                value=1300000,
                step=10000
            )

        with c2:
            hari_terakhir = st.number_input(
                "Hari Sejak Transaksi Terakhir",
                min_value=0,
                max_value=183,
                value=5,
                step=1
            )

            persen_promo = st.slider(
                "Persentase Transaksi Menggunakan Promo (%)",
                min_value=0,
                max_value=100,
                value=20
            )

        kategori_favorit = st.selectbox(
            "Kategori Produk Favorit",
            options=sorted(
                df["kategori_favorit"]
                .dropna()
                .unique()
                .tolist()
            ),
            format_func=lambda x: x.replace("_", " ").title()
        )

        st.caption(
            "Kategori favorit digunakan untuk informasi produk. "
            "Model K-Means menggunakan empat indikator transaksi."
        )

        submitted = st.form_submit_button(
            "Analisis Pelanggan",
            type="primary",
            use_container_width=True
        )

    if submitted:
        data_baru = pd.DataFrame([{
            "hari_sejak_transaksi_terakhir": hari_terakhir,
            "jumlah_transaksi_6bln": jumlah_transaksi,
            "total_belanja_rp": total_belanja,
            "persen_pakai_promo": persen_promo
        }])

        try:
            label_cluster = int(
                model_bundle["pipeline"].predict(
                    data_baru[model_bundle["fitur"]]
                )[0]
            )

            segmen = model_bundle["nama_segmen"][label_cluster]

            membership = (
                "Gold"
                if total_belanja >= model_bundle["batas_gold"]
                else "Green"
            )

            promo = model_bundle["strategi_promo"][segmen]

            benefit = model_bundle[
                "benefit_membership"
            ][membership]

            st.session_state["hasil_prediksi_damai"] = {
                "cluster": label_cluster,
                "segmen": segmen,
                "membership": membership,
                "promo": promo,
                "benefit": benefit,
                "kategori": kategori_favorit,
                "transaksi": jumlah_transaksi,
                "belanja": total_belanja,
                "recency": hari_terakhir,
                "persen_promo": persen_promo
            }

        except Exception as error:
            st.error(f"Prediksi gagal dijalankan: {error}")

    if "hasil_prediksi_damai" in st.session_state:
        hasil = st.session_state["hasil_prediksi_damai"]

        st.markdown(
            '<div class="section-heading">Customer Analysis Result</div>',
            unsafe_allow_html=True
        )

        hasil1, hasil2 = st.columns(2)

        with hasil1:
            st.metric(
                "Customer Segment",
                hasil["segmen"]
            )

        with hasil2:
            st.metric(
                "Membership Level",
                hasil["membership"]
            )

        st.markdown(
            '<div class="section-heading">Personalized Promotion</div>',
            unsafe_allow_html=True
        )

        promo = hasil["promo"]

        st.markdown(
            f"""
            <div style="
                background:#FFFFFF;
                border:1px solid #E7D8C8;
                border-left:5px solid #C9A45C;
                border-radius:14px;
                padding:24px;
                margin-bottom:20px;
            ">
                <div style="
                    font-family:Georgia,serif;
                    color:#4B3428;
                    font-size:24px;
                    margin-bottom:12px;
                ">
                    {promo["nama_promo"]}
                </div>
                <div style="
                    color:#795540;
                    font-size:17px;
                    font-weight:600;
                    margin-bottom:12px;
                ">
                    {promo["penawaran"]}
                </div>
                <div style="
                    color:#765F50;
                    line-height:1.8;
                ">
                    <strong>Syarat:</strong> {promo["syarat"]}<br>
                    <strong>Tujuan:</strong> {promo["tujuan"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-heading">Membership Benefits</div>',
            unsafe_allow_html=True
        )

        if hasil["membership"] == "Gold":
            st.success(
                f"Gold Member — {hasil['benefit']}"
            )
        else:
            st.info(
                f"Green Member — {hasil['benefit']}"
            )

        with st.expander("Lihat ringkasan data pelanggan"):
            ringkasan_input = pd.DataFrame({
                "Indikator": [
                    "Jumlah Transaksi",
                    "Total Belanja",
                    "Hari Sejak Transaksi Terakhir",
                    "Penggunaan Promo",
                    "Kategori Favorit",
                    "Cluster K-Means"
                ],
                "Nilai": [
                    f"{hasil['transaksi']} kali",
                    f"Rp{hasil['belanja']:,.0f}",
                    f"{hasil['recency']} hari",
                    f"{hasil['persen_promo']}%",
                    hasil["kategori"].replace("_", " ").title(),
                    hasil["cluster"]
                ]
            })

            st.dataframe(
                ringkasan_input,
                use_container_width=True,
                hide_index=True
            )

        st.caption(
            "Hasil segmentasi berasal dari model K-Means yang "
            "telah dilatih. Membership dan rekomendasi promo "
            "ditentukan melalui aturan bisnis. "
            "Seluruh penawaran merupakan simulasi akademik."
        )


elif halaman == "Loyalty & Promo":
    st.title("Loyalty & Promo")
    st.caption(
        "Program keanggotaan dan strategi promosi "
        "yang disesuaikan dengan perilaku pelanggan DaMai."
    )

    jumlah_gold = int((df["membership"] == "Gold").sum())
    jumlah_green = int((df["membership"] == "Green").sum())
    total_member = len(df)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Total Member", f"{total_member:,}")

    with m2:
        st.metric(
            "Green Member",
            f"{jumlah_green:,}",
            f"{jumlah_green / total_member * 100:.2f}%",
            delta_color="off"
        )

    with m3:
        st.metric(
            "Gold Member",
            f"{jumlah_gold:,}",
            f"{jumlah_gold / total_member * 100:.2f}%",
            delta_color="off"
        )

    tab1, tab2, tab3 = st.tabs([
        "Membership Program",
        "Personalized Promotions",
        "Analisis Membership"
    ])

    with tab1:
        st.markdown(
            '<div class="section-heading">DaMai Rewards</div>',
            unsafe_allow_html=True
        )

        st.write(
            "DaMai memiliki dua tingkatan membership berdasarkan "
            "total belanja pelanggan selama enam bulan."
        )

        green_col, gold_col = st.columns(2)

        with green_col:
            with st.container(border=True):
                st.markdown("### 🌿 Green Member")
                st.caption("EVERYDAY REWARDS")

                st.markdown(
                    "**Total belanja kurang dari Rp1.000.000**"
                )

                st.write("Benefit:")
                st.write("• Akses promo reguler anggota")
                st.write("• Penawaran sesuai segmen pelanggan")
                st.write("• Kesempatan meningkatkan status ke Gold")

        with gold_col:
            with st.container(border=True):
                st.markdown("### ✨ Gold Member")
                st.caption("EXCLUSIVE REWARDS")

                st.markdown(
                    "**Total belanja minimal Rp1.000.000**"
                )

                st.write("Benefit:")
                st.write("• Seluruh akses Green Member")
                st.write("• Penawaran eksklusif anggota Gold")
                st.write("• Prioritas informasi paket dan preorder")

        st.info(
            "Membership ditentukan berdasarkan total belanja, "
            "sedangkan segmen pelanggan ditentukan oleh K-Means. "
            "Keduanya merupakan sistem yang berbeda."
        )

    with tab2:
        st.markdown(
            '<div class="section-heading">Personalized Promotions</div>',
            unsafe_allow_html=True
        )

        st.write(
            "Pilih segmen untuk melihat rekomendasi promo "
            "yang dirancang berdasarkan hasil analisis pelanggan."
        )

        pilihan_promo = st.selectbox(
            "Customer Segment",
            SEGMENT_ORDER,
            key="pilihan_promo_damai"
        )

        data_promo = df_promotions.loc[
            df_promotions["segmen"] == pilihan_promo
        ]

        if data_promo.empty:
            st.warning(
                "Strategi promo untuk segmen ini belum tersedia."
            )
        else:
            promo_terpilih = data_promo.iloc[0]

            with st.container(border=True):
                st.caption("DAMAI EXCLUSIVE OFFER")
                st.subheader(promo_terpilih["nama_promo"])

                st.markdown("**Penawaran**")
                st.write(promo_terpilih["penawaran"])

                st.markdown("**Syarat dan Ketentuan**")
                st.write(promo_terpilih["syarat"])

                st.markdown("**Tujuan Strategi**")
                st.write(promo_terpilih["tujuan"])

                st.markdown("**Masa Berlaku**")
                st.write(
                    f"{int(promo_terpilih['masa_berlaku_hari'])} hari"
                )

            p1, p2 = st.columns(2)

            jumlah_target = int(
                (df["segmen"] == pilihan_promo).sum()
            )

            with p1:
                st.metric(
                    "Pelanggan dalam Segmen",
                    f"{jumlah_target:,}"
                )

            with p2:
                st.metric(
                    "Proporsi Pelanggan",
                    f"{jumlah_target / total_member * 100:.2f}%"
                )

        st.caption(
            "Seluruh promo merupakan rancangan simulasi. "
            "Biaya dan efektivitas program belum diuji secara operasional."
        )

    with tab3:
        st.markdown(
            '<div class="section-heading">Membership by Segment</div>',
            unsafe_allow_html=True
        )

        tabel_membership = pd.crosstab(
            df["segmen"],
            df["membership"]
        ).reindex(
            index=SEGMENT_ORDER,
            columns=["Green", "Gold"],
            fill_value=0
        )

        fig_membership = go.Figure()

        for level, warna in [
            ("Green", COLORS["sage"]),
            ("Gold", COLORS["gold"])
        ]:
            fig_membership.add_trace(
                go.Bar(
                    name=level,
                    x=tabel_membership.index,
                    y=tabel_membership[level],
                    marker_color=warna,
                    text=tabel_membership[level],
                    textposition="inside",
                    hovertemplate=(
                        "%{x}<br>"
                        + level
                        + ": %{y:,} pelanggan<extra></extra>"
                    )
                )
            )

        fig_membership.update_layout(
            barmode="stack",
            height=400,
            margin=dict(l=20, r=20, t=35, b=55),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color=COLORS["espresso"]),
            xaxis_title="",
            yaxis_title="Jumlah Pelanggan",
            legend_title="Membership"
        )

        st.plotly_chart(
            fig_membership,
            use_container_width=True
        )

        st.dataframe(
            tabel_membership.reset_index().rename(
                columns={"segmen": "Segmen"}
            ),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("#### Business Insights")

        st.write(
            "Gold Member terkonsentrasi pada Loyal Customers "
            "dan Occasion Buyers. Seluruh Promo Seekers dan "
            "Inactive Customers saat ini berada pada tingkat Green."
        )

        st.caption(
            "Hasil merupakan simulasi berdasarkan dataset "
            "Januari–Juni 2026."
        )


elif halaman == "Analisis Model":
    st.title("Analisis Model")
    st.caption(
        "Evaluasi dan pengembangan model K-Means "
        "untuk segmentasi pelanggan DaMai Coffee & Bakery."
    )

    @st.cache_data
    def load_evaluation():
        baseline = pd.read_csv(
            DATA_DIR / "damai_baseline_metrics.csv"
        )
        optimized = pd.read_csv(
            DATA_DIR / "damai_optimized_metrics.csv"
        )
        return baseline, optimized

    try:
        baseline, optimized = load_evaluation()
    except (FileNotFoundError, ValueError) as error:
        st.error(f"Data evaluasi tidak dapat dimuat: {error}")
        st.stop()

    baseline = baseline.sort_values("k").copy()
    optimized = optimized.sort_values("k").copy()

    best_baseline = baseline.loc[
        baseline["Silhouette Score"].idxmax()
    ]

    best_optimized = optimized.loc[
        optimized["Silhouette Score"].idxmax()
    ]

    k_final = int(best_optimized["k"])
    silhouette_final = float(
        best_optimized["Silhouette Score"]
    )
    dbi_final = float(
        best_optimized["Davies-Bouldin Index"]
    )

    peningkatan = (
        silhouette_final
        - float(best_baseline["Silhouette Score"])
    )

    st.markdown("""
    <div class="hero">
        <div class="hero-label">MACHINE LEARNING PERFORMANCE</div>
        <div class="hero-title">
            Behind every segment,<br>
            there's a pattern.
        </div>
        <div class="hero-description">
            Evaluasi kualitas pengelompokan pelanggan menggunakan
            K-Means, perbandingan preprocessing, dan pemilihan
            jumlah cluster berdasarkan hasil eksperimen.
        </div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Jumlah Cluster", k_final)

    with m2:
        st.metric(
            "Silhouette Score",
            f"{silhouette_final:.4f}"
        )

    with m3:
        st.metric(
            "Davies-Bouldin",
            f"{dbi_final:.4f}"
        )

    with m4:
        st.metric(
            "Peningkatan Silhouette",
            f"+{peningkatan:.4f}"
        )

    tab1, tab2, tab3 = st.tabs([
        "Performa Model",
        "Evaluasi Jumlah Cluster",
        "Metodologi"
    ])

    with tab1:
        st.markdown(
            '<div class="section-heading">Model Performance</div>',
            unsafe_allow_html=True
        )

        perbandingan_model = pd.DataFrame([
            {
                "Model": "K-Means Baseline",
                "Preprocessing": "StandardScaler",
                "Jumlah Cluster": int(best_baseline["k"]),
                "Silhouette Score": float(
                    best_baseline["Silhouette Score"]
                ),
                "Davies-Bouldin Index": float(
                    best_baseline["Davies-Bouldin Index"]
                )
            },
            {
                "Model": "K-Means Optimasi",
                "Preprocessing": "Log1p + StandardScaler",
                "Jumlah Cluster": k_final,
                "Silhouette Score": silhouette_final,
                "Davies-Bouldin Index": dbi_final
            }
        ])

        st.dataframe(
            perbandingan_model,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Silhouette Score": st.column_config.NumberColumn(
                    format="%.4f"
                ),
                "Davies-Bouldin Index": st.column_config.NumberColumn(
                    format="%.4f"
                )
            }
        )

        c1, c2 = st.columns(2)

        fig_silhouette = go.Figure()

        for nama, data, warna in [
            ("Baseline", baseline, COLORS["terracotta"]),
            ("Optimasi", optimized, COLORS["sage"])
        ]:
            fig_silhouette.add_trace(
                go.Scatter(
                    x=data["k"],
                    y=data["Silhouette Score"],
                    mode="lines+markers",
                    name=nama,
                    line=dict(color=warna, width=3),
                    marker=dict(size=9)
                )
            )

        fig_silhouette.update_layout(
            title="Silhouette Score",
            height=360,
            xaxis=dict(
                title="Jumlah Cluster (k)",
                dtick=1
            ),
            yaxis=dict(title="Silhouette Score"),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color=COLORS["espresso"]),
            margin=dict(l=30, r=20, t=60, b=40),
            legend=dict(orientation="h", y=-0.3)
        )

        fig_dbi = go.Figure()

        for nama, data, warna in [
            ("Baseline", baseline, COLORS["terracotta"]),
            ("Optimasi", optimized, COLORS["sage"])
        ]:
            fig_dbi.add_trace(
                go.Scatter(
                    x=data["k"],
                    y=data["Davies-Bouldin Index"],
                    mode="lines+markers",
                    name=nama,
                    line=dict(color=warna, width=3),
                    marker=dict(size=9)
                )
            )

        fig_dbi.update_layout(
            title="Davies-Bouldin Index",
            height=360,
            xaxis=dict(
                title="Jumlah Cluster (k)",
                dtick=1
            ),
            yaxis=dict(title="Davies-Bouldin Index"),
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color=COLORS["espresso"]),
            margin=dict(l=30, r=20, t=60, b=40),
            legend=dict(orientation="h", y=-0.3)
        )

        with c1:
            st.plotly_chart(
                fig_silhouette,
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                fig_dbi,
                use_container_width=True
            )

        st.success(
            f"Model optimasi memperoleh Silhouette Score "
            f"{silhouette_final:.4f}, meningkat "
            f"{peningkatan:.4f} poin dibandingkan baseline. "
            f"Davies-Bouldin Index juga lebih rendah, "
            f"menunjukkan perbaikan kualitas cluster "
            f"menurut kedua metrik tersebut."
        )

    with tab2:
        st.markdown(
            '<div class="section-heading">Cluster Evaluation</div>',
            unsafe_allow_html=True
        )

        st.write(
            "Jumlah cluster diuji dari k=2 hingga k=8. "
            "Evaluasi mempertimbangkan Silhouette Score, "
            "Inertia, Davies-Bouldin Index, dan "
            "Calinski-Harabasz Score."
        )

        fig_elbow = go.Figure()

        fig_elbow.add_trace(
            go.Scatter(
                x=optimized["k"],
                y=optimized["Inertia"],
                mode="lines+markers",
                line=dict(
                    color=COLORS["coffee"],
                    width=3
                ),
                marker=dict(size=10)
            )
        )

        fig_elbow.update_layout(
            title="Elbow Method — Model Optimasi",
            xaxis=dict(
                title="Jumlah Cluster (k)",
                dtick=1
            ),
            yaxis=dict(title="Inertia"),
            height=370,
            paper_bgcolor="white",
            plot_bgcolor="white",
            font=dict(color=COLORS["espresso"]),
            margin=dict(l=30, r=30, t=60, b=40)
        )

        st.plotly_chart(
            fig_elbow,
            use_container_width=True
        )

        st.markdown("#### Hasil Evaluasi Lengkap")

        pilihan_evaluasi = st.radio(
            "Pilih model",
            ["Optimasi", "Baseline"],
            horizontal=True
        )

        data_evaluasi = (
            optimized
            if pilihan_evaluasi == "Optimasi"
            else baseline
        )

        st.dataframe(
            data_evaluasi.round(4),
            use_container_width=True,
            hide_index=True
        )

        st.info(
            f"Berdasarkan Silhouette Score, jumlah cluster "
            f"terbaik pada model optimasi adalah k={k_final}. "
            f"Pemilihan model juga mempertimbangkan "
            f"karakteristik dan kegunaan segmen bagi UMKM."
        )

    with tab3:
        st.markdown(
            '<div class="section-heading">Model Methodology</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        #### 1. Dataset

        Dataset terdiri atas 10.000 pelanggan unik DaMai
        Coffee & Bakery berdasarkan ringkasan transaksi
        selama enam bulan hingga Juni 2026.

        #### 2. Algoritma

        Model menggunakan K-Means Clustering, yaitu metode
        unsupervised learning yang mengelompokkan pelanggan
        berdasarkan kedekatan karakteristik.

        #### 3. Fitur Clustering

        - Recency: hari sejak transaksi terakhir.
        - Frequency: jumlah transaksi enam bulan.
        - Monetary: total belanja enam bulan.
        - Promo Usage: persentase penggunaan promo.

        #### 4. Preprocessing

        - Penanganan missing values menggunakan median.
        - Transformasi log1p pada Recency, Frequency,
          dan Monetary untuk model optimasi.
        - StandardScaler untuk menyamakan skala fitur.

        #### 5. Evaluasi

        - Silhouette Score: semakin tinggi semakin baik.
        - Davies-Bouldin Index: semakin rendah semakin baik.
        - Inertia: digunakan dalam Elbow Method.
        - Calinski-Harabasz Score: semakin tinggi semakin baik.

        #### 6. Kestabilan

        Pengujian pada notebook menggunakan random seed
        21, 42, dan 123 menghasilkan Adjusted Rand Index
        sebesar 1,0 terhadap hasil model acuan untuk
        ketiga pengujian tersebut.

        #### 7. Implementasi Bisnis

        Hasil K-Means diterjemahkan menjadi empat segmen:
        Loyal Customers, Inactive Customers, Occasion Buyers,
        dan Promo Seekers.

        Membership Green/Gold dan rekomendasi promo dibuat
        menggunakan aturan bisnis terpisah.
        """)

        st.warning(
            "Evaluasi clustering tidak sama dengan akurasi "
            "klasifikasi. Hasil ini menunjukkan kualitas "
            "pengelompokan pada dataset simulasi, bukan "
            "jaminan peningkatan penjualan atau efektivitas "
            "promosi di dunia nyata."
        )

    st.divider()
    st.caption(
        "DaMai Coffee & Bakery • K-Means Model Evaluation • 2026"
    )
