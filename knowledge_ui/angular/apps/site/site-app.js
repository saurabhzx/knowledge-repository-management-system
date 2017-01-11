'use strict';

  var geditorApp = angular
                    .module('geditorApp', ['SharedServices',,'ngResource', 'ngRoute','angularFileUpload', 'ngCookies'])
                    .constant('apiPrefix', '//127.0.0.1:9000/');

  geditorApp.config(function ($routeProvider, $locationProvider, $interpolateProvider) {
    $routeProvider
      .when('/', {
          templateUrl: 'angular/partials/blog-home.html', 
          controller: 'ArticleCtrl'})

      .when('/questions', {
          templateUrl: 'angular/partials/questions.html', 
          controller: 'QuestionCtrl'})

      .when('/question/new', {
          templateUrl: 'angular/partials/question-post.html', 
          controller: 'QuestionNew'})

      .when('/question/:id', {
          templateUrl: 'angular/partials/question-detail.html', 
          controller: 'QuestionDetailCtrl'})

      .when('/question/:id/edit', {
          templateUrl: 'angular/partials/question-post.html', 
          controller: 'QuestionEditCtrl'})

      .when('/articles', {
          templateUrl: 'angular/partials/blog-home.html', 
          controller: 'ArticleCtrl'})

      .when('/article/new', {
          templateUrl: 'angular/partials/article-post.html',
          controller: 'ArticleNew'})

      .when('/article/:id', {
          templateUrl: 'angular/partials/article-detail.html', 
          controller: 'ArticleDetailCtrl'})

      .when('/article/:id/edit', {
          templateUrl: 'angular/partials/article-post.html', 
          controller: 'ArticleEditCtrl'})

      .when('/register', {
          templateUrl: 'angular/partials/register.html', 
          controller: 'UserCtrl'})

      .when('/user/edit-profile', {
          templateUrl: 'angular/partials/register.html', 
          controller: 'MyProfileCtrl'})

      .when('/user/my-profile', {
          templateUrl: 'angular/partials/my-profile.html', 
          controller: 'MyProfileCtrl'})

      .when('/user/profile/:username', {
          templateUrl: 'angular/partials/user-profile.html', 
          controller: 'UserProfileCtrl'})

      .when('/search-article/:search', {
          templateUrl: 'angular/partials/blog-home.html', 
          controller: 'ArticleCtrl'})

      .when('/search-question/:search', {
          templateUrl: 'angular/partials/questions.html', 
          controller: 'QuestionCtrl'})

      .otherwise({redirectTo: '/'});
      $locationProvider.html5Mode(true);
      //$locationProvider.hashPrefix('!');

      $interpolateProvider
        .startSymbol('[[')
        .endSymbol(']]');
  });

  geditorApp.run(function($rootScope, $templateCache) {
   $rootScope.$on('$viewContentLoaded', function() {
      $templateCache.removeAll();
      console.log("history");
   });
  });

  geditorApp.factory('authInterceptor', function ($rootScope, $q, $window) {
    return {
      request: function (config) {
        config.headers = config.headers || {};
        if ($window.sessionStorage.token) {
          config.headers.Authorization = 'Token ' + $window.sessionStorage.token;
        }
        return config;
      },
      response: function (response) {
        if (response.status === 401) {
          // handle the case where the user is not authenticated
        }
        return response || $q.when(response);
      }
    };
  });

  geditorApp.config(["$httpProvider", function(provider) {
    //provider.defaults.headers.common["X-CSRFToken"] = getCookie('csrftoken');
    //provider.defaults.headers.post["Content-Type"] = "application/json";
    provider.interceptors.push('authInterceptor');
  }]);


  