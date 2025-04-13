<?php
// إعدادات الاتصال بقاعدة البيانات الأولى (المصدر)
$servername1 = "localhost";
$username1 = "root";
$password1 = "";
$dbname1 = "project";

// إعدادات الاتصال بقاعدة البيانات الثانية (الهدف)
$servername2 = "localhost";
$username2 = "root";
$password2 = "";
$dbname2 = "login";

// إنشاء الاتصال بقاعدة البيانات المصدر
$conn_project = new mysqli($servername1, $username1, $password1, $project);
if ($conn1->connect_error) {
    die("Connection failed: " . $conn1->connect_error);
}

// إنشاء الاتصال بقاعدة البيانات الهدف
$conn_login = new mysqli($servername2, $username2, $password2, $login);
if ($conn2->connect_error) {
    die("Connection failed: " . $conn2->connect_error);
}

// المتغيرات التي سيتم استخدامها للبحث
$ = "";   
$ = "";
$ = "";
$ = "";
$ = "";
$ = "";
$ = "";
$ = "";

// استعلام لاستخراج البيانات بناءً على المتغيرين من قاعدة البيانات الأولى
$sql = "SELECT * FROM students WHERE student_phone = ? AND student_ticketnumberr = ? AND student_comment = ? AND student_email = ? AND student_id = ? AND student_name = ? AND student_servies = ? AND student_dep = ?; 
$stmt = $conn1->prepare($sql);
$stmt->bind_param("ss", $student_phone, $student_ticketnumberr, $student_comment, $student_email, $student_id, $student_name, $student_servies, $student_dep); 
$stmt->execute();
$result = $stmt->get_result();

// إذا كانت هناك بيانات مستخرجة من قاعدة البيانات الأولى
if ($result->num_rows > 0) {
    // استخراج البيانات من الاستعلام
    while ($row = $result->fetch_assoc()) {
        // نقل البيانات إلى قاعدة البيانات الثانية
        $column1 = $row['column1'];
        $column2 = $row['column2'];
        $column3 = $row['column3'];

        
        $insertSql = "INSERT INTO login ( computer , mange , stu , gg) VALUES (?, ?, ?)";
        $insertStmt = $conn2->prepare($insertSql);
        $insertStmt->bind_param("sss", $column1, $column2, $column3); 
        $insertStmt->execute();
    }


// استعلام سحب البيانات من قاعدة بيانات project
$sql = "SELECT column_name, value_column FROM source_table WHERE column_name IN ('computer', 'mang', 'stu', 'gg')";
$result = $project_conn->query($sql);

// التحقق من وجود نتائج
if ($result->num_rows > 0) {
    // تحضير استعلام لإدخال البيانات إلى قاعدة بيانات login
    while($row = $result->fetch_assoc()) {
        $computer = ($row['column_name'] == 'computer') ? $row['value_column'] : NULL;
        $mang = ($row['column_name'] == 'mang') ? $row['value_column'] : NULL;
        $stu = ($row['column_name'] == 'stu') ? $row['value_column'] : NULL;
        $gg = ($row['column_name'] == 'gg') ? $row['value_column'] : NULL;

        // استعلام لإدخال البيانات في جدول login
        $insert_sql = "INSERT INTO login (computer, mang, stu, gg) 
                        VALUES ('$computer', '$mang', '$stu', '$gg')";

        // تنفيذ الاستعلام في قاعدة بيانات login
        if ($login_conn->query($insert_sql) === TRUE) {
            echo "New record created successfully\n";
        } else {
            echo "Error: " . $insert_sql . "<br>" . $login_conn->error;
        }








    echo "Data transferred successfully.";
} else {
    echo "No data found matching the conditions.";
}


$stmt->close();
$insertStmt->close();
$conn1->close();
$conn2->close();
?>
