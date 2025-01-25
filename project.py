import streamlit as st
import yfinance as finance

def get_ticker(tag):
    return finance.Ticker(tag)

def download(tag, start, end):
    return finance.download(tag, start=start, end=end)

def history(comp, time):
    return comp.history(period=time)

def main():
    st.title("Stock Market App")
    st.header("Dynamic Stock Market Application (Created for cs50p Final Project 2023 by Tirath Bhathawala)")
    # st.sidebar.header("Tirath \n Bhathawala")

    comp1 = get_ticker("GOOGL")
    comp2 = get_ticker("MSFT")

    google = download("GOOGL", "2024-10-01", "2024-12-01")
    microsoft = download("MSFT", "2024-10-01", "2024-12-01")

    data1 = history(comp1, "3mo")
    data2 = history(comp2, "3mo")

    st.write("""### Google""")

    st.write(comp1.info['longBusinessSummary'])
    st.write(google)

    st.line_chart(data1.values)

    st.write("""### MICROSOFT""")

    st.write(comp2.info['longBusinessSummary'])
    st.write(microsoft)

    st.line_chart(data2.values)

if __name__ == '__main__':
    main()
