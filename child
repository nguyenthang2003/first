import streamlit as st

# Hàm tính toán năng lượng dựa trên nhu cầu khuyến nghị
def energy_needs(age_months, gender, weight):
    if gender == 'nam':
        if age_months <= 6:
            return 98 * weight  # kcal/kg/ngày cho bé nam 0-6 tháng
        else:
            return 82 * weight  # kcal/kg/ngày cho bé nam 7-24 tháng
    else:
        if age_months <= 6:
            return 95 * weight  # kcal/kg/ngày cho bé nữ 0-6 tháng
        else:
            return 80 * weight  # kcal/kg/ngày cho bé nữ 7-24 tháng

# Hàm tính số gam chất dinh dưỡng dựa trên năng lượng
def macronutrient_cal(energy_needs):
    protein_kcal = energy_needs * 0.07  # 7% từ protein
    carbohydrate_kcal = energy_needs * 0.55  # 55% từ carbohydrate
    fat_kcal = energy_needs * 0.38  # 38% từ chất béo

    protein_gram = protein_kcal / 4  # 1g protein = 4 kcal
    carbohydrate_gram = carbohydrate_kcal / 4  # 1g carbohydrate = 4 kcal
    fat_gram = fat_kcal / 9  # 1g fat = 9 kcal
    
    return protein_gram, carbohydrate_gram, fat_gram

# Tiêu đề và các mục nhập của ứng dụng Streamlit
st.title('Công cụ tính nhu cầu năng lượng cho trẻ từ 0-2 tuổi')
st.write('Nhập tuổi, giới tính và cân nặng của trẻ để tính toán nhu cầu năng lượng')

# Nhập liệu từ người dùng
age_months = st.number_input('Tuổi của trẻ (tháng):', min_value=0, max_value=24, step=1)
gender = st.radio('Giới tính của trẻ: ', ('nam', 'nữ'))
weight = st.number_input('Cân nặng của trẻ (kg):', min_value=0.0, step=0.1)

# Tính toán nhu cầu năng lượng và các chất dinh dưỡng
st.header('Kết quả tính nhu cầu năng lượng và dinh dưỡng')
if st.button('Tính nhu cầu năng lượng'):
    if weight > 0 and age_months >= 0:
        # Tính nhu cầu năng lượng
        energy = energy_needs(age_months, gender, weight)
        st.success(f'Nhu cầu năng lượng của trẻ là: {energy:.2f} kcal/ngày')

        # Tính số gam protein, carbohydrate, chất béo
        protein_gram, carbohydrate_gram, fat_gram = macronutrient_cal(energy)
        st.write(f'Protein: {protein_gram:.2f}g/ngày')
        st.write(f'Carbohydrate: {carbohydrate_gram:.2f}g/ngày')
        st.write(f'Chất béo: {fat_gram:.2f}g/ngày')
    else:
        st.error('Vui lòng nhập dữ liệu hợp lệ về tuổi và cân nặng.')

st.markdown("""<hr style="border:1px solid gray">""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>© 2024 bởi Bác sĩ Thắng Nguyễn. Bảo lưu mọi quyền.</p>", unsafe_allow_html=True)
