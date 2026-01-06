"""
🚀 PROFESSIONAL MARKET ANALYTICS PLATFORM - CRYSTAL CLEAR EDITION
=================================================================
Perfect Clarity • Sharp Text • Proper Alignment • No Blur
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import requests
import time
from scipy import stats as scipy_stats
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Market Intelligence Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CRYSTAL CLEAR CSS - NO BLUR, PERFECT ALIGNMENT
# ============================================================================

st.markdown("""
    <style>
    /* Import Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* RESET BLUR - Make Everything Sharp */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        -webkit-font-smoothing: antialiased !important;
        -moz-osx-font-smoothing: grayscale !important;
        text-rendering: optimizeLegibility !important;
    }
    
    /* Remove ALL blur effects */
    .main, .block-container, [data-testid="stSidebar"] {
        backdrop-filter: none !important;
        filter: none !important;
    }
    
    /* Dark Background - NO Blur */
    .main {
        background: #0a0e27 !important;
        color: #ffffff !important;
        padding-top: 0 !important;
    }
    
    .block-container {
        padding: 1rem 1rem 2rem 1rem !important;
        background: #0f1419 !important;
        border-radius: 0 !important;
        max-width: 100% !important;
        margin-top: 0 !important;
    }
    
    /* Fix Streamlit Header Toolbar Overlap */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Ensure disclaimer banner is visible */
    .element-container:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Perfect Metric Cards - Clear & Sharp */
    .stMetric {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.25) !important;
        transition: transform 0.2s ease !important;
    }
    
    .stMetric:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.35) !important;
    }
    
    .stMetric label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        margin-bottom: 0.5rem !important;
        display: block !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.875rem !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        margin: 0.5rem 0 !important;
    }
    
    .stMetric [data-testid="stMetricDelta"] {
        color: #fbbf24 !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }
    
    /* Crystal Clear Buttons - NO Text Wrap */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        width: 100% !important;
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: clip !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.25) !important;
        transition: all 0.2s ease !important;
        height: auto !important;
        min-height: 3rem !important;
        line-height: 1.5 !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(139, 92, 246, 0.4) !important;
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
    }
    
    /* Sharp Sidebar - NO Blur */
    [data-testid="stSidebar"] {
        background: #0f1419 !important;
        border-right: 1px solid rgba(139, 92, 246, 0.2) !important;
        padding: 2rem 1rem !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Fix Sidebar Text Overlap */
    [data-testid="stSidebar"] .element-container {
        margin-bottom: 1rem !important;
    }
    
    [data-testid="stSidebar"] h3 {
        margin-top: 1.5rem !important;
        margin-bottom: 0.75rem !important;
        clear: both !important;
    }
    
    [data-testid="stSidebar"] .stTextInput > label,
    [data-testid="stSidebar"] .stSelectbox > label {
        display: block !important;
        margin-bottom: 0.5rem !important;
        clear: both !important;
    }
    
    [data-testid="stSidebar"] .stTextInput > div,
    [data-testid="stSidebar"] .stSelectbox > div {
        margin-top: 0.5rem !important;
        margin-bottom: 1rem !important;
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.75rem !important;
        display: block !important;
        clear: both !important;
    }
    
    /* Clear Info Boxes */
    .info-box {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        color: #ffffff !important;
    }
    
    .info-box h3 {
        color: #ffffff !important;
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
    }
    
    .info-box p {
        color: rgba(255, 255, 255, 0.8) !important;
        margin: 0 !important;
        font-size: 0.875rem !important;
        line-height: 1.5 !important;
    }
    
    /* Success Box */
    .success-box {
        background: rgba(16, 185, 129, 0.15) !important;
        border: 1px solid rgba(16, 185, 129, 0.4) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
    }
    
    .success-box h3 {
        color: #10b981 !important;
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
    }
    
    .success-box p {
        color: rgba(16, 185, 129, 0.9) !important;
        margin: 0 !important;
        font-size: 0.875rem !important;
    }
    
    /* Pattern Cards - Color Coded */
    .pattern-card {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 2px solid !important;
        border-radius: 12px !important;
        padding: 1.25rem !important;
        margin: 0.75rem 0 !important;
        transition: transform 0.2s ease !important;
    }
    
    .pattern-card:hover {
        transform: translateX(4px) !important;
    }
    
    .pattern-card h4 {
        margin: 0 0 0.5rem 0 !important;
        font-size: 1.125rem !important;
        font-weight: 700 !important;
        line-height: 1.3 !important;
    }
    
    .pattern-card p {
        margin: 0 !important;
        font-size: 0.875rem !important;
        line-height: 1.5 !important;
        opacity: 0.9 !important;
    }
    
    .pattern-bullish {
        border-color: #10b981 !important;
        color: #10b981 !important;
    }
    
    .pattern-bearish {
        border-color: #ef4444 !important;
        color: #ef4444 !important;
    }
    
    .pattern-warning {
        border-color: #f59e0b !important;
        color: #f59e0b !important;
    }
    
    .pattern-opportunity {
        border-color: #3b82f6 !important;
        color: #3b82f6 !important;
    }
    
    /* Sharp Input Fields */
    .stTextInput > div > div > input,
    .stTextInput input {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.9375rem !important;
        font-weight: 500 !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.15) !important;
        outline: none !important;
    }
    
    .stTextInput label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Select Box */
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }
    
    /* Number Input */
    .stNumberInput label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }
    
    .stNumberInput input {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }
    
    /* Slider */
    .stSlider label {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
    }
    
    /* Radio Buttons */
    .stRadio div[role="radiogroup"] label {
        background: rgba(99, 102, 241, 0.1) !important;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    .stRadio div[role="radiogroup"] label:hover {
        border-color: #8b5cf6 !important;
        background: rgba(99, 102, 241, 0.15) !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(99, 102, 241, 0.15) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 8px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 1rem !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(99, 102, 241, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%) !important;
    }
    
    /* Headers - Clear & Sharp */
    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 2.5rem !important;
        line-height: 1.2 !important;
        margin: 1rem 0 !important;
        text-align: center !important;
    }
    
    h2 {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.875rem !important;
        line-height: 1.3 !important;
        margin: 1.5rem 0 1rem 0 !important;
    }
    
    h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 1.25rem !important;
        line-height: 1.4 !important;
        margin: 1rem 0 0.75rem 0 !important;
    }
    
    /* Regular Text */
    p, span, div, label {
        color: #ffffff !important;
    }
    
    /* Divider */
    hr {
        border: none !important;
        height: 1px !important;
        background: rgba(139, 92, 246, 0.2) !important;
        margin: 2rem 0 !important;
    }
    
    /* Badge - Sharp */
    .badge {
        display: inline-block !important;
        padding: 0.5rem 1rem !important;
        border-radius: 20px !important;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        font-size: 0.8125rem !important;
        font-weight: 600 !important;
        margin: 0.25rem !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        white-space: nowrap !important;
    }
    
    /* DataFrame */
    .dataframe {
        border: 1px solid rgba(139, 92, 246, 0.2) !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    /* Ensure Everything is Readable */
    .stMarkdown, .stText {
        color: #ffffff !important;
    }
    
    /* Remove any text shadows that cause blur */
    * {
        text-shadow: none !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }
    
    ::-webkit-scrollbar-track {
        background: #0f1419 !important;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #6366f1 !important;
        border-radius: 4px !important;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #8b5cf6 !important;
    }
    
    /* CRITICAL: Fix Header Cropping */
    .main .block-container {
        padding-top: 3rem !important;
        max-width: 100% !important;
    }
    
    /* Ensure top disclaimer is never cropped */
    section[data-testid="stAppViewContainer"] {
        padding-top: 0 !important;
    }
    
    section[data-testid="stAppViewContainer"] > div:first-child {
        padding-top: 1rem !important;
    }
    
    /* Fix Streamlit toolbar overlap */
    header[data-testid="stHeader"] {
        background-color: rgba(10, 14, 39, 0.8) !important;
        backdrop-filter: blur(10px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Continue with rest of app...

# ============================================================================
# CRYSTAL CLEAR HEADER
# ============================================================================

# Legal Disclaimer Banner
st.markdown("""
    <div style='background: rgba(239, 68, 68, 0.15); border: 2px solid #ef4444; 
                border-radius: 12px; padding: 1rem; margin-bottom: 1.5rem;'>
        <p style='margin: 0; font-size: 0.875rem; color: #ef4444; font-weight: 600; text-align: center;'>
            ⚠️ <b>DISCLAIMER:</b> This is an educational tool for learning purposes only. 
            NOT financial advice. NOT a recommendation to buy or sell securities. 
            Past performance does not guarantee future results. Consult a licensed financial advisor before investing.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 2rem 0; margin-bottom: 2rem;'>
        <h1 style='font-size: 3rem; margin-bottom: 1rem; font-weight: 800;'>
            📊 Market Intelligence
        </h1>
        <p style='font-size: 1.125rem; color: rgba(255,255,255,0.7); margin-bottom: 1.5rem; font-weight: 500;'>
            Real-Time Data • Advanced Analytics • Professional Grade
        </p>
        <div style='display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap;'>
            <span class='badge'>🔴 LIVE</span>
            <span class='badge'>📈 REAL-TIME</span>
            <span class='badge'>🤖 AI-POWERED</span>
            <span class='badge'>⚡ LIGHTNING FAST</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================

if 'alpha_vantage_key' not in st.session_state:
    st.session_state.alpha_vantage_key = 'demo'
if 'twelve_data_key' not in st.session_state:
    st.session_state.twelve_data_key = ''

# ============================================================================
# DATA FUNCTIONS
# ============================================================================

@st.cache_data(ttl=300, show_spinner=False)
def fetch_alpha_vantage(symbol, api_key):
    try:
        url = "https://www.alphavantage.co/query"
        params = {"function": "TIME_SERIES_DAILY", "symbol": symbol, "outputsize": "full", "apikey": api_key}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if "Time Series (Daily)" in data:
            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df.index = pd.to_datetime(df.index)
            df = df.sort_index()
            for col in df.columns:
                df[col] = pd.to_numeric(df[col])
            return df, None
        elif "Note" in data:
            return None, "Rate limit"
        else:
            return None, data.get('Error Message', 'Error')
    except Exception as e:
        return None, str(e)

@st.cache_data(ttl=300, show_spinner=False)
def fetch_twelve_data(symbol, api_key):
    if not api_key:
        return None, "No key"
    try:
        url = "https://api.twelvedata.com/time_series"
        params = {"symbol": symbol, "interval": "1day", "outputsize": 365, "apikey": api_key}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data.get("status") == "ok" and "values" in data:
            df = pd.DataFrame(data["values"])
            df['datetime'] = pd.to_datetime(df['datetime'])
            df = df.set_index('datetime').sort_index()
            df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'})
            for col in df.columns:
                df[col] = pd.to_numeric(df[col])
            return df, None
        else:
            return None, data.get("message", "Error")
    except Exception as e:
        return None, str(e)

@st.cache_data(ttl=300, show_spinner=False)
def fetch_yfinance_safe(symbol):
    try:
        import yfinance as yf
        time.sleep(2)
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="2y")
        return df if not df.empty else (None, "No data")
    except Exception as e:
        return None, str(e)

def get_stock_data(symbol, api_source='alpha_vantage'):
    if api_source in ['alpha_vantage', 'auto']:
        df, error = fetch_alpha_vantage(symbol, st.session_state.alpha_vantage_key)
        if df is not None:
            return df, None, 'Alpha Vantage'
    if api_source in ['twelve_data', 'auto'] and st.session_state.twelve_data_key:
        df, error = fetch_twelve_data(symbol, st.session_state.twelve_data_key)
        if df is not None:
            return df, None, 'Twelve Data'
    if api_source in ['yfinance', 'auto']:
        df, error = fetch_yfinance_safe(symbol)
        if df is not None:
            return df, None, 'Yahoo Finance'
    return None, "All failed", None

def calculate_indicators(df):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['BB_Middle'] = df['Close'].rolling(window=20).mean()
    std = df['Close'].rolling(window=20).std()
    df['BB_Upper'] = df['BB_Middle'] + (std * 2)
    df['BB_Lower'] = df['BB_Middle'] - (std * 2)
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    df['MA_200'] = df['Close'].rolling(window=200).mean()
    return df

def detect_patterns(df):
    patterns = []
    if len(df) < 50:
        return patterns
    if df['MA_50'].iloc[-1] > df['MA_200'].iloc[-1] and df['MA_50'].iloc[-2] <= df['MA_200'].iloc[-2]:
        patterns.append(("🌟 Golden Cross", "Bullish", "MA50 crossed above MA200"))
    if df['MA_50'].iloc[-1] < df['MA_200'].iloc[-1] and df['MA_50'].iloc[-2] >= df['MA_200'].iloc[-2]:
        patterns.append(("💀 Death Cross", "Bearish", "MA50 crossed below MA200"))
    if df['RSI'].iloc[-1] > 70:
        patterns.append(("📈 RSI Overbought", "Warning", f"RSI at {df['RSI'].iloc[-1]:.1f}"))
    elif df['RSI'].iloc[-1] < 30:
        patterns.append(("📉 RSI Oversold", "Opportunity", f"RSI at {df['RSI'].iloc[-1]:.1f}"))
    if df['Close'].iloc[-1] > df['BB_Upper'].iloc[-1]:
        patterns.append(("🚀 BB Breakout", "Strong", "Above upper band"))
    elif df['Close'].iloc[-1] < df['BB_Lower'].iloc[-1]:
        patterns.append(("⚠️ BB Breakdown", "Weak", "Below lower band"))
    return patterns

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 1.5rem;'>
            <div style='font-size: 2.5rem; margin-bottom: 0.75rem;'>⚙️</div>
            <h3 style='margin: 0; font-weight: 700;'>Configuration</h3>
        </div>
    """, unsafe_allow_html=True)
    
    with st.expander("🔑 API Keys", expanded=True):
        st.markdown("**Alpha Vantage**")
        alpha_key = st.text_input("API Key", value=st.session_state.alpha_vantage_key, type="password", key="alpha_input")
        if alpha_key != st.session_state.alpha_vantage_key:
            st.session_state.alpha_vantage_key = alpha_key
        if st.session_state.alpha_vantage_key != 'demo':
            st.success("✅ Configured")
        else:
            st.warning("⚠️ Demo key")
        st.markdown("---")
        st.markdown("**Twelve Data (Optional)**")
        twelve_key = st.text_input("API Key", value=st.session_state.twelve_data_key, type="password", key="twelve_input")
        if twelve_key != st.session_state.twelve_data_key:
            st.session_state.twelve_data_key = twelve_key
    
    st.markdown("---")
    st.markdown("### 🌐 Data Source")
    api_source = st.radio("", ['auto', 'alpha_vantage', 'twelve_data', 'yfinance'],
        format_func=lambda x: {'auto': '🔄 Auto (Best)', 'alpha_vantage': '🅰️ Alpha Vantage',
                               'twelve_data': '🕐 Twelve Data', 'yfinance': '📊 Yahoo Finance'}[x])
    
    st.markdown("---")
    st.markdown("### 🎯 Navigation")
    page = st.radio("", ["📊 Dashboard", "📈 Technical Analysis", "⚔️ Strategy Tester", "🎯 Multi-Stock Analyzer", "🎲 Risk Simulator"])


# ============================================================================
# DASHBOARD PAGE
# ============================================================================

if page == "📊 Dashboard":
    st.markdown("## 📊 Real-Time Market Dashboard")
    
    st.markdown("""
        <div class='success-box'>
            <div style='display: flex; align-items: center; justify-content: space-between;'>
                <div>
                    <h3 style='margin-bottom: 0.5rem;'>🟢 LIVE DATA MODE</h3>
                    <p>Real-time market data from professional APIs</p>
                </div>
                <div style='font-size: 2rem;'>📡</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([4, 2, 2])
    with col1:
        symbols_input = st.text_input("📌 Stock Symbols (comma-separated)", value="AAPL,MSFT", label_visibility="visible")
    with col2:
        days_filter = st.selectbox("⏱️ Period", [30, 90, 180, 365], index=3, format_func=lambda x: f"{x} days")
    with col3:
        st.markdown("<div style='height: 1.7rem;'></div>", unsafe_allow_html=True)
        analyze_btn = st.button("ANALYZE", type="primary", use_container_width=True)
    
    symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip()][:3]
    
    if analyze_btn and symbols:
        stock_data = {}
        sources_used = {}
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for idx, symbol in enumerate(symbols):
            status_text.info(f"🔄 Fetching {symbol}... ({idx+1}/{len(symbols)})")
            df, error, source = get_stock_data(symbol, api_source)
            if df is not None:
                cutoff_date = datetime.now() - timedelta(days=days_filter)
                df = df[df.index >= cutoff_date]
                if not df.empty:
                    df = calculate_indicators(df)
                    stock_data[symbol] = df
                    sources_used[symbol] = source
            progress_bar.progress((idx + 1) / len(symbols))
            time.sleep(0.5)
        
        progress_bar.empty()
        status_text.empty()
        
        if stock_data:
            st.markdown(f"""
                <div class='success-box'>
                    <h3>✅ SUCCESS! Loaded {len(stock_data)} stocks from live APIs</h3>
                    <p>Data sources: {', '.join([f"{s}: {src}" for s, src in sources_used.items()])}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 📈 Current Prices & Performance")
            
            cols = st.columns(len(stock_data))
            for idx, (symbol, df) in enumerate(stock_data.items()):
                current = df['Close'].iloc[-1]
                start = df['Close'].iloc[0]
                change = ((current - start) / start) * 100
                with cols[idx]:
                    st.metric(symbol, f"${current:.2f}", f"{change:+.2f}%")
            
            st.markdown("---")
            st.markdown("### 📊 Price Performance Comparison")
            
            fig = go.Figure()
            colors = ['#6366f1', '#8b5cf6', '#a855f7', '#10b981', '#f59e0b']
            for idx, (symbol, df) in enumerate(stock_data.items()):
                normalized = (df['Close'] / df['Close'].iloc[0]) * 100
                fig.add_trace(go.Scatter(x=df.index, y=normalized, name=symbol, mode='lines',
                    line=dict(width=3, color=colors[idx % len(colors)])))
            
            fig.update_layout(
                title="Normalized Performance (Base = 100)",
                xaxis_title="Date", yaxis_title="Normalized Value",
                height=500, template='plotly_dark', hovermode='x unified',
                paper_bgcolor='#0f1419', plot_bgcolor='#0f1419',
                font=dict(color='#ffffff', family='Inter', size=12),
                title_font=dict(size=20, color='#ffffff')
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
            st.markdown("### 📋 Market Statistics")
            
            stats_data = []
            for symbol, df in stock_data.items():
                returns = df['Close'].pct_change().dropna()
                stats_data.append({
                    'Symbol': symbol,
                    'Price': f"${df['Close'].iloc[-1]:.2f}",
                    'High': f"${df['High'].max():.2f}",
                    'Low': f"${df['Low'].min():.2f}",
                    'Volatility': f"{(returns.std() * np.sqrt(252) * 100):.1f}%",
                    'Days': len(df)
                })
            st.dataframe(pd.DataFrame(stats_data), use_container_width=True, hide_index=True)

# ============================================================================
# TECHNICAL ANALYSIS PAGE
# ============================================================================

elif page == "📈 Technical Analysis":
    st.markdown("## 📈 Technical Analysis Suite")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        symbol = st.text_input("📌 Stock Symbol", "AAPL", label_visibility="visible")
    with col2:
        st.markdown("<div style='height: 1.7rem;'></div>", unsafe_allow_html=True)
        analyze_btn = st.button("ANALYZE", type="primary", use_container_width=True)
    
    if analyze_btn:
        df, error, source = get_stock_data(symbol, api_source)
        if df is not None:
            df = df.tail(365)
            df = calculate_indicators(df)
            patterns = detect_patterns(df)
            
            st.markdown(f"""
                <div class='success-box'>
                    <h3>✅ Data loaded from {source}</h3>
                    <p>📊 {len(df)} days of market data analyzed</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.markdown("### 📊 Current Metrics")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("💰 Price", f"${df['Close'].iloc[-1]:.2f}")
            with col2:
                st.metric("📈 RSI", f"{df['RSI'].iloc[-1]:.1f}")
            with col3:
                st.metric("📊 MACD", f"{df['MACD'].iloc[-1]:.2f}")
            with col4:
                day_change = ((df['Close'].iloc[-1] - df['Close'].iloc[-2]) / df['Close'].iloc[-2] * 100)
                st.metric("📅 Day Change", f"{day_change:+.2f}%")
            
            st.markdown("---")
            st.markdown("### 🎯 Detected Patterns")
            
            if patterns:
                for name, sentiment, desc in patterns:
                    css_class = {'Bullish': 'pattern-bullish', 'Bearish': 'pattern-bearish',
                                'Warning': 'pattern-warning', 'Opportunity': 'pattern-opportunity',
                                'Strong': 'pattern-bullish', 'Weak': 'pattern-bearish'
                               }.get(sentiment, 'pattern-card')
                    st.markdown(f"""
                        <div class='pattern-card {css_class}'>
                            <h4>{name}</h4>
                            <p><b>{sentiment}:</b> {desc}</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No significant patterns detected in current market conditions")
            
            st.markdown("---")
            st.markdown("### 📊 Technical Chart")
            
            fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                               row_heights=[0.6, 0.2, 0.2],
                               subplot_titles=('Price & Indicators', 'RSI', 'MACD'))
            
            fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                                        low=df['Low'], close=df['Close'], name='Price',
                                        increasing_line_color='#10b981', decreasing_line_color='#ef4444'),
                         row=1, col=1)
            
            fig.add_trace(go.Scatter(x=df.index, y=df['MA_20'], name='MA20',
                                    line=dict(width=2, color='#f59e0b')), row=1, col=1)
            fig.add_trace(go.Scatter(x=df.index, y=df['MA_50'], name='MA50',
                                    line=dict(width=2, color='#6366f1')), row=1, col=1)
            
            fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name='RSI',
                                    line=dict(color='#8b5cf6', width=2)), row=2, col=1)
            fig.add_hline(y=70, line_dash="dash", line_color="#ef4444", row=2, col=1)
            fig.add_hline(y=30, line_dash="dash", line_color="#10b981", row=2, col=1)
            
            fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], name='MACD',
                                    line=dict(color='#6366f1', width=2)), row=3, col=1)
            fig.add_trace(go.Scatter(x=df.index, y=df['Signal'], name='Signal',
                                    line=dict(color='#a855f7', width=2)), row=3, col=1)
            
            fig.update_layout(height=900, template='plotly_dark', showlegend=True,
                            hovermode='x unified', paper_bgcolor='#0f1419', plot_bgcolor='#0f1419',
                            font=dict(color='#ffffff', family='Inter'))
            fig.update_xaxes(rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# STRATEGY TESTER
# ============================================================================

elif page == "⚔️ Strategy Tester":
    st.markdown("## ⚔️ Strategy Backtesting Arena")
    
    st.markdown("""
        <div class='info-box'>
            <h3>🎯 Test Your Trading Strategies</h3>
            <p>Compare different strategies against buy & hold benchmark using real historical data</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📈 Moving Average Strategy")
        ma_fast = st.slider("Fast MA Period", 5, 50, 20)
        ma_slow = st.slider("Slow MA Period", 50, 200, 50)
    with col2:
        st.markdown("### 📉 RSI Mean Reversion")
        rsi_low = st.slider("Buy Below (Oversold)", 10, 40, 30)
        rsi_high = st.slider("Sell Above (Overbought)", 60, 90, 70)
    
    symbol = st.text_input("📌 Test Symbol", "AAPL", label_visibility="visible")
    
    if st.button("RUN BACKTEST", type="primary", use_container_width=True):
        df, error, source = get_stock_data(symbol, api_source)
        if df is not None:
            df = df.tail(365)
            df = calculate_indicators(df)
            df['MA_Fast'] = df['Close'].rolling(ma_fast).mean()
            df['MA_Slow'] = df['Close'].rolling(ma_slow).mean()
            df['Signal_MA'] = np.where(df['MA_Fast'] > df['MA_Slow'], 1, 0)
            df['Signal_RSI'] = 0
            df.loc[df['RSI'] < rsi_low, 'Signal_RSI'] = 1
            df.loc[df['RSI'] > rsi_high, 'Signal_RSI'] = -1
            df['Returns'] = df['Close'].pct_change()
            df['Strat_MA'] = df['Returns'] * df['Signal_MA'].shift(1)
            df['Strat_RSI'] = df['Returns'] * df['Signal_RSI'].shift(1)
            df['Cum_BH'] = (1 + df['Returns']).cumprod()
            df['Cum_MA'] = (1 + df['Strat_MA'].fillna(0)).cumprod()
            df['Cum_RSI'] = (1 + df['Strat_RSI'].fillna(0)).cumprod()
            
            st.markdown("---")
            st.markdown("### 🏆 Backtest Results")
            
            col1, col2, col3 = st.columns(3)
            bh_ret = (df['Cum_BH'].iloc[-1] - 1) * 100
            ma_ret = (df['Cum_MA'].iloc[-1] - 1) * 100
            rsi_ret = (df['Cum_RSI'].iloc[-1] - 1) * 100
            
            with col1:
                st.metric("📊 Buy & Hold", f"{bh_ret:.2f}%", "Benchmark")
            with col2:
                st.metric("📈 MA Strategy", f"{ma_ret:.2f}%", f"{ma_ret-bh_ret:+.2f}%")
            with col3:
                st.metric("📉 RSI Strategy", f"{rsi_ret:.2f}%", f"{rsi_ret-bh_ret:+.2f}%")
            
            st.markdown("---")
            st.markdown("### 📈 Cumulative Performance")
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df.index, y=df['Cum_BH'], name='Buy & Hold',
                                    line=dict(dash='dash', color='#9ca3af', width=2)))
            fig.add_trace(go.Scatter(x=df.index, y=df['Cum_MA'], name='MA Strategy',
                                    line=dict(width=3, color='#6366f1')))
            fig.add_trace(go.Scatter(x=df.index, y=df['Cum_RSI'], name='RSI Strategy',
                                    line=dict(width=3, color='#ef4444')))
            
            fig.update_layout(title="Strategy Performance Comparison", height=500,
                            template='plotly_dark', hovermode='x unified',
                            paper_bgcolor='#0f1419', plot_bgcolor='#0f1419',
                            font=dict(color='#ffffff', family='Inter'))
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# MULTI-STOCK ANALYZER PAGE (NEW!)
# ============================================================================

elif page == "🎯 Multi-Stock Analyzer":
    st.markdown("## 🎯 Multi-Stock Strategy Analyzer")
    
    st.markdown("""
        <div class='info-box'>
            <h3>🚀 Compare Multiple Stocks & Find Best Opportunities</h3>
            <p>Analyze multiple stocks simultaneously, compare strategies, and get actionable buy recommendations</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for storing results
    if 'multi_stock_results' not in st.session_state:
        st.session_state.multi_stock_results = None
    if 'multi_stock_data' not in st.session_state:
        st.session_state.multi_stock_data = None
    
    # Input Section
    col1, col2 = st.columns([3, 1])
    with col1:
        symbols_input = st.text_input("📌 Stock Symbols (comma-separated)", value="AAPL,MSFT,TSLA", label_visibility="visible")
    with col2:
        period_days = st.selectbox("⏱️ Analysis Period", [90, 180, 365], index=2, format_func=lambda x: f"{x} days")
    
    # Strategy Parameters
    st.markdown("### ⚙️ Strategy Parameters")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📈 Moving Average Strategy**")
        ma_fast = st.slider("Fast MA Period", 5, 50, 20, key="multi_ma_fast")
        ma_slow = st.slider("Slow MA Period", 50, 200, 50, key="multi_ma_slow")
    
    with col2:
        st.markdown("**📉 RSI Strategy**")
        rsi_low = st.slider("Buy Below (Oversold)", 10, 40, 30, key="multi_rsi_low")
        rsi_high = st.slider("Sell Above (Overbought)", 60, 90, 70, key="multi_rsi_high")
    
    # Analyze Button
    if st.button("🔍 ANALYZE ALL STOCKS", type="primary", use_container_width=True):
        symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip()][:5]
        
        if not symbols:
            st.error("Please enter at least one stock symbol")
        else:
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Store results
            analysis_results = []
            stock_dataframes = {}
            
            # Analyze each stock
            for idx, symbol in enumerate(symbols):
                status_text.info(f"📊 Analyzing {symbol}... ({idx+1}/{len(symbols)})")
                
                df, error, source = get_stock_data(symbol, api_source)
                
                if df is not None:
                    # Filter by period
                    cutoff_date = datetime.now() - timedelta(days=period_days)
                    df = df[df.index >= cutoff_date]
                    
                    if len(df) > 50:
                        # Store dataframe
                        stock_dataframes[symbol] = df.copy()
                        
                        # Calculate indicators
                        df = calculate_indicators(df)
                        
                        # Calculate strategies
                        df['MA_Fast'] = df['Close'].rolling(ma_fast).mean()
                        df['MA_Slow'] = df['Close'].rolling(ma_slow).mean()
                        df['Signal_MA'] = np.where(df['MA_Fast'] > df['MA_Slow'], 1, 0)
                        
                        df['Signal_RSI'] = 0
                        df.loc[df['RSI'] < rsi_low, 'Signal_RSI'] = 1
                        df.loc[df['RSI'] > rsi_high, 'Signal_RSI'] = -1
                        
                        df['Returns'] = df['Close'].pct_change()
                        df['Strat_MA'] = df['Returns'] * df['Signal_MA'].shift(1)
                        df['Strat_RSI'] = df['Returns'] * df['Signal_RSI'].shift(1)
                        
                        df['Cum_BH'] = (1 + df['Returns']).cumprod()
                        df['Cum_MA'] = (1 + df['Strat_MA'].fillna(0)).cumprod()
                        df['Cum_RSI'] = (1 + df['Strat_RSI'].fillna(0)).cumprod()
                        
                        # Calculate returns
                        bh_return = (df['Cum_BH'].iloc[-1] - 1) * 100
                        ma_return = (df['Cum_MA'].iloc[-1] - 1) * 100
                        rsi_return = (df['Cum_RSI'].iloc[-1] - 1) * 100
                        
                        # Calculate volatility (annualized)
                        volatility = df['Returns'].std() * np.sqrt(252) * 100
                        
                        # Calculate Sharpe Ratio (simplified, assuming 2% risk-free rate)
                        risk_free = 2.0
                        sharpe_bh = (bh_return - risk_free) / volatility if volatility > 0 else 0
                        sharpe_ma = (ma_return - risk_free) / volatility if volatility > 0 else 0
                        sharpe_rsi = (rsi_return - risk_free) / volatility if volatility > 0 else 0
                        
                        # Determine best strategy
                        returns_dict = {
                            'Buy & Hold': bh_return,
                            'MA Strategy': ma_return,
                            'RSI Strategy': rsi_return
                        }
                        best_strategy = max(returns_dict, key=returns_dict.get)
                        best_return = returns_dict[best_strategy]
                        
                        # Recommendation logic
                        if best_return >= 15:
                            recommendation = "🟢 Strong Buy"
                            rec_color = "#10b981"
                        elif best_return >= 5:
                            recommendation = "🟡 Buy"
                            rec_color = "#f59e0b"
                        elif best_return >= 0:
                            recommendation = "🟠 Hold"
                            rec_color = "#f97316"
                        else:
                            recommendation = "🔴 Avoid"
                            rec_color = "#ef4444"
                        
                        # Store result
                        analysis_results.append({
                            'symbol': symbol,
                            'bh_return': bh_return,
                            'ma_return': ma_return,
                            'rsi_return': rsi_return,
                            'volatility': volatility,
                            'sharpe_bh': sharpe_bh,
                            'sharpe_ma': sharpe_ma,
                            'sharpe_rsi': sharpe_rsi,
                            'best_strategy': best_strategy,
                            'best_return': best_return,
                            'recommendation': recommendation,
                            'rec_color': rec_color,
                            'current_price': df['Close'].iloc[-1],
                            'source': source,
                            'days': len(df)
                        })
                
                progress_bar.progress((idx + 1) / len(symbols))
                time.sleep(0.3)
            
            progress_bar.empty()
            status_text.empty()
            
            # Store results in session state
            st.session_state.multi_stock_results = analysis_results
            st.session_state.multi_stock_data = stock_dataframes
    
    # Display results if available
    if st.session_state.multi_stock_results:
        analysis_results = st.session_state.multi_stock_results
        stock_dataframes = st.session_state.multi_stock_data
        
        if not analysis_results:
            st.error("Could not analyze any stocks. Please check symbols and try again.")
        else:
            # Success message
            st.markdown(f"""
                <div class='success-box'>
                    <h3>✅ Analysis Complete! Analyzed {len(analysis_results)} stocks</h3>
                    <p>Period: {period_days} days | Strategies: Buy & Hold, MA({ma_fast}/{ma_slow}), RSI({rsi_low}/{rsi_high})</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Ranking Options - NOW DYNAMIC!
            st.markdown("### 📊 Ranking & Results")
            
            col1, col2 = st.columns([2, 3])
            with col1:
                rank_by = st.selectbox(
                    "📈 Rank Stocks By:",
                    ["Best Overall Return", "Best Strategy Performance", "Risk-Adjusted Return (Sharpe Ratio)"],
                    key="rank_method"
                )
            
            # Sort results based on ranking method - NO RE-ANALYZE NEEDED!
            if rank_by == "Best Overall Return":
                sorted_results = sorted(analysis_results, key=lambda x: max(x['bh_return'], x['ma_return'], x['rsi_return']), reverse=True)
                rank_desc = "Highest absolute return across all strategies"
            elif rank_by == "Best Strategy Performance":
                sorted_results = sorted(analysis_results, key=lambda x: x['best_return'], reverse=True)
                rank_desc = "Best performing strategy for each stock"
            else:  # Sharpe Ratio
                sorted_results = sorted(analysis_results, key=lambda x: max(x['sharpe_bh'], x['sharpe_ma'], x['sharpe_rsi']), reverse=True)
                rank_desc = "Best risk-adjusted returns"
            
            st.markdown(f"*{rank_desc}*")
            
            st.markdown("---")
            
            # PERFORMANCE COMPARISON CHART - NEW!
            st.markdown("### 📈 Performance Comparison Chart")
            
            if stock_dataframes:
                fig = go.Figure()
                colors = ['#6366f1', '#8b5cf6', '#ef4444', '#10b981', '#f59e0b']
                
                for idx, (symbol, df) in enumerate(stock_dataframes.items()):
                    # Normalize to base 100
                    normalized = (df['Close'] / df['Close'].iloc[0]) * 100
                    fig.add_trace(go.Scatter(
                        x=df.index, 
                        y=normalized, 
                        name=symbol, 
                        mode='lines',
                        line=dict(width=3, color=colors[idx % len(colors)])
                    ))
                
                fig.update_layout(
                    title="Normalized Performance (Base = 100)",
                    xaxis_title="Date",
                    yaxis_title="Normalized Value",
                    height=500,
                    template='plotly_dark',
                    hovermode='x unified',
                    paper_bgcolor='#0f1419',
                    plot_bgcolor='#0f1419',
                    font=dict(color='#ffffff', family='Inter', size=12),
                    title_font=dict(size=20, color='#ffffff'),
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                    )
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("---")
                
            # Display Individual Stock Cards
            st.markdown("### 📋 Detailed Stock Analysis")
            
            # Store selections
            if 'selected_stocks' not in st.session_state:
                st.session_state.selected_stocks = []
            
            for rank, result in enumerate(sorted_results, 1):
                with st.expander(f"**#{rank} - {result['symbol']}** | {result['recommendation']} | Best: {result['best_strategy']} ({result['best_return']:+.2f}%)", expanded=False):
                    
                    # Checkbox for selection
                    is_selected = st.checkbox(
                        f"✅ Select {result['symbol']} for purchase",
                        key=f"select_{result['symbol']}",
                        value=result['symbol'] in st.session_state.selected_stocks
                    )
                    
                    if is_selected and result['symbol'] not in st.session_state.selected_stocks:
                        st.session_state.selected_stocks.append(result['symbol'])
                    elif not is_selected and result['symbol'] in st.session_state.selected_stocks:
                        st.session_state.selected_stocks.remove(result['symbol'])
                    
                    # Stock details
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("💰 Current Price", f"${result['current_price']:.2f}")
                    with col2:
                        st.metric("📊 Buy & Hold", f"{result['bh_return']:+.2f}%")
                    with col3:
                        st.metric("📈 MA Strategy", f"{result['ma_return']:+.2f}%")
                    with col4:
                        st.metric("📉 RSI Strategy", f"{result['rsi_return']:+.2f}%")
                    
                    st.markdown("**📊 Risk Metrics**")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(f"**Volatility:** {result['volatility']:.2f}%")
                    with col2:
                        st.write(f"**Sharpe (BH):** {result['sharpe_bh']:.2f}")
                    with col3:
                        st.write(f"**Best Sharpe:** {max(result['sharpe_bh'], result['sharpe_ma'], result['sharpe_rsi']):.2f}")
                    
                    # Recommendation box
                    st.markdown(f"""
                        <div class='pattern-card pattern-bullish' style='border-color: {result["rec_color"]}; color: {result["rec_color"]};'>
                            <h4>{result['recommendation']}</h4>
                            <p><b>Best Strategy:</b> {result['best_strategy']} with {result['best_return']:+.2f}% return</p>
                        </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Comparison Table
            st.markdown("### 📊 Comparison Table")
            
            table_data = []
            for rank, result in enumerate(sorted_results, 1):
                table_data.append({
                    'Rank': f"#{rank}",
                    'Symbol': result['symbol'],
                    'Price': f"${result['current_price']:.2f}",
                    'Buy & Hold': f"{result['bh_return']:+.2f}%",
                    'MA Strategy': f"{result['ma_return']:+.2f}%",
                    'RSI Strategy': f"{result['rsi_return']:+.2f}%",
                    'Best Strategy': result['best_strategy'],
                    'Volatility': f"{result['volatility']:.1f}%",
                    'Recommendation': result['recommendation']
                })
            
            st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)
            
            st.markdown("---")
            
            # Selected Stocks Summary
            if st.session_state.selected_stocks:
                st.markdown("### 🎯 Your Selected Stocks")
                
                selected_data = [r for r in sorted_results if r['symbol'] in st.session_state.selected_stocks]
                
                # Summary cards
                cols = st.columns(len(selected_data))
                for idx, result in enumerate(selected_data):
                    with cols[idx]:
                        st.markdown(f"""
                            <div class='success-box' style='text-align: center; padding: 1rem;'>
                                <h3 style='margin: 0;'>{result['symbol']}</h3>
                                <p style='font-size: 1.5rem; margin: 0.5rem 0; font-weight: 700;'>
                                    ${result['current_price']:.2f}
                                </p>
                                <p style='margin: 0;'>{result['best_strategy']}</p>
                                <p style='font-size: 1.25rem; margin: 0.5rem 0; font-weight: 700;'>
                                    {result['best_return']:+.2f}%
                                </p>
                            </div>
                        """, unsafe_allow_html=True)
                
                # Investment calculator
                st.markdown("### 💰 Investment Calculator")
                
                col1, col2 = st.columns(2)
                with col1:
                    total_investment = st.number_input(
                        "Total Investment Amount ($)",
                        min_value=100,
                        max_value=1000000,
                        value=10000,
                        step=100,
                        key="total_investment"
                    )
                with col2:
                    allocation = st.radio(
                        "Allocation Method",
                        ["Equal Split", "Weighted by Performance"],
                        key="allocation_method"
                    )
                
                # Calculate allocation
                if allocation == "Equal Split":
                    per_stock = total_investment / len(selected_data)
                    allocations = {r['symbol']: per_stock for r in selected_data}
                else:
                    # Weight by best return (normalized)
                    total_return = sum(max(0, r['best_return']) for r in selected_data)
                    if total_return > 0:
                        allocations = {
                            r['symbol']: total_investment * (max(0, r['best_return']) / total_return)
                            for r in selected_data
                        }
                    else:
                        per_stock = total_investment / len(selected_data)
                        allocations = {r['symbol']: per_stock for r in selected_data}
                
                # Show allocation table
                allocation_data = []
                total_expected = 0
                
                for result in selected_data:
                    amount = allocations[result['symbol']]
                    shares = amount / result['current_price']
                    expected_value = amount * (1 + result['best_return'] / 100)
                    expected_profit = expected_value - amount
                    total_expected += expected_value
                    
                    allocation_data.append({
                        'Stock': result['symbol'],
                        'Investment': f"${amount:,.2f}",
                        'Shares': f"{shares:.2f}",
                        'Strategy': result['best_strategy'],
                        'Expected Return': f"{result['best_return']:+.2f}%",
                        'Expected Value': f"${expected_value:,.2f}",
                        'Expected Profit': f"${expected_profit:+,.2f}"
                    })
                
                st.dataframe(pd.DataFrame(allocation_data), use_container_width=True, hide_index=True)
                
                # Total summary
                total_profit = total_expected - total_investment
                total_return = (total_profit / total_investment) * 100
                
                st.markdown(f"""
                    <div class='success-box' style='text-align: center;'>
                        <h3>💰 Portfolio Summary</h3>
                        <div style='display: flex; justify-content: space-around; margin-top: 1rem;'>
                            <div>
                                <p style='margin: 0; opacity: 0.8;'>Total Investment</p>
                                <p style='font-size: 1.5rem; margin: 0; font-weight: 700;'>${total_investment:,.2f}</p>
                            </div>
                            <div>
                                <p style='margin: 0; opacity: 0.8;'>Expected Value</p>
                                <p style='font-size: 1.5rem; margin: 0; font-weight: 700;'>${total_expected:,.2f}</p>
                            </div>
                            <div>
                                <p style='margin: 0; opacity: 0.8;'>Expected Profit</p>
                                <p style='font-size: 1.5rem; margin: 0; font-weight: 700; color: {"#10b981" if total_profit > 0 else "#ef4444"};'>
                                    ${total_profit:+,.2f} ({total_return:+.2f}%)
                                </p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Clear selection button
                if st.button("🗑️ Clear All Selections", key="clear_selections"):
                    st.session_state.selected_stocks = []
                    st.rerun()
            
            else:
                st.info("👆 Select stocks using the checkboxes above to see investment summary")

# ============================================================================
# RISK SIMULATOR PAGE
# ============================================================================

elif page == "🎲 Risk Simulator":
    st.markdown("## 🎲 Monte Carlo Risk Simulator")
    
    st.markdown("""
        <div class='info-box'>
            <h3>🎯 Quantify Your Portfolio Risk</h3>
            <p>Run thousands of simulations to understand potential outcomes and calculate Value at Risk</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        symbol = st.text_input("📌 Stock Symbol", "AAPL", label_visibility="visible")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        investment = st.number_input("💰 Investment Amount ($)", 1000, 1000000, 10000, 1000)
    with col2:
        days_forward = st.slider("📅 Days Forward", 30, 365, 252)
    with col3:
        num_sims = st.slider("🔄 Simulations", 100, 5000, 1000, 100)
    
    if st.button("RUN SIMULATION", type="primary", use_container_width=True):
        df, error, source = get_stock_data(symbol, api_source)
        if df is not None:
            df = df.tail(365)
            returns = df['Close'].pct_change().dropna()
            mu = returns.mean()
            sigma = returns.std()
            last_price = df['Close'].iloc[-1]
            
            st.markdown(f"""
                <div class='info-box'>
                    <p>📊 Historical Parameters: Mean Return = {mu*100:.4f}%, Volatility = {sigma*100:.2f}%</p>
                </div>
            """, unsafe_allow_html=True)
            
            simulations = []
            np.random.seed(42)
            progress = st.progress(0)
            for i in range(num_sims):
                prices = [last_price]
                for _ in range(days_forward):
                    shock = np.random.normal(mu, sigma)
                    prices.append(prices[-1] * (1 + shock))
                simulations.append(prices)
                if i % 100 == 0:
                    progress.progress((i + 1) / num_sims)
            progress.empty()
            
            sim_array = np.array(simulations)
            shares = investment / last_price
            portfolio_sims = sim_array * shares
            final_values = portfolio_sims[:, -1]
            
            st.markdown("---")
            st.markdown("### 📊 Simulation Results")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("💵 Initial", f"${investment:,.0f}")
            with col2:
                st.metric("📈 Mean Final", f"${final_values.mean():,.0f}")
            with col3:
                profit = final_values.mean() - investment
                st.metric("💰 Expected Profit", f"${profit:,.0f}", f"{(profit/investment*100):+.1f}%")
            with col4:
                var_95 = np.percentile(final_values, 5)
                st.metric("⚠️ VaR (95%)", f"${investment - var_95:,.0f}")
            
            st.markdown("---")
            st.markdown("### 🌊 Simulation Paths")
            
            fig = go.Figure()
            sample = min(100, num_sims)
            for i in range(sample):
                fig.add_trace(go.Scatter(y=portfolio_sims[i], mode='lines',
                    line=dict(width=0.5, color='rgba(99, 102, 241, 0.1)'),
                    showlegend=False, hoverinfo='skip'))
            fig.add_trace(go.Scatter(y=portfolio_sims.mean(axis=0), mode='lines',
                line=dict(width=4, color='#ef4444'), name='Mean Path'))
            fig.add_hline(y=investment, line_dash="dash", line_color='#10b981')
            
            fig.update_layout(title=f"{num_sims:,} Monte Carlo Simulations",
                            height=500, template='plotly_dark',
                            paper_bgcolor='#0f1419', plot_bgcolor='#0f1419',
                            font=dict(color='#ffffff', family='Inter'))
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# FOOTER WITH LEGAL DISCLAIMER
# ============================================================================

st.markdown("---")

# Comprehensive Legal Disclaimer
st.markdown("""
<div style='background: rgba(239, 68, 68, 0.1); border: 2px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 2rem; margin: 2rem 0;'>
    <h3 style='color: #ef4444; margin-top: 0; text-align: center;'>⚠️ IMPORTANT LEGAL DISCLAIMER</h3>
    <div style='color: rgba(255,255,255,0.9); font-size: 0.875rem; line-height: 1.8;'>
        <p style='margin-bottom: 1rem;'><strong>EDUCATIONAL PURPOSE ONLY:</strong> This application is provided for educational and informational purposes only. It is NOT intended as financial, investment, trading, or any other type of professional advice.</p>
        <p style='margin-bottom: 1rem;'><strong>NOT FINANCIAL ADVICE:</strong> Nothing contained in this application constitutes a solicitation, recommendation, endorsement, or offer to buy or sell any securities or other financial instruments in any jurisdiction.</p>
        <p style='margin-bottom: 1rem;'><strong>NO GUARANTEES:</strong> Past performance is not indicative of future results. All trading and investing involves risk of loss. Historical data, backtesting results, and simulations do not guarantee future performance.</p>
        <p style='margin-bottom: 1rem;'><strong>DO YOUR OWN RESEARCH:</strong> You should conduct your own research and due diligence and obtain professional advice before making any investment decision. Consult with a licensed financial advisor, accountant, and/or attorney before making any financial decisions.</p>
        <p style='margin-bottom: 1rem;'><strong>NO LIABILITY:</strong> The creator(s) of this application assume no responsibility or liability for any errors or omissions in the content, data, or analysis. Under no circumstances shall the creator(s) be liable for any direct, indirect, special, incidental, or consequential damages arising out of the use of this application.</p>
        <p style='margin-bottom: 1rem;'><strong>DATA ACCURACY:</strong> While we strive to provide accurate data from third-party APIs, we cannot guarantee the accuracy, completeness, or timeliness of any information. Data may be delayed, incorrect, or unavailable.</p>
        <p style='margin-bottom: 1rem;'><strong>THIRD-PARTY APIS:</strong> This application uses third-party data providers (Alpha Vantage, Yahoo Finance, Twelve Data). We are not affiliated with these providers and are not responsible for their data accuracy or availability.</p>
        <p style='margin-bottom: 1.5rem;'><strong>USE AT YOUR OWN RISK:</strong> By using this application, you acknowledge and agree that you are using it at your own risk and that you will not hold the creator(s) liable for any losses or damages resulting from your use.</p>
        <p style='text-align: center; margin-top: 1.5rem; margin-bottom: 0; font-weight: 600; color: #ef4444;'>IF YOU DO NOT AGREE WITH THESE TERMS, DO NOT USE THIS APPLICATION.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h3 style='margin-bottom: 1rem; font-weight: 700;'>📊 Market Intelligence Platform</h3>
    <p style='color: rgba(255,255,255,0.6); margin-bottom: 1rem;'>Real-Time Data • Advanced Analytics • Professional Grade</p>
    <p style='color: rgba(255,255,255,0.5); font-size: 0.875rem; margin-bottom: 1rem;'>Educational Tool • Not Financial Advice • Use at Your Own Risk</p>
    <div style='display: flex; justify-content: center; gap: 0.5rem; flex-wrap: wrap;'>
        <span class='badge'>Built with Python</span>
        <span class='badge'>Powered by Streamlit</span>
        <span class='badge'>Real-Time APIs</span>
    </div>
    <p style='color: rgba(255,255,255,0.4); font-size: 0.75rem; margin-top: 1rem;'>© 2026 Market Intelligence. For Educational Purposes Only.</p>
</div>
""", unsafe_allow_html=True)
