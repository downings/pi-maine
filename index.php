<?php
echo "<!DOCTYPE html>";
echo "<html>";
echo "<head>";
echo "<meta name = 'viewport' content = 'width = device-width'>";
echo "</head>";
echo "<body>";

echo 'The current temperature is ';
$result = exec('python temperature.py');
echo number_format((float)$result, 1, '.', '');
echo ' degrees Fahrenheit';
echo '<br>';echo '<br>';

$filename = '2temps.png';
echo "The plot was last modified on " . date ("F d Y H:i", filemtime($filename));
echo '<br>';echo '<br>';

#$result = exec('plotTempsLocal.py');
echo '<img src="2temps.png" alt="cant find image" height="368" width="500">';

print "</body>";
print "</html>";
?>

