import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="CodeX: Beverage Price Prediction", layout="wide")
st.title("CodeX: Beverage Price Prediction")

# ---- Row 1 ----
row1 = st.columns(4)
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
with row1[1]:
    gender = st.selectbox("Gender", ["M", "F"])
with row1[2]:
    zone = st.selectbox("Zone", ["Urban", "Metro", "Rural", "Semi-Urban"])
with row1[3]:
    occupation = st.selectbox("Occupation", ["Working Professional", "Student", "Entrepreneur", "Retired"])

# ---- Row 2 ----
row2 = st.columns(4)
with row2[0]:
    income_levels = st.selectbox(
        "Income Level (In L)",
        ["<10L", "10L - 15L", "16L - 25L", "26L - 35L","> 35L", "not reported"]
    )
with row2[1]:
    consume_freq = st.selectbox("Consume Frequency (weekly)", ["5-7 times","3-4 times", "0-2 times"])
with row2[2]:
    current_brand = st.selectbox("Current Brand", ["Newcomer", "Established"])
with row2[3]:
    size = st.selectbox("Preferable Consumption Size", [ "Large (1 L)","Medium (500 ml)","Small (250 ml)"])

# ---- Row 3 ----
row3 = st.columns(4)
with row3[0]:
    awareness = st.selectbox("Awareness of other brands", ["0 to 1", "2 to 4", "above 4"])
with row3[1]:
    reasons = st.selectbox("Reasons for choosing brands", ["Price", "Quality", "Availability", "Brand Reputation"])
with row3[2]:
    flavor = st.selectbox("Flavor Preference", ["Traditional", "Exotic"])
with row3[3]:
    channel = st.selectbox("Purchase Channel", ["Online", "Retail Store"])

# ---- Row 4 ----
row4 = st.columns(3)
with row4[0]:
    packaging = st.selectbox("Packaging Preference", ["Simple", "Premium", "Eco-Friendly"])
with row4[1]:
    health = st.selectbox(
        "Health Concerns",
        ["Low (Not very concerned)","Medium (Moderately health-conscious)","High (Very health-conscious)"],
    )
with row4[2]:
    situation = st.selectbox(
        "Typical Consumption Situations",
        ["Active (eg. Sports, gym)", "Social (eg. Parties)", "Casual (eg. At home)"],
    )

st.markdown("---")
if st.button("Calculate Price Range", use_container_width=True):
    prediction = predict(age, gender, zone, occupation, income_levels, consume_freq, current_brand, size,
                         awareness, reasons, flavor, channel, packaging, health, situation)
    st.success(f'Price of Drink is:{prediction}')


