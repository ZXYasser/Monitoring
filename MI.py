
# # from flask import Flask, render_template, request, redirect, url_for
# # import sqlite3
# # import csv
# # import codecs
# # import os

# # app = Flask(__name__)

# # # Function to store lecture details
# # def store_lecture(teacher_name, lecture_topic, email, room_number,lecture_time, attendance):
# #     conn = sqlite3.connect('lectures.db')
# #     c = conn.cursor()
# #     c.execute("INSERT INTO lectures (teacher_name, lecture_topic, email, room_number,lecture_time, attendance) VALUES (?, ?, ?, ?, ?, ?)",
# #               (teacher_name, lecture_topic, email, room_number,lecture_time, attendance))
# #     conn.commit()
# #     conn.close()

# # # Function to get all lectures
# # def get_all_lectures():
# #     conn = sqlite3.connect('lectures.db')
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM lectures")
# #     lectures = c.fetchall()
# #     conn.close()
# #     return lectures

# # # Function to get all uploaded CSV files
# # def get_uploaded_files():
# #     return [filename for filename in os.listdir('uploads') if filename.endswith('.csv')]

# # # Route for adding a new lecture
# # @app.route('/add_lecture', methods=['GET', 'POST'])
# # def add_lecture():
# #     if request.method == 'POST':
# #         file = request.files['file']
# #         filename = request.form['filename']
# #         if file.filename == '':
# #             return 'No file selected'
# #         if file:
# #             filepath = os.path.join('uploads', filename + '.csv')
# #             file.save(filepath)
# #             # Read the CSV file and process each row
# #             with open(filepath, 'r', encoding='utf-8') as csvfile:
# #                 reader = csv.reader(csvfile)
# #                 next(reader)  # Skip header row if present
# #                 for row in reader:
# #                     if len(row) == 5:  # Check if the row has all required fields
# #                         teacher_name, lecture_topic, email, room_number, lecture_time = row
# #                         attendance = request.form.get(f'attendance_{teacher_name}_{lecture_topic}_{email}_{room_number}_{lecture_time}')
# #                         store_lecture(teacher_name, lecture_topic, email, room_number,lecture_time, attendance)
# #                     else:
# #                         return 'Invalid CSV format. Each row should contain teacher name, lecture topic, email, and room number.'
# #             return 'Lectures added successfully!'
# #     else:
# #         # Render the form for adding a new lecture
# #         return render_template('add_lecture.html')

# # # Route for viewing all uploaded files
# # @app.route('/view_lectures')
# # def view_files():
# #     files = get_uploaded_files()
# #     return render_template('view_files.html', files=files)

# # # Route for viewing lectures from a specific file
# # @app.route('/view_lectures/<filename>')
# # def view_lectures(filename):
# #     filepath = os.path.join('uploads', filename)
# #     lectures = []
# #     with open(filepath, 'r', encoding='utf-8') as csvfile:
# #         reader = csv.reader(csvfile)
# #         next(reader)  # Skip header row if present
# #         for row in reader:
# #             lectures.append(row)
# #     return render_template('view_lectures.html', lectures=lectures)

# # # Route for updating attendance
# # @app.route('/update_attendance', methods=['POST'])
# # def update_attendance():
# #     if request.method == 'POST':
# #         for key, value in request.form.items():
# #             if key.startswith('attendance_'):
# #                 lecture_id = key.split('_')[1]
# #                 update_lecture_attendance(lecture_id, value)
# #         return 'Attendance updated successfully!'
    
    

# # def update_lecture_attendance(lecture_id, attendance):
# #     conn = sqlite3.connect('lectures.db')
# #     c = conn.cursor()
# #     c.execute("UPDATE lectures SET attendance = ? WHERE id = ?", (attendance, lecture_id))
# #     conn.commit()
# #     conn.close()


# # if __name__ == '__main__':
# #     if not os.path.exists('uploads'):
# #         os.makedirs('uploads')
# #     app.run(debug=True)




# from flask import Flask, render_template, request
# import sqlite3
# import os
# import csv

# app = Flask(__name__)

# # Function to store lecture details in the Room database
# def store_lecture(room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name):
#     conn = sqlite3.connect('Room.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO lectures (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#               (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name))
#     conn.commit()
#     conn.close()

# # Function to get all lectures from the Room database
# def get_all_lectures():
#     conn = sqlite3.connect('Room.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM lectures")
#     lectures = c.fetchall()
#     conn.close()
#     return lectures

