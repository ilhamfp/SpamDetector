<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap.tagsinput/0.4.2/bootstrap-tagsinput.css" />
    <link rel="stylesheet" href="static/style.css" />
    <title>Spam Detector</title>
     <!-- Tweet Timeline Style                                                      -->
     <!-- Source: https://bootsnipp.com/snippets/featured/timeline-single-column    -->
     <!-- Sidebar & Content Style                                                   -->
     <!-- Source: https://bootstrapious.com/p/bootstrap-sidebar                     -->
     <!-- dengan sedikit modifikasi untuk tugas besar strategi algoritma 3          -->
     
</head>
<body>
    <div class="wrapper">
        <!-- Sidebar Holder -->
        <nav id="sidebar">
            <div class="sidebar-header">
                <h3>Welcome!</h3>
            </div>
            <br>

            <!-- Sidebar Form -->

            <form action = "<?php $_PHP_SELF ?>" method = "POST" id="main-form">
                <label for="keywordSearch">Tweet Keyword:</label>
                <input type="text" class="form-control" placeholder=" Pemilu 2019, Presiden, Indonesia "  id="keywordSearch" name="keywordSearch">
                <br>

                <label for="select">Algorithm</label>
                <select class="form-control" id="select" form="main-form" name="algorithm">
                    <option value="0">Knuth-Morris-Pratt</option>
                    <option value="1">Boyer-Moore</option>
                    <option value="2">Regex</option>
                </select>
                <br>

                <label for="keyword-container">Spam Keywords</label>
                <input type="text" id="keyword-container" name="keywordSpam" class="form-control" value="" data-role="tagsinput" placeholder=" Top 10 Fakta Mengejutkan!" />

                <button type="submit" class="btn btn-primary btn-block" style="margin-top: 10%">Run</button>
            </form>


            <ul class="list-unstyled CTAs">
                <li><a href="http://localhost:5000/about" class="about" style="margin-top: 110%">About Us</a></li>
            </ul>
        </nav>

        <!-- Page Content Holder -->
        <div id="content">

            <nav class="navbar navbar-default">
                <div class="container-fluid">

                    <div class="navbar-header">
                        <button type="button" id="sidebarCollapse" class="navbar-btn">
                            <span></span>
                            <span></span>
                            <span></span>
                        </button>
                    </div>

                    <h1 class="text-center">
                        <img class="rounded" src="static/bird.png"></a>
                        Twitter Spam Detector
                    </h1>
                </div>
            </nav>
            
            <!-- Tweet Content -->

            <?php

                $url = 'http://127.0.0.1:5000/';
                if(isset($_POST['keywordSpam']) || isset($_POST['keywordSearch'])) {
                    if($_POST['keywordSpam'] || $_POST['keywordSearch']) {
                        showTweet($url, $_POST);
                    }   
                }

                function showTweet($url, $data) {
                    $ch = curl_init($url);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
                    $response = curl_exec($ch);
                    curl_close($ch);

                    // Ambil hasil
                    $arr = json_decode($response);
                    echo "
                    <br>
                    ";

                    // Untuk setiap hasil tweet, echo hasilnya
                    foreach ( $arr->hasil as $tweet ){
                        echo getTweet($tweet);
                    }
                }

                function getTweet($tweet){
                    if($tweet->spam){
                        $verdictText = "<a class=\"spam\">Spam!!</a>";
                    } else {
                        $verdictText = "<a class=\"not-spam\">Not spam</a>";
                    }
                    $tweet = "
                    <div class=\"qa-message-list\" id=\"wallmessages\">
                        <div class=\"message-item\" id=\"m16\">
                            <div class=\"message-inner\">
                                <div class=\"message-head clearfix\">
                                    <div class=\"avatar pull-left\"><a href=\"http://twitter.com/". $tweet->username."\"><img src=\"". $tweet->image. "\"></a></div>
                                    <div class=\"user-detail\">
                                        <h5 class=\"handle\">". $tweet->name."</h5>
                                        <div class=\"post-meta\">
                                            <div class=\"asker-meta\">
                                                <span class=\"qa-message-what\"></span>
                                                <span class=\"qa-message-when\">
                                                    <span class=\"qa-message-when-data\">". $tweet->date."</span>
                                                </span>
                                                <span class=\"qa-message-who\">
                                                    <span class=\"qa-message-who-pad\">by </span>
                                                    <span class=\"qa-message-who-data\"><a href=\"http://twitter.com/". $tweet->username. "\">@". $tweet->username. "</a></span>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class=\"qa-message-content\">"
                                    . $tweet->text.
                                    "<br><br>".
                                    "Verdict : ".
                                    $verdictText.
                                    "<br>".
                                    "<span class=\"qa-message-who-data\"><a href=\"http://twitter.com/".$tweet->username."/status/".$tweet->id. "\">View Tweet Source</a></span>".
                                "</div>
                            </div>
                        </div>
                    ";
                    return $tweet;
                }
            ?>
        </div>
    </div>

    <!-- jQuery CDN -->
    <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
    <!-- Bootstrap Js CDN -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- jQuery Custom Scroller CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/malihu-custom-scrollbar-plugin/3.1.5/jquery.mCustomScrollbar.concat.min.js"></script>

    <script type="text/javascript">
        $(document).ready(function () {
            $("#sidebar").mCustomScrollbar({
                theme: "minimal"
            });
            $('#sidebarCollapse').on('click', function () {
                $('#sidebar, #content').toggleClass('active');
                $('.collapse.in').toggleClass('in');
                $('a[aria-expanded=true]').attr('aria-expanded', 'false');
                $(this).toggleClass('active');
            });
        });
    </script>
</body>
</html>