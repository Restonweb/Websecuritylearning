<?php
/*
前后端的交互过程就是HTTP协议的处理过程：请求与响应的处理过程。
*/

//echo $username . '-' . $password . '-' . $vcode;

//*前后端的数据提交获取方式必须一致

// $username = $_GET['username'];
// $password = $_GET['password'];
// $vcode = $_GET['vcode'];
// echo $username . '-' . $password . '-' . $vcode;

/*
在PHP中如何访问MySql数据库？
MySQLi和PDO
1.连接到MySQL数据库
2.执行SQL语句（CRUD）
3.处理SQL语句的结果
4.关闭数据库操作
*/

//验证码验证应该先于数据库连接
?>