# # Function to get all uploaded CSV files
# def get_uploaded_files():
#     return [filename for filename in os.listdir('uploads') if filename.endswith('.csv')]

# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = request.form['filename']
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Read the CSV file and process each row
#             with open(filepath, 'r', encoding='utf-8') as csvfile:
#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip header row if present
#                 for row in reader:
#                     if len(row) == 9:  # Check if the row has all required fields
#                         room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                         # Store the lecture details
#                         store_lecture(room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                     else:
#                         return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')

# # Route for viewing all uploaded files
# @app.route('/view_lectures')
# def view_files():
#     files = get_uploaded_files()
#     return render_template('view_files.html', files=files)

# # Route for viewing lectures from a specific file
# @app.route('/view_lectures/<filename>')
# def view_lectures(filename):
#     filepath = os.path.join('uploads', filename)
#     lectures = []
#     with open(filepath, 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row if present
#         for row in reader:
#             lectures.append(row)
#     return render_template('view_lectures.html', lectures=lectures)

# # Route for updating attendance
# @app.route('/update_attendance', methods=['POST'])
# def update_attendance():
#     if request.method == 'POST':
#         for key, value in request.form.items():
#             if key.startswith('attendance_'):
#                 Lecture_id = key.split('_')[1]
#                 update_lecture_attendance(Lecture_id, value)
#         print("Attendance updated successfully!")
#         return 'Attendance updated successfully!'

# def update_lecture_attendance(Lecture_id, attendance):
#     print("Updating attendance for Lecture ID:", Lecture_id)
#     print("New Attendance Value:", attendance)
#     conn = sqlite3.connect('Room.db')
#     c = conn.cursor()
#     c.execute("UPDATE lectures SET attendance = ? WHERE room_number = ?", (attendance, Lecture_id))
#     conn.commit()
#     conn.close()

# if __name__ == '__main__':
#     # Create the Room database if it doesn't exist
#     if not os.path.exists('Room.db'):
#         conn = sqlite3.connect('Room.db')
#         c = conn.cursor()
#         c.execute('''CREATE TABLE lectures
#                      (room_number TEXT, day TEXT, lecture_time TEXT, group_num TEXT, group_type TEXT, course_code TEXT, course_name TEXT, stu_num TEXT, teacher_name TEXT, attendance TEXT)''')
#         conn.commit()
#         conn.close()
    
#     app.run(debug=True)


#--------------------------------------------------------------------------------------------------------        



# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = request.form['filename']
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Read the CSV file and process each row
#             with open(filepath, 'r', encoding='utf-8') as csvfile:
#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip header row if present
#                 for row in reader:
#                     if len(row) == 9:  # Check if the row has all required fields
#                         room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                         # Store the lecture details
#                         store_lecture(room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                     else:
#                         return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')
    




 
    # c.execute('''CREATE TABLE IF NOT EXISTS lectures (
    #              id INTEGER PRIMARY KEY,
    #              room_number TEXT,
    #              day TEXT,
    #              lecture_time TEXT,
    #              group_num TEXT,
    #              group_type TEXT,
    #              course_code TEXT,
    #              course_name TEXT,
    #              stu_num TEXT,
    #              teacher_name TEXT
    #              )''')
    # conn.commit()
    # conn.close()

# # Function to store lecture details in the Room database
# def store_lecture(room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name):
#     conn = sqlite3.connect('Room.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO lectures (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#               (room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name))
#     conn.commit()
#     conn.close()
# Function to store lecture details in the corresponding table


# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename.replace('.csv', '')  # Remove the '.csv' extension from the filename
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Create a table for the uploaded file
#             create_table_for_file(filename)
#             # Read the CSV file and process each row
#             with open(filepath, 'r', encoding='utf-8') as csvfile:
            



#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip header row if present
#                 for row in reader:
#                     if len(row) == 9:  # Check if the row has all required fields
#                         room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                         # Store the lecture details in the corresponding table
#                         store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                     else:
#                         return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')


# # Route for updating attendance
# @app.route('/update_attendance', methods=['POST'])
# def update_attendance():
#     if request.method == 'POST':
#         room_numbers = request.form.getlist('room_number[]')
#         days = request.form.getlist('day[]')
#         lecture_times = request.form.getlist('lecture_time[]')
#         group_nums = request.form.getlist('group_num[]')
#         group_types = request.form.getlist('group_type[]')
#         course_codes = request.form.getlist('course_code[]')
#         course_names = request.form.getlist('course_name[]')
#         stu_nums = request.form.getlist('stu_num[]')
#         teacher_names = request.form.getlist('teacher_name[]')
#         attendances = [request.form[f'attendance_{i}'] for i in range(1, len(room_numbers) + 1)]

