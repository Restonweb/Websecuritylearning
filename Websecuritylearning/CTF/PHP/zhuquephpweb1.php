<?php
function gettime($func, $p) {
$result = call_user_func($func, $p);
$a= gettype($result);
if ($a == "string") {
return $result;
} else {return "";}
}

class Test {
var $p = "参数";
var $func = "函数";
function __destruct() {
if ($this->func != "") {
echo gettime($this->func, $this->p);
}
}
}

$a = new Test();
echo serialize($a)
?>
