
<?php
date_default_timezone_set('Asia/Shanghai');
/*请注意ob_flush()和flush()的区别。
前者是把数据从PHP的缓冲中释放出来，后者是把不在缓冲中的或者说是被释放出来的数据发送到浏览器。所以当缓冲存在的时候，我们必须ob_flush()和flush()同时使用。*/
$i =date("s");
while($i<=30){
    ob_flush();
    flush();
    echo date("Y-m-d H:i:s")."<br/>";
    $i = date("s");
    sleep(1);//sleep会阻塞缓存区输出，需要使用flush以及ob_flush进行缓存区的输出
}
?>