#         for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
#               if attendance == "missed":
#                 # Call send_email for missed lectures
#                 send_email(DEAN_EMAIL, missed_lecture=True, attachment_path="C:\\Users\\Abdullah\\Desktop\\PHP\\1.pdf")


#         # Now you have all the data, you can process it accordingly
#         for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
#             # Process each lecture's attendance data
#             print(f"Room Number: {room_number}, Day: {day}, Lecture Time: {lecture_time}, Group Number: {group_num}, Group Type: {group_type}, Course Code: {course_code}, Course Name: {course_name}, Student Number: {stu_num}, Teacher Name: {teacher_name}, Attendance: {attendance}")
#         # After processing, you may want to redirect the user to another page
#         return redirect(url_for('view_files'))  # Redirect to view_files route after processing
#     else:
#         return redirect(url_for('view_files'))  # Redirect to view_files route if request method is not POST


# # Route for updating attendance
# @app.route('/update_attendance', methods=['POST'])
# def update_attendance():
#     if request.method == 'POST':
#         room_numbers = request.form.getlist('room_number[]')
#         days = request.form.getlist('day[]')
#         lecture_times = request.form.getlist('lecture_time[]')
#         group_nums = request.form.getlist('group_num[]')
#         group_types = request.form.getlist('group_type[]')
#         course_codes = request.form.getlist('course_code[]')
#         course_names = request.form.getlist('course_name[]')
#         stu_nums = request.form.getlist('stu_num[]')
#         teacher_names = request.form.getlist('teacher_name[]')
#         attendances = [request.form[f'attendance_{i}'] for i in range(1, len(room_numbers) + 1)]

#         # List to store details of missed lectures
#         missed_lecture_details = []

#         for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
#             if attendance == "missed":
#                 # Add details of missed lecture to the list
#                 missed_lecture_details.append(f"Room Number: {room_number}, Day: {day}, Lecture Time: {lecture_time}, Group Number: {group_num}, Group Type: {group_type}, Course Code: {course_code}, Course Name: {course_name}, Student Number: {stu_num}, Teacher Name: {teacher_name}")

#         # If there are missed lectures, send an email notification
#         if missed_lecture_details:
#             # Join the details into a single string
#             missed_lecture_details_str = "\n".join(missed_lecture_details)
#             # Call send_email function with the missed lecture details
#             send_email(receiver_email=DEAN_EMAIL, missed_lecture=True, attachment_path="C:\\Users\\Abdullah\\Desktop\\PHP\\1.pdf", missed_lecture_details=missed_lecture_details_str)

#         # Now you have all the data, you can process it accordingly
#         for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
#             # Process each lecture's attendance data
#             print(f"Room Number: {room_number}, Day: {day}, Lecture Time: {lecture_time}, Group Number: {group_num}, Group Type: {group_type}, Course Code: {course_code}, Course Name: {course_name}, Student Number: {stu_num}, Teacher Name: {teacher_name}, Attendance: {attendance}")
#         # After processing, you may want to redirect the user to another page
#         return redirect(url_for('view_files'))  # Redirect to view_files route after processing
#     else:
#         return redirect(url_for('view_files'))  # Redirect to view_files route if request method is not POST


# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename.replace('.csv', '')  # Remove the '.csv' extension from the filename
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Create a table for the uploaded file
#             create_table_for_file(filename)
#             # Read the CSV file and process each row
#             with open(filepath, 'r', encoding='utf-8') as csvfile:
            



#                 reader = csv.reader(csvfile)
#                 next(reader)  # Skip header row if present
#                 for row in reader:
#                     if len(row) == 9:  # Check if the row has all required fields
#                         room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                         # Store the lecture details in the corresponding table
#                         store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                     else:
#                         return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')



# def send_email(receiver_email, missed_lecture=False,attachment_path=None):
#     sender_email = "yasserza9@gmail.com"  # Replace with your email address
#     password = "ndzxmhmclfvqlrsk"  # Replace with your email password
    
    

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["Subject"] = "تنبيه بعدم تنفيذ محاضره"

