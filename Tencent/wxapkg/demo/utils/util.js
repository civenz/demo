const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('-') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

const clearAll = all => {
  //清理文件
  wx.getSavedFileList({
    success: function (res) {
      if (res.fileList.length > 0) {
        wx.removeSavedFile({
          filePath: res.fileList[0].filePath,
          complete: function (res) {
            console.log(res);
          }
        });
      }
    }
  });

  //清理数据缓存
  try {
    wx.clearStorage();
  } catch (e) {
    console.log(e);
  }

  try {
    wx.clearStorageSync();
  } catch (e) {
    console.log(e);
  }
}

const isGetUser = user => {
  wx.getSetting({
    success: function (res) {
      if (res.authSetting['scope.userInfo'] && res.authSetting['scope.userInfo'] == true) return true;
      return false;
    }
  });
}

// const isGetGps = gps => {
//   wx.getSetting({
//     success: function (res) {
//       if (res.authSetting['scope.userLocation'] && res.authSetting['scope.userLocation'] == true) return true;
//       return false;
//     }
//   });
// }


module.exports = {
  formatTime: formatTime,
  clearAll: clearAll,
  isGetUser: isGetUser,
  // isGetGps: isGetGps,
}
