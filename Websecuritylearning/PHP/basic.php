<?php
    //必须使用这两个符号进行包裹PHP
    /*
    在PHP中，可以通过两个函数往页面中输出注释：
    (1)echo
    (2)print
    HTML中，所有的语句被浏览器进行处理，所以注释，语句代码（css,js,图片等）都会被输出到网页上
    而PHP会在PHP脚本引擎进行预处理后再向浏览器发送
    在PHP中，换行符\n无法被浏览器解析，<br>才可被浏览器解析
    */
    echo "郭哥最牛逼<br/>";
    print "AAA";

    echo "111","222","333<br>";//print不能用这种方式分割字符串
    //在PHP中，“.”表示字符串连接符
    echo "111"."222"."333<br>";
    //eg:
    echo "余额：". 20000 ."元<br>";

    /*引号的用法
    1、双引号可以包裹字符串和变量
    2、单引号只能包裹字符串，不能包含变量
    3、反引号用于执行操作系统命令并返回结果
    */
    $addr = "tokoyo";
    echo "Current address:$addr<br>";
    echo 'Current address:$addr<br>';
    //header("content-type:text/html;charset='GBK'");
    echo `ipconfig`;

    /*编码格式
    在执行上面的ipconfig命令时，会在网页上输出乱码，因为网页的编码为UTF-8，而操作系统的编码格式是GBK（中文编码）
    1、使用header函数向网页中写入GBK的响应头，让浏览器使用GBK编码格式处理整个网页
    2、使用PHP内置函数：iconv来对需要进行转码的文本进行格式转换，而不影响其他内容
    */
    $result = `ipconfig`;
    $result = iconv("GBK","UTF-8",$result);
    echo $result;

    /*PHP变量   https://www.runoob.com/php/php-variables.html
    PHP 支持以下几种数据类型:
    String（字符串）
    Integer（整型）
    Float（浮点型）
    Boolean（布尔型）
    Array（数组）
    Object（对象）
    NULL（空值）
    Resource（资源类型）

    PHP 变量规则：
    变量以 $ 符号开始，后面跟着变量的名称
    变量名必须以字母或者下划线字符开始
    变量名只能包含字母、数字以及下划线（A-z、0-9 和 _ ）
    变量名不能包含空格
    变量名是区分大小写的（$y 和 $Y 是两个不同的变量）
    */

    //运算符    https://www.runoob.com/php/php-operators.html

    /*正则表达式（regular expression）  https://www.runoob.com/regexp/regexp-tutorial.html
    1、用于判断或匹配某个字符串是否满足要求
    2、用于从一个字符串中找到满足要求的内容
    3、用于把一个字符串中满足要求的内容替换成其他内容
    */
?>