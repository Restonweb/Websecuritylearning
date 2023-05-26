<?php
     $str = "点我生成验证码";
     $img = imagecreate(190,30);
     $font = "C:\Windows\Fonts\SIMYOU.ttf";
     imagecolorallocate($img,0xff,0xff,0xff);
     $black=imagecolorallocate($img,0x00,0x00,0x00);
     imagettftext($img,20,0,0,23,$black,$font,$str);
     header("Content-Type:image/png");
     imagepng($img,"vv.png");
?>