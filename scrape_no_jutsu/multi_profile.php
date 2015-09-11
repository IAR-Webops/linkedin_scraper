<?php
    $profilesfile = fopen("multi_file", "w") or die("Unable to open file!");
    ftruncate($profilesfile);
    fwrite($profilesfile, $_GET['mpid']);
    fclose($profilesfile);

    shell_exec("./multi_profile.sh");
    header("Location: index.php");
?>
