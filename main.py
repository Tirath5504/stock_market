
import streamlit as st
import yfinance as finance


def get_ticker(name):
    return finance.Ticker(name)


def market():

    st.title("Stock Market App")
    st.header("Data Science Application")
    st.sidebar.header("Tirath \n Bhathawala")

    comp1 = get_ticker("GOOGL")
    comp2 = get_ticker("MSFT")

    google = finance.download("GOOGL", start="2023-05-01", end="2023-05-01")
    microsoft = finance.download("MSFT", start="2023-05-01", end="2023-05-01")

    data1 = comp1.history(period="3mo")
    data2 = comp2.history(period="3mo")

    st.write("""
    ### Google
    """)

    st.write(comp1.info['longBusinessSummary'])
    st.write(google)

    st.line_chart(data1.values)

    st.write("""
    ### MICROSOFT
    """)

    st.write(comp2.info['longBusinessSummary'])
    st.write(microsoft)

    st.line_chart(data2.values)


if __name__ == '__main__':
    market()
