import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="ChurnAI • Enterprise Analytics",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "best_churn_pipeline.pkl"
    return joblib.load(model_path)

model = load_model()

# ---------- COMPLETE BLACK DARK THEME CSS ----------
st.markdown(
    """
<style>
/* Global Reset & Pure Black Theme */
html, body, .stApp {
    background-color: #000000 !important;
    color: #ffffff !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

.block-container {
    max-width: 1280px;
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

/* Header / Hero Section */
.hero {
    text-align: center;
    padding: 2rem 1rem;
    background: linear-gradient(180deg, #0d0d12 0%, #000000 100%);
    border-bottom: 1px solid #1a1a24;
    margin-bottom: 2rem;
    border-radius: 16px;
}

.badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.3);
    color: #818cf8;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

.title {
    font-size: 52px;
    font-weight: 900;
    margin: 12px 0 6px;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 50%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #71717a;
    font-size: 16px;
    font-weight: 400;
}

/* Glassmorphic Dark Cards */
.card {
    background: #08080a;
    border: 1px solid #18181b;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.section-title {
    font-size: 20px;
    font-weight: 800;
    color: #f4f4f5;
    letter-spacing: -0.01em;
}

.section-text {
    color: #71717a;
    font-size: 13px;
    margin-bottom: 22px;
}

/* Inputs Styling Overrides */
.stNumberInput input, .stSelectbox [data-baseweb="select"] {
    background-color: #000000 !important;
    border: 1px solid #27272a !important;
    color: #ffffff !important;
    border-radius: 10px !important;
}

/* Primary Action Button */
.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.02em;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(99, 102, 241, 0.5);
}

/* Prediction Cards */
.result-card {
    text-align: center;
    padding: 32px 20px;
    border-radius: 16px;
    background: #000000;
    border: 1px solid #27272a;
    margin-bottom: 20px;
}

.result-card.high-risk {
    border-color: #f43f5e;
    background: radial-gradient(circle at center, rgba(244, 63, 94, 0.1) 0%, #000000 80%);
}

.result-card.low-risk {
    border-color: #10b981;
    background: radial-gradient(circle at center, rgba(16, 185, 129, 0.1) 0%, #000000 80%);
}

.result-icon {
    font-size: 48px;
    margin-bottom: 8px;
}

.result-title {
    font-size: 24px;
    font-weight: 800;
}

.high-risk .result-title { color: #fb7185; }
.low-risk .result-title { color: #34d399; }

.probability {
    font-size: 56px;
    font-weight: 900;
    margin: 8px 0;
    letter-spacing: -0.02em;
}

.high-risk .probability { color: #f43f5e; }
.low-risk .probability { color: #10b981; }

/* Detail Breakdown Grid */
.detail-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 15px;
}

.detail-item {
    background: #000000;
    border: 1px solid #1c1c22;
    padding: 12px 16px;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.detail-label {
    font-size: 12px;
    color: #a1a1aa;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    font-weight: 600;
}

.detail-value {
    font-size: 14px;
    color: #ffffff;
    font-weight: 700;
}

/* Footer */
.footer {
    text-align: center;
    color: #52525b;
    margin-top: 50px;
    font-size: 13px;
}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- HERO ----------
st.markdown(
    """
<div class="hero">
    <div class="badge">
        ✦ AI Powered Customer Intelligence
    </div>
    <div class="title">
        ChurnAI
    </div>
    <div class="subtitle">
        Enterprise-grade Predictive Analytics & Risk Assessment
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ---------- LAYOUT ----------
left, right = st.columns([1.2, 1], gap="large")


# ---------- INPUTS ----------
with left:
    st.markdown(
        """
    <div class="card">
        <div class="section-title">👤 Customer Demographic & Financial Profile</div>
        <div class="section-text">
            Configure parameters to predict real-time churn probability.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        credit_score = st.number_input("💳 Credit Score", 300, 900, 650)
        country = st.selectbox("🌍 Country", ["France", "Spain", "Germany"])
        gender = st.selectbox("👤 Gender", ["Male", "Female"])
        age = st.number_input("🎂 Age", 18, 100, 35)
        tenure = st.number_input("📅 Tenure (Years)", 0, 10, 3)

    with col2:
        balance = st.number_input(
            "💰 Account Balance ($)", min_value=0.0, value=50000.0, step=1000.0
        )
        products = st.selectbox("📦 Active Products", [1, 2, 3, 4])
        credit_card = st.selectbox("💳 Credit Card Holder", ["Yes", "No"])
        active_member = st.selectbox("⚡ Active Member Status", ["Yes", "No"])
        salary = st.number_input(
            "💵 Estimated Salary ($)", min_value=0.0, value=75000.0, step=2500.0
        )

    st.markdown("<br>", unsafe_allow_html=True)
    predict = st.button("🔮 RUN CHURN PREDICTION")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------- RESULT & ANALYTICS ----------
with right:
    st.markdown(
        """
    <div class="card">
        <div class="section-title">🧠 Prediction Analytics & Profile Summary</div>
        <div class="section-text">
            Real-time inference generated by machine learning pipeline.
        </div>
    """,
        unsafe_allow_html=True,
    )

    if predict:
        # Prepare input dataframe matching target columns
        input_data = pd.DataFrame(
            [
                {
                    "credit_score": credit_score,
                    "country": country,
                    "gender": gender,
                    "age": age,
                    "tenure": tenure,
                    "balance": balance,
                    "products_number": products,
                    "credit_card": credit_card,
                    "active_member": active_member,
                    "estimated_salary": salary,
                }
            ]
        )

        # Feature Engineering Pipeline replica
        input_data["salary_balance_ratio"] = input_data["estimated_salary"] / (
            input_data["balance"] + 1
        )
        input_data["balance_per_product"] = (
            input_data["balance"] / input_data["products_number"]
        )
        input_data["high_balance"] = (input_data["balance"] > 100000).astype(int)

        def get_tenure_bucket(t):
            if t <= 2:
                return "Low"
            elif t <= 7:
                return "Medium"
            else:
                return "High"

        input_data["tenure_bucket"] = input_data["tenure"].apply(get_tenure_bucket)

        def get_age_group(a):
            if a < 30:
                return "Young"
            elif a < 50:
                return "Adult"
            else:
                return "Senior"

        input_data["age_group"] = input_data["age"].apply(get_age_group)

        # Predict probability
        prediction_proba = model.predict_proba(input_data)[0][1]
        churn_probability = prediction_proba * 100

        # Display Result Card
        if churn_probability >= 50:
            st.markdown(
                f"""
            <div class="result-card high-risk">
                <div class="result-icon">🚨</div>
                <div class="result-title">High Churn Risk</div>
                <div class="probability">{churn_probability:.1f}%</div>
                <div style="color: #a1a1aa; font-size: 13px;">Estimated Probability of Departure</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.warning(
                "💡 **Action Required:** High-risk customer detected. Consider offering exclusive retention packages or priority support."
            )
        else:
            st.markdown(
                f"""
            <div class="result-card low-risk">
                <div class="result-icon">🛡️</div>
                <div class="result-title">Low Churn Risk</div>
                <div class="probability">{churn_probability:.1f}%</div>
                <div style="color: #a1a1aa; font-size: 13px;">Estimated Probability of Departure</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.success(
                "✨ **Healthy Account:** Customer profile shows strong retention indicators."
            )

        # Detailed Customer Profile Overview
        st.markdown(
            "<h4 style='font-size: 15px; font-weight: 700; color: #e4e4e7; margin-top: 25px; margin-bottom: 10px;'>📊 Analyzed Customer Details</h4>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
        <div class="detail-grid">
            <div class="detail-item">
                <span class="detail-label">Age / Group</span>
                <span class="detail-value">{age} yrs ({input_data['age_group'].iloc[0]})</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Location</span>
                <span class="detail-value">{country}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Credit Score</span>
                <span class="detail-value">{credit_score}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Balance</span>
                <span class="detail-value">${balance:,.2f}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Active Member</span>
                <span class="detail-value">{active_member}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Products</span>
                <span class="detail-value">{products} Active</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Tenure</span>
                <span class="detail-value">{tenure} yrs ({input_data['tenure_bucket'].iloc[0]})</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Est. Salary</span>
                <span class="detail-value">${salary:,.2f}</span>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            """
        <div class="result-card">
            <div class="result-icon">🤖</div>
            <div class="result-title" style="color: #f4f4f5;">Awaiting Analysis</div>
            <div style="color: #71717a; margin-top: 8px; font-size: 14px;">
                Enter customer parameters on the left and click<br><b>RUN CHURN PREDICTION</b> to analyze risk.
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown(
    """
<div class="footer">
    ChurnAI • Enterprise Machine Learning Customer Churn Intelligence
    <br>
    Powered by Scikit-learn Pipeline • Built with Streamlit
</div>
""",
    unsafe_allow_html=True,
)
