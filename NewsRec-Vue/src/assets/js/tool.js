exports.install = function (Vue, options) {
  Vue.prototype.timeFormat = function (time) {
    if (!time) return false
    var datetime = new Date(time)
    var y = datetime.getFullYear()
    var m = datetime.getMonth() + 1 < 10 ? '0' + parseInt(datetime.getMonth() + 1) : parseInt(datetime.getMonth() + 1)
    var d = datetime.getDate() < 10 ? '0' + datetime.getDate() : datetime.getDate()
    var h = datetime.getHours() < 10 ? '0' + datetime.getHours() : datetime.getHours()
    var mm = datetime.getMinutes() < 10 ? '0' + datetime.getMinutes() : datetime.getMinutes()
    var s = datetime.getSeconds() < 10 ? '0' + datetime.getSeconds() : datetime.getSeconds()
    return y + '/' + m + '/' + d + '  ' + h + ':' + mm + ':' + s
  }
  Vue.prototype.getUrlparams = function(url){
    console.log(url)
  }
}
