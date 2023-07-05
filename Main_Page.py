import streamlit as st
import datetime
import DatabaseManager
from PIL import Image

st.set_page_config(page_title="Hotel Booking", page_icon=":office:")

st.title('Welcome to Four Seasons Hotel')
st.write("The Four Seasons Hotel offers luxurious guest rooms, elegant dining options, a fitness center, "
         "spa, and indoor pool. Perfect choice for a memorable stay.")
st.write("---")

one = st.empty()
two = st.empty()
three = st.empty()


def main():
    with one.container():
        st.header('Enter Details Below')
        col1, col2 = st.columns([1, 0.5])
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

        cname = st.text_input('Enter Your Full Name')
        cage = int(st.number_input('Enter Your Age', step=1))
        aadhar = st.text_input('Enter your SSN/Aadhaar')
        phone = st.text_input('Enter your phone number')
        caddress = st.text_area('Enter Your Address')

    with two.container():
        st.write("---")
        st.header('Select Room')

        with st.container():
            col1, col2 = st.columns([0.5, 1])
            row = DatabaseManager.getRoomType(1)
            with col1:
                image1 = Image.open('Images\Room1.jpg')
                st.image(image1)
            with col2:
                st.write(f'Room Number: {row[0]}')
                st.write(f'Description: {row[4]}')
                st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
                st.write(f'Air Conditioning: {row[2]}')
                st.write(f'Price: {row[3]}')
                st.write("---")
        with st.container():
            col3, col4 = st.columns([0.5, 1])
            row = DatabaseManager.getRoomType(2)
            with col3:
                image1 = Image.open('Images\Room2.jpg')
                st.image(image1)
            with col4:
                st.write(f'Room Number: {row[0]}')
                st.write(f'Description: {row[4]}')
                st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
                st.write(f'Air Conditioning: {row[2]}')
                st.write(f'Price: {row[3]}')
                st.write("---")

        with st.container():
            col5, col6 = st.columns([0.5, 1])
            row = DatabaseManager.getRoomType(3)
            with col5:
                image1 = Image.open('Images\Room3.jpg')
                st.image(image1)
            with col6:
                st.write(f'Room Number: {row[0]}')
                st.write(f'Description: {row[4]}')
                st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
                st.write(f'Air Conditioning: {row[2]}')
                st.write(f'Price: {row[3]}')
                st.write("---")

        with st.container():
            col7, col8 = st.columns([0.5, 1])
            row = DatabaseManager.getRoomType(4)
            with col7:
                image1 = Image.open('Images\Room4.jpg')
                st.image(image1)
            with col8:
                st.write(f'Room Number: {row[0]}')
                st.write(f'Description: {row[4]}')
                st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
                st.write(f'Air Conditioning: {row[2]}')
                st.write(f'Price: {row[3]}')
                st.write("---")

        with st.container():
            col9, col10 = st.columns([0.5, 1])
            row = DatabaseManager.getRoomType(5)
            with col9:
                image1 = Image.open('Images\Room5.jpg')
                st.image(image1)
            with col10:
                st.write(f'Room Number: {row[0]}')
                st.write(f'Description: {row[4]}')
                st.write(f'Number of Beds: {row[1]} || Air Conditioning: {row[2]}')
                st.write(f'Air Conditioning: {row[2]}')
                st.write(f'Price: {row[3]}')
                st.write("---")

        roomtypeid = st.number_input('Select Room Number', step=1)
        flag = 0

        if st.button('Submit'):
            if checkin > checkout:
                st.error('Check-out cannot be before check-in')
                flag = 1
            try:
                int(aadhar.replace(' ', ''))
            except ValueError:
                st.error('(SSN/Aadhaar) cannot have letters')
                flag = 1
            else:
                aadhar = int(aadhar.replace(' ', ''))
            if cage < 18:
                st.error('You need to be an adult to book a hotel room')
                flag = 1
            if len(phone) != 10:
                st.error('Phone Number must be 10 digits')
                flag = 1
            try:
                int(phone)
            except ValueError:
                st.error('Phone Number cannot have letters')
                flag = 1
            else:
                phone = int(phone)
            if flag == 0:
                st.success('Details Saved')

            if roomtypeid < 1 or roomtypeid > 5:
                st.error('Room Does Not Exist')
                flag = 1
            try:
                int(roomtypeid)
            except ValueError:
                st.error('Room Number cannot have letters')
                flag = 1
            else:
                roomtypeid = int(roomtypeid)
            if flag == 0:
                totalprice = DatabaseManager.selectRoom(roomtypeid, checkin, checkout)
                cid = DatabaseManager.addCustDetails(aadhar, cname, cage, phone, caddress, totalprice, checkin,
                                                     checkout)
                end(cid, checkin, checkout)


def end(cid, checkin, checkout):
    with three.container():
        one.empty()
        two.empty()
        row = DatabaseManager.getCustDetails(cid)
        st.success('Booking Confirmed')
        st.write(f'Customer ID: {cid}')
        st.write(f'Customer Name: {row[2]}')
        st.write(f'Customer Aadhaar: {row[1]}')
        st.write(f'Check In: {checkin}')
        st.write(f'Check Out: {checkout}')
        st.write(f'Customer Phone Number: {row[4]}')
        st.write(f'Room Amount: {row[6]}')
        st.info('Bill will be due after your Stay')


main()
