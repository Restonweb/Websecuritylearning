<?php
/*
使用PHP执行操作系统命令
1、使用反引号直接执行
2、
*/

$result = `ipconfig`;
$result = iconv('gbk','utf-8',$result);
echo "$result";
?>