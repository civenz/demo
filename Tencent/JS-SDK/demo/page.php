<?php if( isset($_SERVER['HTTP_USER_AGENT'])  && preg_match('/MicroMessenger/i', $_SERVER['HTTP_USER_AGENT']) ): ?>
<script type="text/javascript">
var jssdkUrl        = "<?= $pageUrl ?>";
var jssdkTitle      = "<?= $pageTile ?>";
var jssdkImage      = "<?= $pageImg ?>";
var jssdkDesc       = "<?= $pageDesc ?>";
var jssdkType       = "link";
var jssdkDataUrl    = "";
</script>
<script src="http://res.wx.qq.com/open/js/jweixin-1.5.0.js"></script>
<script type="text/javascript" src="./wconfig.js"></script>
<?php endif; ?>