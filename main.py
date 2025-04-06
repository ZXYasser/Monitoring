from flask import Flask, jsonify, redirect, render_template, request, url_for
import sqlite3
import os
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io
import os
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/static')
app.config['JSON_AS_ASCII'] = False

def create_attendance_table():
    conn = sqlite3.connect('room.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 room_number TEXT,
                 day TEXT,
                 lecture_time TEXT,
                 group_num TEXT,
                 group_type TEXT,
                 course_code TEXT,
                 course_name TEXT,
                 stu_num TEXT,
                 teacher_name TEXT,
                 attendance TEXT,
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

# Call the function to create the attendance table before using it
create_attendance_table()

#--------------------------------------------------------------------------------------------------------

# Define the dean's email address
DEAN_EMAIL = "yasserza009@gmail.com"



def send_email(receiver_email, missed_lecture=False, attachment_path=None, missed_lecture_details=None):
    sender_email = "FSCT.Follow@gmail.com"  # Replace with your email address
    password = "gygpaitrndtfiffu"  # Replace with your email password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = "تنبيه بعدم تنفيذ محاضره"

    if missed_lecture:
        # Send an email to the dean for missed lectures
        message["To"] = DEAN_EMAIL
        # Modify the body to indicate that it's a missed lecture notification
        body = """\
        عزيزي وكيل شؤون المدربين,

        هذه رساله للتنبيه بعدم تنفيذ محاضره. تجدون في النموذج المعلومات الكافيه.
        يرجى اتخاذ الإجراء المناسب.

        احترامي

        قسم المتابعه 
        فرع الكليه التقنيه بفرسان

        """
        message.attach(MIMEText(body, "plain"))

        # Attach the Word file if the attachment_path is provided
        if attachment_path:
            attachment_filename = os.path.basename(attachment_path)
            attachment = open(attachment_path, "rb")
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment_filename}",
            )
            message.attach(part)
    
    # If there are missed lecture details, include them in the email body
    if missed_lecture_details:
        message.attach(MIMEText(missed_lecture_details, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with your SMTP server
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to your Gmail account
        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

        




#--------------------------------------------------------------------------------------------------------


# Define a custom Jinja filter to sort days
def sort_days(days):
    day_order = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5}
    return sorted(days, key=lambda x: day_order[x])

    

# Register the custom filter in your Flask app
app.jinja_env.filters['sort_days'] = sort_days


#--------------------------------------------------------------------------------------------------------


# Function to create the 'teachers' table if it doesn't exist
def create_teachers_table():
    conn = sqlite3.connect('Teachers.db')
    c = conn.cursor()

    

    c.execute('''CREATE TABLE IF NOT EXISTS general_teachers (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
                 major TEXT
                 )''')
    
     # Create a table for computer teachers
    c.execute('''CREATE TABLE IF NOT EXISTS computer_teachers (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
               major TEXT
                 )''')
    # Create a table for management teachers
    c.execute('''CREATE TABLE IF NOT EXISTS management_teachers (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT,
               major TEXT
                 )''')
    conn.commit()
    conn.close()


# Call the function to create the table before using it
create_teachers_table()

# Function to store teacher details in the Teachers database
def store_teacher(name, email, major):
    conn = sqlite3.connect('Teachers.db')
    c = conn.cursor()
    if major.lower() == 'كمبيوتر':
        c.execute("INSERT INTO computer_teachers (name, email, major) VALUES (?, ?, ?)", (name, email, major))
    elif major.lower() == 'اداره':
        c.execute("INSERT INTO management_teachers (name, email, major) VALUES (?, ?, ?)", (name, email, major))
    else:
        c.execute("INSERT INTO General_teachers (name, email, major) VALUES (?, ?, ?)", (name, email, major))
    conn.commit()
    conn.close()

# Function to get all teachers from the Teachers database
def get_all_teachers():
    conn = sqlite3.connect('Teachers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM teachers")
    teachers = c.fetchall()
    conn.close()
    return teachers


#--------------------------------------------------------------------------------------------------------

# Function to create the 'room' database if it doesn't exist
def create_room_database():
    conn = sqlite3.connect('room.db')
    conn.close()

# Call the function to create the database before using it
create_room_database()

# Function to create a table for each uploaded CSV file
def create_table_for_file(filename):
    # Sanitize the filename to create a valid table name
    table_name = "table_" + ''.join(c if c.isalnum() else '_' for c in filename)
    conn = sqlite3.connect('room.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                 id INTEGER PRIMARY KEY,
                 room_number TEXT,
                 day TEXT,
                 lecture_time TEXT,
                 group_num TEXT,
                 group_type TEXT,
                 course_code TEXT,
                 course_name TEXT,
                 stu_num TEXT,
                 teacher_name TEXT
                 )''')
    conn.commit()
    conn.close()

# Function to store lecture details in the corresponding table
def store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name):
    # Sanitize the filename to get the table name
    table_name = "table_" + ''.join(c if c.isalnum() else '_' for c in filename)
    conn = sqlite3.connect('room.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO {table_name} (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name))
    conn.commit()
    conn.close()



#--------------------------------------------------------------------------------------------------------


# Route for adding a new lecture
@app.route('/add_lecture', methods=['GET', 'POST'])
def add_lecture():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename.replace('.csv', '')  # Remove the '.csv' extension from the filename
        if file.filename == '':
            return 'No file selected'
        if file:
            filepath = os.path.join('uploads', filename + '.csv')
            file.save(filepath)
            # Create a table for the uploaded file
            create_table_for_file(filename)
            # Read the CSV file and process each row
            encodings = ['utf-8', 'latin-1', 'iso-8859-1']  # List of possible encodings to try
            delimiters = [',', ';', '\t']  # List of possible delimiters to try
            for encoding in encodings:
                for delimiter in delimiters:
                    try:
                        with open(filepath, 'r', encoding=encoding) as f:
                            reader = csv.reader(f, delimiter=delimiter)
                            headers = next(reader, None)  # Read the header row
                            if headers is not None:
                                headers = [header.strip() for header in headers]  # Strip any extra whitespace
                                if len(headers) != 9:
                                    continue  # Try the next delimiter
                            else:
                                continue  # Missing header row, try the next delimiter
                            for row in reader:
                                if len(row) == 9:  # Check if the row has all required fields
                                    row = [item.strip() for item in row]  # Strip any extra whitespace
                                    room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
                                    # Store the lecture details in the corresponding table
                                    store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
                                else:
                                    return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
                        # If no exception is raised, break the loops and continue
                        break
                    except UnicodeDecodeError:
                        # If an exception is raised, try the next encoding
                        continue
                else:
                    # If none of the delimiters worked, try the next encoding
                    continue
                # If successful, break the encoding loop
                break
            else:
                return 'Failed to decode the file using any of the supported encodings and delimiters.'
            return 'Lectures added successfully!'
    else:
        # Render the form for uploading a CSV file and entering the filename
        return render_template('add_lecture.html')



# Function to get all lectures from the Room database
def get_all_lectures():
    conn = sqlite3.connect('Room.db')
    c = conn.cursor()
    c.execute("SELECT * FROM lectures")
    lectures = c.fetchall()
    conn.close()
    return lectures












#--------------------------------------------------------------------------------------------------------

# Function to get all uploaded CSV files
def get_uploaded_files():
    return [filename for filename in os.listdir('uploads') if filename.endswith('.csv')]




#--------------------------------------------------------------------------------------------------------
# Add route to render the add teacher form
@app.route('/add_teacher')
def add_teacher_form():
    return render_template('add_teacher.html')

# Route to handle form submission and store teacher data in the database
@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        major = request.form['major']
        if name and email:
            store_teacher(name, email, major)  # Store teacher data in the database
            return 'Teacher added successfully!'
        else:
            return 'Name and email and major are required fields.'
        

#--------------------------------------------------------------------------------------------------------#


@app.route('/view_lectures')
def view_files():
    files = get_uploaded_files()
    return render_template('view_files.html', files=files)


@app.route('/view_lectures/<filename>')
def view_lectures(filename, encodings=['utf-8', 'latin-1', 'iso-8859-1'], delimiters=[',', ';', '\t']):
    filepath = os.path.join('uploads', filename)
    days = set()  # Set to store unique days

    try:
        for encoding in encodings:
            for delimiter in delimiters:
                with open(filepath, 'r', encoding=encoding, errors='replace') as csvfile:
                    reader = csv.reader(csvfile, delimiter=delimiter)
                    headers = next(reader, None)  # Read the header row
                    if headers is None or len(headers) != 9:
                        continue  # Try the next delimiter or encoding
                    for row in reader:
                        if len(row) != 9:
                            print(f"Skipping invalid row: {row}")  # Debugging output for invalid rows
                            continue
                        days.add(row[1])  # Add the day to the set
                    break  # Stop trying delimiters if successful
            else:
                continue  # Try the next encoding if no delimiter worked
            break  # Stop trying encodings if successful

    except Exception as e:
        print(f"Error processing file: {e}")
        return str(e)

    return render_template('view_days.html', filename=filename, days=sorted(days))

#--------------------------------------------------------------------------------------------------------#

    
@app.route('/view_lectures/<filename>/<day>')
def view_lectures_by_day(filename, day, encodings=['utf-8', 'latin-1', 'iso-8859-1']):
    filepath = os.path.join('uploads', filename)
    lectures = []

    try:
        for encoding in encodings:
            with open(filepath, 'r', encoding=encoding , errors='replace') as csvfile:
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(csvfile.read(1024))  # Read a small portion of the file to detect the dialect
                csvfile.seek(0)  # Reset file pointer to beginning
                reader = csv.reader(csvfile, delimiter=dialect.delimiter)
                next(reader)  # Skip header row if present
                for row in reader:
                    if len(row) != 9:
                        print(f"Skipping invalid row: {row}")  # Debugging output for invalid rows
                        continue
                    if row[1] == day:  # Check if the row's day matches the requested day
                        lectures.append(row)
                break  # Stop trying encodings if successful

    except Exception as e:
        print(f"Error processing file: {e}")
        return str(e)

    return render_template('view_lectures_by_day.html', day=day, lectures=lectures)


#--------------------------------------------------------------------------------------------------------




@app.route('/update_attendance', methods=['POST'])
def update_attendance():
    print("Current Working Directory:", os.getcwd())
    if request.method == 'POST':
        room_numbers = request.form.getlist('room_number[]')
        days = request.form.getlist('day[]')
        lecture_times = request.form.getlist('lecture_time[]')
        group_nums = request.form.getlist('group_num[]')
        group_types = request.form.getlist('group_type[]')
        course_codes = request.form.getlist('course_code[]')
        course_names = request.form.getlist('course_name[]')
        stu_nums = request.form.getlist('stu_num[]')
        teacher_names = request.form.getlist('teacher_name[]')
        attendances = [request.form[f'attendance_{i}'] for i in range(1, len(room_numbers) + 1)]

        missed_lecture_details = []  # List to accumulate missed lecture details

        for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
            # Insert each attendance record into the attendance table
            conn = sqlite3.connect('room.db')
            c = conn.cursor()
            # c.execute("INSERT INTO attendance (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            #           (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance))
            # conn.commit()
            # conn.close()

            # Only insert records where attendance is either 'attended' or 'missed'
            if attendance in ('attended', 'missed'):
                c.execute("INSERT INTO attendance (room_number, day, lecture_time, group_num, group_type, "
                          "course_code, course_name, stu_num, teacher_name, attendance) "
                          "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (room_number, day, lecture_time, group_num, group_type,
                           course_code, course_name, stu_num, teacher_name, attendance))
                

                conn.commit()
            conn.close()


            if attendance == "missed":
                # Accumulate missed lecture details
                missed_lecture_details.append(f"{room_number}  :رقم القاعه ")
                missed_lecture_details.append(f"  {day} :اليوم  ")
                missed_lecture_details.append(f" {lecture_time} :وقت المحاضره ")
                missed_lecture_details.append(f"{teacher_name} : اسم المدرس")
                missed_lecture_details.append(f"{course_name} : اسم  المقرر")

        if missed_lecture_details:
            # Concatenate all missed lecture details into a single string
            missed_lecture_details_str = "\n".join(missed_lecture_details)
            # Send email with missed lecture details
            send_email(receiver_email=DEAN_EMAIL, missed_lecture=True, attachment_path="/home/ZXYasser/Monitoring/s.docx", missed_lecture_details=missed_lecture_details_str)
# C:\\Users\\ياسر الزهراني\\Desktop\\LecMonitoring\\s.docx
# /home/ZXYasser/Monitoring/s.docx
        # After processing, you may want to redirect the user to another page
        return redirect(url_for('view_files'))  # Redirect to view_files route after processing
    else:
        return redirect(url_for('view_files'))  # Redirect to view_files route if request method is not POST


#--------------------------------------------------------------------------------------------------------


@app.route('/delete_file', methods=['POST'])
def delete_file():
    if request.method == 'POST':
        # Get the filename from the request data
        filename = request.json.get('filename')

        # Check if the filename is provided
        if filename:
            filepath = os.path.join('uploads', filename)
            
            # Check if the file exists
            if os.path.exists(filepath):
                # Remove the file from the system
                os.remove(filepath)
                
                # Remove the corresponding table from the database
                table_name = "table_" + ''.join(c if c.isalnum() else '_' for c in filename.replace('.csv', ''))
                conn = sqlite3.connect('room.db')
                c = conn.cursor()
                c.execute(f"DROP TABLE IF EXISTS {table_name}")
                conn.commit()
                conn.close()
                
                return 'File and corresponding table deleted successfully', 200
            else:
                return 'File not found', 404
        else:
            return 'Filename not provided', 400
    else:
        return 'Method not allowed', 405

    
#--------------------------------------------------------------------------------------------------------

    
# Function to fetch teachers based on type (computer, management, general)
def get_teachers_by_type(type):
    conn = sqlite3.connect('Teachers.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {type}_teachers")
    teachers = c.fetchall()
    conn.close()
    return teachers

@app.route('/get_teachers')
def get_teachers():
    teacher_type = request.args.get('type')
    if teacher_type in ['computer', 'management', 'general']:
        teachers = get_teachers_by_type(teacher_type)
        return jsonify(teachers)
    else:
        return 'Invalid teacher type'
    
#--------------------------------------------------------------------------------------------------------


@app.route('/contactUs')     
def contactUs():
    return render_template('contactUs.html')

#--------------------------------------------------------------------------------------------------------


@app.route('/Equipment')     
def Equipment():
    return render_template('Equipment.html')



#--------------------------------------------------------------------------------------------------------



@app.route('/stat')     
def stat():
    conn = sqlite3.connect('room.db')
    c = conn.cursor()
    # Modify the SQL query to fetch only attended and missed lectures
    c.execute("SELECT * FROM attendance WHERE attendance IN ('attended', 'missed') ORDER BY timestamp DESC")
    attendance_records = c.fetchall()
    conn.close()
    return render_template('stat.html', attendance_records=attendance_records)



#--------------------------------------------------------------------------------------------------------


# @app.route('/view_attendance')
# def view_attendance():
#     conn = sqlite3.connect('room.db')
#     c = conn.cursor()
#     # Modify the SQL query to fetch only attended and missed lectures
#     c.execute("SELECT * FROM attendance WHERE attendance IN ('attended', 'missed') ORDER BY timestamp DESC")
#     attendance_records = c.fetchall()
#     conn.close()
#     return render_template('view_attendance.html', attendance_records=attendance_records)







#--------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # app.run(debug=True)
     app.run(host='0.0.0.0', port=5000, debug=True)