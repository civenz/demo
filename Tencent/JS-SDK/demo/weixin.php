<?php
require_once "./weixin_jssdk/jssdk.php";

$appId      = 'Your_AppID';
$appSecret  = 'Your_AppSecret';

$url = isset($_GET['url']) ? $_GET['url'] : 'http://127.0.0.1';

$jssdk = new JSSDK($appId, $appSecret, $url);
$signPackage = $jssdk->GetSignPackage();

$signPackage['jsApiList'] = [
    'onMenuShareTimeline',
    'onMenuShareAppMessage',
    'onMenuShareQQ',
    'onMenuShareWeibo',
    'onMenuShareQZone',
    'startRecord',
    'stopRecord',
    'onVoiceRecordEnd',
    'playVoice',
    'pauseVoice',
    'stopVoice',
    'onVoicePlayEnd',
    'uploadVoice',
    'downloadVoice',
    'chooseImage',
    'previewImage',
    'uploadImage',
    'downloadImage',
    'translateVoice',
    'getNetworkType',
    'openLocation',
    'getLocation',
    'hideOptionMenu',
    'showOptionMenu',
    'hideMenuItems',
    'showMenuItems',
    'hideAllNonBaseMenuItem',
    'showAllNonBaseMenuItem',
    'closeWindow',
    'scanQRCode',
    'chooseWXPay',
    'openProductSpecificView',
    'addCard',
    'chooseCard',
    'openCard',
];

echo json_encode($signPackage);
?>