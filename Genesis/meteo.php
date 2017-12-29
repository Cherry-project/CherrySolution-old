<?php

$city=$incparam;
$city=substr($city, 1);

$result1 = file_get_contents("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22$city%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys");

$data=json_decode($result1,true);
if($data['query']['results']['channel']['item']['condition'] != ""){
 	//Get current Temperature in CelsiusS
	if($data['query']['results']['channel']['item']['condition']['text']=="Mostly Cloudy"){
		$meteo = "plutôt nuageux";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Cloudy"){
		$meteo = "nuageux";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Partly Cloudy"){
		$meteo = "partiellement nuageux";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Mostly Sunny"){
		$meteo = "plutôt ensoleillé";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Sunny"){
		$meteo = "ensoleillé";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Partly Sunny"){
		$meteo = "partiellement ensoleillé";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Scattered Showers"){
		$meteo = "plutôt pluvieux";
	}else if($data['query']['results']['channel']['item']['condition']['text']=="Rain"){
		$meteo = "pluvieux";
	}else{
		$meteo="inconnu";
	}
	$temptoday = (intval($data['query']['results']['channel']['item']['condition']['temp'])-32)*(5/9);
	$reponsebot="Pour l'instant il fait un temps ".$meteo." à".$incparam." et il fait ".round($temptoday)." degrés";
}else{
	$reponsebot = "Je ne connais pas la météo à ".$city." désolée";
}

?>