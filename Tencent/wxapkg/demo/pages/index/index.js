//index.js
//获取应用实例
const util = require('../../utils/util.js');

const app = getApp();

Page({
  data: {
    date: util.formatTime(new Date()),
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),

    iconSize: [20, 30, 40, 50, 60, 70],
    iconColor: ['red', 'orange', 'yellow', 'green', 'rgb(0,255,255)', 'blue', 'purple'],
    iconType: ['success', 'success_no_circle', 'info', 'warn', 'waiting', 'cancel', 'download', 'search', 'clear'],
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
        // console.info(res.userInfo);
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  // getUserInfo: function(e) {
  //   //console.log(e)
  //   if (e.detail.errMsg == 'getUserInfo:ok') {
  //     app.globalData.userInfo = e.detail.userInfo
  //     this.setData({
  //       userInfo: e.detail.userInfo,
  //       hasUserInfo: true
  //     });
  //   }
  // },
  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  getUserDetail: function () {
    wx.getUserInfo({
      success: res => {
        console.log(res)
      },
      fail: err => {
        wx.openSetting({
          success: (res) => {
            if (res.authSetting['scope.userInfo'] == true) {
              wx.reLaunch({url: 'index'})
            }
          }
        })
      },
      // complete: done => {
      //   console.log('ok')
      // },
    })
  },

  getGps: function () {
    wx.getLocation({
      type: 'wgs84',
      success: function (res) {
        var latitude = res.latitude
        var longitude = res.longitude
        var speed = res.speed
        var accuracy = res.accuracy
      },
      fail: err => {
        wx.openSetting({
          success: (res) => {
            if (res.authSetting['scope.userLocation'] == true) {
              wx.reLaunch({ url: 'index' })
            }
          }
        })
      },
      // complete: done => {
      //   console.log('ok')
      // },
    });
  },

  getDeviceInfo: function () {
    /**
     * wx.canIUse('getSystemInfoSync')
     * wx.canIUse('getNetworkType')
     * wx.canIUse('getLocation')
     */
    console.log(wx.canIUse('getNetworkType'));
    console.log(wx.getSystemInfoSync());
    console.log(wx.getNetworkType());
    
    /**
     * SDKVersion
     * brand
     * fontSizeSetting
     * language
     * model
     * pixelRatio
     * platform
     * screenHeight
     * screenWidth
     * system
     * version
     */
  },

  getNetworkStatus: function () {
    wx.getNetworkType({
      fail: function () {
        console.log('Error')
      },
      success: function (res) {
        console.log(res.networkType)
      },
    })
  },

  scanQrCode: function () {
    wx.scanCode({
      // onlyFromCamera: true,
      success: (res) => {
        console.log(res)
      }
    })
  },

  clearCahce: function() {
    util.clearAll();
  },

  isGetUser: function() {
    wx.getSetting({
      success: function (res) {
        if (res.authSetting['scope.userInfo'] && res.authSetting['scope.userInfo'] == true) return true;
        return false;
      }
    });
  },

  isGetGps: function() {
    wx.getSetting({
      success: function (res) {
        if (res.authSetting['scope.userLocation'] && res.authSetting['scope.userLocation'] == true) return true;
        return false;
      }
    });
  }

})