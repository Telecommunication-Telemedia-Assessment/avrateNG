<!-- this template defines a Better/worse button form. 
When creating custom forms copy this basic structure.
Don't change the form attributes "action" and "method"-->


<div class="container">
  <form action="/save_rating?video_index={{video_index}}" method="post"> 

    <!--This input field contains the mouse tracking data and needs to be declared inside the submit form -->
    <input type="hidden" id="mouse_track" name="mouse_track" value=""/>

    <div class="row">
      <div class="col-lg-6">
        <button id="submitButton" name="submit" value="1" class="btn-lg btn-success btn-block" onclick="log_position()">Better</button>	
      </div>
      <div class="col-lg-6">
        <button id="submitButton" name="submit" value="0" class="btn-lg btn-danger btn-block" onclick="log_position()">Worse</button>	
      </div>
    </div>
  </form>
</div>


