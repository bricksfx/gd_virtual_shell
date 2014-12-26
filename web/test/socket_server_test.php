<?php
//TEST

error_reporting(E_ALL);
set_time_limit(0);
ob_implicit_flush();

$address = '127.0.0.1';
$port = 10086;

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
    $connection = 1;
    
    $buf = socket_read($msgsock, 8192);
    echo $buf;
    
    $msg = "hi!";
    socket_write($msgsock, $msg, strlen($msg));
    //welcome发送到客户端
    for ($i = 0; $i < 20; ++$i){
        $msg = "server send: welcome\n";
        if (FALSE === socket_write($msgsock, $msg, strlen($msg))){
            socket_close($msgsock);
            $connection = 0;
            break;
        }
        sleep(1);
    }
    $msg = "#";
    socket_write($msgsock, $msg, strlen($msg));
    if ($connection){
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
    }
    
} while (true);

socket_close($sock);