<?php
// الاتصال بقاعدة البيانات
$servername = "localhost";
$username = "root"; // اسم المستخدم في MySQL
$password = ""; // كلمة مرور MySQL
$dbname = "project"; // اسم قاعدة البيانات

// إنشاء الاتصال
$conn = new mysqli($servername, $username, $password, $dbname);

// التحقق من الاتصال
if ($conn->connect_error) {
    die("فشل الاتصال: " . $conn->connect_error);
}

// التحقق من وجود جلسة وتأكد من تسجيل الدخول
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.php"); // توجيه المستخدم إلى صفحة تسجيل الدخول إذا لم يكن مسجل الدخول
    exit();
}

// التحقق من وجود قيمة في المتغير student_dep
$student_dep = isset($_GET['student_dep']) ? $_GET['student_dep'] : '';

// استعلام لجلب بيانات الطلاب بناءً على student_dep
$sql = "SELECT * FROM students WHERE student_dep = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $student_dep); // ربط المتغير مع الاستعلام
$stmt->execute();
$result = $stmt->get_result();

// التحقق من وجود نتائج
if ($result->num_rows > 0) {
    // عرض البيانات في جدول HTML
    echo "<h2>بيانات الطلاب في قسم: $student_dep</h2>";
    echo "<table border='1'>
            <tr>
                <th> الرقم التدريبي</th>
                <th> اسم المتدرب</th>
                <th> القسم</th>
                <th> البريد الإلكتروني</th>
                <th> رقم الجوال </th>
                <th> نوع الخدمة </th>
                <th> ملاحظات  </th>
            </tr>";
    
    // عرض كل سطر من البيانات
    while ($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . $row['student_id'] . "</td>
                <td>" . $row['student_name'] . "</td>
                <td>" . $row['student_dep'] . "</td>
                <td>" . $row['student_email'] . "</td>
                <td>" . $row['student_servies'] . "</td>
                <td>" . $row['student_comment'] . "</td>
                <td>" . $row['student_phone'] . "</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "لا توجد بيانات للعرض.";
}

$stmt->close();
$conn->close();
?>
