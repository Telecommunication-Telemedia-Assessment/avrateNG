<!-- this template defines a Better/worse button form. 
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post"> 
    <div class="row">
      <div class="col-lg-6">
        <button id="Button" name="submit" value="better" class="btn-lg btn-success btn-block" onclick="">Better</button>	
      </div>
      <div class="col-lg-6">
        <button id="Button" name="submit" value="worse" class="btn-lg btn-danger btn-block">Worse</button>	
      </div>
    </div>
  </form>
</div>



<script>
// this script is reponsible for engaging the wait screen during playback
$(document).ready(function(){
    $("#Button").click(function(){
        $("#playback").show();
        $("#content").hide(); 
    });

});
</script>
