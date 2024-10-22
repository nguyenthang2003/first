import streamlit as st



st.title('Theo dõi BMI và nhu cầu năng lượng')
st.write('Created **Thắng Nguyễn MD** & ***a little helped*** by **ChatGPT**')
st.write('----------------------------')
col1, col2 = st.columns([1, 2])

with col1: 
    gender = st.selectbox('Giới tính', ['Nam', 'Nữ'])
    age = st.slider(label='Tuổi của bạn ', value=30)
    h = st.number_input(label='Chiều cao (cm): ', value=160.00, step=0.1)
    w = st.number_input(label='Cân nặng (kg): ', value=50.00, step=0.1)
    listActive = ['ít hoạt động', 'hoạt động nhẹ', 'hoạt động TB', 'hoạt động nặng', 'hoạt động rất nặng']
    active = st.selectbox('Mức độ hoạt động hằng ngày của bạn: ', listActive)
    
    # Calculate BMR
    if gender == 'Nam':
        bmr_value = 10 * w + 6.25 * h - 5 * age + 5
    else:
        bmr_value = 10 * w + 6.25 * h - 5 * age - 161
    
    dict_active = {'ít hoạt động': 1.2, 'hoạt động nhẹ': 1.375, 'hoạt động TB': 1.55, 'hoạt động nặng': 1.725, 'hoạt động rất nặng': 1.9}
    tdee = bmr_value * dict_active[active]

with col2:
    if h > 0:
        bmi = w / ((h / 100) ** 2)
        st.write(f'Chỉ số **BMI** của bạn: **{bmi:.1f}** (kg/m2)')
    else:
        st.write('**Chú ý nhập dữ liệu đúng**')
    
    st.write('Thể trạng của bạn thuộc nhóm: ')
    if bmi < 18.5:
        st.write('**Gầy**')
    elif 18.5 <= bmi < 23:
        st.write('**Cân nặng bình thường**')
    elif 23 <= bmi < 25:
        st.write('**Thừa cân**')
    elif bmi >= 25:
        st.write('**Béo phì**')
    else:
        st.write('***Vui lòng nhập đầy đủ thông tin***')
    
    good_w = 22.5 * h * h / 10000
    st.write(f' Cân nặng nên có của bạn: **{good_w:.1f}**')
    st.write('----------------------')
    st.write(f'Nhu cầu năng lượng BMR hiện tại của bạn là : **{bmr_value:.1f}** (kcal/day)')
    st.write(f'Nhu cầu năng lượng hiện tại với mức hoạt động **{active}** là: **{tdee:.1f}** (kcal/day)')
    st.write('----------------------')
