from app.APIs.data_av import get_exchange_rate, get_data_monthy_adjusted, get_data_daily_adjusted, get_data_intraday
import streamlit as st

st.set_page_config(layout="wide")

with st.container():
    st.markdown("<h1 style='text-align: center; color: black;'>🤖 Asistente virtual</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Que quieres hacer hoy?</h2>", unsafe_allow_html=True)

    st.write("Opciones disponibles:")
    exchange = st.button("Consultar USD vs EUR", type="secondary", disabled=False)
    data_monthly = st.button("Consultar datos mensuales", type="secondary", disabled=False)
    data_intraday = st.button("Consultar datos intradía", type="secondary", disabled=False)
    #option = st.chat_input("Indica tu solicitud")

    if exchange:
        st.write(get_exchange_rate('USD', 'EUR'))
    elif data_monthly:
        st.write(get_data_monthy_adjusted('AAPL'))
    elif data_intraday:
        st.write(get_data_intraday('AAPL'))
    
    
    #print(get_data_monthy_adjusted('AAPL'))
    #print(get_data_daily_adjusted('AAPL'))
    #print(get_data_intraday('AAPL'))
    #print(get_exchange_rate('USD', 'EUR'))  