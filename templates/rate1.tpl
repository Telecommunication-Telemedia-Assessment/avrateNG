<!DOCTYPE html>
<html>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Max" >
  <head>
    <title>{{title}}</title>
    % include('templates/header.tpl')
    <!-- track mouse positions -->
    <script src="/static/track_mouse.js"></script>
    <script>
        // this script is reponsible for engaging the wait screen during playback
        $(document).ready(function(){
            $("#submitButton").click(function(){
            $("#playback").show();
            $("#content").hide(); 
            });
        });
    </script>
  </head>

<!-- Basic template for the rating procedure. For different rating forms insert 
respective slider/button/radio templates at id="form-template".
video_index needs to be given as input -->

  <body>
    <div id="playback"></div>
    <div class="container" id="content">
      
      <br>
      % include('templates/progressBar.tpl', video_index=video_index, video_count=video_count)

      <div class="row">
        <h3 style="float: left; width: 34%; text-align: left;">Please rate the watched video</h3>
        <h3 style="float: right; width: 34%; text-align: right;">User ID: {{user_id}}</h3>
        <br><br><br><br><br><br>
      </div>

      <div class="row" id="form-template">
        % include('templates/' + rating_template, video_index=video_index)   # replace with slider1.tpl or button1.tpl
      <form method="post" id="tracking_form">
            
      </form> 
        <br><br>
        
      </div>

      % include('templates/footer.tpl')
      
    </div> 
    
    
  </body>

</html>
