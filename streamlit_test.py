import streamlit as st
from PIL import Image

#사이드바 화면
st.sidebar.header("로그인")
user_id=st.sidebar.text_input("아이디 입력",value='',max_chars=15)
user_password=st.sidebar.text_input("패스워드 입력",value='',type='password')


#비번 누르기
if user_id=='pptnz' and user_password =='1234':
    st.sidebar.header("그림목록")
    sel_options=["",'20주년(1)','20주년(2)','20주년(3)']
    user_opt=st.sidebar.selectbox("페퍼톤스",sel_options,index=0)
    st.sidebar.write("**페퍼톤스,",user_opt)

#메인화면
st.subheader("페퍼톤스 20주년 이미지")
image_files=["pptns_welcome.jpg",'pptnz1.jpg','pptnz2.jpg','pptnz3.jpg']
sel_index = sel_options.index(user_opt)
image_file=image_files[sel_index]
image_local=Image.open(f"{image_file}")
st.image(image_local,caption=user_opt)








































