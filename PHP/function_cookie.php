<?php

/**
 * @description     设置 Cookies 原生设置需要二次访问
 *
 * @param string    $name
 * @param string    $value
 * @param int       $expire
 * @param string    $domain
 * @param bool      $secure
 * @param bool      $httponly
 */
function cookieSet($name = '', $value = '', $expire= 0, $path = '', $domain = '', $secure = false, $httponly = false ) {
    $_COOKIE[$name] = $value;
    return setcookie($name, $value, $expire, $path, $domain, $secure, $httponly);
}

/**
 * @description     清空 cookies
 */
function cookieClear() {
    $_COOKIE = array_filter($_COOKIE);

    if (count( $_COOKIE ) > 0 ) {

        foreach ( $_COOKIE as $k => $v ) {
            unset($_COOKIE[ $k ]);
            setcookie($k, '');
        }
    }
}