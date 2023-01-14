import streamlit as st
import DatabaseManager

st.set_page_config(page_title="Management Page", page_icon=":wrench:")

st.title('Management Page')
st.write("---")

with st.expander('Get Price to Pay at Check Out'):
    cid = int(st.number_input('Enter Customer ID', step=1))
    if st.button('Submit'):
        totalamt = DatabaseManager.getFinalAmount(cid)
        st.info(f'Amount to be paid is {totalamt}')
        DatabaseManager.addBookingDetails(cid, totalamt)
        st.success('Successfully Updated')

with st.expander('Add Room Service Ticket'):
    itemid = int(st.number_input('Enter Item ID', step=1))
    quantity = int(st.number_input('Enter Quantity', step=1))
    rscid = int(st.number_input('Enter CustomerID', step=1))
    if st.button('Add Ticket'):
        DatabaseManager.addRoomService(itemid, quantity, rscid)
        st.success('Successfully Updated')

with st.expander('List of Items'):
    df = DatabaseManager.getAllItems()
    st.table(data=df)

with st.expander('List of Employees'):
    df = DatabaseManager.getAllEmployees()
    st.table(data=df)

with st.expander('List of Employee Roles'):
    df = DatabaseManager.getAllRoles()
    st.table(data=df)

with st.expander('List of Rooms'):
    df = DatabaseManager.getAllRooms()
    st.table(data=df)

with st.expander('List of Room Types'):
    df = DatabaseManager.getAllRoomTypes()
    st.table(data=df)

with st.expander('List of Bookings'):
    df = DatabaseManager.getAllBookingDetails()
    st.table(data=df)

with st.expander('List of Customers'):
    df = DatabaseManager.getAllCustomerDetails()
    st.table(data=df)

with st.expander('List of Orders'):
    df = DatabaseManager.getAllOrders()
    st.table(data=df)
