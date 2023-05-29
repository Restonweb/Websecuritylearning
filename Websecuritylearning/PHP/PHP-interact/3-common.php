<?php
    date_default_timezone_set("PRC");

    function create_connection(){
        $conn = mysqli_connect('127.0.0.1','root','','test') or die("数据库连接失败");
        mysqli_query($conn,"set names utf8");
        return $conn;
        }
?>