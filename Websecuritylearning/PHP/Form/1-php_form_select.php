
<?php
/*
htmlspecialchars() 函数把预定义的字符转换为 HTML 实体。

预定义的字符是：

& （和号）成为 &
" （双引号）成为 "
' （单引号）成为 '
< （小于）成为 <
> （大于）成为 >
提示：如需把特殊的 HTML 实体转换回字符，请使用 htmlspecialchars_decode() 函数。
*/
$q = isset($_GET['q'])? htmlspecialchars($_GET['q']) : '';
if($q) {
        if($q =='<b>RUNOOB</b>') {
                echo '菜鸟教程<br>http://www.runoob.com';
                echo $q;
        } else if($q =='GOOGLE') {
                echo 'Google 搜索<br>http://www.google.com';
        } else if($q =='TAOBAO') {
                echo '淘宝<br>http://www.taobao.com';
        }
} else {
?>
<body>
<form action="" method="get"> 
    <select name="q">
    <option value="">选择一个站点:</option>
    <option value="RUNOOB">Runoob</option>
    <option value="GOOGLE">Google</option>
    <option value="TAOBAO">Taobao</option>
    </select>
    <input type="submit" value="提交">
    </form>
</body>
<?php
}
?>