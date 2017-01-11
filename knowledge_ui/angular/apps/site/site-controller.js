'use strict';

geditorApp.controller('HomeCtrl', 
  function HomeCtrl($scope, $rootScope, $routeParams, $window, $location) {
  });


//controller for articles

geditorApp.controller('ArticleCtrl', 
  function ArticleCtrl($scope, $rootScope, $routeParams, $window, $location, Article) {
    $scope.articles = {};
    if($routeParams.search){
            var articles = Article.query({search:$routeParams.search},function(data)
            {
               $scope.articles = articles;
             });
    }
    else{
    var articles = Article.query(function(data)
    {
      $scope.articles = articles;
    });
  }

    console.log($scope.articles);
  });

//controller for edit articles

geditorApp.controller('ArticleEditCtrl', 
  function ArticleCtrl($scope, $rootScope, $routeParams, $window, $location, Article) {
    $scope.article= {};
    $scope.comments = {};
    var article = Article.get({id:$routeParams.id},function(data) 
    {
      $scope.article = article;
      $scope.comments = article.comments;
    });

    $scope.save = function(article){
      article.owner = $rootScope.me.id;
      console.log(article.title);
        var fb = new FormData();
        fb.append('title',article.title);
        fb.append('description',article.description);
        fb.append('file',article.file);
        fb.append('tags',article.tags);
        console.log(fb);
        Article.saveEdit({id:article.id},fb).$promise.then(function(data){
          console.log(data);
           $location.path('/');
        }).catch(function(errorResult) {
          $location.path('/');
          $scope.error = errorResult.data;        
        }
        );

    }

    console.log("hello.... " +$scope.comments);
  });

//controller for Article dettail

geditorApp.controller('ArticleDetailCtrl', 
  function ArticleDetailCtrl($scope, $rootScope, $routeParams, $route, $window, $location, Article, Comment) {
    $scope.article= {};
    $scope.comments = {};
    var article = Article.get({id:$routeParams.id},function(data) 
    {
      $scope.article = article;
      $scope.comments = article.comments;
    });

    $scope.like=function(question){
      $scope.article.article_analytic.likes++;
      var article_analytic ={}
      article_analytic = article.article_analytic
      Article.analytics({id:article.id,article_analytic},function(data){

      },function(errorResult){

      });
    }

    $scope.submitComment = function(comment){
      if($rootScope.loggedIn === true){
        comment.id = $scope.article.id;
        console.log(comment);
        Comment.create(comment,function(data){
          $route.reload();
        },function(errorResult){

        });
      }
      else{
       $location.path("/article/"+$scope.article.id);
       $("#login-modal").modal('show');    
     }
   }
 });

//controller for new article

geditorApp.controller('ArticleNew', 
  function ArticleNew($scope, $rootScope, $routeParams, $window, $location, Article) {
    console.log("add new article");
    if($rootScope.loggedIn == true){
      $scope.article={};
      $scope.save = function(article){
        console.log(article.file);
        article.owner = $rootScope.me.id;
        console.log(article.title);
        var fb = new FormData();
        fb.append('title',article.title);
        fb.append('description',article.description);
        fb.append('file',article.file);
        fb.append('tags',article.tags);
        console.log(fb);
        Article.upload({},fb).$promise.then(function(data){
          console.log(data);
          
        }).catch(function(errorResult) {
          $location.path('/');
          $scope.error = errorResult.data;        
        }
        );
      }
    }
    else{
      $location.path("/");
      $("#login-modal").modal('show');
    }
  });
//controller for new questions

geditorApp.controller('QuestionNew', 
  function QuestionNew($scope, $rootScope, $routeParams, $window, $location, Question) {
    console.log("add new question");
    if($rootScope.loggedIn == true){
      $scope.question={};
      $scope.save = function(question){
        question.owner = $rootScope.me.id;
        console.log(question.title);
        Question.create(question,function(data){
          console.log(data);
          $location.path('/questions');
        },function(errorResult) {
          $scope.error = errorResult.data;        
        }
        );
      }
    }
    else{
     $location.path("/questions");
     $("#login-modal").modal('show')   
   }
 });


//controller for question edit

geditorApp.controller('QuestionEditCtrl', 
  function QuestionEditCtrl($scope, $rootScope, $routeParams, $window, $location, Question) {
    $scope.question= {};
    $scope.answers = {};
    var question = Question.get({id:$routeParams.id},function(data) 
    {
      $scope.question = question;
      $scope.answers = question.answers;
    });

    $scope.save = function(question){
      question.owner = $rootScope.me.id;
      console.log(question.title);
      Question.save(question,function(data){
        console.log(data);
        $location.path('/question/'+question.id);
      },function(errorResult) {
        $scope.error = errorResult.data;        
      }
      );
    }

  });

//controller for questions

geditorApp.controller('QuestionCtrl', 
  function QuestionCtrl($scope, $rootScope, $routeParams, $window, $location, Question) {
    $scope.questions = {};
    if($routeParams.search){
            var questions = Question.query({search:$routeParams.search},function(data)
            {
              $scope.questions = questions;
              console.log(data);
          });
    }
    else{
    var questions = Question.query(function(data) 
    {
      $scope.questions = questions;
      console.log(data);
    });
  }
    
    console.log($scope.questions);

  });

//controller for questions dettail

