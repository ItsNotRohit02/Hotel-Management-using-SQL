import streamlit as st
import datetime


st.set_page_config(page_title="Hotel Booking",page_icon=":bar_chart:")


st.title('Welcome to Four Seasons Hotel')
st.write("XXX")
st.write("---")
col1,col2 = st.columns([1,0.5])
date = datetime.datetime.now().date()
with col1:
    st.write('Enter Check-in and Check-out date')
with col2:
    st.button(f"Today's Date 🗓️ {date}")

col5, col6 = st.columns(2)
with col5:
    checkin = st.date_input('Enter Check-in Date🗓️')
with col6:
    checkout = st.date_input('Enter Check-out Date🗓️')
if checkin>checkout:
    st.error('Check-out cannot be before check-in')

cname = st.text_input('Enter Your Full Name',value='Full Name Here')
cage = int(st.number_input('Enter Your Age',value=20))
if cage<18:
    st.error('You need to be an adult to book a hotel room')
aadhar = st.text_input('Enter your ID Number (SSN/Aadhaar)',value='1234 5678 9123')
try:
    int(aadhar.replace(' ', ''))
except ValueError:
    st.error('(SSN/Aadhaar) cannot have letters')
else:
    aadhar=int(aadhar.replace(' ', ''))
phone = st.text_input('Enter your phone number',value='9900880011')
if len(phone)!=10:
    st.error('Phone Number must be 10 digits')
try:
    int(phone)
except ValueError:
    st.error('Phone Number cannot have letters')
else:
    phone=int(phone)
caddress=st.text_area('Enter Your Address')
st.button('Submit')








