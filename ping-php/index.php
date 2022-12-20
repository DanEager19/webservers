<h1>See if a host is up!</h1>
<form method="post">
    <label for="host">Host IP:</label>
    <input type="text" name="host" id="host">
    <input type="submit" name="submit" value="ping">
</form>
<pre>
    <?php 
        if (isset($_POST['submit'])) {
            $host = $_POST['host'];
            $output = shell_exec("ping -c 4 $host");
            echo($output);
        }
    ?>
</pre>