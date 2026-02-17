import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Garment Accounting Dashboard", layout="wide")

# Gaya CSS Custom untuk tampilan elegan
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA DUMMY ---
data = {
    'Tanggal': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']),
    'Pendapatan': [50000000, 75000000, 60000000, 90000000],
    'Pengeluaran': [30000000, 40000000, 35000000, 45000000],
    'Kategori': ['Bahan Baku', 'Gaji Karyawan', 'Listrik/Air', 'Logistik']
}
df = pd.DataFrame(data)
df['Profit'] = df['Pendapatan'] - df['Pengeluaran']

# --- SIDEBAR ---
st.sidebar.header("Filter Akuntansi")
rentang_waktu = st.sidebar.date_input("Pilih Rentang Waktu", [])

# --- HEADER ---
st.title("🧵 Garment System Accounting Dashboard")
st.markdown("Monitor kesehatan finansial produksi garmen Anda secara real-time.")

# --- METRICS (KPI) ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Pendapatan", f"Rp {df['Pendapatan'].sum():,}", "+12%")
col2.metric("Total Pengeluaran", f"Rp {df['Pengeluaran'].sum():,}", "-5%")
col3.metric("Net Profit", f"Rp {df['Profit'].sum():,}", "+15%")

st.divider()

# --- VISUALISASI ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Tren Laba Bersih")
    fig_line = px.line(df, x='Tanggal', y='Profit', markers=True, 
                       line_shape='spline', color_discrete_sequence=['#2E86C1'])
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    st.subheader("Distribusi Pengeluaran")
    fig_pie = px.pie(df, values='Pengeluaran', names='Kategori', 
                     hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- DATA TABLE ---
st.subheader("Detail Transaksi Terakhir")
st.dataframe(df, use_container_width=True)