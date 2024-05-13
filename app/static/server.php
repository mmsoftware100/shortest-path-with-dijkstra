<?php
// echo "this is server";
// we should return in JOSN format
/*
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
heaser('Access-Control-Allow-Headers: X-Requested-With');
*/

require('conn.php');
$returned_data = array("status"=>"fail");
$misc = json_encode($_GET);
$returned_data['misc'] = $misc;

$operation = "";
//$operation = $_GET['operation'];


if(isset($_GET['operation'])){
	$operation = $_GET['operation'];
}

//echo "opeation is ".$operation;
if($operation == "get_categories"){
	//echo "this is get cat";
	// select all categories from database and add rows data to returned data object

    $sql="SELECT * FROM categories";
    $result=$conn->query($sql);
    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();
        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
        }
        //echo "returend data is ".json_encode($returned_rows);
        $returned_data['categories'] = $returned_rows;
        $returned_data['status'] = "success";
    }
    else{
        $returned_data['err_msg']= "There is no rows in category table";
    }

}
else if($operation == "get_graph"){
    // 

    $sql="SELECT * FROM places";
    $result=$conn->query($sql);
    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();

        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
        }
        //echo "returend data is ".json_encode($returned_rows);
        $returned_data['places'] = $returned_rows;
        $returned_data['status'] = "success";
    }
    else{
        $returned_data['err_msg']= "There is no rows in places table in sql "+$sql;
    }

    $sql="SELECT * FROM links";
    $result=$conn->query($sql);
    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();

        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
        }
        //echo "returend data is ".json_encode($returned_rows);
        $returned_data['links'] = $returned_rows;
        $returned_data['status'] = "success";
    }
    else{
        $returned_data['status'] = "fail";
        $returned_data['err_msg']= "There is no rows in link table in sql ".$sql;
    }


}
else if($operation == "get_places"){
	$cat_id = $_GET['cat_id'];
	// select places acccording to categories
    //echo "this is get cat";
    // select all categories from database and add rows data to returned data object

    $sql="SELECT * FROM places WHERE cat_id = ".$cat_id;
    $result=$conn->query($sql);
    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();

        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
        }
        //echo "returend data is ".json_encode($returned_rows);
        $returned_data['places'] = $returned_rows;
        $returned_data['status'] = "success";
    }
    else{
        $returned_data['err_msg']= "There is no rows in places table in sql "+$sql;
    }


}
else if($operation == "places"){

    $sql="SELECT * FROM places";
    $result=$conn->query($sql);
    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();

        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
        }
        $returned_data['places'] = $returned_rows;
        $returned_data['status'] = "success";
    }
    else{
        $returned_data['err_msg']= "There is no rows in places table in sql "+$sql;
    }


}
else if($operation == "shortest_path"){
	$source = $_GET['source_id'];
	$destination = $_GET['destination_id'];

	// initialize graph from database

	// search shortest path between source and destination nodes

	// return solution path and distance in returned data object


    $sql="SELECT * FROM links";
    $result=$conn->query($sql);

    if ($result->num_rows >0){
        $num_index = 0;
        $returned_rows= array();

        require('graph_dijkstra.php');
        $pol_graph = array();

        while($row=$result->fetch_assoc()){
            $returned_rows[$num_index] = $row;
            $num_index++;
            add_vertice($pol_graph,$row['node1'],$row['node2'],$row['distance']);
        }

        //echo "<h2>The Pol Graph</h2>";
        //echo json_encode($pol_graph);

        //echo "<h2>The Solution Graph</h2>";
        $g = new Dijkstra($pol_graph);
        //echo json_encode($g->shortestPath($source,$destination));

        //echo "<br>";
        //echo "returend data is ".json_encode($returned_rows);
        $returned_data['links'] = $returned_rows;
        $returned_data['status'] = "success";
        $returned_data['solution'] = $g->shortestPath($source,$destination);

            
        $sql="SELECT * FROM places";
        $result=$conn->query($sql);
        if ($result->num_rows >0){
            $num_index = 0;
            $returned_rows= array();

            while($row=$result->fetch_assoc()){
                $returned_rows[$num_index] = $row;
                $num_index++;
            }
            //echo "returend data is ".json_encode($returned_rows);
            $returned_data['places'] = $returned_rows;
            $returned_data['status'] = "success";
        }
        else{
            $returned_data['err_msg']= "There is no rows in places table in sql "+$sql;
        }

    }
    else{
        $returned_data['status']= "fail";
        $returned_data['err_msg']= "There is no rows in places table in sql ".$sql;
    }




}

echo json_encode($returned_data);
?>