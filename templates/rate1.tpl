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
  			
    <div class="container">
      % include('templates/nav.tpl')
        
      <div class="row">
        <h3>Please rate the basic image quality<br><br></h3>
      </div>
        
      % include('templates/slider1.tpl')    
      % include('templates/footer.tpl')
    </div>

  </body>

</html>
