<!-- this template defines a radio button form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form id="form1" action="/save_rating?video_index={{video_index}}" method="post">
    <div class="row">

      <!-- Radio buttons used for selecting the video rating -->
      <div class="funkyradio">
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio5" value="5"/>
          <label for="radio5"><h4>Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio4" value="4"/>
          <label for="radio4"><h4>Good</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio3" value="3"/>
          <label for="radio3"><h4>Fair</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio2" value="2"/>
          <label for="radio2"><h4>Poor</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio1" value="1"/>
          <label for="radio1"><h4>Very poor</h4></label>
        </div>
      </div>



      <h4>Select the effects that may have lowered the score</h4>
      <!-- Check boxes used for selecting reasons for the rating selection -->
      <div class="funkyradio funkyradio-compact">

        <div class="funkyradio-success">
          <input type="checkbox" name="lack_of_global_contrast" id="lack_of_global_contrast"/>
          <label for="lack_of_global_contrast"><h4>Lack of global contrast</h4></label>
        </div>

        <div class="funkyradio-success">
          <input type="checkbox" name="name" id="lack_of_local_contrast"/>
          <label for="lack_of_local_contrast"><h4>Lack of local contrast</h4></label>
        </div>

        <div class="funkyradio-success">
          <input type="checkbox" name="low_clarity_for_small_details" id="low_clarity_for_small_details"/>
          <label for="low_clarity_for_small_details"><h4>Low clarity for small details</h4></label>
        </div>

        <div class="funkyradio-success">
          <input type="checkbox" name="name" id="visible_blocking_artifacts"/>
          <label for="visible_blocking_artifacts"><h4>Visible blocking artifacts</h4></label>
        </div>

        <div class="funkyradio-success">
          <input type="checkbox" name="visible_bands_of_colour" id="visible_bands_of_colour"/>
          <label for="visible_bands_of_colour"><h4>Visible bands of colour</h4></label>
        </div>

        <div class="funkyradio-success">
          <input type="checkbox" name="choppy_motion" id="choppy_motion"/>
          <label for="choppy_motion"><h4>Choppy motion</h4></label>
        </div>

      </div>


    </div>

    <!--This input field contains the mouse tracking data and needs to be declared inside the submit form -->
    <input type="hidden" id="mouse_track" name="mouse_track" value=""/>

    <div class="row">
      <br>
      <button id="submitButton" class="btn-lg btn-success btn-block" onclick="log_position()" disabled>Submit and continue</button>
    </div>
  </form>
</div>

<!-- this script enables the submit button after one option was checked -->
<script>
$(document).ready(function(){
    $(".funkyradio").click(function(){
        $("#submitButton").removeAttr("disabled");
    });
});

</script>
