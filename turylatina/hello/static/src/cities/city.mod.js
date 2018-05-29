(function (ng) {

    var mod = ng.module("cityModule", ['ui.router']);

    mod.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/cities");

        $stateProvider
            .state('cities', {
                url: "/cities",
                views: {
                    'cities': {
                        templateUrl: 'src/cities/cities.html',
                        controller: 'cityController'
                    }
                }
            })

        ;
        }]);

})(window.angular);


(function (ng) {

    var mod = ng.module("cityModule");
    mod.constant("cityContext", "api/cities");

    mod.controller('cityController', ['$scope', '$http', 'cityContext', '$state',

        function ($scope, $http, cityContext, $state) {

            $http({
                method: 'GET',
                url: 'src/cities/cities.json'
            }).then(function successCallback(response) {
                
                $scope.cities = response.data;
                
            }, function errorCallback(response) {
                
                console.log('ERROR ' + response.status );
                
            });


        } /*END FUNCTION CONTROLLER*/
    ]); /*END CONTROLLER*/
})(window.angular);
