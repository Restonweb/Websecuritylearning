<?php
    $conn = mysqli_connect("127.0.0.1","root","","test");
    mysqli_query($conn,"set names utf8");
    $result = mysqli_query($conn,"SELECT articleid FROM article");
    $result = mysqli_fetch_all($result);
    $r = count($result);
    echo "$r";
?>