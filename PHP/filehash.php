<?php
// 查看文件 [ md5 sha1 sha256 ]
// CMD> php filehash.php "C:\Downloads\CentOS-7-x86_64-Minimal-1810.iso" sha256

if(!isset($argv)) {
    header('Cache-Control: no-store, no-cache, must-revalidate');
    header('Pragma: no-cache');
    header("Expires: 0");
    header("Content-Type: text/html; charset=utf-8");
    echo '不支持浏览器访问! 请使用命令执行!';
    exit();
}

$tips = 'For Example: [php filehash.php "C:\Downloads\CentOS-7-x86_64-Minimal-1810.iso" sha256]' . PHP_EOL;

if(count($argv) != 3) {
    echo  PHP_EOL . 'Error command.' . PHP_EOL;
    echo $tips;
    exit();
}

try {
    $result = @hash_file($argv[2], $argv[1]);

    if($result)
        echo PHP_EOL . $argv[2] . ' - [' . $result . ']' . PHP_EOL;
    else
        throw new Exception('Invalid path or hash type!' . PHP_EOL);

} catch (Exception $e) {
    echo  PHP_EOL . $e->getMessage();
    echo $tips;
}