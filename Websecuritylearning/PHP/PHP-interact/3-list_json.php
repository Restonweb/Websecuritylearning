<?php
    require_once('3-common.php');
    $conn = create_connection();
    $sql = "SELECT articleid,author,headline,viewcount,createtime FROM article WHERE articleid < 30";
    $result = mysqli_query($conn,$sql);
    $data = mysqli_fetch_all($result,MYSQLI_ASSOC);
    echo json_encode($data);
?>