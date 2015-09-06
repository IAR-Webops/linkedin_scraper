<!DOCTYPE html>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
<script src= "http://ajax.googleapis.com/ajax/libs/angularjs/1.3.15/angular.min.js"></script>
<script src= "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<link href= "style.css" rel="stylesheet">
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
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-right">
                <li class="navbar_link"><a data-toggle="modal" data-target="#creds_modal" href="#">Set Credentials</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->

    </div><!-- /.container-fluid -->
</nav>

<div id="creds_modal" class=" modal fade" role="dialog">
    <div class="modal-dialog">

        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">Please set your linked in credentials to use scraping tool:</h4>
            </div>
            <div class="modal-body container">
                <div class="row common_container">
                    <form action="creds.php" method="POST">
                        <h4>Please save your username and password details for authentication.</h4>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Linked In Username" name="username"></input>
                        </div>
                        <div class="form-group">
                            <input type="password" class="form-control" placeholder="Linked In Password" name="password"></input>
                        </div>
                        <button type="submit" class=" save_button btn btn-primary">Save</button>
                    </form>
                </div>
            </div>
            <div class="modal-footer">
                <p class="center_align">We will not use your credentials for any other purposes rather than scraping.</p>
            </div>
        </div>

    </div>
</div>

<div class="main container-fluid" ng-app="myApp"> 

    <div class="row tools_container">
        <div class="single_profile col-xs-6 tool_common">
            <div class="tool_heading"><h4><u>Single Profile Scraping</u></h4></div>
            <form action="single_profile.php" class="single_profile_form" method="GET">
                        <h5>Please give profile id of person to scrape.</h5>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Profile ID" name="pid"></input>
                        </div>
                        <button type="submit" class=" save_button btn btn-primary">Save in DB</button>
            </form>
        </div>
        <div class="multiple_profile col-xs-6 tool_common">
            <div class="tool_heading"><h4><u>Multiple Profile Scraping</u></h4></div>
        </div>
    </div>


</div>

<script>
var app = angular.module('myApp', []);
</script>

</body>
</html>
