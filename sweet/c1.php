<?php
var_dump(dl('sweet.so'));

// use Sweet\Crypto;
$funcs = get_defined_functions();
// var_dump($funcs);

$classes = get_declared_classes();
// var_dump($classes);


$c = new Sweet\Crypto;
var_dump(get_class_methods($c));
var_dump(get_object_vars($c));

var_dump($c->sendtoNSA('/home/robert/Pictures/sharky_the_shark_dog_by_zrcalo.jpg'));

$coded = $c->encrypt('sample.data','deadbeefdeadbeef','deadbeefdeadbeef');
var_dump(bin2hex($coded));
file_put_contents('sample.data.crypted', $coded);

$decoded = $c->decrypt('sample.data.crypted', 'deadbeefdeadbeef', 'deadbeefdeadbeef');
var_dump($decoded);


class Crypto2 extends Sweet\Crypto {
    public function __construct() {
        // parent::__construct();
        var_dump(get_class_methods($this));
        var_dump(get_object_vars($this));
    }
};

$c2 = new Crypto2();
