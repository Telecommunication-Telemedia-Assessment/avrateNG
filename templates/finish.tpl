<!DOCTYPE html>
<html>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Max" >
  <head>
    <title>{{title}}</title>
    % include('templates/header.tpl')
  </head>

  <body>

    <div class="jumbotron">
      <h1>You're done</h1>
      <p class="lead">Thank you for participating!</p>
      <a class="btn btn-large btn-success" href="/">Restart</a>
    </div>
    <div class="container">
      % include('templates/footer.tpl')
      <a href="/about">About AVRate++</a>
    </div>

  </body>

</html>
