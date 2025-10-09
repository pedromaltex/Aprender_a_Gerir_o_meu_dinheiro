APP_INFO = {
    "title": "📊 Call and Put Payoff Visualizer",
    "description": "Learn how options behave at expiration! "
    "Visualize profit and loss for long and short positions, adjusting strike price and premium interactively."
}

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from ..call_put_options.call_put_aux import call_option, put_option

def run():
    # --- Interface Streamlit ---
    st.set_page_config(page_title="Call and Put Payoff", page_icon="📈")
    st.title(APP_INFO["title"])

    st.info(
        """
        **Instructions**

        - Choose the option type (Call or Put) and your position (Long or Short).  
        - Enter the strike price and the option premium.  
        - The graph will show the **profit/loss profile** of the option for a range of stock prices.
        """
    )

    # Inputs
    with st.sidebar.form("params_form"):
        st.header("Parameters")    

        strike_price = st.number_input(
            label="Strike Price $", 
            step=0.1, 
            format="%.2f", 
            value=100.0
        )

        type_option = st.radio(
            label="Select option type",
            options=["Call Option", "Put Option"]
        )
        type_position = st.radio(
            label="Select position",
            options=["Long", "Short"]
        )

        premium = st.number_input(
            label="Premium $", 
            step=1.0, 
            format="%.2f", 
            value=0.0
        )

        submit = st.form_submit_button("Calculate")

    if submit:
        # --- Simulação do payoff ---
        stock_prices = np.arange(0, 2*strike_price)
        if type_option == "Call Option":
            if type_position=="Long":
                option_value = [call_option(strike_price, p, True) - premium for p in stock_prices]
            else:
                option_value = [call_option(strike_price, p, False) + premium for p in stock_prices]
        else:
            if type_position=="Long":
                option_value = [put_option(strike_price, p, True) - premium for p in stock_prices]
            else:
                option_value = [put_option(strike_price, p, False) + premium for p in stock_prices]


        # --- Gráfico ---
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=stock_prices, 
            y=option_value, 
            mode='lines', 
            name="Option value",
        ))
        fig.update_layout(
            title=f"{type_position} {type_option} Payoff",
            xaxis_title="Stock Price at Expiration ($)",
            yaxis_title="Profit / Loss ($)",
            margin=dict(l=0, r=0, t=50, b=0),
        )


        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

if __name__=="__main__":
    run()