import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title('Onlei Technologies')
st.header('By Akankshya Sahoo')
st.text('This is a tutorial on streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1><WELCOME></h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name ')
        dob=st.date_input('Choose Date of Birth ')
        marks=st.slider('Choose Marks ')
        k=st.form_submit_button('Submit Form')
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Downloads'):
    st.header('Downloads')
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt')
    
