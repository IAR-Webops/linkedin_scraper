<!DOCTYPE html>
<html>
<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
<script src= "http://ajax.googleapis.com/ajax/libs/angularjs/1.3.14/angular.min.js"></script>
<script src= "style.css" rel="stylesheet"></script>
<head>
<title>LinkedIn Scraper Tool</title>
</head>
<body>

<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
    <div class=" navbar_container container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                <div class="sr-only">Toggle navigation</div>
                <div class="icon-bar"></div>
                <div class="icon-bar"></div>
                <div class="icon-bar"></div>
            </button>
            <a class="navbar-brand" href="#"><b>LinkedIn Scraper Tool</b></a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>

<div class="main container-fluid" ng-app="myApp"> 

    <div class="row common_container">
        <form>
        <h5>Please save your username and password details for authentication.</h5>
            <div class="form-group">
                <input type="text" class="form-control" placeholder="Linked In Username"></input>
            </div>
            <div class="form-group">
                <input type="password" class="form-control" placeholder="Linked In Password"></input>
            </div>
            <button type="submit" class=" save_button btn btn-primary">Save</button>
        </form>
    </div>
    <hr>
    <div class="row tools_container">
        <div class="single_profile col-xs-4 tool_common">
            <div class="tool_heading">This is the div for single profile scraping</div>
        </div>
        <div class="multiple_profile col-xs-4 tool_common">
            <div class="tool_heading">This is the div for multiple profile scraping</div>
