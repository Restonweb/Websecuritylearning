<?php

class example{

private $a = 1;
private $b = 2;

public function __wakeup()
{
    if($this->a != 1 || $this->b != 2){
        die("NOPE");
    }
}

}

class fxxkexample{

    private $a = 1;
    private $b = 2;
    private $c = 3;

    public function __wakeup()
    {
        if($this->a != 1 || $this->b != 2){
            die("NOPE");
        }
    }

    public function speak(){
        echo "yessssssss";
    }

    public function __construct()
    {
    $this->speak();
    }

    }

$adam = new example();
$aser = serialize($adam);
echo $aser;
$aser = str_replace('"example":2','"example":3',$aser);
echo $aser;
unserialize($aser);


?>