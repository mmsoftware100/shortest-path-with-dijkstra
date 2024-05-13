<?php
$servername = "localhost";
$username = "root";
$password = "";
$db_name = "sandar";

$conn = new mysqli($servername, $username, $password, $db_name);

if($conn->connect_error){
	//echo "error in connection ". $conn->connect_error;
}
else {
	//echo "<br> Database Connected ";
}

?>