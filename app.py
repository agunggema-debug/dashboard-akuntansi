import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Garment Accounting Dashboard", 
    page_icon="🧵",
    layout="wide"
)

# 2. DATA UTAMA (Definisikan 'df' di sini)
@st.cache_data
def load_data():
    data = {
        'Tanggal': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']),
        'Pendapatan': [50000000, 75000000, 60000000, 90000000],
        'Pengeluaran': [30000000, 42000000, 35000000, 48000000],
        'Kategori': ['Bahan Baku', 'Gaji Karyawan', 'Listrik/Air', 'Logistik']
    }
    df_result = pd.DataFrame(data)
    df_result['Profit'] = df_result['Pendapatan'] - df_result['Pengeluaran']
    return df_result

df = load_data()

# 3. CUSTOM CSS (Optimasi Dark Mode & Badge)
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 12px;
    }
    .main {
        background-color: #0e1117;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.title("🧵 Garment Accounting System")
st.write("Visualisasi keuangan produksi secara otomatis.")

# 5. BAGIAN METRIK (KPI) DENGAN IKON
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="💰 Total Pendapatan", 
        value=f"Rp {df['Pendapatan'].sum():,}", 
        delta="12% YoY"
    )

with col2:
    # delta_color="inverse" karena penurunan biaya adalah hal positif (hijau)
    st.metric(
        label="📉 Total Biaya", 
        value=f"Rp {df['Pengeluaran'].sum():,}", 
        delta="-5% Efisiensi",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="💎 Net Profit", 
        value=f"Rp {df['Profit'].sum():,}", 
        delta="15% Margin"
    )

st.divider()

# 6. GRAFIK TREN (Plotly otomatis menyesuaikan Dark Mode)
st.subheader("Analisis Performa Bulanan")
fig_line = px.area(df, x='Tanggal', y='Profit', 
                   title="Tren Keuntungan Bersih",
                   template="plotly_dark", # Tema gelap untuk grafik
                   color_discrete_sequence=['#00CC96'])
st.plotly_chart(fig_line, use_container_width=True)

# 7. TABEL DATA
st.subheader("Data Transaksi Terperinci")
st.dataframe(df, use_container_width=True)