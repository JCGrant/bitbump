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

window.app = {

    // Fields
    mode: 'receive',
    state: 'idle',

    // Application Constructor
    initialize: function() {
        this.bindEvents();
        var btc = window.localStorage.getItem('btc');
        if (btc != null) {
          $('#btc').text(btc);
        }
        var gbp = window.localStorage.getItem('gbp');
        if (gbp != null) {
          $('#value').text(gbp);
        }
    },

    send: function(ring_id) {
      var sender_id, receiver_id;
      var phone_id = 1;
      var amount = $('#amount').val();
      amount = app.gbpToSatoshi(amount);
      if (app.mode === 'send') {
        sender_id = phone_id;
        receiver_id = ring_id;
      } else {
        sender_id = ring_id;
        receiver_id = phone_id;
      }
      $('#wait-for-ring').addClass('hidden');
      console.log($('#wait-for-ring').attr('class'));
      cordovaHTTP.post('http://188.226.239.28:5000/transaction',
          {
            'sender': sender_id,
            'receiver': receiver_id,
            'amount': amount
          }, {},
          function (data) {
            app.state = 'finished';
            console.log('>>>>>>>>>>>>>>>>>>>>finished');
            $('#payment-success').removeClass('hidden');
            setTimeout(function () {
              app.state = 'idle';
              $('#payment-success').addClass('hidden');
              $('#amount-box-layer').addClass('hidden')
              window.requestAnimationFramme(function () {
                $('#amount-box-layer').addClass('opacity');
              });
              $('#confirm-amount').removeClass('hidden');
              app.updateBalance();
            }, 2000);
            $('#wait-for-ring').addClass('hidden');
          },
          function (data) {
            app.state = 'error';
            alert(JSON.stringify(data));
            $('#wait-for-ring').addClass('hidden');
            $('#payment-failure').removeClass('hidden');
            setTimeout(function () {
              app.state = 'idle';
              $('#payment-failure').addClass('hidden');
              $('#amount-box-layer').addClass('hidden').addClass('opacity');
              $('#confirm-amount').removeClass('hidden');
            }, 2000);

          }
      );
      
      app.updateBalance();
      app.state = 'waiting-confirm';
    },


    updateBalance: function() {
      var roundBTC = function (btc) {
        return Math.round(btc * 100 * 1000000) / (100 * 1000000);
      };
      var roundGBP = function (gbp) {
        return Math.round(gbp * 100) / 100;
      }
      cordovaHTTP.get('http://188.226.239.28:5000/balance',
        {
          'user_id': 1,
        }, {},
        function balanceSuccess(response) {
          var gbp = '£' + roundGBP(parseInt(response.data) * 209.05 / 100000000);
          var btc = '(' + roundBTC(parseInt(response.data) / 100000000) + ' BTC)';
          $('#value').text(gbp);
          $('#btc').text(btc);
          window.localStorage.setItem('btc', btc);
          window.localStorage.setItem('gbp', gbp);
        },
        function balanceFailure(response) {
          alert(JSON.stringify(response));
      });
    },

    gbpToSatoshi: function (gbp) {
      return Math.floor(gbp * 100000000 / 209.05);
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
              if (app.state != 'waiting-ring') {
                 console.log("NOT READY");
                 return;
               }
               navigator.vibrate(0.2);
                var tag = nfcEvent.tag,
                    ndefMessage = tag.ndefMessage,
                    sender_id;

                var id = nfc.bytesToString(ndefMessage[0].payload).substring(3);
                app.send(id);
            }, 
            function nfcSuccess() { // success callback
                //alert("Waiting for NDEF tag");
            },
            function nfcError (error) { // error callback
                alert("Error adding NDEF listener " + JSON.stringify(error));
            }
        );

        setInterval(function () {
          app.updateBalance();
        }, 5000);
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        //var parentElement = document.getElementById(id);
        //var listeningElement = parentElement.querySelector('.listening');
        //var receivedElement = parentElement.querySelector('.received');

        //listeningElement.setAttribute('style', 'display:none;');
        //receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

app.initialize();
