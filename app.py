import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import io
from datetime import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Garment Accounting Pro", page_icon="🧵", layout="wide")

# 2. DATA UTAMA
@st.cache_data
def load_data():
    data = {
        'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
        'Realisasi': [4500, 5200, 4800, 6100, 5900],
        'Target': [5000, 5000, 5000, 6000, 6000],
        'Pendapatan': [50000000, 75000000, 60000000, 90000000, 85000000],
        'Pengeluaran': [30000000, 42000000, 35000000, 48000000, 40000000]
    }
    df_result = pd.DataFrame(data)
    df_result['Profit'] = df_result['Pendapatan'] - df_result['Pengeluaran']
    return df_result

df_master = load_data()

# 3. SIDEBAR FILTER
st.sidebar.header("🔍 Filter Laporan")
bulan_pilihan = st.sidebar.multiselect(
    "Pilih Bulan:",
    options=df_master['Bulan'].unique(),
    default=df_master['Bulan'].unique()
)

# Filter Data Berdasarkan Pilihan
df_filtered = df_master[df_master['Bulan'].isin(bulan_pilihan)]

# 4. CUSTOM CSS (Dark Mode & Footer)
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

# 5. HEADER & METRICS (Berdasarkan Data Terfilter)
st.title("🧵 Garment Production & Accounting")
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Pendapatan", f"Rp {df_filtered['Pendapatan'].sum():,}")
col2.metric("📉 Total Biaya", f"Rp {df_filtered['Pengeluaran'].sum():,}")
col3.metric("💎 Net Profit", f"Rp {df_filtered['Profit'].sum():,}")

st.divider()

# 6. TABEL DENGAN FORMAT RUPIAH
st.subheader("📝 Detail Transaksi (Format Rupiah)")

df_display = df_filtered.copy()

# Gunakan fungsi lambda untuk memformat agar checker tipe data senang
st.dataframe(
    df_display.style.format({
        'Pendapatan': lambda x: f"Rp {x:,.0f}",
        'Pengeluaran': lambda x: f"Rp {x:,.0f}",
        'Profit': lambda x: f"Rp {x:,.0f}"
    }), 
    use_container_width=True
)

# 7. FITUR EKSPOR (Hanya mengekspor data yang difilter)
def to_excel(df_to_save):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_to_save.to_excel(writer, index=False, sheet_name='Laporan_Filter')
    return output.getvalue()

st.download_button(
    label="📥 Download Data Terfilter ke Excel",
    data=to_excel(df_filtered),
    file_name=f"Laporan_Garmen_Filtered_{datetime.now().strftime('%H%M%S')}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
# . FOOTER CUSTOM
st.markdown("""
    <div class="custom-footer">
        © 2026 Garment Accounting System | Build with ❤️ using Python & Streamlit | <a href="https://github.com/agunggema-debug/dashboard-akuntansi.git" style="color: #2E86C1;">GitHub Repository</a>
    </div>
    """, unsafe_allow_html=True)