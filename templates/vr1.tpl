<!-- this template defines a radio button form.
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form id="form1" action="/save_rating?video_index={{video_index}}" method="post">
    <div class="row">
      <div class="funkyradio">
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality6" value="6" required/>
          <label for="quality6"><h4>6 - Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality5" value="5" required/>
          <label for="quality5"><h4>5 - Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality4" value="4"/>
          <label for="quality4"><h4>4 - Good</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality3" value="3"/>
          <label for="quality3"><h4>3 - Fair</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality2" value="2"/>
          <label for="quality2"><h4>2 - Poor</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality1" value="1"/ >
          <label for="quality1"><h4>1 - Bad</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="quality" id="quality0" value="0"/ >
          <label for="quality0"><h4>0 - XYZ</h4></label>
        </div>
      </div>
    </div>
    <hr>
    <h3>simulator sickness? </h3>
    <div class="row">
      <div class="funkyradio">
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq6" value="6" required/>
          <label for="ssq6"><h4>6 - Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq5" value="5" required/>
          <label for="ssq5"><h4>5 - Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq4" value="4"/>
          <label for="ssq4"><h4>4 - Good</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq3" value="3"/>
          <label for="ssq3"><h4>3 - Fair</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq2" value="2"/>
          <label for="ssq2"><h4>2 - Poor</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq1" value="1"/ >
          <label for="ssq1"><h4>1 - Bad</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="ssq" id="ssq0" value="0"/ >
          <label for="ssq0"><h4>0 - XYZ</h4></label>
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
