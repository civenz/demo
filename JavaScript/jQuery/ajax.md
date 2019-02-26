```
<!-- 引入 3.3.1 版的 jQuery -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/core.js"></script>
<script>var jq3_3 = jQuery.noConflict(true);</script>

<script>
(function($){    
    $.ajax({
        url: 'https://civenz.github.io/',
        type: 'get',
        async: true,
        timeout: 1 * 10 * 1000,
        
        success: function(data) {
            console.log($(data).find('#civen').html());
        },
        error: function(XHR, textStatus, errorThrow) {
            //console.log(XHR);
        },
        complete: function(XHR, textStatus) {
            //console.log(XHR);
        },
    });
})(jq3_3);
</script>
```
