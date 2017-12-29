<?php


class ChildrobotDAO {
    private static $TABLE_NAME = 'Childrobot';
    private $client;
    
    public function __construct ($dynamoClient) {
        $this->client = $dynamoClient;
    }
    
    public function create ($content) {
        try {
            $this->client->putItem(array(
                'TableName' => ChildrobotDAO::$TABLE_NAME,
                'Item' => array(
                    'name'    => array('S' => $content->getName()),
                    'nameid'    => array('S' => $content->getName()),
                    'age'   => array('S' => $content->getAge()),
                    'dessinA'     => array('S' => $content->getDessinA())
                    )
            )); 
        } catch (Exception $e) {
            print $e->getMessage();
        }
    }
    
     public function get ($name) {
        
        $user = $this->getUser();
        $userDTO = $this->getUserDTO($name);
        if ($userDTO != null) {
            $this->fillUserAttributes($userDTO, $user);
            return $user;
        } else {
            return null;
        }
        return $user;
    }   
    protected function getUserDTO ($name) {

    $response = $this->client->getItem(array(
    'TableName' => ChildrobotDAO::$TABLE_NAME,
    'Key' => array(
        'name'  => array('S' => $name),
        'nameid'  => array('S' => $name),
    )
));

print_r($response['Item']);
        
        return $response['Item'];
    }
    
    protected function getUser () {
        return new Childrobot();
    }
    
    protected function fillUserAttributes ($userDTO, $user) {
        $user->setName($userDTO['name']['S']);
        $user->setAge($userDTO['age']['S']);
        $user->setDessinA($userDTO['dessinA']['S']);
    }
    

    /*//méthode à tester
    public function get($name) {
        $result = $this->client->getItem(array(
            'ConsistentRead' => true,
            'TableName' => ChildrobotDAO::$TABLE_NAME,
            'Key' => array(
                'name' => array('S' => $name)
            )
        ));
        $content = $this->toModel($result['Item']);
        return $content;
    }
    */
    public function delete ($name) {
        try {
            // DELETE the file from DynamoDB, table 'Contents'
            $this->client->deleteItem(array(
                'TableName' => ChildrobotDAO::$TABLE_NAME,
                'Key' => array(
                    'name'    => array('S' => $name),
                    'nameid'    => array('S' => $name),
                    )
            ));
        } catch (Exception $e) {
            echo '<p>Exception reçue : ',  $e->getMessage(), "\n</p>";
        }
    }
    
    private function toModel($dto) {
        // Convert DTO into model object
        $content = new Childrobot();
        $content->setName($dto['name']['S']);
        $content->setAge($dto['age']['S']);
        $content->setDessinA($dto['dessinA']['S']);
        return $content;
    }
    
    /*public function UpDate($content)
    {
        try {
            $result = $this->client->updateItem([
                'TableName' => ChildrobotDAO::$TABLE_NAME,
                'Key' => array(
                            'name'    => array('S' => $content->getName())
                        ),
                'ExpressionAttributeNames' => [
                    '#NA' => 'url'
                ],
                'ExpressionAttributeValues' =>  [
                    ':val1' => array('S' => $content->getUrl())
                ] ,
                'UpdateExpression' => 'set #NA = :val1 '
            ]);
        }
        catch (Exception $e) {
            print $e->getMessage();
        }
    }*/
}
