<?php

define('FLAG', 'DCTF{HIDDEN}');
define('AES_KEY', 'deadbeef');
define('AES_IV', 'deadbeefdeadbeef');


function compress($arr) {
    return implode('÷', array_map(function ($v, $k) { return $k.'¡'.$v; }, $arr, array_keys($arr) ));
}

function decompress($cookie) {
    if(preg_match('/[^\x00-\x7F]+\ *(?:[^\x00-\x7F]| )*/im',$cookie, $m) == 0) {
        echo('Decryption error (1).');
        return false;
    }

    $t = explode("÷", $cookie);

    $arr = [];
    foreach($t as $el) {
        $el = explode("¡", $el);
        $arr[$el[0]] = $el[1];
    }
    var_dump($arr);

    if(!isset($arr['checksum'])) {
        echo('Decryption error (2).');
        return false;
    }

    $checksum = intval($arr['checksum']);
    unset($arr['checksum']);
    $cookie = compress($arr);
    var_dump($checksum);
    var_dump(crc32($cookie));
    if($checksum != crc32($cookie)) {
        echo('Decryption error (3).');
        return false;
    }

    return $arr;
}

function encryptCookie($arr) {
    $cookie = compress($arr);
    $arr['checksum'] = crc32($cookie);
    return encrypt(compress($arr), AES_KEY, AES_IV);
}

function decryptCookie($cypher) {
    return decompress(decrypt($cypher, AES_KEY, AES_IV));
}

function encrypt($plaintext, $key, $iv) {
    $length     = strlen($plaintext);
    $ciphertext = openssl_encrypt($plaintext, 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);
    return base64_encode($ciphertext) . sprintf('%06d', $length - strlen('.checksum.324115451')-2);
    // return base64_encode($ciphertext) . sprintf('%06d', $length);
}

function decrypt($ciphertext, $key, $iv) {
    $length     = intval(substr($ciphertext, -6, 6));
    $ciphertext = substr($ciphertext, 0,-6);
    $output     = openssl_decrypt(base64_decode($ciphertext), 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $iv);
    if($output == FALSE) {
        echo('Decryption error (0).');
        die();
    }
    return substr($output, 0, $length);
}

$cc = encryptCookie([
    'id' => 11313,
    'username' => 'marcelo',
    // 'email' => 'maka@gmail.com',
    'email' => 'maka@gmail.com÷id¡1÷checksum¡2258609470÷a¡',
]);
var_dump($cc);

$dcc = decryptCookie($cc);
var_dump($dcc);
