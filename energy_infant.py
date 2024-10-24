import streamlit as st
import pandas as pd
# infants nutrition
# import data
rda_dat= pd.read_excel('rda_data.xlsx')
who_dat=pd.read_excel('who_data.xlsx')


#get rda follow age of month
def get_rda(MonthOfAge):
    if 0< MonthOfAge <= 6  :
        return rda_dat[rda_dat['age_group']=='0_6'].iloc[0]
    elif 6 < MonthOfAge <=12 :
        return rda_dat[rda_dat['age_group']=='7_12'].iloc[0]
    else:
        return None
st.title('NHU CẦU DINH DƯỠNG CHO TRẺ :blue[0-12] THÁNG TUỔI')
st.write('***Created by :blue[Thắng Nguyễn MD] and :blue[ChatGPT]***',divider=True)
#get WHO_W_H data
def get_w_h(gender,age_month):
    if gender== 'Nam':
        return who_dat[(who_dat['age']==age_month)&(who_dat['gender']=='nam')].iloc[0]
    else:
        return who_dat[(who_dat['age']==age_month)&(who_dat['gender']=='nữ')].iloc[0]
    





col1, col2= st.columns([1,1])
with col1 :
    age_month= st.slider(label='Tháng tuổi của trẻ: ',
                            value= 2,
                            min_value=1,
                            max_value=24,
                            step=1)
    gender=st.selectbox(label='Giới tính của trẻ',options=['Nam','Nữ'])
    weight_now= st.number_input(label='Cân nặng của trẻ',
                              value=4.0,
                              min_value=1.0,
                              max_value=20.0,
                              step=0.1)
with col2 :
    st.subheader('Khuyến cáo về dinh dưỡng', divider=True)
    if st.button(label='**Kết quả khuyến cáo**'):
        rda= get_rda(age_month)
        if rda is not None:
            st.header(f':blue[Khuyến cáo dinh dưỡng cho trẻ] :red[***{age_month} tháng tuổi***]',divider=True)
            st.write(f"**Năng lượng**: {rda['Energy']} kcal/kg/ngày")
            st.write(f"**Chất bột đường**: {rda['Carbohydrate']} g/ngày")
            st.write(f"**Protein**: {rda['Protein']} g/ngày")
            st.write(f"**Chất béo**: {rda['Fat']} g/ngày")
            st.write(f'**Can-xi**: {rda['Calcium']} mg/ngày')
            st.write(f'**Vitamin D**: {rda['VitaminD']} mcg/ngày')
            st.write(f'**Kẽm**: {rda['Zinc']} mg/ngày')
        else: 
            st.write('dữ liêu chưa sẵn sàng')

        wh=get_w_h(gender,age_month)
        st.subheader(':blue[Khuyến cáo về cân nặng và chiều cao theo tháng tuổi]',divider=True)
        if wh is not None:
            st.write(f'CÂN NẶNG (kg):[ **:red[{wh['min_w']}]** -------- **:blue[{wh['max_w']}]**]')
            st.write(f'CHIỀU CAO (cm):[ **:red[{wh['min_h']}]** -------- **:blue[{wh['max_h']}]**]')
        else:
            st.write('NA')
