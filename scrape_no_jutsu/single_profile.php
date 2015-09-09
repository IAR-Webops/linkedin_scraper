<?php
    $profilesfile = fopen("profiles", "w") or die("Unable to open file!");
    ftruncate($profilesfile);
    fwrite($profilesfile, $_GET['pid']);
    fclose($profilesfile);

    shell_exec("./single_profile.sh");
    header("Location: index.php");
?>
