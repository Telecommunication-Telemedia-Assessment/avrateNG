<form action="/save_rating" method="post">
  <div class="row">
    <div class="col-lg-10">
      <div class="input-group input-group-lg">
	<span class="input-group-addon" id="sizing-addon2">Poor</span>
	<input type="range" class="form-control" id="slider" name="submit" min="0" max="100" step="1">
	<span class="input-group-addon" id="sizing-addon2">Excellent</span>
      </div>
    </div>
    <div class="col-lg-2">
      <button id="submitButton" class="btn-lg btn-success" disabled>Submit</button>
    </div>
  </div>
</form>

<script>
$(document).ready(function(){
    $("#slider").click(function(){
        $("#submitButton").removeAttr("disabled");
    });
});
</script>