#     if missed_lecture:
#         # Send an email to the dean for missed lectures
#         message["To"] = DEAN_EMAIL
#         # Modify the body to indicate that it's a missed lecture notification
#         body = """\
#         عزيزي وكيل شؤون المدربين,

#         هذه رساله للتنبيه بعدم تنفيذ محاضره. تجدون في النموذج المعلومات الكافيه.
#         يرجى اتخاذ الإجراء المناسب.

#         احترامي

#         قسم المتابعه 
#         فرع الكليه التقنيه بفرسان

#         """
#         message.attach(MIMEText(body, "plain"))

#         # Attach the Word file if the attachment_path is provided
#         if attachment_path:
#             attachment_filename = os.path.basename(attachment_path)
#             attachment = open(attachment_path, "rb")
#             part = MIMEBase("application", "octet-stream")
#             part.set_payload(attachment.read())
#             encoders.encode_base64(part)
#             part.add_header(
#                 "Content-Disposition",
#                 f"attachment; filename= {attachment_filename}",
#             )
#             message.attach(part)

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with your SMTP server
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)  # Login to your Gmail account
#         # Send the email
#         text = message.as_string()
#         server.sendmail(sender_email, receiver_email, text)



# # Route for viewing lectures for a specific day
# @app.route('/view_lectures/<filename>/<day>')
# def view_lectures_by_day(filename, day):
#     filepath = os.path.join('uploads', filename)
#     lectures = []
#     with open(filepath, 'r', encoding='utf-8') as csvfile:
    

#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row if present
#         for row in reader:
#             if row[1] == day:  # Check if the row's day matches the requested day
#                 lectures.append(row)

#     return render_template('view_lectures_by_day.html', day=day, lectures=lectures)








# # Route for updating attendance
# @app.route('/update_attendance', methods=['POST'])
# def update_attendance():
#     if request.method == 'POST':
#         room_numbers = request.form.getlist('room_number[]')
#         days = request.form.getlist('day[]')
#         lecture_times = request.form.getlist('lecture_time[]')
#         group_nums = request.form.getlist('group_num[]')
#         group_types = request.form.getlist('group_type[]')
#         course_codes = request.form.getlist('course_code[]')
#         course_names = request.form.getlist('course_name[]')
#         stu_nums = request.form.getlist('stu_num[]')
#         teacher_names = request.form.getlist('teacher_name[]')
#         attendances = [request.form[f'attendance_{i}'] for i in range(1, len(room_numbers) + 1)]

#         # Iterate over each lecture and send email if missed
#         for room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name, attendance in zip(room_numbers, days, lecture_times, group_nums, group_types, course_codes, course_names, stu_nums, teacher_names, attendances):
#             if attendance == "missed":
#                 # Prepare missed lecture details for this lecture
#                 missed_lecture_details = f"""\
#                     رقم القاعه: {room_number}
#                     اليوم: {day}
#                     وقت المحاضره: {lecture_time}
#                     اسم المدرس: {teacher_name}
#                     اسم المقرر: {course_name}
#                 """
                
#                 # Send email for this missed lecture
#                 send_email(receiver_email=DEAN_EMAIL, missed_lecture=True, missed_lecture_details=missed_lecture_details)


#         # After sending emails, you may want to process the data or redirect the user
#         # Here, I'm redirecting the user to another page after sending emails
#         return redirect(url_for('view_files'))  # Redirect to view_files route after processing
#     else:
#         return redirect(url_for('view_files'))  # Redirect to view_files route if request method is not POST






# # Example usage
# trainer_name = "اسم المدرب"
# course_name = "اسم المقرر"
# absence_status = "غياب"
# date = "2024-05-10"
# time_period = "24 ساعة"

# create_and_send_absence_certificate(trainer_name, course_name, absence_status, date, time_period)


# # Define the dean's email address
# DEAN_EMAIL = "yasserza009@gmail.com"

# def send_email(receiver_email, missed_lecture_details):
#     sender_email = "yasserza9@gmail.com"  # Replace with your email address
#     password = "ndzxmhmclfvqlrsk"  # Replace with your email password

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["Subject"] = "تنبيه بعدم تنفيذ محاضره"

#     # Send an email to the dean for missed lectures
#     message["To"] = receiver_email

#     # Modify the body to indicate that it's a missed lecture notification
#     body = """\
#     عزيزي وكيل شؤون المدربين,

#     هذه رساله للتنبيه بعدم تنفيذ محاضره. تجدون في النموذج المعلومات الكافيه.
#     يرجى اتخاذ الإجراء المناسب.

