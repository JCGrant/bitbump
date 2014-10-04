cordova-webview-setting
====================
a plugin for general webview setting:

* to fix viewport issue: Viewport meta tag ignored in Android 4.4 WebView
* enable autoplay for video/audio tag, for ios, juste add this line to the config.xml: ``<preference name="MediaPlaybackRequiresUserAction" value="false"/>``


How to use
==============
```js
window.plugin.webviewSetting.set(function(err,status){
   if(err){
     console.error('failed');
   }else{
     console.log('fixed')
   }
});
```
