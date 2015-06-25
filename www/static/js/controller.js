var app = angular.module('LearningAnaliticsControllers', []);

app.controller('Dashboard', ['$scope', '$sce',
 function($scope, $sce){

 	// this to trust source
 	$scope.trustAsResourceUrl = $sce.trustAsResourceUrl;

 	// this is for init
	$scope.currentProfile = {
		"role": "étudiant",
		"id": 1
	};
	$scope.iframeUrl = "http://localhost:5601/#/dashboard/%C3%89tudiant?embed&_g=()&_a=(filters:!(),panels:!((col:6,id:'Nombre-d!'inscriptions-%C3%A0-un-cours-par-jour',row:3,size_x:3,size_y:2,type:visualization),(col:6,id:Nombre-de-cours-suivi-par-les-%C3%A9l%C3%A8ves,row:1,size_x:3,size_y:2,type:visualization),(col:9,id:Nombre-de-connexions-par-jour,row:1,size_x:4,size_y:4,type:visualization),(col:1,id:'Mode-d!'emploi-:-%C3%A9tudiant',row:1,size_x:3,size_y:4,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'actor.name:1')),title:%C3%89tudiant)";
	$scope.tab = {"n":true};

 	$scope.refreshIframe = function(){
	    $scope.tab.refresh = true;
	};


	$scope.changeIframeUrl = function(){
		if ($scope.currentProfile.role == "admin") {
			$scope.iframeUrl="http://localhost:5601/#/dashboard/Dashboard-1?embed&_g=()&_a=(filters:!(),panels:!((col:1,id:Nombre-de-cours-suivi-par-les-%C3%A9l%C3%A8ves,row:1,size_x:5,size_y:3,type:visualization),(col:7,id:'Nombre-d!'utilisateurs-inscrit-sur-la-plateforme',row:4,size_x:2,size_y:3,type:visualization),(col:1,id:Les-5-%C3%A9tudiants-ayant-suivis-le-plus-de-cours,row:4,size_x:3,size_y:3,type:visualization),(col:9,id:'Nombre-d!'inscriptions-%C3%A0-un-cours-par-jour',row:4,size_x:4,size_y:3,type:visualization),(col:4,id:Nombre-de-donn%C3%A9es,row:4,size_x:3,size_y:3,type:visualization),(col:6,id:Nombre-de-connexions-par-jour,row:1,size_x:7,size_y:3,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:'Dashboard%201')";

		} else if ($scope.currentProfile.role == "étudiant") {
			$scope.iframeUrl = "http://localhost:5601/#/dashboard/%C3%89tudiant?embed&_g=()&_a=(filters:!(),panels:!((col:6,id:'Nombre-d!'inscriptions-%C3%A0-un-cours-par-jour',row:3,size_x:3,size_y:2,type:visualization),(col:6,id:Nombre-de-cours-suivi-par-les-%C3%A9l%C3%A8ves,row:1,size_x:3,size_y:2,type:visualization),(col:9,id:Nombre-de-connexions-par-jour,row:1,size_x:4,size_y:4,type:visualization),(col:1,id:'Mode-d!'emploi-:-%C3%A9tudiant',row:1,size_x:3,size_y:4,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'actor.name:"+ $scope.currentProfile.id +"')),title:%C3%89tudiant)";

		} else if ($scope.currentProfile.role == "professeur") {
			$scope.iframeUrl = "";
		};

		$scope.refreshIframe();


	};

	$scope.changeProfile = function(role) {
		$scope.currentProfile.role = role;
		$scope.changeIframeUrl();
	};
 
}]);
