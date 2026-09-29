import streamlit as st
import pandas as pd
import pickle
from datetime import date


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Diabetes Risk Prediction System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Main title */
    .main-title {
        font-size: 38px;
        font-weight: 700;
        text-align: center;
        color: #1f2937;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-header {
        font-size: 23px;
        font-weight: 650;
        color: #1f2937;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Patient card */
    .patient-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }

    /* Result card */
    .result-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
        margin-top: 20px;
    }

    .result-title {
        font-size: 26px;
        font-weight: 700;
    }

    .probability {
        font-size: 20px;
        color: #4b5563;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

try:

    with open("diabetes_model.pkl", "rb") as file:
        model = pickle.load(file)

except FileNotFoundError:

    st.error(
        "❌ Model file not found. Please run 'train_model.py' first."
    )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🩺 Diabetes Prediction")

    st.write(
        "This application uses a Machine Learning model "
        "to predict diabetes risk based on patient measurements."
    )

    st.divider()

    st.subheader("Model Information")

    st.write("**Algorithm:** Logistic Regression")
    st.write("**Dataset:** Pima Indians Diabetes Dataset")
    st.write("**Task:** Binary Classification")

    st.divider()

    st.subheader("Prediction")

    st.write("0 → No Diabetes")
    st.write("1 → Diabetes")


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🩺 Diabetes Risk Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Patient Risk Assessment'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# PATIENT DETAILS
# =========================================================

st.markdown(
    '<div class="section-header">👤 Patient Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2, col3 = st.columns(3)

    with col1:

        patient_name = st.text_input(
            "Patient Name",
            placeholder="Enter patient name"
        )

    with col2:

        patient_id = st.text_input(
            "Patient ID",
            placeholder="Example: PAT001"
        )

    with col3:

        gender = st.selectbox(
            "Gender",
            ["Select", "Male", "Female", "Other"]
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        patient_age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30
        )

    with col2:

        prediction_date = st.date_input(
            "Assessment Date",
            value=date.today()
        )

    with col3:

        doctor_name = st.text_input(
            "Doctor / Assessor",
            placeholder="Enter name"
        )


# =========================================================
# MEDICAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-header">🩸 Medical Measurements</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1,
            help="Number of times the patient has been pregnant."
        )

    with col2:

        glucose = st.number_input(
            "Glucose",
            min_value=0,
            max_value=300,
            value=120,
            help="Plasma glucose concentration."
        )

    with col3:

        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=0,
            max_value=200,
            value=70,
            help="Diastolic blood pressure."
        )

    with col4:

        skin_thickness = st.number_input(
            "Skin Thickness",
            min_value=0,
            max_value=100,
            value=20
        )

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        insulin = st.number_input(
            "Insulin",
            min_value=0,
            max_value=900,
            value=80
        )

    with col2:

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=25.0,
            step=0.1
        )

    with col3:

        diabetes_pedigree = st.number_input(
            "Diabetes Pedigree",
            min_value=0.0,
            max_value=3.0,
            value=0.5,
            step=0.01,
            help="A value related to family history of diabetes."
        )

    with col4:

        family_history = st.selectbox(
            "Family History",
            ["Select", "Yes", "No"]
        )


# =========================================================
# ADDITIONAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-header">📋 Additional Information</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    symptoms = st.multiselect(
        "Reported Symptoms",
        [
            "Increased thirst",
            "Frequent urination",
            "Increased hunger",
            "Fatigue",
            "Blurred vision",
            "Unexplained weight change",
            "No reported symptoms"
        ]
    )

    notes = st.text_area(
        "Additional Notes",
        placeholder="Enter any additional notes..."
    )


# =========================================================
# BUTTONS
# =========================================================

st.write("")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    predict_button = st.button(
        "🔍 Predict Diabetes",
        use_container_width=True,
        type="primary"
    )

with col2:
    clear_button = st.button(
        "🔄 Clear",
        use_container_width=True
    )


# =========================================================
# CLEAR
# =========================================================

if clear_button:

    st.rerun()


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # Basic validation

    if patient_name.strip() == "":
        st.warning("⚠️ Please enter the patient's name.")

    elif patient_id.strip() == "":
        st.warning("⚠️ Please enter the Patient ID.")

    elif gender == "Select":
        st.warning("⚠️ Please select the patient's gender.")

    elif family_history == "Select":
        st.warning("⚠️ Please select family history.")

    else:

        # -------------------------------------------------
        # Create model input
        # -------------------------------------------------

        input_data = pd.DataFrame({

            "Pregnancies": [pregnancies],

            "Glucose": [glucose],

            "BloodPressure": [blood_pressure],

            "SkinThickness": [skin_thickness],

            "Insulin": [insulin],

            "BMI": [bmi],

            "DiabetesPedigreeFunction": [diabetes_pedigree],

            "Age": [patient_age]

        })


        # -------------------------------------------------
        # Prediction
        # -------------------------------------------------

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        probability_percent = probability * 100


        st.divider()

        # -------------------------------------------------
        # PATIENT SUMMARY
        # -------------------------------------------------

        st.markdown(
            '<div class="section-header">📄 Patient Summary</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("**Patient Name**")
                st.write(patient_name)

            with col2:
                st.write("**Patient ID**")
                st.write(patient_id)

            with col3:
                st.write("**Age**")
                st.write(f"{patient_age} years")

            with col4:
                st.write("**Gender**")
                st.write(gender)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("**Assessment Date**")
                st.write(str(prediction_date))

            with col2:
                st.write("**Doctor / Assessor**")
                st.write(doctor_name if doctor_name else "Not provided")

            with col3:
                st.write("**Family History**")
                st.write(family_history)


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.markdown(
            '<div class="section-header">📊 Prediction Result</div>',
            unsafe_allow_html=True
        )

        if prediction == 1:

            st.error(
                f"⚠️ Diabetes Predicted for {patient_name}"
            )

            result_text = "Diabetes"

        else:

            st.success(
                f"✅ No Diabetes Predicted for {patient_name}"
            )

            result_text = "No Diabetes"


        # -------------------------------------------------
        # RESULT DETAILS
        # -------------------------------------------------

        with st.container(border=True):

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Prediction",
                    result_text
                )

            with col2:

                st.metric(
                    "Probability",
                    f"{probability_percent:.2f}%"
                )

            with col3:

                st.metric(
                    "Model",
                    "Logistic Regression"
                )


            st.write("")

            st.write("### Prediction Probability")

            st.progress(
                min(int(probability_percent), 100)
            )


        # -------------------------------------------------
        # MEASUREMENTS SUMMARY
        # -------------------------------------------------

        st.markdown(
            '<div class="section-header">🩸 Measurement Summary</div>',
            unsafe_allow_html=True
        )

        with st.container(border=True):

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Glucose", glucose)

            with col2:
                st.metric("Blood Pressure", blood_pressure)

            with col3:
                st.metric("BMI", f"{bmi:.1f}")

            with col4:
                st.metric("Insulin", insulin)


        # -------------------------------------------------
        # NOTES
        # -------------------------------------------------

        if notes:

            st.markdown(
                '<div class="section-header">📝 Notes</div>',
                unsafe_allow_html=True
            )

            st.info(notes)


        # -------------------------------------------------
        # DISCLAIMER
        # -------------------------------------------------

        st.warning(
            "⚠️ This prediction is generated by a Machine Learning "
            "model for educational purposes only. It is not a medical "
            "diagnosis and should not replace professional medical advice."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Diabetes Risk Prediction System • Logistic Regression • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)