#     احترامي

#     قسم المتابعه 
#     فرع الكليه التقنيه بفرسان
#     """
#     message.attach(MIMEText(body, "plain"))

#     # If there are missed lecture details, include them in the email body
#     if missed_lecture_details:
#         message.attach(MIMEText(missed_lecture_details, "plain"))

#     with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with your SMTP server
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)  # Login to your Gmail account
#         # Send the email
#         text = message.as_string()
#         server.sendmail(sender_email, receiver_email, text)

# # Assume missed_lectures is a list of dictionaries, each representing a missed lecture.
# for lecture in missed_lectures:
#     # Construct the email details for this missed lecture
#     missed_lecture_details = f"""
#         رقم القاعه: {lecture['room_number']}
#         اليوم: {lecture['day']}
#         وقت المحاضره: {lecture['start_time']} - {lecture['end_time']}
#         اسم المدرس: {lecture['teacher_name']}
#         اسم المقرر: {lecture['course_name']}
#     """
#     # Send the email for this missed lecture
#     send_email(DEAN_EMAIL, missed_lecture_details)







# def create_absence_certificate(trainer_name, course_name, absence_status, date, time_period):
#     # Create a new Document
#     doc = Document()
    
#     # Add a title to the document
#     doc.add_heading('إفادة عن عدم تواجد', level=1)
    
#     # Add the provided information to the document
#     table = doc.add_table(rows=1, cols=2)
#     table.style = 'Table Grid'
#     table.cell(0, 0).text = 'اسم المدرب:'
#     table.cell(0, 1).text = trainer_name
    
#     row_cells = table.add_row().cells
#     row_cells[0].text = 'اسم المقرر:'
#     row_cells[1].text = course_name
    
#     row_cells = table.add_row().cells
#     row_cells[0].text = 'حالة عدم التواجد:'
#     row_cells[1].text = absence_status
    
#     row_cells = table.add_row().cells
#     row_cells[0].text = 'التاريخ:'
#     row_cells[1].text = date
    
#     row_cells = table.add_row().cells
#     row_cells[0].text = 'الفترة (الوقت):'
#     row_cells[1].text = time_period
    
#     # Add current date at the end of the document
#     today_date = datetime.now().strftime("%Y-%m-%d")
#     doc.add_paragraph(f"\nتاريخ الإنشاء: {today_date}")
    
#     # Save the document
#     doc.save("absence_certificate.docx")

# # Example usage
# trainer_name = "اسم المدرب"
# course_name = "اسم المقرر"
# absence_status = "غياب"
# date = "2024-05-10"
# time_period = "24 ساعة"

# create_absence_certificate(trainer_name, course_name, absence_status, date, time_period)


# def create_and_send_absence_certificate(trainer_name, course_name, absence_status, date, time_period):
#     # Create the absence certificate document
#     create_absence_certificate(trainer_name, course_name, absence_status, date, time_period)
    
#     # Define the attachment path
#     attachment_path = "absence_certificate.docx"

#     # Send the email with the attachment
#     send_email(receiver_email=DEAN_EMAIL, missed_lecture=True, attachment_path=attachment_path)









# Route for viewing lectures for a specific day
# @app.route('/view_lectures/<filename>/<day>')
# def view_lectures_by_day(filename, day):
#     filepath = os.path.join('uploads', filename)
#     attended_count = 0
#     missed_count = 0
#     lectures = []

    
    # # Retrieve lectures for the specified day from the database
    # with open(filepath, 'r', encoding='utf-8') as csvfile:
    #     reader = csv.reader(csvfile)
    #     next(reader)  # Skip header row if present
    #     for row in reader:
    #         if row[1] == day:  # Check if the row's day matches the requested day
    #             lectures.append(row)
    #             # Increment attended or missed count based on the attendance status
    #             if row[-1] == "attended":
    #                 attended_count += 1
    #             elif row[-1] == "missed":
    #                 missed_count += 1
                    
    # # Build the URL for stat.html using url_for
    # stat_url = url_for('stat', filename=filename, day=day)

    # return render_template('stat.html', day=day, attended_count=attended_count, missed_count=missed_count)


# def get_attended_lecture_count(filename, day):
#     # Connect to your database
#     conn = sqlite3.connect('your_database.db')
#     c = conn.cursor()

#     # Query the database to count attended lectures
#     c.execute("SELECT COUNT(*) FROM attendances WHERE filename = ? AND day = ? AND attendance = 'attended'", (filename, day))
#     attended_count = c.fetchone()[0]

