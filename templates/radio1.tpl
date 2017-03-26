<!-- this template defines a radio button form. 
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form id="form1" action="/save_rating?video_index={{video_index}}" method="post">
    <div class="row">
      <div class="funkyradio">
        <div class="funkyradio-success">
          <input type="radio" name="submit" id="radio1" value="Excellent"/>
          <label for="radio1"><h4>Excellent</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="submit" id="radio2" value="Good"/>
          <label for="radio2"><h4>Good</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="submit" id="radio3" value="Fair"/>
          <label for="radio3"><h4>Fair</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="submit" id="radio4" value="Poor"/>
          <label for="radio4"><h4>Poor</h4></label>
        </div>
        <div class="funkyradio-success">
          <input type="radio" name="submit" id="radio5" value="Very_poor"/>
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
