import streamlit as st
st.title("Suresh Rathod")
st.header("Namaste")
st.subheader("Hi hello")
st.text("Today i am starting Streamlit app")
st.write("Suresh Rathod")

# markdown function to write as html 
# it will run all markdown functions 

st.markdown("#### Hello") # heading tags 
st.markdown("**Bold text** and *italic text*") #bold text and italic text
st.markdown("1. apple") #ordered list
st.markdown("- namaste") #unorder list

st.markdown("[Google](https://www.google.com)") # hyper link
st.markdown("![suresh](https://merriam-webster.com/assets/mw/images/quiz/quiz-global-side-widget/alt-633b10471e2d4-9638-8574d472514fd4976be805512a1a9c1a@1x.jpg)") #image tag
st.markdown("---") #hr tag

st.caption("Hi this is a caption")
st.markdown("---")

# applying the latex tags

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") # you can apply all latex functions there ( you can access matrix code)

# you can all practise all latex tags

st.markdown("---")

st.header("Json function")

# example json function 
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)

st.markdown("---")

st.header("Code Implementation")

code="""
a=10
b=20
print(a+b) #printing the result
"""
st.code(code,language="py")

st.markdown("---")

# st.write(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

st.write("## Write function") # used to write anything and also for markup langugae

st.markdown("---") 

st.metric(label="Wind speed",value="120ms⁻¹",delta="-1.4ms⁻¹") # creating matric
st.markdown("---") 

import pandas as pd
st.header("DataFrame")

table=pd.DataFrame({"Name":["Suresh","Ramesh","naresh"],"Id No":[1,2,3]})
st.subheader("With table")
st.table(table) 
st.subheader("With Pandas dataframe")
st.dataframe(table)

st.markdown("---") 

# media managing
st.header("Media manager")
st.subheader("Image")
st.image("suresh.jpg",caption="This is my image",width=300)

st.subheader("Audio")
st.audio("namo_namo.mp3")
st.markdown("---")

st.header("Removing The Humburder and footBar")

hum="""
<style>
.css-eh5xgm.e1ewe7hr3{
    visibility: hidden
}
</style>
"""

foot="""
<style>
.css-cio0dv.e1g8pov61{
    visibility: hidden
}
</style>
"""

st.markdown(hum,unsafe_allow_html=True)
st.markdown(foot,unsafe_allow_html=True)

st.caption("code for Removing Humberger and footbar")
st.code(hum,language="html")
st.code(foot,language="html")

st.markdown("---")

st.header("Basic Wodgets")

# check box
def change():
    print(st.session_state.check)
state=st.checkbox("Click it ",value=False,on_change=change,key="check")
if state:
    st.write("Welcome Suersh")
else:
    st.write("Please Click it")

# radio button 
rad_btn=st.radio("what is capital city of ind?",options=["New delhi","Hyd","Mum"],key="ans")

#Button
def btn(ans):
    if ans=="New delhi":
        st.write("Correct Answer")
    else:
        st.write("Wrong Answer \n Correct Answer : New delhi")
st.button("Click me",on_click=btn(st.session_state.ans))

# select box 
select_bx=st.selectbox("who is your fav cricketer? select the answer:",options=["Suresh raina","Ms Dhoni","Virat Kohli","Rohit"],key="sel")

st.write(f"I am the fan of {st.session_state.sel}")

multi_select_bx=st.multiselect("who is your fav cricketer? select the answer:",options=["Suresh raina","Ms Dhoni","Virat Kohli","Rohit"],key="mulsel")

st.write(st.session_state.mulsel)

st.markdown("---")
st.title("File Uploading...")
image=st.file_uploader("Please upload an image",type=["jpg","png","jpeg"],accept_multiple_files=True)
if image is not None:
    st.image(image)
audio=st.file_uploader("Please upload an audio",type=["mp3","wav"])
if audio is not None:
    st.audio(audio)

try:
    video=st.file_uploader("Please upload an video",type=["mp4","mkv"])
    if video is not None:
        st.video(video)
except:
    st.caption("Please upload file less than 200 mb")

# some imp widgets 

# slider

st.slider("This is a slider1",max_value=1000,key="s1")
st.slider("This is a slider2",max_value=1000,key="s2",value=40)
st.caption("The sum of two sliders:")
st.write(f"{st.session_state.s1}+{st.session_state.s2} = {st.session_state.s1+st.session_state.s2}")

import streamlit as st

color,end_c = st.select_slider(
   'Select a color of the rainbow',
   options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
   value=("red","blue"))
st.write('My favorite color is', color,end_c)

# text input 

st.markdown("---")

st.title("Text Input..")

#one line input
val=st.text_input("Enter your Course Title:")
st.write(val)

# text area
text_a=st.text_area("Enter the code:",max_chars=4000,height=250)
if text_a is not None:
    st.code(text_a,language="py")


#date input 
data_input=st.date_input("Enter your DOB:")

#time input
time_input=st.time_input("Set Time",disabled=False)

#progress bar
import time

bar=st.progress(0)
progress_status=st.empty()
for i in range(100):
    bar.progress(i+1)
    progress_status.write(str(i+1)+"%")
    if(i==90):
        break
    time.sleep(0.1)
if(progress_status=="100%"):
    st.success("Task Completed")
else:
    st.error("This is an Error showing")




