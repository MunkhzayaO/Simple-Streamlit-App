import streamlit as st
import streamlit.components.v1 as components




# Header iSection
st.set_page_config(page_title="A better You", page_icon=":tada", layout="wide")



##load assets
st.subheader("Hello everyone, We are the 'A Better You' team :wave:")
st.title("Self-improvement online course")
st.write("Our team goal is to help you craft your both inner & outer beauty")
#

# What we do
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What do we teach?")
    st.write("##")
    st.write("- We teach a morning & night meditation")
    st.write("- We teach a morning & night yoga")
    st.write("- We teach a healthy meal plan")
    st.write("- We provide free therapy classes")
    
with right_column:
    components.html("""
    <iframe src="https://lottie.host/?file=13e0ef29-293b-47c4-9ab7-7f4f1a99b29a/H5XtpG2S7U.json">
    </iframe>
    """)
   
#Contact
with st.container():
    st.write("--")
    st.header("Get In Touch With Us!")
    st.write("##")
    
    
    contact_form = """
    <form action="https://formsubmit.co/abetteryou.hello@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with right_column:
        st.empty()