<?php
    require "./includes.php";

	 	$s3 = new S3Access(LocalDBClientBuilder::get());
		$childrobotDao = new ChildrobotDAO(LocalDBClientBuilder::get());//DynamoDbClientBuilder::get());
        
        $child = $childrobotDao->get($incparam);
        $nom = $child->getName();
        $age = $child->getAge();
        $dessin = $child->getDessinA();

	$reponsebot=$age;

?>