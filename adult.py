import pandas as pd
import streamlit as st
import os
from git import Repo

# Set up GitHub authentication
GITHUB_REPO_PATH = 'https://github.com/nguyenthang2003/first.git'  # Local path where your GitHub repo is cloned
CSV_FILE_PATH = os.path.join(GITHUB_REPO_PATH, 'data.csv')  # The CSV file that will store data

# Set up the session state to store the data
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=['Giới tính', 'Tuổi', 'Chiều cao', 'Cân nặng', 'Hoạt động', 'BMI', 'BMR', 'TDEE'])

st.title('Theo dõi sức khoẻ')
st.write('Created **Thắng Nguyễn MD** & ***a little helped*** of **ChatGPT**')
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

# Append new entry to session data
new_data = {
    'Giới tính': gender,
    'Tuổi': age,
    'Chiều cao': h,
    'Cân nặng': w,
    'Hoạt động': active,
    'BMI': bmi,
    'BMR': bmr_value,
    'TDEE': tdee
}

# Add new row of data to session state DataFrame
st.session_state['data'] = st.session_state['data'].append(new_data, ignore_index=True)

# Display the accumulated data
st.subheader('Thông tin đã lưu:')
st.dataframe(st.session_state['data'])

# Save the data to a CSV file
st.session_state['data'].to_csv(CSV_FILE_PATH, index=False)

# Function to push changes to GitHub
def push_to_github(repo_path, commit_message):
    try:
        repo = Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        origin = repo.remote(name='origin')
        origin.push()
        st.success('Dữ liệu đã được lưu và đẩy lên GitHub thành công!')
    except Exception as e:
        st.error(f'Có lỗi xảy ra khi đẩy dữ liệu lên GitHub: {e}')

# Push the updated data to GitHub
if st.button('Lưu và đẩy lên GitHub'):
    push_to_github(GITHUB_REPO_PATH, 'Update data.csv with new user input')
