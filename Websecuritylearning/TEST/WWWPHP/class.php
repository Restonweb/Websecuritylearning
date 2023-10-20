<?php

use Name as GlobalName;





class Name{
    private $username = 'nonono';
    private $password = 'yesyes';

    public function __construct($username,$password){
        $this->username = $username;
        $this->password = $password;
    }



            
        }

$a=new Name('admin',100);
echo serialize($a)
?>