#     # Close the database connection
#     conn.close()

#     return attended_count

# def get_missed_lecture_count(filename, day):
#     # Connect to your database
#     conn = sqlite3.connect('your_database.db')
#     c = conn.cursor()

#     # Query the database to count missed lectures
#     c.execute("SELECT COUNT(*) FROM attendances WHERE filename = ? AND day = ? AND attendance = 'missed'", (filename, day))
#     missed_count = c.fetchone()[0]

#     # Close the database connection
#     conn.close()

#     return missed_count


# @app.route('/statistics')
# def stat(filename, day):
#     # Query your database or perform data processing to get attended and missed counts
#     # For demonstration, I'll assume you have functions to retrieve these counts
#     attended_count = get_attended_lecture_count(filename, day)
#     missed_count = get_missed_lecture_count(filename, day)
#     return render_template('stat.html', day=day, attended_count=attended_count, missed_count=missed_count)







# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename.replace('.csv', '')  # Remove the '.csv' extension from the filename
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Create a table for the uploaded file
#             create_table_for_file(filename)
#             # Read the CSV file and process each row
#             # Open the file in binary mode and decode it to a string
#             with open(filepath, 'rb') as f:
#                 cleaned_content = f.read().decode('utf-8', errors='ignore')
#             # Parse the cleaned content as a CSV file
#             csvfile = io.StringIO(cleaned_content)
#             reader = csv.reader(csvfile)
#             next(reader)  # Skip header row if present
#             for row in reader:
#                 if len(row) == 9:  # Check if the row has all required fields
#                     room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                     # Store the lecture details in the corresponding table
#                     store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                 else:
#                     return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')









# # Route for viewing all uploaded files
# @app.route('/view_lectures')
# def view_files():
#     files = get_uploaded_files()
#     return render_template('view_files.html', files=files)


# # Modify the view_lectures route to display links for each day
# @app.route('/view_lectures/<filename>')
# def view_lectures(filename):
#     filepath = os.path.join('uploads', filename)
#     days = set()  # Set to store unique days
#     with open(filepath, 'r', encoding='latin-1') as csvfile:
    

#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row if present
#         for row in reader:
#             days.add(row[1])  # Add the day to the set

#     return render_template('view_days.html', filename=filename, days=sorted(days))\








# # Route for adding a new lecture
# @app.route('/add_lecture', methods=['GET', 'POST'])
# def add_lecture():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename.replace('.csv', '')  # Remove the '.csv' extension from the filename
#         if file.filename == '':
#             return 'No file selected'
#         if file:
#             filepath = os.path.join('uploads', filename + '.csv')
#             file.save(filepath)
#             # Create a table for the uploaded file
#             create_table_for_file(filename)
#             # Read the CSV file and process each row
#             encodings = ['utf-8', 'latin-1', 'iso-8859-1']  # List of possible encodings to try
#             for encoding in encodings:
#                 try:
#                     with open(filepath, 'r', encoding=encoding) as f:
#                         reader = csv.reader(f)
#                         next(reader)  # Skip header row if present
#                         for row in reader:
#                             if len(row) == 9:  # Check if the row has all required fields
#                                 room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name = row
#                                 # Store the lecture details in the corresponding table
#                                 store_lecture(filename, room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, teacher_name)
#                             else:
#                                 return 'Invalid CSV format. Each row should contain room_number, day, lecture_time, group_num, group_type, course_code, course_name, stu_num, and teacher_name.'
#                     # If no exception is raised, break the loop and continue
#                     break
#                 except UnicodeDecodeError:
#                     # If an exception is raised, try the next encoding
#                     continue
#             else:
#                 return 'Failed to decode the file using any of the supported encodings.'
#             return 'Lectures added successfully!'
#     else:
#         # Render the form for uploading a CSV file and entering the filename
#         return render_template('add_lecture.html')


   
    




# # Route for viewing lectures for a specific day
# @app.route('/view_lectures/<filename>/<day>')
# def view_lectures_by_day(filename, day):
#     filepath = os.path.join('uploads', filename)
#     lectures = []
#     with open(filepath, 'r', encoding='latin-1') as csvfile:
    

#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header row if present
#         for row in reader:
#             if row[1] == day:  # Check if the row's day matches the requested day
#                 lectures.append(row)

#     return render_template('view_lectures_by_day.html', day=day, lectures=lectures)


