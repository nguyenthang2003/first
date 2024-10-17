import streamlit as st

# BMI calculation function
def bmi_cal(w, h):
    return w / (h / 100)**2

# BMR calculation function
def bmr_cal(w, h, age, gender):
    if gender == 'male':
        return 10 * w + 6.25 * h - 5 * age + 5
    else:
        return 10 * w + 6.25 * h - 5 * age - 161

# Streamlit app title and inputs
st.title('BMI, BMR, TDEE Calculator')
st.write('Enter your height, weight, age, and gender for calculation')

# User inputs
w = st.number_input('Weight (kg):', min_value=0.0, step=0.5)
h = st.number_input('Height (cm):', min_value=0.0, step=0.5)
age = st.number_input('Age (years):', min_value=10, step=1)
gender = st.radio('Gender: ', ('male', 'female'))

# Activity level dictionary and selection
activity_list = {
    'no': 1.2,
    'lightly': 1.375,
    'moderate': 1.55,
    'very': 1.725,
    'extremely': 1.9
}
activity = st.selectbox('Choose your level of activity:', list(activity_list.keys()))

# Combined Calculation (BMI, BMR, TDEE)
st.header('BMI, BMR, and TDEE Calculation')
if st.button('Calculate All'):
    if w > 0 and h > 0 and age > 0:
        # Calculate BMI
        bmi = bmi_cal(w, h)
        best_w = 22.5 * (h / 100) ** 2
        st.write(f'Your BMI is: {bmi:.2f}')
        st.write(f'Your optimal weight should be: {best_w:.1f} kg')
        
        # Calculate BMR
        bmr = bmr_cal(w, h, age, gender)
        st.success(f'Your BMR is: {bmr:.2f} kcal/day')
        
        # Calculate TDEE
        tdee = bmr * activity_list[activity]
        st.success(f'Your TDEE is: {tdee:.2f} kcal/day')
    else:
        st.error('Please enter valid weight, height, and age data.')

st.markdown("""<hr style="border:1px solid gray">""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>© 2024 by Bac si Thang Nguyen. All rights reserved.</p>", unsafe_allow_html=True)