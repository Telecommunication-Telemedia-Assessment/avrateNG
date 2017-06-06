<!-- this template defines a simple slider form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post">

    <div class="row">
      <h3>
      <div class="col-lg-4 col-lg-offset-4">
        <output id="slider_value"><h3>Current slider value: 50 </script></h3></output>
      </div>
      </h3>
    </div>

    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
	      <span class="input-group-addon" id="sizing-addon2">0%</span>
	      <input type="range" class="form-control" id="slider" name="slider" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value)">
	      <span class="input-group-addon" id="sizing_addon2">100%</span>
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
