import streamlit as st
import pandas as pd
import plotly.express as px
import re

st.set_page_config(page_title="Branch Revenue Dashboard", layout="wide")
st.title("🌟 Branch Revenue Dashboard")

# =========================
# File Upload
# =========================
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Make sure Date is datetime
    df["Date"] = pd.to_datetime(df["Date"])
    
    st.subheader("Raw Data")
    st.dataframe(df)
    
    # =========================
    # Parse Revenue
    # =========================
    def parse_revenue(s):
        if isinstance(s, str):
            return float(re.sub(r"[^\d.]", "", s))
        return float(s)
    
    df['RevenueNumeric'] = df['Revenue'].apply(parse_revenue)
    
    st.subheader("Revenue Numeric")
    st.dataframe(df[['Branch', 'Date', 'Revenue', 'RevenueNumeric']])
    
    # =========================
    # Filters
    # =========================
    branches = df['Branch'].unique().tolist()
    months = df['Date'].dt.strftime('%B %Y').unique().tolist()
    
    selected_branch = st.selectbox("Select Branch", ["All"] + branches)
    selected_month = st.selectbox("Select Month", ["All"] + list(months))
    expected_revenue = st.number_input("Enter Expected Revenue", min_value=0.0, value=10000.0)
    
    # Filter dataframe
    df_filtered = df.copy()
    if selected_branch != "All":
        df_filtered = df_filtered[df_filtered['Branch'] == selected_branch]
    if selected_month != "All":
        df_filtered = df_filtered[df_filtered['Date'].dt.strftime('%B %Y') == selected_month]
    
    # =========================
    # Status: Above / Equal / Below
    # =========================
    def revenue_status(value):
        if value > expected_revenue:
            return "Above"
        elif value == expected_revenue:
            return "Equal"
        else:
            return "Below"
    
    df_filtered['Status'] = df_filtered['RevenueNumeric'].apply(revenue_status)
    
    # =========================
    # KPI Metrics
    # =========================
    st.subheader("📊 Branch Revenue Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    total_branches = df_filtered['Branch'].nunique()
    highest_revenue = df_filtered['RevenueNumeric'].max()
    top_branch = df_filtered.loc[df_filtered['RevenueNumeric'].idxmax(), 'Branch'] if not df_filtered.empty else "N/A"
    
    col1.metric("🏢 Top Branch", top_branch)
    col2.metric("💰 Highest Revenue", f"{highest_revenue:,.0f}")
    col3.metric("📈 Branches Analyzed", total_branches)
    
    # =========================
    # Charts
    # =========================
    if not df_filtered.empty:
        # Bar chart by branch
        bar_fig = px.bar(
            df_filtered.groupby('Branch', as_index=False)['RevenueNumeric'].sum(),
            x='Branch',
            y='RevenueNumeric',
            title="Total Revenue by Branch",
            text_auto=".2s",
            color='RevenueNumeric',
            color_continuous_scale='Viridis'
        )
        bar_fig.update_layout(yaxis_title="Revenue", xaxis_title="Branch")
        st.plotly_chart(bar_fig, use_container_width=True)
        
        # Pie chart by Status
        pie_fig = px.pie(
            df_filtered,
            names='Status',
            title="Revenue Status Distribution",
            color='Status',
            color_discrete_map={'Above':'green','Equal':'blue','Below':'red'}
        )
        st.plotly_chart(pie_fig, use_container_width=True)
        
        # Trend over months (if all months selected)
        if selected_branch != "All":
            trend_fig = px.line(
                df[df['Branch'] == selected_branch],
                x='Date',
                y='RevenueNumeric',
                title=f"{selected_branch} Revenue Trend",
                markers=True
            )
            trend_fig.update_layout(yaxis_title="Revenue", xaxis_title="Date")
            st.plotly_chart(trend_fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")
