import streamlit as st 
import pandas as pd
import plotly_express as px 


@st.cache_data
def get_bond_prices(url):
    tables = pd.read_html(url)
    prices = tables[0]
    prices = (prices
            .drop(prices.columns[1:10], axis=1)
            .assign(Date=lambda df: pd.to_datetime(df['Date']))
            .set_index('Date')
            )
    return prices


url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2023'
prices = get_bond_prices(url)

agg_times = st.multiselect('Choose Timeframe', options=prices.columns, default=['1 Mo', '1 Yr', '2 Yr', '10 Yr'])

temp_df = prices[agg_times]

fig = px.line(temp_df)

st.plotly_chart(fig)


