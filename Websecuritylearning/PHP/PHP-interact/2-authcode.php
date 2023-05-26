<?php
session_start();
$q=$_REQUEST['q'];
if($q == 'p'){
    $username = $_POST['username'];
    $password = $_POST['password'];
    $vcode = $_POST['vcode'];
    
//设置编码格式的两种方式
$conn = mysqli_connect('127.0.0.1','root','','test');

mysqli_query($conn,"set names utf8");
mysqli_set_charset($conn,"utf8");

//拼接SQL语句并执行它
$sql = "select * from test_login where username = '$username' and password = '$password'";
$result = mysqli_query($conn,$sql); //result获取到的查询结果，称为结果集

if(mysqli_num_rows($result) == 1 && $vcode == $_SESSION['vcodes'] ){
    echo 'window.location.href="2-list.php"';
    $_SESSION['vcodes'] = 66666;
}else{
    echo "window.alert('登陆失败！')";
    $_SESSION['vcodes'] = 66666;
}
//关闭数据库
mysqli_close($conn);
}else if($q=='g')
{ 
$authcode = rand(1000,9999);
$_SESSION['vcodes']=$authcode;
// $authcode = "1234";
 $authimg = imagecreate(190,30);
 $font = "C:\Windows\Fonts\Arial.ttf";
 imagecolorallocate($authimg,0xff,0xff,0xff);
 $black=imagecolorallocate($authimg,0x00,0x00,0x00);
 imagettftext($authimg,20,0,55,23,$black,$font,$authcode);
 header("Content-Type:image/png");
 imagepng($authimg);}
?>