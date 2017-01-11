'use strict';

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

angular.module('SharedServices', ['ngResource','chieffancypants.loadingBar'])
  .config(function ($httpProvider, cfpLoadingBarProvider) {
    cfpLoadingBarProvider.includeSpinner = true;
    $httpProvider.responseInterceptors.push('myHttpInterceptor');
    var spinnerFunction = function (data, headersGetter) {
        // todo start the spinner here
        //alert('start spinner');
        $("#loading").show();
        return data;
    };
    $httpProvider.defaults.transformRequest.push(spinnerFunction);
  })
  // register the interceptor as a service, intercepts ALL angular ajax http calls
  .factory('myHttpInterceptor', function ($q, $window) {
    return function (promise) {
      return promise.then(function (response) {
        // do something on success
        // todo hide the spinner
        //alert('stop spinner');
        $("#loading").hide();
        $('#status').hide();
        return response;

      }, function (response) {
        // do something on error
        // todo hide the spinner
        //alert('stop spinner');
        $("#loading").hide();
        $('#spinner').hide();
        $('#status').show();
        if(response.status >= 500){
          $('#status').show();
          response.data.error = true;
          return response;
        }
        return $q.reject(response);
      });
    };
  });


  angular.module('ng').filter('roundup', function () {
    return function (value, decimalplace) {
      if (!value) return '';
      decimalplace = Math.pow(10, decimalplace);
      value = Math.round(value*decimalplace, 10)/decimalplace;
      return value;
    };
  });

  angular.module('ng').filter('cut', function () {
    return function (value, wordwise, max, tail) {
      if (!value) return '';

      max = parseInt(max, 10);
      if (!max) return value;
      if (value.length <= max) return value;

      value = value.substr(0, max);
      if (wordwise) {
        var lastspace = value.lastIndexOf(' ');
        if (lastspace != -1) {
            value = value.substr(0, lastspace);
        }
      }
      return value + (tail || '...');
    };
  });

  