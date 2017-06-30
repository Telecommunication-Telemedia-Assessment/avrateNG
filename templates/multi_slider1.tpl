<!-- this template defines a simple slider form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post">

    <div id="first_part">

      <div class="row">
        <div style="text-align:center" >
          <output id="slider_value_X"><h3>Quality (Qualität) value: 50 value: 50value: 50 value: 50 </h3></output>
        </div>
      </div>

      <!--When customizing the form, only change the following section and leave the rest untouched-->
      <div class="row">
        <div class="col-lg-12">
          <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2">0%</span>
          <input type="range" class="form-control" id="Quality (Qualität)" name="Quality (Qualität)" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_X', 'Quality (Qualität)')">
          <span class="input-group-addon" id="sizing_addon2">100%</span>
          </div>
        </div>
        <div class="col-lg-12">
          <div class="">
          <span class="input-group-addon" id="">bad (schlecht)</span>
          <span class="input-group-addon" id=""> </span>
          <span class="input-group-addon" id="">excellent (sehr gut)</span>
          </div>
        </div>

      </div>
      <div class="btn-lg btn-success btn-block" onclick="next()" >next </div>
    </div>


    <div style="display:none" id="second_part">

      <div class="row">
        <div style="text-align:center" >
          <output id="slider_value_1"><h3>Colorlessness (Farblosigkeit) value: 50 </h3></output>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-12">
          <div class="input-group input-group-lg">
  	      <span class="input-group-addon" id="sizing-addon2">0%</span>
  	      <input type="range" class="form-control" id="Colorlessness (Farblosigkeit)" name="Colorlessness (Farblosigkeit)" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_1', 'Colorlessness (Farblosigkeit)')">
  	      <span class="input-group-addon" id="sizing_addon2">100%</span>
          </div>
        </div>
         <div class="col-lg-12">
          <div class="">
          <span class="input-group-addon" id="">none (keine)</span>
          <span class="input-group-addon" id=""> </span>
          <span class="input-group-addon" id="">many (sehr viel)</span>
          </div>
        </div>
      </div>


      <div class="row">

        <div style="text-align:center" >
          <output id="slider_value_2"><h3>Blurriness (Unschärfe) value: 50 </h3></output>
        </div>
      </div>

      <!--When customizing the form, only change the following section and leave the rest untouched-->
      <div class="row">
        <div class="col-lg-12">
          <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2">0%</span>
          <input type="range" class="form-control" id="Blurriness (Unschärfe)" name="Blurriness (Unschärfe)" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_2', 'Blurriness (Unschärfe)')">
          <span class="input-group-addon" id="sizing_addon2">100%</span>
          </div>
        </div>
  		    <div class="col-lg-12">
            <div class="">
            <span class="input-group-addon" id="">none (keine)</span>
            <span class="input-group-addon" id=""> </span>
            <span class="input-group-addon" id="">many (sehr viel)</span>
          </div>
        </div>
      </div>

      <div class="row">

        <div style="text-align:center" >
          <output id="slider_value_3"><h3>Fragmentation (Fragmentierung) value: 50 </h3></output>
        </div>
      </div>

      <!--When customizing the form, only change the following section and leave the rest untouched-->
      <div class="row">
        <div class="col-lg-12">
          <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2">0%</span>
          <input type="range" class="form-control" id="Fragmentation (Fragmentierung)" name="Fragmentation (Fragmentierung)" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_3', 'Fragmentation (Fragmentierung)')">
          <span class="input-group-addon" id="sizing_addon2">100%</span>
          </div>
        </div>
          <div class="col-lg-12">
            <div class="">
            <span class="input-group-addon" id="">none (keine)</span>
            <span class="input-group-addon" id=""> </span>
            <span class="input-group-addon" id="">many (sehr viel)</span>
          </div>
        </div>
      </div>

      <div class="row">

        <div style="text-align:center" >
          <output id="slider_value_4"><h3>Movement disturbance (Bewegungsstörung) value: 50 </h3></output>
        </div>
      </div>

      <!--When customizing the form, only change the following section and leave the rest untouched-->
      <div class="row">
        <div class="col-lg-12">
          <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2">0%</span>
          <input type="range" class="form-control" id="Movement disturbance (Bewegungsstörung)" name="Movement disturbance (Bewegungsstörung)" min="0" max="100" step="1" value="50" oninput="sliderChange(this.value, 'slider_value_4', 'Movement disturbance (Bewegungsstörung)')">
          <span class="input-group-addon" id="sizing_addon2">100%</span>
          </div>
        </div>
          <div class="col-lg-12">
            <div class="">
            <span class="input-group-addon" id="">none (keine)</span>
            <span class="input-group-addon" id=""> </span>
            <span class="input-group-addon" id="">many (sehr viel)</span>
          </div>
        </div>
      </div>

      <!--This input field contains the mouse tracking data and needs to be declared inside the submit form -->
      <input type="hidden" id="mouse_track" name="mouse_track" value=""/>

      <div class="row">

        <div style="text-align:center" >
          <button id="submitButton" class="btn-lg btn-success btn-block" onclick="log_position()" disabled>Submit</button>
        </div>
      </div>
    </div>
  </form>
</div>



<script>

    function sliderChange(val, slider_headline_id, slider_name) {
        document.getElementById(slider_headline_id).innerHTML = "<h3>" + slider_name +  " value: " + val + "</h3>";
        document.getElementById("submitButton").disabled = false;
    }

    function next() {
        document.getElementById("first_part").style.display = "none";
        document.getElementById("second_part").style.display = "inline";
    }
</script>
