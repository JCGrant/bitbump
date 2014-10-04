package com.darktalker.cordova.webviewsetting;

import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CordovaWebView;
import org.apache.cordova.CordovaInterface;
import org.apache.cordova.CallbackContext;
import org.json.JSONArray;
import org.json.JSONException;

import android.os.Build;

import android.util.Log;



public class WebviewSetting extends CordovaPlugin {
    private CordovaWebView webView;
    private static final String LOG_TAG = "WebviewSetting";
    @Override
    public void initialize(final CordovaInterface cordova, CordovaWebView webView) {
        Log.d(LOG_TAG, "set viewport");
        this.webView = webView;
        super.initialize(cordova, webView); 
        
    }
    @Override
    public boolean execute(String action, JSONArray args, final CallbackContext callbackContext) throws JSONException {
        if ("set".equals(action)) {
            cordova.getActivity().runOnUiThread(new Runnable() {
                public void run() {
                    webView.getSettings().setLoadWithOverviewMode(true);
                    webView.getSettings().setUseWideViewPort(true);
                    
                    if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN_MR1) {
            	        webView.getSettings().setMediaPlaybackRequiresUserGesture(false);
            	
            	        Log.d(LOG_TAG, "setMediaPlaybackRequiresUserGesture: FALSE");
                    }
                    
                    callbackContext.success();
                }
            });
            return true;
        }
        return false;  // Returning false results in a "MethodNotFound" error.
    }
}
