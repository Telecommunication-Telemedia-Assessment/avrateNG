<!-- this template defines a radio button form. 
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form id="form1" action="/save_rating?video_index={{video_index}}" method="post">
    <div class="row">
      <div class="funkyradio">
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio1" value="5"/>
          <label for="radio1"><h4>Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio2" value="4"/>
          <label for="radio2"><h4>Good</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio3" value="3"/>
          <label for="radio3"><h4>Fair</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio4" value="2"/>
          <label for="radio4"><h4>Poor</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="radio" id="radio5" value="1"/>
          <label for="radio5"><h4>Very poor</h4></label>
        </div>
      </div>
    </div>
    <div class="row">
      <br>
      <button id="submitButton" class="btn-lg btn-success btn-block" disabled>Submit and continue</button>
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
// this script is reponsible for engaging the wait screen during playback
$(document).ready(function(){
    $("#submitButton").click(function(){
        $("#playback").show();
        $("#content").hide(); 
    });

});
</script>
