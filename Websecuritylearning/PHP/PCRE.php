<?php
/*正则表达式（regular expression）* https://www.runoob.com/regexp/regexp-tutorial.html
1、用于判断或匹配某个字符串是否满足要求
2、用于从一个字符串中找到满足要求的内容
3、用于把一个字符串中满足要求的内容替换成其他内容
*/

/*
\	
将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。

^	
匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。

$	
匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。

*	
匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。

+	
匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。

?	
匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。

{n}	
n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。

{n,}	
n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。

{n,m}	
m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。
最多匹配m次后，即判定为匹配成功，后面的内容将不影响结果，除非使用“$”来标注结尾

?	
当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。

.	
匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.|\n)"的模式。
*/

//匹配
function re_01(){
    $source = "Google";
    $pattern = "/^Go*/";
    $result = preg_match($pattern,$source);
    if($result){
        echo "Matched!";    
    }else{
        echo "Not Matched!";
    }
}
//查找
function re_find(){
    $source = "google is Google";
    $pattern = "/go/";
    $matchedTimes = preg_match_all($pattern,$source,$result);
    print_r($result);//$result是一个数组变量，输出需要使用print_r或var_dump
    echo "<br/>Matched times:$matchedTimes";
}
//替换
function re_replace(){
    $source = "Google is Google";
    $pattern = "/Google/";
    echo "$source<br/>";
    $source = preg_replace($pattern,"xxxxxx",$source);
    echo "$source";
}
//re_01();
//re_find();
re_replace();
?>