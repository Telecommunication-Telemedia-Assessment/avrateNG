<!-- this template defines a simple slider form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post">

    <div class="row">
      <h3>
      <div class="col-lg-4 col-lg-offset-4">
        <output id="slider_value_1"><h3>Current slider1 value: 50 </script></h3></output>
      </div>
      </h3>
    </div>

    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
	      <span class="input-group-addon" id="sizing-addon2">0%</span>
	      <input type="range" class="form-control" id="slider" name="slider1" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1')">
	      <span class="input-group-addon" id="sizing_addon2">100%</span>
        </div>
      </div>
    </div>

    <br><br>

    <div class="row">
      <h3>
      <div class="col-lg-4 col-lg-offset-4">
        <output id="slider_value_2"><h3>Current slider2 value: 50 </script></h3></output>
      </div>
      </h3>
    </div>

    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
        <span class="input-group-addon" id="sizing-addon2">0%</span>
        <input type="range" class="form-control" id="slider" name="slider2" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_2')">
        <span class="input-group-addon" id="sizing_addon2">100%</span>
        </div>
      </div>
    </div>

    <div class="row">
      <h3>
      <div class="col-lg-4 col-lg-offset-4">
        <output id="slider_value_3"><h3>Current slider3 value: 50 </script></h3></output>
      </div>
      </h3>
    </div>

    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
        <span class="input-group-addon" id="sizing-addon2">0%</span>
        <input type="range" class="form-control" id="slider" name="slider3" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_3')">
        <span class="input-group-addon" id="sizing_addon2">100%</span>
        </div>
      </div>
    </div>

        <div class="row">
      <h3>
      <div class="col-lg-4 col-lg-offset-4">
        <output id="slider_value_4"><h3>Current slider 4 value: 50 </script></h3></output>
      </div>
      </h3>
    </div>

    <!--When customizing the form, only change the following section and leave the rest untouched-->
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
        <span class="input-group-addon" id="sizing-addon2">0%</span>
        <input type="range" class="form-control" id="slider" name="slider4" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_4')">
        <span class="input-group-addon" id="sizing_addon2">100%</span>
        </div>
      </div>
    </div>

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

    function sliderChange(val, slider_headline_id) {
        document.getElementById(slider_headline_id).innerHTML = "<h3>Current slider value: " + val + "</h3>";
        document.getElementById("submitButton").disabled = false;
    }
</script>
