<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Max" >
    <title>{{title}}</title>
    % include('templates/header.tpl')
  </head>

  <body>
    <div id="playback"></div>
    <div class="jumbotron" id="jumbotron">
      <h1>Welcome to AVRateNG </h1>
      <p class="lead">This is the training stage</p>
      <a class="btn btn-large btn-success" href="/rate/0" id="start">Start training</a> <!-- Jump to first trainingsplaylist item -->
      <br><br>
      <p class="lead">User ID: {{user_id}}</p>
    </div>
    <div class="container" id="footer">
      % include('templates/footer.tpl')
    </div>

  </body>

  <script>
  // this script is reponsible for engaging the wait screen during playback
  $(document).ready(function(){
      $("#start").click(function(){
          $("#playback").show();
          $("#jumbotron").hide();
          $("#footer").hide();
      });

  });
  </script>

</html>
