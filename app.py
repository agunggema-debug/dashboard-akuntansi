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
    df_result = pd.DataFrame(data)
    df_result['Profit'] = df_result['Pendapatan'] - df_result['Pengeluaran']
    return df_result

df = load_data()

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

# 4. HEADER
st.title("🧵 Garment Production & Accounting")
st.write(f"Update Terakhir: {datetime.now().strftime('%d %B %Y')}")

# 5. KPI METRICS
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Produksi", f"{df['Realisasi'].sum():,} Pcs", "Realisasi")
col2.metric("🎯 Total Target", f"{df['Target'].sum():,} Pcs", "Kapasitas")
col3.metric("💰 Efisiensi Biaya", "88%", "+2.5%")

st.divider()

# 6. GRAFIK TARGET VS REALISASI (Grouped Bar Chart)
st.subheader("📊 Perbandingan Target vs Realisasi Produksi")

fig_prod = go.Figure()

# Bar untuk Target
fig_prod.add_trace(go.Bar(
    x=df['Bulan'],
    y=df['Target'],
    name='Target Produksi',
    marker_color='rgba(158, 158, 158, 0.5)' # Abu-abu transparan
))

# Bar untuk Realisasi
fig_prod.add_trace(go.Bar(
    x=df['Bulan'],
    y=df['Realisasi'],
    name='Realisasi Produksi',
    marker_color='#00CC96' # Hijau cerah
))

fig_prod.update_layout(
    barmode='group', 
    template="plotly_dark",
    xaxis_title="Bulan",
    yaxis_title="Jumlah (Pcs)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig_prod, use_container_width=True)



# 7. TABEL DATA
with st.expander("Lihat Detail Data Mentah"):
    st.table(df)

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