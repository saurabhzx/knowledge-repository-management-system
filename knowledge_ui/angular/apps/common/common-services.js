'use strict';

geditorApp.factory('Question', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'questions/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{}, isArray:false},
    create: {method:'POST', params:{}},
    assets: {method: 'GET', params:{entity: 'assets'}},
    analytics: {method: 'POST', params:{entity:'analytics'}},
    upload: {
          method: 'POST',
          headers: {enctype:'multipart/form-data'}
        },
  });
});

geditorApp.factory('Answer', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'answers/question/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{}, isArray:false},
    create: {method:'POST', params:{}},
  });
});

//articles service 
geditorApp.factory('Article', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'articles/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{}, isArray:false},
    create: {method:'POST', params:{}},
    assets: {method: 'GET', params:{entity: 'assets'}},
    analytics: {method: 'POST', params:{entity:'analytics'}},
    saveTags: {method: 'POST', params:{entity:'tags'}},
    upload: {
          method: 'POST',
            transformRequest: angular.identity,
          headers: { 'Content-Type': undefined },
          params:{}
          //headers: {enctype:'multipart/form-data'}
        },
    saveEdit: {
          method: 'POST',
            transformRequest: angular.identity,
          headers: { 'Content-Type': undefined },
          params:{}
          //headers: {enctype:'multipart/form-data'}
        },
  });
});

//services for comments articles

geditorApp.factory('Comment', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'comments/article/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{}, isArray:false},
    create: {method:'POST', params:{}},
  });
});

//services for user

geditorApp.factory('User', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'users/:id/:entity', {id: '@id', entity: '@entity'}, {
    create: {method:'POST', params:{}},
    login: {method:'POST',params:{id: 'authenticate', entity: 'auth'}},
    activate: {method:'GET',params:{id: 'activate'}},
    me: {method:'GET', params:{id: 'me'}}, 
  });
});

























//service for men items

//service for compare men shirt
geditorApp.factory('CompareMenShirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'userpik/user-clothing/user-men/compare-men-shirt-feature/user-men-shirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{id:'my'}, isArray:false},
  });
});


//service for compare men tshirt
geditorApp.factory('CompareMenTshirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'userpik/user-clothing/user-men/compare-men-tshirt-feature/user-men-tshirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{id:'my'}, isArray:false},
  });
});


//service for getting men-tshirts
geditorApp.factory('MenTshirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'product/clothing/men/men-tshirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
  });
});


//service for getting men-shirts
geditorApp.factory('MenShirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'product/clothing/men/men-shirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
  });
});


//Service for women items


//service for compare women dress
geditorApp.factory('CompareWomenDress', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'userpik/user-clothing/user-women/compare-women-dress-feature/user-women-dress/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{id:'my'}, isArray:false},
  });
});


//service for compare women tshirt
geditorApp.factory('CompareWomenTshirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'userpik/user-clothing/user-women/compare-women-tshirt-feature/user-women-tshirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
    my: {method:'GET', params:{id:'my'}, isArray:false},
  });
});


//service for getting women-dress
geditorApp.factory('WomenDress', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'product/clothing/women/women-dress/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
  });
});


//service for getting women-jumpSuits
geditorApp.factory('WomenJumpSuit', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'product/clothing/women/women-jump-skirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
  });
});


//service for getting women-tees
geditorApp.factory('WomenTshirt', function($resource, apiPrefix) {
  return $resource(apiPrefix + 'product/clothing/women/women-tshirt/:id/:entity', {id: '@id', entity: '@entity'}, {
    query: {method:'GET', params:{}, isArray:false},
  });
});