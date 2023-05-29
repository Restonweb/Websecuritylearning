<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文章列表</title>
    <style>
        table{
            width:800px;
            margin:auto;
            border:solid 1px green;
            border-spacing: 0px;
        }
        td{
            border:solid 1px green;
            height: 20px;
        }
        table tr button.delete{
            text-decoration: underline;
            font-size: smaller;
            width: 90px;
            text-align: center;
        }
        table tr button.delete:hover{
            color:red;
            cursor: pointer;
            font-size: small;
        }
    </style>
    <script type="text/javascript" src="jquery-3.7.0.min.js"></script>
    <script>function dodelete(){
        var articleid = $("#deleteid").val();
        var XMlde = new XMLHttpRequest();
        XMlde.onreadystatechange=function(){
            if(XMlde.readyState == 4 && XMlde.status == 200){
                // window.alert("已删除文章id为" + $arcticleid + "的文章");
                eval(XMlde.response);
            }
        }
        XMlde.open("GET","2-delete.php?articleid=" + articleid);
        XMlde.send();
    }
    </script>
</head>
<body>
    <?php
    session_start();
    if($_SESSION['islogin'] == false){
        die("请先登录再进行操作");
    }
    $conn = mysqli_connect('127.0.0.1','root','','test');

    mysqli_query($conn,"set names utf8");

    $sql = "select articleid,author,headline,viewcount,createtime from article where articleid<255";
    $result = mysqli_query($conn,"$sql");

    //将数据库查询的结果集中的数据取出，保存到一个数组中
    $rows = mysqli_fetch_all($result);

    //将结果遍历输出到页面上
    // foreach($rows as $row){
    //     echo $row[0] . '-' . $row[1] . '-' . $row[2] . '-' . $row[3] . '-' . $row[4] . "<br/>";
    // }
    echo '<table>';
    echo '<tr>';
    echo '<td>' . "文章标号" . '<td/>';
    echo '<td>' . "作者" . '<td/>';
    echo '<td>' . "标题" . '<td/>';
    echo '<td>' . "浏览次数" . '<td/>';
    echo '<td>' . "创建时间" . '<td/>';
    echo '<tr/>';
    //遍历结果在表格中显示
    foreach($rows as $row){
        echo '<tr>';
        echo '<td>' . $row[0] . '<td/>';
        echo '<td>' . $row[1] . '<td/>';
        echo '<td><a href="2-read.php?id=' . $row[0] . '">' . $row[2] . '<td/>';
        echo '<td>' . $row[3] . '<td/>';
        echo '<td>' . $row[4] . '<td/>';
        // echo '<button class="delete" onclick=' . '"dodelete()"' . '>' . '删除文章' . $row[0] .'</button>';
        echo '<tr/>';
    }
    echo '<table/>';
    mysqli_close($conn);
    ?>
    <input type="number" id="deleteid"/>
    <button type="button" class="delete" onclick="dodelete()">Delete</button>
</body>
</html>

<!-- 
    1、完善登录过程，完善验证码的验证
    2、设计一个新页面，实现用户的注册（用户名不能重复，如果可能，试着上传一张头像）-working
    3、实现文章列表的页面，同时在该页面添加“删除”按钮，用AJAX完成对文章的删除--ok
    4、实现read.php的文章阅读页面。--ok
    5、实现一个新页面，可以新增一篇文章。
 -->