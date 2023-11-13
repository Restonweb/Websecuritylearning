<?php
    $file = $_GET['category'];

    if(isset($file))
    {
        if( strpos( $file, "woofers" ) !==  false || strpos( $file, "meowers" ) !==  false || strpos( $file, "index")){
            include ($file . '.php');
        }
        else{
            echo "Sorry, we currently only support woofers and meowers.";
        }
    }
?>