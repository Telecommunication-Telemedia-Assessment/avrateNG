<!-- this template defines the progress bar on top of the AVrate pages.
The JS part dynamically changes the value and width of the bar according to
total number of videos in playlist and current video_index-->


<div class="progress">
  <div id="progress_bar" class="progress-bar" role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100" style="width:20%">
           {{video_index+1}} / {{video_count}}
  </div>
</div>
<hr/>

<script>
var barwidth = 100*{{video_index+1}}/{{video_count}}
$(document).ready(function(){
    $("#progress_bar").attr("aria-valuenow",{{video_index}});
    $("#progress_bar").css("width",barwidth + '%');

});
</script>
