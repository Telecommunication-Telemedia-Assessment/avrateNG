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

  <style>
    .input-group-addon, h4 {
      text-align: center;
    }
    .negative-label {
      color: #555555;
    }
    .positive-label {
      color: #55AA55;
    }

  </style>

</head>

<!-- Basic template for the rating procedure. For different rating forms insert
respective slider/button/radio templates at id="form-template".
video_index needs to be given as input -->

<body>
<div id="playback"></div>
<div class="container" id="content">

  <br>


  <div class="row" id="form-template">



<!-- this template defines a simple slider form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->

    <script>

        function sliderChange(val, slider_headline_id, slider_name) {
            //document.getElementById(slider_headline_id).innerHTML = "<h5>" + val + "</h5>";
            //document.getElementById("submitButton").disabled = false;
        }
    </script>

<div class="container">
  <form action="/save_feedback" method="post">

    <h2>The end...</h2>

    <h4  style="text-align: left; padding-left: 1em; width: 25em; text-align: justify;"> The test is getting to the end, please answer a few last questions about the rating that you provided </h4>

    <br>

    <h3>Please tell us how much these phenomens played a role in your rating:</script></h3>

    <!-- Beginning of a slider -->
    <div class="row">
      <h3>
        <div class="col-lg-4 col-lg-offset-4">
          <h4>Presence of blocky artifacts</h4>
        </div>
      </h3>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
          <span class="input-group-addon negative-label" id="sizing-addon2">Weakly</span>
          <input type="range" class="form-control" id="blocking_slider" name="blocking" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1', 'slider 1')">
          <span class="input-group-addon positive-label" id="sizing_addon2">Strongly</span>
        </div>
      </div>
    </div>
    <br><br>
    <!-- End of a slider -->


    <!-- Beginning of a slider -->
    <div class="row">
      <h3>
        <div class="col-lg-4 col-lg-offset-4">
          <h4>Visible bands of colour</h4>
        </div>
      </h3>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
          <span class="input-group-addon negative-label" id="sizing-addon2">Weakly</span>
          <input type="range" class="form-control" id="banding_slider" name="banding" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1', 'slider 1')">
          <span class="input-group-addon positive-label" id="sizing_addon2">Strongly</span>
        </div>
      </div>
    </div>
    <br><br>
    <!-- End of a slider -->


    <!-- Beginning of a slider -->
    <div class="row">
      <h3>
        <div class="col-lg-4 col-lg-offset-4">
          <h4>Smoothness of the playback</h4>
        </div>
      </h3>
    </div>

    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
          <span class="input-group-addon negative-label" id="sizing-addon2">Weakly</span>
          <input type="range" class="form-control" id="choppiness_slider" name="choppiness" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1', 'slider 1')">
          <span class="input-group-addon positive-label" id="sizing_addon2">Strongly</span>
        </div>
      </div>
    </div>
    <br><br>
    <!-- End of a slider -->


    <h3>How sure were you about the rating that you provided?</script></h3>

    <!-- Beginning of a slider -->

    <div class="row">
      <h3>
        <div class="col-lg-4 col-lg-offset-4">
          <h4>Confidence</h4>
        </div>
      </h3>
    </div>


    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
          <span class="input-group-addon negative-label" id="sizing-addon2">Unsure</span>
          <input type="range" class="form-control" id="confidence_slider" name="confidence" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1', 'slider 1')">
          <span class="input-group-addon positive-label" id="sizing_addon2">Sure</span>
        </div>
      </div>
    </div>
    <br><br>
    <!-- End of a slider -->


    <!--This input field contains the mouse tracking data and needs to be declared inside the submit form -->
    <input type="hidden" id="mouse_track" name="mouse_track" value=""/>

    <div class="row">
      <div class="col-lg-4 col-lg-offset-4">
        <button id="submitButton" class="btn-lg btn-success btn-block" onclick="log_position()">Submit</button>
      </div>
    </div>

  </form>
</div>




    <form method="post" id="tracking_form">

    </form>
    <br><br>

  </div>

  % include('templates/footer.tpl')

</div>


</body>

</html>
