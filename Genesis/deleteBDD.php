<?php
    require "./includes.php";

	if(strpos($incparam, ",")!==false){
	$coup=explode(",",$incparam);
	}
	 	$s3 = new S3Access(LocalDBClientBuilder::get());
		$childrobotDao = new ChildrobotDAO(LocalDBClientBuilder::get());//DynamoDbClientBuilder::get());
        
        $childrobotDao->delete($coup[0]);
	//$reponsebot='<span>'.$coup[0].$coup[1].$coup[2].'</span>';

?>