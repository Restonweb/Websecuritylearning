<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
/*
前后端的交互过程就是HTTP协议的处理过程：请求与响应的处理过程。
*/
foreach($_SERVER as $parm => $value){
    echo '<table>';
    echo '<tr>';
    echo '<td>' . $parm . '=' . $value . '<td/>';
    echo '<tr/>';
    echo '<table/>';
}
?>

</body>
</html>
