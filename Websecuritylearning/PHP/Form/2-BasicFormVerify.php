<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>信息验证</title>
    <style>
        .error{
            color: red;
        }
    </style>
</head>
<body>
    <!-- $_SERVER["PHP_SELF"] 变量有可能会被黑客使用！
    当黑客使用跨网站脚本的HTTP链接来攻击时，$_SERVER["PHP_SELF"]服务器变量也会被植入脚本。原因就是跨网站脚本是附在执行文件的路径后面的，
    因此$_SERVER["PHP_SELF"]的字符串就会包含HTTP链接后面的JavaScript程序代码。
    $_SERVER["PHP_SELF"] 可以通过 htmlspecialchars() 函数来避免被利用。
    -->
    <!-- 界面表单元素 -->
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <span class="error">*必填字段</span><br/>
    姓名：<input type="text" name="name"><span class="error">*</span><br/>
    手机号码：<input type="text" name="PhoneNumber"><span class="error">*</span><br/>
    备注：<textarea name="comment" cols="40" rows="5"></textarea><br/>
    性别：<input type="radio" name="gender" value="male">男
    <input type="radio" name="gender" value="female">女<span class="error">*</span>
    
    </form>

    <?php
    $name = $number = $gender = $comment ='';
    $nameErr = $numberErr = $genderErr = '';
    //必要字段错误信息提示
    if($_SERVER["REQUEST_METHOD"] == "POST")// 关于$_SERVER的用法： https://www.w3schools.cn/php/php_superglobals_server.asp
    {
        
    }
    //输入元素处理
    ?>
</body>
</html>