<?php
$set = 1;
$Number = $_GET["num"];
//用ifelse进行判断
function judgeByIf(){
    global $Number;
    if((strlen($Number))!=11){
        echo "Phone Number Length Error!";
    }else if($Number[0]!='1'){
        echo "Phone Number Format Error!";
    }else if((is_numeric($Number))==false){
        echo "Is this Phone 'Number'??";
    }else{
        echo "Correct!!!!!!!!!!!!";
    }
}
/*正则表达式（regular expression）* https://www.runoob.com/regexp/regexp-tutorial.html
1、用于判断或匹配某个字符串是否满足要求
2、用于从一个字符串中找到满足要求的内容
3、用于把一个字符串中满足要求的内容替换成其他内容
*/

function judgeByRe(){
    global $Number;
    $pattern = "/^1\d{10}$/";
    $result = preg_match($pattern,$Number);
    if($result){
        echo "Correct!";
    }else{
        echo "Invalid Number!";
    }
}

if($set = 1 ){
    judgebyre();
}else if($set = 0){
    judgeByIf();
}

?>