import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Weather Forecast & Alert Application",
    page_icon="🌦️",
    layout="wide"
)

# ---------------------------------------------------
# CREATE OUTPUT FOLDERS
# ---------------------------------------------------
os.makedirs("reports", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ---------------------------------------------------
# CUSTOM HEADER
# ---------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #1E90FF;'>
    🌦️ Weather Forecast & Alert Application
    </h1>

    <p style='text-align: center;'>
    Simulated Weather Monitoring Dashboard using Python & Streamlit
    </p>

    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("data/weather_data.csv")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("📍 Select City")

city = st.sidebar.selectbox(
    "Choose City",
    df["City"]
)

# ---------------------------------------------------
# FILTER CITY DATA
# ---------------------------------------------------
city_data = df[df["City"] == city].iloc[0]

# ---------------------------------------------------
# METRIC CARDS
# ---------------------------------------------------
st.subheader(f"🌍 Weather Details for {city}")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡️ Temperature", f"{city_data['Temperature']} °C")
col2.metric("💧 Humidity", f"{city_data['Humidity']} %")
col3.metric("🌪️ Wind Speed", f"{city_data['WindSpeed']} km/h")
col4.metric("🌧️ Rainfall", f"{city_data['Rainfall']} mm")

st.info(f"☁️ Weather Condition: {city_data['Weather']}")

# ---------------------------------------------------
# ALERT SYSTEM
# ---------------------------------------------------
st.subheader("🚨 Weather Alerts")

alerts = []

if city_data["Temperature"] > 40:
    alerts.append("🔥 Heat Alert: Very High Temperature!")

if city_data["Rainfall"] > 5:
    alerts.append("🌧️ Rain Alert: Heavy Rain Expected!")

if city_data["Humidity"] > 80:
    alerts.append("💧 Humidity Alert: High Humidity Levels!")

if city_data["WindSpeed"] > 15:
    alerts.append("🌪️ Wind Alert: Strong Winds Expected!")

if alerts:
    for alert in alerts:
        st.error(alert)
else:
    st.success("✅ No Weather Alerts")

# ---------------------------------------------------
# VISUALIZATION SECTION
# ---------------------------------------------------
st.subheader("📊 Weather Analytics")

chart1, chart2 = st.columns(2)

# ---------------------------------------------------
# TEMPERATURE CHART
# ---------------------------------------------------
with chart1:

    fig1, ax1 = plt.subplots()

    ax1.bar(df["City"], df["Temperature"])

    ax1.set_title("Temperature Analysis")
    ax1.set_xlabel("City")
    ax1.set_ylabel("Temperature (°C)")

    plt.xticks(rotation=45)

    # SAVE CHART
    fig1.savefig("outputs/temperature_chart.png")

    st.pyplot(fig1)

# ---------------------------------------------------
# HUMIDITY CHART
# ---------------------------------------------------
with chart2:

    fig2, ax2 = plt.subplots()

    ax2.plot(df["City"], df["Humidity"], marker='o')

    ax2.set_title("Humidity Analysis")
    ax2.set_xlabel("City")
    ax2.set_ylabel("Humidity (%)")

    plt.xticks(rotation=45)

    # SAVE CHART
    fig2.savefig("outputs/humidity_chart.png")

    st.pyplot(fig2)

# ---------------------------------------------------
# RAINFALL CHART
# ---------------------------------------------------
fig3, ax3 = plt.subplots()

ax3.bar(df["City"], df["Rainfall"])

ax3.set_title("Rainfall Analysis")
ax3.set_xlabel("City")
ax3.set_ylabel("Rainfall (mm)")

plt.xticks(rotation=45)

# SAVE CHART
fig3.savefig("outputs/rainfall_chart.png")

st.pyplot(fig3)

# ---------------------------------------------------
# REPORT GENERATION
# ---------------------------------------------------
st.subheader("📄 Generate Weather Report")

if st.button("Generate CSV Report"):

    report_path = f"reports/{city}_weather_report.csv"

    report_df = pd.DataFrame([city_data])

    report_df.to_csv(report_path, index=False)

    st.success("✅ Report Generated Successfully!")

    st.write(f"📁 File Saved: {report_path}")

# ---------------------------------------------------
# COMPLETE DATASET
# ---------------------------------------------------
st.subheader("📋 Complete Weather Dataset")

st.dataframe(df)

# ---------------------------------------------------
# OUTPUT FILES SECTION
# ---------------------------------------------------
st.subheader("📁 Generated Output Files")

st.write("Charts are automatically saved inside the outputs folder.")

st.write("Saved Files:")
st.write("✅ temperature_chart.png")
st.write("✅ humidity_chart.png")
st.write("✅ rainfall_chart.png")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    """
    <center>
    Developed using <b>Python</b>, <b>Pandas</b>, 
    <b>Matplotlib</b>, and <b>Streamlit</b> 🚀
    </center>
    """,
    unsafe_allow_html=True
)