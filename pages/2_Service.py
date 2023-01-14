import streamlit as st
import DatabaseManager

st.set_page_config(page_title="Service Page", page_icon=":wrench:")

st.title('Service Page')
st.write("---")

with st.expander('Add New Employee Details'):
    empid = int(st.number_input('Enter Employee ID', step=1))
    aadhar = st.text_input('Enter Employee SSN/Aadhaar')
    ename = st.text_input('Enter Employee Full Name')
    age = int(st.number_input('Enter Employee Age', step=1))
    gender = st.radio('Enter Employee Gender', options=['Male', 'Female'])
    roleid = int(st.number_input('Enter Employee RoleID', step=1))
    if st.button('Add Employee'):
        DatabaseManager.addEmployeeDetails(empid, aadhar, ename, age, gender, roleid)
        st.success('Successfully Updated')

with st.expander('Add New Items'):
    itemid = int(st.number_input('Enter Item ID', step=1))
    itemname = st.text_input('Enter Item Name')
    itemrate = float(st.number_input('Enter Price per Item'))
    if st.button('Add Item'):
        DatabaseManager.addItem(itemid, itemname, itemrate)
        st.success('Successfully Updated')

with st.expander('Add New Employee Roles'):
    roleid = int(st.number_input('Enter Role ID', step=1))
    rolename = st.text_input('Enter Role Name')
    rolesal = float(st.number_input('Enter Base Salary'))
    if st.button('Add Role'):
        DatabaseManager.addRole(roleid, rolename, rolesal)
        st.success('Successfully Updated')

with st.expander('Add New Room Types'):
    roomtypeid = int(st.number_input('Enter Room Type ID', step=1))
    bednum = int(st.number_input('Enter Number of Beds', step=1))
    ac = st.radio('Enter Air Conditioning', options=['AC', 'Non-AC'])
    roomrate = float(st.number_input('Enter Nightly Rate'))
    desc = st.text_area('Enter Room Description')
    if st.button('Add Room Type'):
        DatabaseManager.addRoomType(roomtypeid, bednum, ac, roomrate, desc)
        st.success('Successfully Updated')

with st.expander('Add New Rooms'):
    roomnum = int(st.number_input('Enter Room Number', step=1))
    roomid = int(st.number_input('Enter Room Type', step=1))
    size = int(st.number_input('Enter Room Size in sq-ft', step=1))
    if st.button('Add Room'):
        DatabaseManager.addRoom(roomnum, roomid, size)
        st.success('Successfully Updated')
