import streamlit as st
import pandas as pd
import io
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Garment Production Pro", page_icon="🧵", layout="wide")

# 2. DATA UTAMA (Ditambah kolom Target)
@st.cache_data
def load_data():
    data = {
        'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
        'Realisasi': [4500, 5200, 4800, 6100, 5900], # Jumlah pcs garmen
        'Target': [5000, 5000, 5000, 6000, 6000],
        'Pendapatan': [50000000, 75000000, 60000000, 90000000, 85000000],
        'Pengeluaran': [30000000, 42000000, 35000000, 48000000, 40000000]
    }
    # Data Kategori Pengeluaran (Contoh rata-rata per bulan)
    data_kategori = {
        'Kategori': ['Bahan Baku', 'Gaji Karyawan', 'Listrik & Air', 'Logistik', 'Maintenance'],
        'Nilai': [45, 30, 10, 10, 5]  # Dalam persentase atau nilai total
    }

    df_result = pd.DataFrame(data)
    df_result['Profit'] = df_result['Pendapatan'] - df_result['Pengeluaran']
    df_kat= pd.DataFrame(data_kategori)
    return df_result, df_kat

df, df_kategori = load_data()
# Memformat kolom angka menjadi Rupiah menggunakan Styler
def format_rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")
# 3. CUSTOM CSS (Dark Mode & Footer)
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 10px;
    }
    footer {
        visibility: hidden;
    }
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #777;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

#4.  SIDEBAR FILTER
st.sidebar.header("🔍 Filter Laporan")
bulan_pilihan = st.sidebar.multiselect(
    "Pilih Bulan:",
    options=df['Bulan'].unique(),
    default=df['Bulan'].unique()
)

# Filter Data Berdasarkan Pilihan
df_filtered = df[df['Bulan'].isin(bulan_pilihan)]


# 5. CUSTOM CSS (Dark Mode & Footer)
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 10px;
    }
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: #777;
        text-align: center; padding: 10px; font-size: 14px;
        border-top: 1px solid #333; z-index: 100;
    }
    </style>
    """, unsafe_allow_html=True)

# 6. HEADER
st.title("🧵 Garment Production & Accounting")
st.write(f"Update Terakhir: {datetime.now().strftime('%d %B %Y')}")

# 7. KPI METRICS
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Produksi", f"{df_filtered['Realisasi'].sum():,} Pcs", "Realisasi")
col2.metric("🎯 Total Target", f"{df_filtered['Target'].sum():,} Pcs", "Kapasitas")
col3.metric("💰 Efisiensi Biaya", "88%", "+2.5%")

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Pendapatan", f"Rp {df_filtered['Pendapatan'].sum():,}")
col2.metric("📉 Total Biaya", f"Rp {df_filtered['Pengeluaran'].sum():,}")
col3.metric("💎 Net Profit", f"Rp {df_filtered['Profit'].sum():,}")

st.divider()


# 8. GRAFIK TARGET VS REALISASI 

# VISUALISASI: BAR CHART & PIE CHART
col_grafik1, col_grafik2 = st.columns([6, 4])

with col_grafik1:
    st.subheader("📊 Target vs Realisasi Produksi")
    fig_prod = go.Figure()
    fig_prod.add_trace(go.Bar(x=df_filtered['Bulan'], y=df_filtered['Target'], name='Target', marker_color='gray'))
    fig_prod.add_trace(go.Bar(x=df_filtered['Bulan'], y=df_filtered['Realisasi'], name='Realisasi', marker_color='#00CC96'))
    fig_prod.update_layout(barmode='group', template="plotly_dark", height=400)
    st.plotly_chart(fig_prod, use_container_width=True)

with col_grafik2:
    st.subheader("🍕 Struktur Biaya")
    fig_pie = px.pie(
        df_kategori, 
        values='Nilai', 
        names='Kategori',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.RdBu,
        template="plotly_dark"
    )
    fig_pie.update_layout(height=400)
    st.plotly_chart(fig_pie, use_container_width=True)


# 9. TABEL DATA
with st.expander("Lihat Detail Data Mentah"):
    # 1. Salin dataframe agar data asli tidak berubah formatnya (penting untuk perhitungan)
    df_raw_display = df_filtered.copy()

    # 2. Definisikan kolom yang ingin diformat ke Rupiah
    kolom_uang = ['Pendapatan', 'Pengeluaran', 'Profit']

    # 3. Terapkan format Rupiah (Contoh: Rp 50.000.000)
    for col in kolom_uang:
        df_raw_display[col] = df_raw_display[col].apply(lambda x: f"Rp {x:,.0f}".replace(",", "."))

    # 4. Tampilkan tabel
    st.table(df_raw_display)

st.divider()
st.subheader("📥 Ekspor Laporan")

# Fungsi untuk mengonversi DataFrame ke Excel
def to_excel(df):
    output = io.BytesIO()
    # Menggunakan context manager agar file tertutup otomatis
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Laporan_Garmen')
    processed_data = output.getvalue()
    return processed_data

# Membuat data excel
excel_data = to_excel(df)

# Tombol Unduh
st.download_button(
    label="Download Laporan Excel (XLSX)",
    data=excel_data,
    file_name=f"Laporan_Garmen_{datetime.now().strftime('%Y-%m-%d')}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    help="Klik untuk mengunduh seluruh data dalam format Excel"
)
# . FOOTER CUSTOM
st.markdown("""
    <div class="custom-footer">
        © 2026 Garment Accounting System | Build with ❤️ using Python & Streamlit | <a href="https://github.com/agunggema-debug/dashboard-akuntansi.git" style="color: #2E86C1;">GitHub Repository</a>
    </div>
    """, unsafe_allow_html=True)