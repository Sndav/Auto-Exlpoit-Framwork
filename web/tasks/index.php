<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
	<script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
	<meta charset="utf-8">
	<title>Auto-Exploit Web Console</title>
	<script>    
		$('li.dropdown').mouseover(function() {
     	$(this).addClass('open');}).mouseout(function() {$(this).removeClass('open');}); 
	</script>
</head>
<body>
	<nav class="navbar navbar-default" role="navigation">
	   <div class="navbar-header">
	      <a class="navbar-brand" href="#">Auto-Exploit Console</a>
	   </div>
	   <div>
	      <ul class="nav navbar-nav">
	         <li><a href="../index.php">Home</a></li>
	         <li><a href="../exploit">Exploit Manage</a></li>
	         <li class="active"><a href="../tasks">Tasks</a></li>
	         <li class="dropdown">
	            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
	               Tools 
	               <b class="caret"></b>
	            </a>
	            <ul class="dropdown-menu">
	               <li><a href="../tools/?method=domain">Find Subdomain</a></li>
	               <li class="divider"></li>
	               <li><a href="../tools/?method=dir">Fuzz Direction</a></li>
	            </ul>
	         </li>
	      </ul>
	   </div>
	</nav>
</body>
</html>