<?php

$places = array();
$graph = array(
  'A' => array('B' => 3, 'D' => 3, 'F' => 6),
  'B' => array('A' => 3, 'D' => 1, 'E' => 3),
  'C' => array('E' => 2, 'F' => 3),
  'D' => array('A' => 3, 'B' => 1, 'E' => 1, 'F' => 2),
  'E' => array('B' => 3, 'C' => 2, 'D' => 1, 'F' => 5),
  'F' => array('A' => 6, 'C' => 3, 'D' => 2, 'E' => 5),
  'view_corner' => array('A' => 6, 'C' => 3, 'D' => 2, 'E' => 5),
  'famous' => array('A' => 6, 'C' => 3, 'D' => 2, 'E' => 5),
  'nation_mart' => array('A' => 6, 'C' => 3, 'D' => 2, 'E' => 5)
);



function add_vertice(&$graph,$source,$destination,$distance){
  // add to graph
  $graph[$source][$destination] = (int) $distance;
  $graph[$destination][$source] = (int) $distance;

}

add_vertice($graph,1,2,55);
add_vertice($graph,1,3,18);
add_vertice($graph,'A',3,18);
//echo json_encode($graph);


class Dijkstra
{
  protected $graph;

  public function __construct($graph) {
    $this->graph = $graph;
  }

  public function shortestPath($source, $target) {
    // array of best estimates of shortest path to each
    // vertex
    $d = array();
    // array of predecessors for each vertex
    $pi = array();
    // queue of all unoptimized vertices
    $Q = new SplPriorityQueue();

    $edge_count = 0;
    $edges = array();

    foreach ($this->graph as $v => $adj) {
      $d[$v] = INF; // set initial distance to "infinity"
      $pi[$v] = null; // no known predecessors yet
      foreach ($adj as $w => $cost) {
        // use the edge cost as the priority
        $Q->insert($w, $cost);
        $edges[$edge_count] = array($w,$cost);
        $edge_count++;
      }
    }

    // initial distance at source is 0
    $d[$source] = 0;

    // we have count of edage 

    // we need to loop those count , not once 



    for($k = 0; $k<$edge_count; $k++){
      //echo "<h2>it is k $k</h2>";
      for($x =0; $x<$edge_count; $x++){
        $u = $edges[$x][0];
        if (!empty($this->graph[$u])) {
        // "relax" each adjacent vertex
        foreach ($this->graph[$u] as $v => $cost) {
          // alternate route length to adjacent neighbor
          $alt = $d[$u] + $cost;
          // if alternate route is shorter
          if ($alt < $d[$v]) {
            $d[$v] = $alt; // update minimum length to vertex
            $pi[$v] = $u;  // add neighbor to predecessors
                           //  for vertex
          }
        }
      }
      }
    }  


    while (!$Q->isEmpty()) {
      // extract min cost
      $u = $Q->extract();
      if (!empty($this->graph[$u])) {
        // "relax" each adjacent vertex
        foreach ($this->graph[$u] as $v => $cost) {
          // alternate route length to adjacent neighbor
          $alt = $d[$u] + $cost;
          // if alternate route is shorter
          if ($alt < $d[$v]) {
            $d[$v] = $alt; // update minimum length to vertex
            $pi[$v] = $u;  // add neighbor to predecessors
                           //  for vertex
          }
        }
      }
    }

    // we can now find the shortest path using reverse
    // iteration
    $S = new SplStack(); // shortest path with a stack
    $u = $target;
    $dist = 0;
    $solution_path = array();
    $solution = array("status"=>"no_route");

    // traverse from target to source
    while (isset($pi[$u]) && $pi[$u]) {
      $S->push($u);
      $dist += $this->graph[$u][$pi[$u]]; // add distance to predecessor
      $u = $pi[$u];
    }

    $solution['distance'] = $dist;
    // stack will be empty if there is no route back
    if ($S->isEmpty()) {
      //echo "No route from $source to $target \n";
      $solution["err_msg"] = "No route from $source to $target";
    }
    else {
      // add the source node and print the path in reverse
      // (LIFO) order
      $solution["status"] = "route";
      $S->push($source);
      //echo "$dist:";
      $sep = '';
      $node_count = 0;
      foreach ($S as $v) {
        //echo $sep, $v;
        $sep = '->';
        $solution_path[$node_count] = $v;
        $node_count++;
      }
      //echo "<br>";

      $solution['solution_path'] = $solution_path;

    }

    return $solution;
  }
}


$g = new Dijkstra($graph);

//$g->shortestPath('D', 'C');  // 3:D->E->C
//$g->shortestPath('C', 'A');  // 6:C->E->D->A
//$g->shortestPath('B', 'F');  // 3:B->D->F
//$g->shortestPath('F', 'A');  // 5:F->D->A 
//$g->shortestPath('E', 3);  // No route from A to G

//echo json_encode($g->shortestPath(5,'C'));
?>