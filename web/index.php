<?php
	$info = 'Info';
	$info_id = '0';
	$task1 = 'task1';
	$task2 = 'task2';
	$task3 = 'task3';
	$task1_w = '60%';
	$task2_w = '60%';
	$task3_w = '60%';
?>
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

	<div class="container-fluid">
	<div class="row clearfix">
		<div class="col-md-12 column">
			<nav class="navbar navbar-default" role="navigation">
				<div class="navbar-header">
					<a class="navbar-brand" href="#">Auto-Exploit Console</a>
				</div>
				<div>
					<ul class="nav navbar-nav">
						<li class="active"><a href="./index.php">Home</a></li>
						<li><a href="./exploit/">Exploit Manage</a></li>
						<li><a href="./tasks/">Tasks</a></li>
						<li class="dropdown">
							<a href="#" class="dropdown-toggle" data-toggle="dropdown">
								Tools 
								<b class="caret"></b>
							</a>
							<ul class="dropdown-menu">
								<li><a href="./tools/?method=domain">Find Subdomain</a></li>
								<li class="divider"></li>
								<li><a href="./tools/?method=dir">Fuzz Direction</a></li>
							</ul>
						</li>
					</ul>
				</div>
			</nav>


		<!-- for infomation tab -->
			<?php 
				if(true) echo
			'
			<div class="alert alert-success alert-dismissable">
				 <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
				 ×
				 </button>
				<strong>Infomation</strong> '.$info.' <a href="'.$info_id.'" class="alert-link">Click here</a>
			</div>
			';
			?>

		</div>
	</div>
	<!-- for task progress-->
	<div class="row clearfix">
		<div class="col-md-12 column">
			<div class="row clearfix">
				<div class="col-md-8 column">
					<h3>
						Task Progress
					</h3>
				</div>
				<div class="col-md-4 column">
					 <button type="button" class="btn btn-success btn-block btn-lg">Add Task</button>
				</div>
			</div>
			<div class="row clearfix">
				<div class="col-md-4 column">
					 <span class="label label-default"><?php echo "$task1";?></span>
					 <p></p>
					<div class="progress progress-striped active" >
						<div class="progress-bar progress-success" style="width: <?php echo $task1_w;?>">
						</div>
					</div>
				</div>
				<div class="col-md-4 column">
					 <span class="label label-default"><?php echo "$task2";?></span>
					 <p></p>
					<div class="progress progress-striped active"> 
						<div class="progress-bar progress-success" style="width: <?php echo $task2_w;?>">
						</div>
					</div>
				</div>
				<div class="col-md-4 column">
					 <span class="label label-default"><?php echo "$task3";?></span>
					 <p></p>
					<div class="progress progress-striped">
						<div class="progress-bar progress-success" style="width: <?php echo $task3_w;?>">
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<br>
	<!-- Command Exec-->
	<div class="row clearfix">
		<div class="col-md-12 column">
			<div class="row clearfix">
				<div class="col-md-12 column">
					<h3>
						Command Exec
					</h3>
				</div>
			</div>
			<div class="row clearfix">
				<form class="form-inline" role="form" method="post" action="#">
					<div class="col-md-8 column">
						<div class="form-group">
							<input type="text" class="form-control" id="command" placeholder="please enter command" style="width: 450%">
						</div>
						
					</div>
					<div class="col-md-4 column">
						 <button type="submit" class="btn btn-default active btn-block btn-success">Exec</button>
					</div>
				</form>
			</div>
			<div class="row-fluid">
			<fieldset>
				<legend>Result:</legend>
			</fieldset>
			<textarea id="logtrace" style="width:100%;overflow-x:hidden;overflow-y:auto;" readonly="readonly" cols="80" rows="21"></textarea>
			</div>
		</div>
	</div>
	<!--bottom-->
	<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="100%" color=#f87cb9 SIZE=3>
	<div class="raw clearfix">
		<div class="col-md-6 column" style="text-align: left;">
			<label>Auto-Exploit-Framework</label>
		</div>
		<div class="col-md-6 column" style="text-align: right;">
		<label>Powered By Sndav</label>
		</div>
	</div>
</div>


</body>
</html>