<?php
/**
 * @description     随机生成字符串
 * @since           2019-02-15 15:35:21
 * @version         1.0.0
 * @author          civen
 * @date            2019-02-15 15:35:21
 */

//echo RandomString::get(8);

class RandomString {

    /**
     * @author civen
     * @date 2019-02-15 15:35:21
     * 
     * @param len
     * 随机字符串长度
     * @param type
     * 生成字符串类型 [a] 代表小写; [A] 代表大写; [0] 代表数字; [-] 代表符号;
     * @param custom
     * 自定义随机字符串的字符;
     * @return string
     * 
     * 生成随机字符串
     * 例子:
     * RandomString::get();             // 默认: 8位 小写字母 & 数字
     * RandomString::get(8, 'aA');      // 8位大小写随机字符串
     * RandomString::get(8, '', 'abc'); // 从abc中随机出8位字符串 
     */
    public static function get($len = 8, $type = 'a0', $custom = false) {

        switch($type) {
            case 'a':
                $factor = 'abcdefghijklmnopqrstuvwxyz';
                break;
            case 'A':
                $factor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
                break;
            case '0':
                $factor = '0123456789';
                break;
            case 'aA':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
                break;
            case 'Aa':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
                break;
            case 'a0':
                $factor = 'abcdefghijklmnopqrstuvwxyz0123456789';
                break;
            case '0a':
                $factor = 'abcdefghijklmnopqrstuvwxyz0123456789';
                break;
            case 'A0':
                $factor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case '0A':
                $factor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case 'aA0':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case 'a0A':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case 'Aa0':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case 'A0a':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case '0aA':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case '0Aa':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                break;
            case 'aA0-':
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=`~!@#$%^&*_+';
                break;
            default:
                $factor = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=`~!@#$%^&*_+';
        }

        if($custom) $factor = $custom;

        $str        = null;
        $max        = strlen($factor) - 1;

        for($i = 0; $i < $len; $i++) {
            $str .= $factor[rand(0, $max)];
        }

        return $str;
    }
}