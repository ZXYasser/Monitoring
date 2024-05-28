# # Function to mark lecture attendance
# from flask import app
# from python import send_email
# import sqlite3



# def mark_attendance(lecture_id, status):
#     conn = sqlite3.connect('lectures.db')
#     c = conn.cursor()
#     c.execute("UPDATE lectures SET attendance = ? WHERE id = ?", (status, lecture_id))
#     conn.commit()
#     conn.close()

# # Function to send email for missed lectures
# def send_missed_lecture_email(teacher_email, lecture_topic):
#     subject = "Missed Lecture Notification"
#     body = f"Dear Professor,\n\nThis is to inform you that your lecture on '{lecture_topic}' was missed today.\nPlease ensure to reschedule it or provide necessary arrangements.\n\nSincerely,\nLecture Management System"
#     send_email(teacher_email, subject, body)

# # Route for marking lecture attendance
# @app.route('/mark_attendance/<int:lecture_id>/<status>')
# def mark_attendance_route(lecture_id, status):
#     mark_attendance(lecture_id, status)
#     if status == 0:  # If lecture is missed
#         lecture = get_lecture_by_id(lecture_id)
#         teacher_email = lecture[4]  # Assuming email is stored in column index 4
#         lecture_topic = lecture[2]  # Assuming lecture topic is stored in column index 2
#         send_missed_lecture_email(teacher_email, lecture_topic)
#     return 'Attendance marked successfully!'

# # Function to get lecture by ID
# def get_lecture_by_id(lecture_id):
#     conn = sqlite3.connect('lectures.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM lectures WHERE id = ?", (lecture_id,))
#     lecture = c.fetchone()
#     conn.close()
#     return lecture







