<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>这是一个PHP页面</title>
</head>
<body>
    <?php
        //可以在PHP的源文件中，直接写HTML代码，是不可以反过来的。
        /*可以用于注释一个段落*/
        echo "FUTURE";
        echo "<div style='width:300px;height:300px;border:solid 2px red;'>" . `time /t` . "</div>"
    ?>
</body>
</html>