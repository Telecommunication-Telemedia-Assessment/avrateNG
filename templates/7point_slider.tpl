<!-- this template defines a simple slider form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->

<input type="image" class="form-control form-control-sm" id="image" alt=7 point slider" src="/static/7point_slider.png">

<br><br>

<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post">


    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <input type="range" class="form-control form-control-sm" id="slider" name="slider" min="1" max="7" step="0.07" value="4" oninput="sliderChange(this.value)">
        </div>
      </div>
    </div>

    <br><br>

    <!--This input field contains the mouse tracking data and needs to be declared inside the submit form -->
    <input type="hidden" id="mouse_track" name="mouse_track" value=""/>

    <div class="row">
      <div class="col-lg-4 col-lg-offset-4">
        <button id="submitButton" class="btn-lg btn-success btn-block" onclick="log_position()" disabled>Submit</button>
      </div>
    </div>

  </form>
</div>



<script>

    function sliderChange(val) {
        document.getElementById("slider_value").innerHTML="<h3>Current slider value: "+val+"</h3>";
        document.getElementById("submitButton").disabled = false;
    }
</script>
