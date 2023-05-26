<?php
    $articleid = $_REQUEST['articleid'];
    $conn = mysqli_connect("127.0.0.1","root","","test");
    mysqli_query($conn,"set names utf8");
    $sql = "DELETE from article WHERE articleid = $articleid";
    $stat = mysqli_query($conn,$sql);
    if($stat){
        echo "window.alert(已经删除文章id为" . $articleid . "的文章" . ")";
    }else{
        echo"window.alert('删除失败！')";
    }
?>