APP_INFO = {
    "title": "⚖️ Exploring Put-Call Parity",
    "description": "Discover the elegant relationship between calls, puts, and forwards. "
    "Test the Put-Call Parity equation with live calculations and visual payoff comparisons."
}


import streamlit as st
import numpy as np
import plotly.graph_objects as go
from ..put_call_parity.options import call_option, put_option


def run():
    st.set_page_config(page_title="Put-Call Parity", page_icon="📈")
    st.title(APP_INFO["title"])

    st.info("""
    **Instructions**
    - Enter Call, Put, and Stock parameters.
    - Click "Calculate" to check if Put-Call Parity holds.
    - View payoff diagrams and equation breakdown.
    """)

    with st.sidebar.form("params_form"):
        st.header("Parameters")

        call_price = st.number_input("Call Price € - C", step=0.1, format="%.2f", value=2.0)
        put_price = st.number_input("Put Price € - P", step=0.1, format="%.2f", value=1.0)
        s0 = st.number_input("Initial Stock Price € - S(0)", step=1.0, format="%.2f", value=100.0)
        strike_price = st.number_input("Strike Price € - E", step=1.0, format="%.2f", value=100.0)
        r = st.slider("Annual interest rate (%)", 0.0, 10.0, 2.0, 0.1) / 100
        time = st.slider("Expiration (years)", 0, 10, 1, 1)

        submit = st.form_submit_button("📊 Calculate", use_container_width=True, type="primary")

    if submit:
        # --- Compute both sides ---
        lhs = call_price - put_price
        rhs = s0 - strike_price * np.exp(-r * time)
        parity_diff = lhs - rhs

        # --- Display results ---
        st.subheader("🔢 Put-Call Parity Calculation")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Left Side (C - P)", f"{lhs:.2f} €")
        with col2:
            st.metric("Right Side (S₀ - E·e⁻ʳᵀ)", f"{rhs:.2f} €")
        with col3:
            st.metric("Difference", f"{parity_diff:.2f} €")

        # --- Verdict ---
        if np.isclose(parity_diff, 0, atol=1e-2):
            st.success("✅ Put-Call Parity holds — no arbitrage opportunity.")
        elif parity_diff > 0:
            st.warning("⚠️ Arbitrage possible: Call may be overpriced or Put underpriced.")
        else:
            st.warning("⚠️ Arbitrage possible: Call may be underpriced or Put overpriced.")

        # --- Equation shown dynamically ---
        st.markdown(
            f"""
            ### Equation Breakdown
            $$
            C - P = S_0 - E e^{{-rT}} \\\\
            {call_price:.2f} - {put_price:.2f} = {s0:.2f} - {strike_price:.2f} e^{{-{r:.3f} \\times {time:.2f}}}
            $$
            """
        )

        st.divider()
        st.subheader("💰 Payoff Diagram")

        # --- Payoff visualization ---
        stock_prices = np.linspace(0, 2 * strike_price, 200)

        payoff_long_call_short_put = np.array([
            call_option(strike_price, s, True) + put_option(strike_price, s, False)
            for s in stock_prices
        ])
        payoff_short_call_long_put = np.array([
            call_option(strike_price, s, False) + put_option(strike_price, s, True)
            for s in stock_prices
        ])

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=stock_prices,
            y=payoff_long_call_short_put,
            mode="lines",
            name="Long Call + Short Put",
            line=dict(width=3)
        ))
        fig.add_trace(go.Scatter(
            x=stock_prices,
            y=payoff_short_call_long_put,
            mode="lines",
            name="Short Call + Long Put",
            line=dict(width=3)
        ))
        fig.add_hline(y=0, line=dict(color="gray", dash="dash"))

        fig.update_layout(
            title="Profit / Loss at Expiration",
            xaxis_title="Stock Price at Expiration (€)",
            yaxis_title="Profit / Loss (€)",
            legend_title="Positions",
            margin=dict(l=0, r=0, t=40, b=0),
        )

        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


if __name__=="__main__":
    run()