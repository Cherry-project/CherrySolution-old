<?php
    require "./includes.php";

	if(strpos($incparam, ",")!==false){
	$coup=explode(",",$incparam);
	}
	 	$s3 = new S3Access(LocalDBClientBuilder::get());
		$childrobotDao = new ChildrobotDAO(LocalDBClientBuilder::get());//DynamoDbClientBuilder::get());
        $content = new Childrobot();
        $content->setName($coup[0]);
        $content->setDessinA($coup[1]);
        $content->setAge($coup[2]);
        $childrobotDao->create($content);
	//$reponsebot='<span>'.$coup[0].$coup[1].$coup[2].'</span>';

?>