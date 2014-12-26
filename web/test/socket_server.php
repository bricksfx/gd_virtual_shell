<?php
error_reporting(E_ALL);
set_time_limit(0);
ob_implicit_flush();

$address = '127.0.0.1';
$port = 10003;

//创建端口
if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === FALSE){
    echo 'socket_create() failed :reason' . socket_strerror(socket_last_error()) . "\n";
}

//绑定
if (socket_bind($sock, $address, $port) === FALSE){
    echo 'socket_bind() failed :reason' . socket_strerror(socket_last_error($sock)) . "\n";
}

//监听
if (socket_listen($sock, 5) === FALSE){
    echo 'socket_listen() failed :reason' . socket_strerror(socket_last_error($sock)) . "\n";
}

do{
    //得到一个链接
    if (($msgsock = socket_accept($sock)) === false){
        echo 'socket_accept() failed :reason' . socket_strerror(socket_last_error($sock)) . "\n";
        break;
    }
    //welcome发送到客户端
    $msg = 'server send: welcome';
    socket_write($msgsock, $msg, strlen($msg));
    echo "read client message \n";
    $buf = socket_read($msgsock, 8192);
    $talkback = "received message: $buf\n";
    echo $talkback;
    if (FALSE === socket_write($msgsock, $talkback, strlen($talkback))){
        echo 'socket_write() failed reason:' . socket_strerror(socket_last_error($sock)) . "\n";
    } else {
        echo 'send success';
    }
    
    socket_close($msgsock);
} while (true);

socket_close($sock);