<?php
// الاتصال بقاعدة البيانات
$servername = "localhost";
$username = "root"; // اسم المستخدم في MySQL
$password = ""; // كلمة مرور MySQL
$dbname = "login"; // اسم قاعدة البيانات

// إنشاء الاتصال
$conn = new mysqli($servername, $username, $password, $dbname);

// التحقق من الاتصال
if ($conn->connect_error) {
    die("فشل الاتصال: " . $conn->connect_error);
}

// التحقق من وجود بيانات المدخلات
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // استلام البيانات من النموذج
    $username = $_POST['username'];
    $password = $_POST['password'];

    // استعلام للتحقق من اسم المستخدم وكلمة المرور
    $sql = "SELECT * FROM loginss WHERE username = ? AND password = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $username, $password); // ربط المتغيرات مع الاستعلام
    $stmt->execute();
    $result = $stmt->get_result();

    // التحقق من وجود البيانات
    if ($result->num_rows > 0) {
        // إذا كان اسم المستخدم وكلمة المرور صحيحين
        session_start(); // بدء الجلسة
        $_SESSION['username'] = $username; // تخزين اسم المستخدم في الجلسة
        header("Location: students.php"); // توجيه المستخدم إلى صفحة رئيسية أو لوحة التحكم
    } else {
        // إذا كانت البيانات غير صحيحة
        echo "<p style='color: red;'>اسم المستخدم أو كلمة المرور غير صحيحة.</p>";
    }

    $stmt->close();
    $conn->close();
}
?>
