<?php
//TEST


error_reporting(E_ALL);
echo "tcp/ip connection \n";
$service_port = 10088;
$address = '127.0.0.1';

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === FALSE){
    echo 'socket_create() failed: reason' . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}

echo "Attempting to connect to '$address' on port '$service_port'...\n";
$result = socket_connect($socket, $address, $service_port);
if ($result === FALSE){
    echo "socket_connect() failed. \nReason: ($result)" . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK\n";
}

$in = "hello world";
echo "sending http head request...";
socket_write($socket, $in, strlen($in));
echo "OK\n";

echo "Reading response:\n\n";
while ($out = socket_read($socket, 8192)){
    echo $out;
}

echo "closeing socket...\n";
socket_close($socket);
echo "ok.\n\n";
