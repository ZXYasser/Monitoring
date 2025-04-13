<?php
// Database connection settings
$servername = "localhost";
$username = "";
$password = "";
$dbname = "project";

// Create database connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to check login
function check_login($student_name, $student_id, $conn) {
    $stmt = $conn->prepare("SELECT * FROM student WHERE student_name = ? AND student_id = ?");
    $stmt->bind_param("si", $student_name, $student_id);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        return true;
    } else {
        return false;
    }
}

// Process login form data
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $student_name = $_POST['student_name'];
    $student_id = $_POST['student_id'];
    $student_email = $_POST['student_email'];
    $student_phone = $_POST['student_phone'];
    $student_comment = $_POST['student_comment'];
    
    if (empty($student_name) || empty($student_id)) {
        echo "Please enter both student name and student ID.";
    } else {
        if (check_login($student_name, $student_id, $conn)) {
            echo "Login successful! Welcome, " . htmlspecialchars($student_name) . ".";
        } else {
            echo "Invalid student name or student ID.";
        }
    }
} else {
    echo "Please use the form to login.";
}

// Close database connection
$conn->close();



// function to fetch data

$sql = "SELECT * FROM project";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "تم التحقق من البيانات : " . $row["column_name"] . "<br>";
    }
} else {
    echo "لا توجد بيانات";
}
$conn->close();


// Data processing

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $data = $_POST['data'];

    $sql = "INSERT INTO table_name (column_name) VALUES ('$data')";
    if ($conn->query($sql) === TRUE) {
        echo "تم إدخال البيانات بنجاح";
    } else {
        echo "خطأ: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();
}

?>
