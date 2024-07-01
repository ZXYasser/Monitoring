### Academia and Resources Monitoring & Track System README

#### Overview
This system is designed to monitor and manage lecture attendance and resources at Farasan Technical College. It allows administrators to track attendance status for each lecture session, notify relevant personnel about missed lectures, and maintain records for reporting and analysis purposes. Additionally, it facilitates the monitoring of various equipment and resources such as computers, projectors, air conditioners, and more, across different rooms and facilities.

#### Features
- **Attendance Management:** Record and manage attendance for each lecture session.
- **Real-time Updates:** Immediate updates on attended and missed lectures.
- **Email Notifications:** Automatic notifications sent to administrators for missed lectures.
- **Equipment Monitoring:** Track the status of equipment like PCs, projectors, and air conditioners in different rooms and facilities.
- **Reporting:** Generate reports on attendance statistics by room, day, teacher, and course, as well as equipment maintenance and status reports.

#### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZXYasser/Monitoring.git
   cd attendance-tracking-system
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the SQLite database:**
   - Ensure `room.db` is in the project root directory.
   - Run database migrations or setup scripts if required.
   
4. **Configure email settings (optional):**
   - Modify `send_email` function in `app.py` to customize email sending behavior.
   - Update email templates in `templates/email_templates` folder if necessary.

#### Usage
- **Start the Flask application:**
  ```bash
  flask run
  ```
- **Access the application:**
  Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.
  
- **View and update attendance:**
  - Navigate to `/view_attendance` to view current attendance records.
  - Use `/add_lecture` to visit the homepage.
  
- **Equipment monitoring:**
  - Ensure to configure equipment options and statuses as per your requirements in the system.

#### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#### License
MIT License

#### Contact
For questions or feedback, contact Yasser Alzhrany at yasserza9@gmail.com

