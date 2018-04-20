<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>My Spam Detection App</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	 <!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.css" />
	<script src="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.min.js"></script>
	<link rel="stylesheet" type="text/css" media="screen" href="static/style.css" />

</head>
<body>
	<div class="container">
		<h1 class="text-center">
			Spam Detection
			<small class="text-muted">using String Matching Algorithm</small>
		</h1>
		<div class="row">
			<div class="col-md-4 col-sm-4">
				<form action = "<?php $_PHP_SELF ?>" method = "POST" id="main-form">
					<label for="username">Twitter Username:</label>
					<input type="text" class="form-control" placeholder="@prabowo" id="username" name="username">
					<br>

					<label for="select">Algorithm</label>
					<select class="form-control" id="select" form="main-form" name="algorithm">
						<option value="0">Boyer-Moore</option>
						<option value="1">KMP</option>
						<option value="2">Regex</option>
					</select>
					<br>

					<label for="keyword-container">Keywords</label>
					<input type="text" id="keyword-container" name="keywords" class="form-control" value="" data-role="tagsinput" />
					<br>
					<br>
					<button type="submit" class="btn btn-primary btn-block">Proceed</button>
      			</form>
			</div>
			<div class="col-md-8 col-sm-8">
			<?php

				$url = 'http://127.0.0.1:5000/';
				if(isset($_POST['keywords']) && isset($_POST['username'])) {
					if($_POST['keywords'] && $_POST['username']) {
						showTweet($url, $_POST);
					}	
				}

				function showTweet($url, $data) {
					$ch = curl_init($url);
					curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
					curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
					
					// execute!
					$response = curl_exec($ch);
					
					// close the connection, release resources used
					curl_close($ch);
					
					// do anything you want with your response
					$arr = json_decode($response);
					
					echo "
					<br>
					";

					foreach ( $arr->data as $data ){
						echo getTweet($data);
					}
				}

				function getTweet($data){
					$spamText = "<a class=\"not-spam\">Not Spam</a>";
					if($data->spam){
						$spamText = "<a class=\"spam\">Spam</a>";
					}
					$tweet = "
					<div class=\"qa-message-list\" id=\"wallmessages\">
						<div class=\"message-item\" id=\"m16\">
							<div class=\"message-inner\">
								<div class=\"message-head clearfix\">
									<div class=\"avatar pull-left\"><a href=\"http://twitter.com/". $data->username."\"><img src=\"". $data->image. "\"></a></div>
									<div class=\"user-detail\">
										<h5 class=\"handle\">". $data->name."</h5>
										<div class=\"post-meta\">
											<div class=\"asker-meta\">
												<span class=\"qa-message-what\"></span>
												<span class=\"qa-message-when\">
													<span class=\"qa-message-when-data\">". $data->date."</span>
												</span>
												<span class=\"qa-message-who\">
													<span class=\"qa-message-who-pad\">by </span>
													<span class=\"qa-message-who-data\"><a href=\"http://twitter.com/". $data->username. "\">@". $data->username. "</a></span>
												</span>
											</div>
										</div>
									</div>
								</div>
								<div class=\"qa-message-content\">"
									. $data->text.
									"<br><br>".
									"<span class=\"qa-message-who-data\"><a href=\"http://twitter.com/".$data->username."/status/".$data->id. "\">View Summary</a></span>".
									"<br>".
									"Verdict : ".
									$spamText.
								"</div>
							</div>
						</div>
					";

					return $tweet;
				}
				?>	
			</div>
		</div>
	</div>
	<br>
</body>
</html>