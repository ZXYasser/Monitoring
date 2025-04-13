<?php
$servername = "localhost"; // Server name
$username = "";        // user name
$password = "";            // password
$dbname = "progect"; // Database name

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

//  check the connection
if ($conn->connect_error) {
    die("فشل الاتصال: " . $conn->connect_error);
}

// Receive data sent via POST
$username = $_POST[''];
$password = $_POST[''];
$email = $_POST[''];

// Entering data into the database
$sql = "INSERT INTO معلومات_الصفحة (اسم , بريد ,  ) VALUES ('$username', '$password', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "تم إرسال البيانات بنجاح";
} else {
    echo "خطأ: " . $sql . "<br>" . $conn->error;
}

// Close the connection
$conn->close();
?>

