Movie Ticket Booking System
Project Overview

The Movie Ticket Booking System is a Database Management System (DBMS) project developed to manage movie ticket reservations efficiently. The system allows users to view movies, select shows, book tickets, and make payments. It also enables administrators to manage movies, theatres, shows, bookings, and payment records.

This project demonstrates the implementation of database concepts such as table creation, relationships, SQL queries, joins, subqueries, stored procedures, triggers, and CRUD operations.

Features
User Module
View available movies
View show timings
Book movie tickets
Make payments
View booking details
Admin Module
Add movies
Update movie details
Delete movies
Manage theatres
Manage shows
View bookings
View payment records
Technologies Used
Frontend
HTML
CSS
JavaScript
Backend
PHP
Database
MySQL
Development Tools
Visual Studio Code
XAMPP/WAMP Server
MySQL Workbench (Optional)
Database Tables
Users

Stores customer information.

Column	Description
user_id	User ID
name	User Name
email	Email Address
phone	Contact Number
Movie

Stores movie details.

Column	Description
movie_id	Movie ID
title	Movie Name
genre	Movie Genre
duration	Duration in Minutes
Theatre

Stores theatre information.

Column	Description
theatre_id	Theatre ID
name	Theatre Name
location	Theatre Location
Shows

Stores movie show details.

Column	Description
show_id	Show ID
movie_id	Movie ID
theatre_id	Theatre ID
show_time	Show Timing
ticket_price	Ticket Price
available_seats	Available Seats
Booking

Stores ticket booking information.

Column	Description
booking_id	Booking ID
user_id	User ID
show_id	Show ID
number_of_tickets	Number of Tickets
Payment

Stores payment details.

Column	Description
payment_id	Payment ID
booking_id	Booking ID
amount	Payment Amount
payment_date	Payment Date
payment_method	Payment Method
Project Workflow
User registers in the system.
User views available movies.
User selects a movie and show.
User books tickets.
System checks seat availability.
Booking information is stored in the database.
Payment is processed.
Payment details are stored.
Trigger updates seat availability automatically.
SQL Operations Performed
CRUD Operations
Insert

Add new users, movies, theatres, bookings, and payments.

Read

Retrieve records from database tables.

Update

Modify movie, booking, and user details.

Delete

Remove records from the database.

SQL Queries Implemented
Retrieve all movies.
Display shows of a specific movie.
Display booking and user details.
Display booking, movie, and theatre details.
Count bookings per movie.
Display movies having more than 100 bookings.
Retrieve movies whose ticket price is greater than average.
Retrieve users who booked more tickets than a specific user.
Display all movies including those with no bookings.
Retrieve shows with no bookings.
Stored Procedures
Calculate Total Ticket Price

Calculates total amount based on ticket count and ticket price.

CALL TotalPrice(301);
Triggers
Seat Availability Trigger

Automatically reduces available seats after successful ticket booking.

CREATE TRIGGER UpdateSeats
AFTER INSERT ON Booking
FOR EACH ROW
Frontend Pages
Home Page

Displays navigation links.

Movies Page

Displays available movies.

Booking Page

Allows ticket booking.

Payment Page

Handles payment information.

Admin Dashboard

Manages records and database operations.

Advantages
Easy ticket booking process
Efficient data management
Automatic seat availability update
Secure payment record maintenance
Reduces manual work
Future Enhancements
Online payment gateway integration
User authentication and login
Seat selection interface
QR code ticket generation
Email and SMS notifications
Mobile application support
Conclusion

The Movie Ticket Booking System successfully demonstrates the practical implementation of Database Management System concepts including database design, normalization, SQL queries, joins, subqueries, stored procedures, triggers, and frontend-backend integration. The system provides an efficient solution for managing movie ticket reservations and theatre operations.
