<?php
  if (isset($_POST['data'])) {
    $data = json_decode($_POST['data']);

    if ($data->{'language'} === "python") $file = "gamify.py";
    if ($data->{'language'} === "java") $file = "gamify.java";
    if ($data->{'language'} === "c_cpp") $file = "gamify.cpp";

    try {
      file_put_contents ("../code/input.txt" , $data->{'input'});
      file_put_contents ("../code/".$file , $data->{'code'});

    } catch (Exception $e) {
      echo $e;
    }


      $output = shell_exec('python3 /var/www/html/GamifyString/code/compiler.py '.$data->{'language'}.' 2>&1');
      echo $output;

  }
  else {
    echo "Some error Occoured";
  }
 ?>
