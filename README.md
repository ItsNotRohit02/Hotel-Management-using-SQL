# Hotel Booking Application

This is a simple hotel booking application built using Python and the Streamlit framework. The application allows users to select a room, provide their details, and confirm their booking. The application integrates with a database to store and retrieve customer and room information.

## Features

- Welcome message and description of the Four Seasons Hotel.
- User input for check-in and check-out dates, full name, age, SSN/Aadhaar, phone number, and address.
- Display of available rooms with their details, including room number, description, number of beds, air conditioning availability, and price.
- Selection of a room by entering the room number.
- Validation of user input for date, age, SSN/Aadhaar, and phone number.
- Confirmation of the booking with the customer details and room information.
- Display of the customer ID, name, SSN/Aadhaar, check-in and check-out dates, phone number, and room amount.
- Information about the bill payment due after the stay.

### The application utilizes the following database tables:

- customerdetails: Stores customer information including the customer ID, Aadhaar/SSN, name, age, phone number, address, final price, check-in date, and check-out date.
- room: Represents the hotel rooms with room number, room type ID, and size.
- roomtype: Contains details about room types, such as room type ID, number of beds, air conditioning availability, rate, and description.
- roomservice: Manages room service orders with order ID, item ID, quantity, and customer ID.
- items: Stores information about available items for room service, including item ID, item name, and rate.
- bookingdetails: Tracks the booking details with booking ID, customer ID, check-in date, check-out date, and final price.
- employees: Keeps records of hotel employees with employee ID, Aadhaar/SSN, name, age, gender, role ID, and salary.
- roles: Contains information about employee roles with role ID, role name, and salary.

### Backend functionality features for staff

- Get Price to Pay at Check Out: Allows the management staff to calculate and display the amount to be paid by a customer at check-out. The staff needs to enter the customer ID, and upon submission, the application retrieves the final amount from the database and displays it. It also updates the booking details with the customer ID and the final amount.
- Add Room Service Ticket: Enables the management staff to add a new room service ticket for a customer. The staff needs to enter the item ID, quantity, and customer ID. Upon clicking the "Add Ticket" button, the application adds the room service ticket to the database and displays a success message.
- List of Items: Displays a table containing the details of all available items for room service. The information includes the item ID, item name, and rate.
- List of Employees: Shows a table containing the details of all employees working at the hotel. The information includes the employee ID, SSN/Aadhaar, full name, age, gender, role ID, and salary.
- List of Employee Roles: Displays a table containing the details of all employee roles. The information includes the role ID, role name, and base salary.
- List of Rooms: Shows a table containing the details of all rooms in the hotel. The information includes the room number, room type ID, and size.
- List of Room Types: Displays a table containing the details of all room types available in the hotel. The information includes the room type ID, number of beds, air conditioning availability, nightly rate, and room description.
- List of Bookings: Shows a table containing the details of all bookings made at the hotel. The information includes the booking ID, customer ID, check-in date, check-out date, and final price.
- List of Customers: Displays a table containing the details of all customers who have booked a room. The information includes the customer ID, SSN/Aadhaar, full name, age, phone number, and address.
- List of Orders: Shows a table containing the details of all room service orders placed by customers. The information includes the order ID, item ID, quantity, and customer ID.

## Note

To run the application, execute Main_Page.py using `streamlt run Main_Page.py` while in command prompt and within the same directory. Make sure the MySQL server is running and the database connection details are correctly set in the DatabaseManager.py module.
