<?php
$city=$incparam;
$city=substr($city, 1);

$result1 = file_get_contents("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22$city%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys");

$data=json_decode($result1,true);
//Get current Temperature in CelsiusS
if($data['query']['results']['channel']['item']['forecast']!=""){

	$days=array();
	$tempinf=array();
	$tempsup=array();
	$meteo=array();
	//Pour une prévision à 7 jours
	for($i=1;$i<=7;$i++){
		// on recupere les infos dans le json
		// jours
		$days[$i]=$data['query']['results']['channel']['item']['forecast'][$i]['day'];
		if($days[$i]=='Mon'){
	    	$days[$i]='Lundi';
	    }else if($days[$i]=="Tue"){
	    	$days[$i]="Mardi";
	    }else if($days[$i]=="Wed"){
	    	$days[$i]="Mercredi";
	    }else if($days[$i]=="Thu"){
	    	$days[$i]="Jeudi";
	    }else if($days[$i]=="Fri"){
	    	$days[$i]="Vendredi";
	    }else if($days[$i]=="Sat"){
	    	$days[$i]="Samedi";
	    }else if($days[$i]=="Sun"){
	    	$days[$i]="Dimanche";
	    }
	    // temperatures inferieures
	    $tempinf[$i]=$data['query']['results']['channel']['item']['forecast'][$i]['low'];
	    // calcul pour la temp en degre celcius
	    $tempinf[$i]=(intval($tempinf[$i])-32)*(5/9);
	    // temperatures superieures
	    $tempsup[$i]=$data['query']['results']['channel']['item']['forecast'][$i]['high'];
	    $tempsup[$i]=(intval($tempsup[$i])-32)*(5/9);
	    // meteo
	    $meteo[$i]=$data['query']['results']['channel']['item']['forecast'][$i]['text'];
	    if($meteo[$i]=="Mostly Cloudy"){
			$meteo[$i] = "plutôt nuageux";
		}else if($meteo[$i]=="Cloudy"){
			$meteo[$i] = "nuageux";
		}else if($meteo[$i]=="Partly Cloudy"){
			$meteo[$i] = "partiellement nuageux";
		}else if($meteo[$i]=="Mostly Sunny"){
			$meteo[$i] = "plutôt ensoleillé";
		}else if($meteo[$i]=="Sunny"){
			$meteo[$i] = "ensoleillé";
		}else if($meteo[$i]=="Partly Sunny"){
			$meteo[$i] = "partiellement ensoleillé";
		}else if($meteo[$i]=="Scattered Showers"){
			$meteo[$i] = "plutôt pluvieux";
		}else if($meteo[$i]=="Rain"){
			$meteo[$i] = "pluvieux";
		}else{
			$meteo[$i]="inconnu";
		}
	}
	$reponsebot="Ah tu veux les prévisions de la semaine à ".$city.". Alors, ";
	for($i=1;$i<=7;$i++){
		echo $days[$i];
		echo $meteo[$i];
		$reponsebot.=" ".$days[$i]." il fera de ".round($tempinf[$i])." à ".round($tempsup[$i])." degrés, et avec un temps ".$meteo[$i].",";
	}
	$reponsebot = substr($reponsebot, 0, -1);
	$reponsebot.=". Voila pour les prévisions de la semaine.";
}else{
	$reponsebot="Je ne connais pas la météo de la semaine, désolé. Trop de recherches Yahou";
}


/*if($data['query']['results']['channel']['item']['condition']['text']=="Mostly Cloudy"){
	$meteo = "plutôt nuageux";
}else if($data['query']['results']['channel']['item']['condition']['text']=="Cloudy"){
	$meteo = "nuageux";
}else if($data['query']['results']['channel']['item']['condition']['text']=="Mostly Sunny"){
	$meteo = "plutôt ensoleillé";
}else if($data['query']['results']['channel']['item']['condition']['text']=="Sunny"){
	$meteo = "ensoleillé";
}else if($data['query']['results']['channel']['item']['condition']['text']=="Scattered Showers"){
	$meteo = "plutôt pluvieux";
}else if($data['query']['results']['channel']['item']['condition']['text']=="Rain"){
	$meteo = "pluvieux";
}else{
	$meteo="inconnu";
}
$temptoday = (intval($data['query']['results']['channel']['item']['condition']['temp'])-32)*(5/9);
$reponsebot="Pour l'instant il fait un temps ".$meteo." à".$incparam." et il fait ".round($temptoday)." degrés";*/
?>