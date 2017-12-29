<?php

class ChildRobot {
    private $name;
    private $age;
    private $dessinA;
    
    public function __construct() {}

    public function getName() {
        return $this->name;
    }
    
    public function getAge() {
        return $this->age;
    }

    public function getDessinA() {
        return $this->dessinA;
    }

    function setName($name) {
        $this->name = $name;
    }

    function setAge($age) {
        $this->age = $age;
    }

    function setDessinA($dessinA) {
        $this->dessinA = $dessinA;
    }
}
