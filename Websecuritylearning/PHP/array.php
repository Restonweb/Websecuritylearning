<?php
/*
https://www.runoob.com/php/php-arrays.html
https://www.runoob.com/php/php-ref-array.html
*/
$color = array('r'=>'Red','b'=>'blue','g'=>'green');
//foreach用来遍历数组的每一个元素或者元素与其键值
foreach($color as $COLOR){//遍历数组的Value
    echo "$COLOR<br/>";
}

foreach($color as $key=>$value){//遍历数组的key与value
    echo "$key" . "===>" . "$value" . "<br/>";
}
$a[]="Anna";
$a[]="Brittany";
$a[]="Cinderella";
$a[]="Diana";
$a[]="Eva";
$a[]="Fiona";
$a[]="Gunda";
$a[]="Hege";
$a[]="Inga";
$a[]="Johanna";
$a[]="Kitty";
$a[]="Linda";
$a[]="Nina";
$a[]="Ophelia";
$a[]="Petunia";
$a[]="Amanda";
$a[]="Raquel";
$a[]="Cindy";
$a[]="Doris";
$a[]="Eve";
$a[]="Evita";
$a[]="Sunniva";
$a[]="Tove";
$a[]="Unni";
$a[]="Violet";
$a[]="Liza";
$a[]="Elizabeth";
$a[]="Ellen";
$a[]="Wenche";
$a[]="Vicky";

print_r($a);

?>