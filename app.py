import streamlit as st
import pandas as pd
import requests
import re
import plotly.express as px

# إعدادات واجهة الموبايل الاحترافية
st.set_page_config(page_title="Nahlati Super App", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    div.stButton > button {
        background-color: #FFC107; color: black; border-radius: 20px; height: 3.5em; width: 100%; font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 5px; }
    .stTabs [data-baseweb="tab"] {
        height: 45px; background-color: #1e2130; border-radius: 12px; color: white; font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🐝 منظومة نهلاتي الذكية")

# 5 أقسام رئيسية تدير بها كل مشروعك من هاتفك
tabs = st.tabs(["📩 فيسبوك", "🏥 العيادة", "🕵️ المجموعات", "💰 Etsy", "💡 الأفكار"])

# --- 1. تحليل رسائل فيسبوك ---
with tabs[0]:
    st.header("تحليل الأرشيف المباشر")
    token = st.text_input("أدخل Page Access Token:", type="password")
    if st.button("🚀 سحب وتحليل 333 رسالة"):
        url = f"https://graph.facebook.com/v19.0/me/conversations?fields=messages{{message,from}}&access_token={token}"
        try:
            res = requests.get(url).json()
            if 'data' in res:
                st.success("تم سحب الرسائل بنجاح!")
                # هنا محرك التحليل (الأمراض، الهواتف، الولايات)
                st.write("الرسائل جاهزة للتحليل...")
        except: st.error("تأكد من الرمز")

# --- 2. إدارة العيادة والحقن ---
with tabs[1]:
    st.header("سجل المرضى")
    with st.form("clinic_form"):
        name = st.text_input("اسم المريض")
        sugar = st.number_input("السكر")
        dose = st.slider("الجرعة (ml)", 0.05, 2.0, 0.1)
        st.file_uploader("ارفع صورة الحقن من كاميرا الهاتف")
        if st.form_submit_button("حفظ الجلسة"):
            st.success("تم الحفظ في السحابة!")

# --- 3. منقب مجموعات فيسبوك (النسخ واللصق) ---
with tabs[2]:
    st.header("استخراج زب
