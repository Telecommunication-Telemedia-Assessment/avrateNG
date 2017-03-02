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
        <h3>Please rate the watched video<br><br></h3>
      </div>

      <div class="row">
        % include('templates/radio1.tpl', video_index=video_index)   # replace with slider1.tpl or button1.tpl
        % include('templates/slider1.tpl')
        % include('templates/button1.tpl', video_index=video_index)
        <br><br>
      </div>

      % include('templates/footer.tpl')
    </div>

  </body>

</html>