geditorApp.controller('QuestionDetailCtrl', 
  function QuestionCtrl($scope, $rootScope, $routeParams, $route, $window, $location, Question, Answer) {
    $scope.question= {};
    $scope.answers = {};
    var question = Question.get({id:$routeParams.id},function(data) 
    {
      $scope.question = question;
      $scope.answers = question.answers;
    });

    $scope.like=function(question){
      $scope.question.question_analytic.likes++;
      var question_analytic ={}
      question_analytic = question.question_analytic
      Question.analytics({id:question.id,question_analytic},function(data){

      },function(errorResult){

      });
    }

    $scope.submitAnswer = function(answer){
      if($rootScope.loggedIn === true){
        answer.id = $scope.question.id;
        console.log(answer);
        Answer.create(answer,function(data){
          $route.reload();
        },function(errorResult){

        });
      }
      else{
       $location.path("/question/"+$scope.question.id);
       $("#login-modal").modal('show');    
     }
   }
 });

/******
 * Login
 ******/
 geditorApp.controller('UserCtrl', 
  function UserCtrl($scope, $rootScope, $routeParams, $timeout, $window, $location, User) {
    var _me = function() {
      var d = User.me({}, function(data) {
        $scope.$emit('userlogged');
        if(d.first_name || d.last_name) {
          d.name = d.first_name + ' ' + d.last_name;
        }else {
          d.name = d.username;      
        }              
      });
      return d;
    };


    $scope.me = _me();
    $rootScope.me = $scope.me;
    $scope.error_response = "";
   // $scope.profile="bhatia";

    $scope.login = function (user) {
    // fix for autofill
    user = {username: $("#username").val(),
    password: $("#password").val()}
    console.log(user);
    User.login(user, function(successResult) {
        // do something on success
        console.log(successResult);
        $window.sessionStorage.token = successResult.token;
        $scope.me = _me();
        $rootScope.me = $scope.me;
        $scope.me.$promise.then(function(data){
          var d = data;
          if(d.first_name || d.last_name) {
            d.name = d.first_name + ' ' + d.last_name;
          }else {
            d.name = d.username;      
          }
         $rootScope.profile = d;
          //$scope.profile = d;
          console.log(JSON.stringify(data))
        });
        $rootScope.loggedIn = true;
        console.log("loggedin "+JSON.stringify($scope.me));

        $("#login-modal").modal('hide');
      }, function(errorResult) {
        console.log(errorResult.status);
        $rootScope.loggedIn = false;
        // do something on error
        if(errorResult.status === 401) {            
          $scope.error_response = 'You have entered wrong user or password';
        }
        // Erase the token if the user fails to log in
        delete $window.sessionStorage.token;
        // Handle login errors here
        //'Error: Invalid user or password';
      }
      );    
  };

  $scope.logout = function () {
    // Erase the token if the user fails to log in
    delete $window.sessionStorage.token;
    $scope.me = _me();
    $rootScope.me = $scope.me;
    $rootScope.loggedIn = false;
    $location.path("/");
  };

  $scope.signup = function(user, auth) {
    if(auth == 'auth') {
      User.create(user, function(successResult) {
        $("#CreatedModal").modal('show');
      }, function(errorResult) {
        $scope.error = errorResult.data;
        console.log(errorResult);
      }
      );
    }   
  };

  $scope.registerPage = function(){
    console.log("i am here");
    $("#login-modal").modal('hide');
    $timeout(function(){ 
     $location.path('/register');
   },1); 
  }

  $scope.haserror = function(name) {
    //if($scope.error)
  }



  $rootScope.login = $scope.login;
  $rootScope.logout = $scope.logout;  
  $rootScope.signup = $scope.signup;  
});


 geditorApp.controller('MyProfileCtrl', 
  function MyProfileCtrl($scope, $rootScope, $routeParams, $window, $location, Question, Article, User) {
    console.log("hello....saurabh");   
    $scope.me= $rootScope.me;
    $scope.tabShow = false;
    $scope.user = {};
    $scope.user= $rootScope.me;
    $scope.articles = {};
    $scope.questions = {};
    var question = Question.query({owner: $scope.me.username},function(data) 
    {
      $scope.questions = question;;
      console.log("here i am "+data);
    });
    var articles = Article.query({owner: $scope.me.username},function(data) 
    {
      $scope.articles = articles;
    });
    $scope.signup = function(user, auth) {
      if(auth == 'auth') {
        User.save(user, function(successResult) {
          $location.path("/");
        }, function(errorResult) {
          $scope.error = errorResult.data;
          console.log(errorResult);
        }
        );
      }   
    };

    $scope.showTab=function(tab){
      console.log("function "+tab);
      if(tab === 'question'){
        $scope.tabShow = false;
      }
      else if(tab === 'article'){
        $scope.tabShow = true;
      }
    }

  });


  geditorApp.controller('UserProfileCtrl', 
  function UserProfileCtrl($scope, $rootScope, $routeParams, $window, $location, Question, Article, User) {
    console.log("i am here in othersss...");
    $scope.tabShow = false;
    $scope.user= $routeParams.username;
    $scope.articles = {};
    $scope.questions = {};
    var question = Question.query({owner: $routeParams.username},function(data) 
    {
      $scope.questions = question;;
      console.log("here i am "+data);
    });
    var articles = Article.query({owner: $routeParams.username},function(data) 
    {
      $scope.articles = articles;
    });

    $scope.showTab=function(tab){
      console.log("function "+tab);
      if(tab === 'question'){
        $scope.tabShow = false;
      }
      else if(tab === 'article'){
        $scope.tabShow = true;
      }
    }

  });

  geditorApp.controller('SearchCtrl', 
  function SearchCtrl($scope, $rootScope, $routeParams, $window, $location) {
    $scope.category = "questions";
    $scope.search = "";

    $scope.showResult = function(){
      if($scope.category === 'articles'){
           $location.path('/search-article/'+$scope.search);
       }
       else if($scope.category === 'questions'){
        $location.path('/search-question/'+$scope.search);
       }

    };


  });