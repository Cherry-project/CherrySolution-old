<?php

$search=$incparam;
$search=substr($search, 1);

$result1 = file_get_contents("https://fr.wikipedia.org/w/api.php?action=query&prop=extracts|info&exintro&titles=$search&format=json&explaintext&redirects&inprop=url&indexpageids");
$data=json_decode($result1);
$test="";
foreach($data->query->pages as $k)
{
    $test.=$k->extract;
}
$reponsebot.="J'ai recherché ".$incparam." sur wikipédia : voila ce que j'ai trouvé : ".$test;
?>