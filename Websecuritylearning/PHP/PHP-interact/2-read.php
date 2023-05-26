<?php 
$id = $_GET['id'];
$conn = mysqli_connect('127.0.0.1','root','','test');

mysqli_query($conn,"set names utf8");

$sql = "select author,headline,createtime,content,viewcount from article where articleid=$id";
        $result = mysqli_query($conn,$sql);
        $articles = mysqli_fetch_all($result);
        // print_r($article); 
        $author = $articles[0][0];
        $headline = $articles[0][1];
        $createtime = $articles[0][2];
        $content = $articles[0][3];
        $viewcount = $articles[0][4];

        mysqli_query($conn,"UPDATE article SET viewcount=$viewcount+1 where articleid=$id");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文章阅读</title>
    <style>
        #box{
            border: solid 2px blue;
        }

        #box .header{
            border: solid 2px blue;
            height: 30px;
        }

        #box .h{
            width: auto;
            height: auto;
            float: left;
            margin-left: 30px;
            font-size: 20px;
        }

        #box .author{
            color: brown;
        }

        #box .headline{
            font-weight: bold;
            font-family: 黑体;
            text-align: center;
            margin-top: 2px;
        }

        #box .createtime{
            float: right;
            color: darkslategray;
            text-decoration: underline aqua;
        }

        #box .viewcount{
            float: right;
            color: darkslategray;
            text-decoration: underline aqua;
        }

        #box .reader{
            border:solid 2px green;
            height: 890px;
            font-size: 40px;
            font-family: 幼圆;
        }
    </style>
</head>
<body style="background-image: url(../../image/bg5.jpg); background-size: cover;">
    <?php
        echo '<div id="box">';
        echo '<div class="header">';
        echo '<div class="h author">'. "作者：$author" .'</div>';
        echo '<div class="h headline">'. "标题：$headline" .'</div>';
        echo '<div class="h createtime">'. "创建时间：$createtime" .'</div>';
        echo '<div class="h viewcount">'. "浏览次数：$viewcount 次" .'</div>';
        echo '</div>';
        echo '<div class="reader">' . "$content" . '</div>';
        echo '</div>';
        mysqli_close($conn);
    ?>
</body>
</html>