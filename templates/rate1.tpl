<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Max" >
    <title>{{title}}</title>
    % include('templates/header.tpl')
    <!-- deactivated track mouse positions
    <script src="/static/track_mouse.js"></script>
    -->
    <script>
        function log_position() { }
        // this script is reponsible for engaging the wait screen during playback
        $(document).ready(function(){
            $("#submitButton").click(function(){
              // Fix issue with html5 validation
              const form = document.body.querySelector('#form1');
              if (form.checkValidity && !form.checkValidity()) {
                  return;
              }
              $("#playback").show();
              $("#content").hide();
            });
        });
    </script>
    <script type="text/javascript">

      function get_request(url) {
        const Http = new XMLHttpRequest();
        Http.open("GET", url);
        Http.send();

        Http.onreadystatechange = (e) => {
          console.log(Http.responseText)
        }
      }

      function play(video_index) {
        console.log("play: video_index:" + video_index);
        get_request("/play/" + video_index);
        setTimeout(
          ()=> {
            document.getElementById("content").style.display = "block";
          },
          1000  // 1 second delay to show the main rating form
        );
      }

      play("{{video_index}}");
    </script>
  </head>

<!-- Basic template for the rating procedure. For different rating forms insert
respective slider/button/radio templates at id="form-template".
video_index needs to be given as input -->

  <body>
    <div id="playback"></div>
    <div class="container" id="content" style="display:none">

      <div style="margin-top: 1em;"></div>
      % include('templates/progressBar.tpl', video_index=video_index, video_count=video_count)

      <div class="container">
        <div class="row">
            <div class="col">
              <h5>{{question}}</h5>
            </div>
            <div class="col text-right">
              <h5>User ID: {{user_id}}</h5>
            </div>
        </div>
      </div>

      <!--<div class="row" id="form-template"> -->
        % include('templates/' + rating_template, video_index=video_index)   # replace with slider1.tpl or button1.tpl
      <form method="post" id="tracking_form">

      </form>
        <br><br>

      <!--</div> -->

      % include('templates/footer.tpl')

    </div>


  </body>

</html>
