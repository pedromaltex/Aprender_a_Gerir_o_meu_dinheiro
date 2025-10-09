APP_INFO = {
    "title": "🧠 Exploring Options",
    "description": "Dive deeper into how calls and puts respond to market moves. "
    "Compare multiple positions, analyze combined payoffs, and build intuition about risk and reward."
}

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from ..options.options import call_option, put_option

def run():
    # --- Page Configuration ---
    st.set_page_config(page_title="Options", page_icon="📈")
    st.title(APP_INFO["title"])

    st.info(
        """
        **Instructions**

        - Choose the option type (Call or Put) and your position (Long or Short).  
        - Enter the strike price and the option premium.  
        - Use the buttons to add, delete, or clear options.  
        - Click "Calculate" to see the profit/loss graph.
        """
    )

    # --- Initialize session state ---
    if 'options' not in st.session_state:
        st.session_state.options = []

    # --- Sidebar Inputs ---
    with st.sidebar.form("params_form"):
        st.header("Parameters")    

        strike_price = st.number_input(
            label="Strike Price €", 
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
            label="Premium €", 
            step=0.1, 
            format="%.2f", 
            value=0.0
        )

        # Cria três colunas para os botões
        col1, col2= st.columns(2)

        with col1:
            add_option = st.form_submit_button("➕ Add Option", use_container_width=True, type="secondary")
        with col2:
            submit = st.form_submit_button("📊 Calculate Payoff", use_container_width=True, type="primary")
        
        col1, col2 = st.columns(2)
        with col1:
            clear_button = st.form_submit_button("♻️ Clear All", use_container_width=True)
        with col2:
            delete_previous = st.form_submit_button("🗑️ Delete Previous", use_container_width=True)

            

        #add_option = st.form_submit_button("Add Option")
        #delete_previous = st.form_submit_button("Delete Previous Option")
        #clear_button = st.form_submit_button("Clear All")
        #submit = st.form_submit_button("Calculate")

    # --- Handle Button Actions ---
    if add_option:
        st.session_state.options.append({
            "strike_price": strike_price,
            "type_option":  type_option,
            "type_position":  type_position,
            "premium":  premium
        })
        st.success("Option added.")

    if delete_previous:
        if st.session_state.options:
            st.session_state.options.pop()
            st.warning("Last option deleted.")
        else:
            st.warning("No options to delete.")

    if clear_button:
        st.session_state.options = []
        st.warning("All options cleared.")

    # --- Show Current Options ---
    if st.session_state.options:
        st.subheader("Current Options")
        for idx, option in enumerate(st.session_state.options):
            st.write(f"{idx+1}. 1 {option['type_position']} {option['type_option']} with strike price {option['strike_price']}€ and premium {option['premium']}€")
    else:
        st.info("No options added yet.")

    # --- Calculate & Plot Payoffs ---
    if submit and st.session_state.options:
        st.subheader("Payoff Diagram")

        # Create a price range covering all options
        all_strikes = [opt["strike_price"] for opt in st.session_state.options]
        max_strike = max(all_strikes)
        stock_prices = np.arange(0, 2 * max_strike + 1)

        fig = go.Figure()

        # Total payoff across all options
        total = np.zeros_like(stock_prices, dtype=float)

        for option in st.session_state.options:
            strike = option["strike_price"]
            premium = option["premium"]
            is_call = option["type_option"] == "Call Option"
            is_long = option["type_position"] == "Long"

            # Calculate payoff per option
            if is_call:
                payoff = np.array([
                    call_option(strike, price, is_long) - premium if is_long
                    else call_option(strike, price, is_long) + premium
                    for price in stock_prices
                ])
            else:
                payoff = np.array([
                    put_option(strike, price, is_long) - premium if is_long
                    else put_option(strike, price, is_long) + premium
                    for price in stock_prices
                ])

            total += payoff  # Accumulate total payoff

            # Plot individual option payoff
            fig.add_trace(go.Scatter(
                x=stock_prices,
                y=payoff,
                mode='lines',
                line=dict(width=1, dash='dash'),
                name=f"{option['type_position']} {option['type_option']} @ {strike}"
            ))

        # Plot total payoff
        fig.add_trace(go.Scatter(
            x=stock_prices,
            y=total,
            mode='lines',
            name="Total Payoff",
            line=dict(color="white", width=3)
        ))

        fig.update_layout(
            title="Profit / Loss at Expiration",
            xaxis_title="Stock Price at Expiration (€)",
            yaxis_title="Profit / Loss (€)",
            margin=dict(l=0, r=0, t=40, b=0),
            legend_title="Options"
        )

        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

if __name__=="__main__":
    run()