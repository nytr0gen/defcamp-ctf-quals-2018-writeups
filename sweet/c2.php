<?php
ini_set('xdebug.collect_params', '1');

var_dump(dl('sweet.so'));
use Sweet\Crypto;

$c = new Sweet\Crypto;

xdebug_start_function_monitor([
    'Sweet\Crypto::encrypt',
    'Sweet\Crypto::sendtoNSA',
    'Sweet\Crypto::decrypt',
]);

var_dump($c->sendtoNSA('/home/robert/Pictures/sharky_the_shark_dog_by_zrcalo.jpg'));

xdebug_break();
$coded = $c->encrypt('sample.data','deadbeefdeadbeef','deadbeefdeadbeef');
var_dump(bin2hex($coded));
file_put_contents('sample.data.crypted', $coded);

$decoded = $c->decrypt('sample.data.crypted', 'deadbeefdeadbeef', 'deadbeefdeadbeef');
var_dump($decoded);


var_dump(xdebug_get_monitored_functions());
xdebug_stop_function_monitor();
