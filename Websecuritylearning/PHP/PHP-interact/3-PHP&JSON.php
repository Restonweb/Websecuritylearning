<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JSON</title>
    <script>
        /**JSON Javascript object notation JS对象标记
        * 1、数组：索引数组适用于大多数编程语言，PHP名为关联数组，JAVA名为hashmap,Python中叫字典，Javascript中叫对象，都是键值对的搭配。
        * 2、CSV:纯文本型数据，带特定格式，使用逗号分隔
        * 3、XML:可扩展标记语言，与HTML格式完全一致，HTML的标签与属性是预先设定好的，用于网页元素的展现，而XML的标签是自定义的，用于存储数据
        * 4、JSON：Javascript object notation，是一种轻量级的数据交换格式，具有清晰简洁的层次结构，是在互联网上传输数据的重要手段。
        * 5、YAML:Yet Another Markup Language通常用于服务器端或应用系统的配置文件
        */
        // function json(){//数组
        //     var users = ["RedCamellia","Reston","Octa","Tempestissmo_125","Camellia"];
        //     for(var i=0;i<users.length;i++){
        //     document.write(users[i] + "||");
        //     }
        // var user1 = {name:"Redcamellia",gender:"male",age:19,ID:"114514",addr:"Earth"};//对象（PHP中的关联数组）：key:value
        // document.write(user1.name + "-" + user1.gender);
            
        // var user1 = {name:"RedCamellia",gender:"male",age:19,ID:"114514",addr:"Earth"};
        // var user2 = {name:"Camellia",gender:"female",age:20,ID:"1919810",addr:"Earth"};
        // var users = [user1,user2];//对象数组
        // document.write(users[1].ID);
        // document.write(users[1]['ID']);

        // var users = [{name:"RedCamellia",gender:"male",age:19,ID:"114514",addr:"Earth"},{name:"Camellia",gender:"female",age:20,ID:"1919810",addr:"Earth"}];//对象数组
        // document.write(users[1].ID);
        // document.write(users[1]['ID']);

        // var users = {user1:["RedCamellia","male",19,"114514","Earth",{isMarried:"nope"}],user2:["Camellia","female",20,"1919810","Earth",{isMarried:"nope"}]};//数组对象
        // document.write(users.user2[3]);
        // document.write(users.user1[5].isMarried);

        //由此可见，JSON就是对象与数组结合的各种形式。

        // }

        
    </script>
</head>
<body>
    <?php
        //引用common.php，如果之前已经引用则不再引用
        // require_once('common.php');
        // $conn = create_connection();
        // $sql = "SELECT articleid,viewcount,createtime FROM article WHERE articleid < 30";
        // $result = mysqli_query($conn,$sql);
        // $data = mysqli_fetch_all($result,MYSQLI_ASSOC);
        // echo json_encode($data);

        $user1 = array('name'=>'RedCameliia','age'=>'19','addr'=>'Earth','ID'=>'114514');
        $user2 = array('name'=>'Cameliia','age'=>'20','addr'=>'Earth','ID'=>'1919810');
        $users = array($user1,$user2);
        $users_json = '[{"name":"RedCameliia","age":"19","addr":"Earth","ID":"114514"},{"name":"Cameliia","age":"20","addr":"Earth","ID":"1919810"}]';
        print_r($users);
        echo json_encode($users);   //JSON序列化，将对象转换成字符串
        print_r(json_decode($users_json));  //JSON反序列化，将字符串转换成对象（PHP：关联数组）
    ?>
</body>
</html>
