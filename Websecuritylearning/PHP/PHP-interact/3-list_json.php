<?php
    require_once('common.php');
    $conn = create_connection();
    $sql = "SELECT articleid,viewcount,createtime FROM article WHERE articleid < 30";
    $result = mysqli_query($conn,$sql);
    $data = mysqli_fetch_all($result,MYSQLI_ASSOC);
    echo json_encode($data);
?>