<?php
$servername = "localhost";  // اسم السيرفر
$username = "root";         // اسم المستخدم لقاعدة البيانات
$password = "";             // كلمة المرور لقاعدة البيانات
$dbname = "project";        // اسم قاعدة البيانات

// إنشاء الاتصال
$conn = new mysqli($servername, $username, $password, $dbname);

// التحقق من الاتصال
if ($conn->connect_error) {
    die("فشل الاتصال: " . $conn->connect_error);
}

// استلام البيانات من النموذج
$student_dep = $_POST['student_dep'];
$student_servies = $_POST['student_servies'];
$student_name = $_POST['student_name'];
$student_phone = $_POST['student_phone'];
$student_id = $_POST['student_id'];
$student_email = $_POST['student_email'];
$student_comment= $_POST['student_comment'];

// تجهيز استعلام SQL لإدخال البيانات في جدول students
$sql = "INSERT INTO students (student_dep, student_servies, student_name, student_phone, student_id, student_email, student_comment) 
        VALUES ('$student_dep', '$student_servies', '$student_name', '$student_phone', '$student_id', '$student_email ', '$student_comment')";

// تنفيذ الاستعلام
if ($conn->query($sql) === TRUE) {
    // إعادة التوجيه إلى صفحة التأكيد
    echo "تم الارسال ، شكراً لك   : " . $conn->error;  // يمكن استبدال 'thankyou.php' بالصفحة التي تريد توجيه المستخدم إليها
    exit();
} else {
    echo "خطأ في إرسال البيانات: " . $conn->error;
}

// إغلاق الاتصال
$conn->close();
?>
