var url = encodeURIComponent(location.href.split('#')[0]);
setTimeout(function(){
    $.get('./weixin.php?url='+url,function(data){
        callback(data);
    },'json');
},400);

function callback(config,fn){
    wx.config(config);
    wx.ready(function() {

        /* 分享到朋友圈 */
        wx.onMenuShareTimeline({
            link:   jssdkUrl,
            title:  jssdkTitle,
            imgUrl: jssdkImage,
            success: function () {
            },
            cancel: function () {
            },
            fail: function () {
            },
            complete: function () {
            },
        });


        /* 分享给朋友 */
        wx.onMenuShareAppMessage({
            link:   jssdkUrl,
            title:  jssdkTitle,
            imgUrl: jssdkImage,
            desc:   jssdkDesc,
            type:   jssdkType,
            dataUrl: jssdkDataUrl,
        });

        /* 分享到QQ */
        wx.onMenuShareQQ({
            link:   jssdkUrl,
            title:  jssdkTitle,
            imgUrl: jssdkImage,
            desc:   jssdkDesc,

        });

        /* 分享到QQ空间 */
        wx.onMenuShareQZone({
            link:   jssdkUrl,
            title:  jssdkTitle,
            imgUrl: jssdkImage,
            desc:   jssdkDesc,
        });

    });
}