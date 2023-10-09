<?php
// $name = 'RedCamellia';

// function test(){
//     global $name;
//     echo "Hello! $name";
// }

// test();

class People{
    var $name = 'RedCamellia'; //类属性
    var $age = '19';
    var $addr = 'Xi`an';

    function talk(){
        echo "With me.<br/>";
    }
}


//实例化People
$p1 = new People();
$p1 -> name = 'Reston';
echo $p1 -> age;
echo $p1 -> name;

$p2 = new People();
$p2 -> talk();

?>