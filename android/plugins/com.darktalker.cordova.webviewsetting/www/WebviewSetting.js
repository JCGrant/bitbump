
var exec = require('cordova/exec'),isAndroid44;
var m = window.navigator.appVersion.match(/Android\s(.*?);/);
if(m){
	isAndroid44 = parseFloat(m[1]) === 4.4;
}
module.exports = {
	set:function(callback) {
		/* if(!isAndroid44){
			return callback && callback(null,'ok');
		} */
		exec(function(res){
			callback && callback(null,res);
		}, function(error){
			callback && callback(error);
		}, "WebviewSetting", "set", []);
	}
};
