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
      <h1>Welcome to AVRate++</h1>  			
      <p class="lead">You will now be asked for your rating, alright?</p>
      <a class="btn btn-large btn-success" href="rate">Get started</a>
    </div>
    <div class="container">
      % include('templates/footer.tpl')
    </div>

  </body>

</html>
