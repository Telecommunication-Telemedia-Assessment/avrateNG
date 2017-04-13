<!-- this template defines a simple slider form. 
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post">
    <div class="row">
      <div class="col-lg-12">
        <div class="input-group input-group-lg">
	      <span class="input-group-addon" id="sizing-addon2">0%</span>
	      <input type="range" class="form-control" id="slider" name="slider" min="0" max="100" step="1" value="50" data-popup-enabled="true" >
	      <span class="input-group-addon" id="sizing_addon2">100%</span>
        </div>
      </div>
    </div>
    <br><br>
    <div class="row">
      <div class="col-lg-4 col-lg-offset-4">
        <button id="submitButton" class="btn-lg btn-success btn-block" disabled>Submit</button>
      </div>
    </div>
  </form>
</div>



<script>
// this script enables the submit button after the slider was moved 
$(document).ready(function(){
    $("#slider").on('click touchstart', function(){
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
