/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {

    // Fields
    amount = 0,

    // Application Constructor
    initialize: function() {
        this.bindEvents();
        this.firstRun();
    },

    getPhoneId: function() {
        return window.localStorage('phone_id');
    },

    recordTransaction: function (sender_id) {
        var amt = this.amount;
        var receiver_id = this.getPhoneId();
        cordovaHTTP.post('http://bit-bump.me/transaction', 
            {
                'sender'  : sender_id,
                'receiver': receiver_id,
                'amount'  : amt
            },
            function HTTPSuccess (response) {
                this.showSuccess(response);
            },

            function HTTPFailure (response) {
                this.showFailure(response);
            }
    }

    },


    firstRun: function() {
        if (window.localStorage('phone_id') == '') {
            //do some stuff if has not loaded before
            window.localStorage('phone_id', this.generateId());
        }
    },

    generateId: function() {
        var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
        var id = '';
        for (var i=0; i < 32; i++) {
            id += alphabet[Math.floor(Math.random() * alphabet.length)];
        }
        return id;
    },

    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');

        // Read NDEF formatted NFC Tags
        nfc.addNdefListener (
            function nfcListener (nfcEvent) {
                var tag = nfcEvent.tag,
                    ndefMessage = tag.ndefMessage,
                    sender_id;

                // dump the raw json of the message
                // note: real code will need to decode
                // the payload from each record
                alert(JSON.stringify(ndefMessage));

                // assuming the first record in the message has 
                // a payload that can be converted to a string.
                alert(nfc.bytesToString(ndefMessage[0].payload).substring(3));
                sender_id = nfc.bytesToString(ndefMessage[0].payload).substring(3);
                recordTransaction(sender_id);
            }, 
            function nfcSuccess() { // success callback
                alert("Waiting for NDEF tag");
            },
            function nfcError (error) { // error callback
                alert("Error adding NDEF listener " + JSON.stringify(error));
            }
        );
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

app.initialize();
