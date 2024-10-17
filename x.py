import streamlit as st

# Hàm tính toán BMI
def bmi_cal(w, h):
    return w / (h / 100)**2

# Hàm tính toán BMR
def bmr_cal(w, h, age, gender):
    if gender == 'nam':
        return 10 * w + 6.25 * h - 5 * age + 5
    else:
        return 10 * w + 6.25 * h - 5 * age - 161

# Tiêu đề và các mục nhập của ứng dụng Streamlit
st.title('Công cụ tính BMI, BMR, và TDEE')
st.write('Nhập chiều cao, cân nặng, tuổi và giới tính của bạn để tính toán')

# Nhập liệu từ người dùng
w = st.number_input('Cân nặng (kg):', min_value=0.0, step=0.5)
h = st.number_input('Chiều cao (cm):', min_value=0.0, step=0.5)
age = st.number_input('Tuổi (năm):', min_value=10, step=1)
gender = st.radio('Giới tính: ', ('nam', 'nữ'))

# Danh sách mức độ hoạt động và lựa chọn
activity_list = {
    'không': 1.2,
    'nhẹ': 1.375,
    'vừa': 1.55,
    'nặng': 1.725,
    'rất nặng': 1.9
}
activity = st.selectbox('Chọn mức độ hoạt động của bạn:', list(activity_list.keys()))

# Tính toán kết hợp (BMI, BMR, TDEE)
st.header('Kết quả tính BMI, BMR và TDEE')
if st.button('Tính tất cả'):
    if w > 0 and h > 0 and age > 0:
        # Tính BMI
        bmi = bmi_cal(w, h)
        best_w = 22.5 * (h / 100) ** 2
        st.write(f'Chỉ số BMI của bạn là: {bmi:.2f}')
        st.write(f'Cân nặng lý tưởng của bạn nên là: {best_w:.1f} kg')
        
        # Tính BMR
        bmr = bmr_cal(w, h, age, gender)
        st.success(f'Chỉ số BMR của bạn là: {bmr:.2f} kcal/ngày')
        
        # Tính TDEE
        tdee = bmr * activity_list[activity]
        st.success(f'Nhu cầu năng lượng hàng ngày của bạn (TDEE) là: {tdee:.2f} kcal/ngày')
    else:
        st.error('Vui lòng nhập dữ liệu hợp lệ về cân nặng, chiều cao và tuổi.')

st.markdown("""<hr style="border:1px solid gray">""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>© 2024 bởi Bác sĩ Thắng Nguyễn. Bảo lưu mọi quyền.</p>", unsafe_allow_html=True)
