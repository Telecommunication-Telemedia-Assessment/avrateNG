<div class="col-12" id="ratingform" >

<h5>{{question}}</h5>


  % route = f"save_rating?stimuli_idx={stimuli_idx}" if not train else "training/" + str(stimuli_idx + 1)
  <form id="form1" action="/{{route}}" method="post">

    <%
      buttons = [
        {"value": 5, "text": "Excellent"},
        {"value": 4, "text": "Good"},
        {"value": 3, "text": "Fair"},
        {"value": 2, "text": "Poor"},
        {"value": 1, "text": "Bad"},

      ]
    %>

    <div class="funkyradio">
      % for button in buttons:

        <div class="funkyradio-success">
          <input type="radio" name="acr" id="radio_{{button['value']}}" value="{{button['value']}}" onchange="radiobutton_clicked(this)">
          <label for="radio_{{button['value']}}">{{button['value']}} - {{button['text']}}</label>
        </div>
      % end
    </div>

<h5>Select the effects that may have lowered the score</h5>

    <%
      labels = [
        {"value":"lack_of_global_contrast", "text": "Lack of global contrast"},
        {"value": "lack_of_local_contrast", "text": "Lack of local contrast"},
        {"value": "low_clarity_for_small_details", "text": "Low clarity for small details"},
        {"value": "visible_blocking_artifacts", "text": "Visible blocking artifacts"},
        {"value": "visible_bands_of_colour", "text": "Visible bands of colour"},
        {"value": "choppy_motion", "text": "Choppy motion"}
      ]
    %>


    <!--<div class="funkyradio">-->
    <div class="funkyradio-success">
      % for label in labels:


          <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" id="switch_{{label['value']}}" name="switch_{{label['value']}}" value="yes">
            <label class="form-check-label" for="switch_{{label['value']}}">{{label['text']}}</label>
          </div>

      % end
    </div>

    % include('templates/rating/common.tpl', stimuli_file=stimuli_file)


    <button type="submit" id="submitButton" class="btn btn-success btn-block" onclick="check_form(event)">submit</button>
    % if dev:
      <button type="submit" class="btn btn-success" formnovalidate>skip (for dev)</button>
    % end

    <div id="ratingselect" class="btn alert-danger" style="display:none;cursor:default; margin-top: 0.5em; margin-bottom: 0.5em" disabled>Please select a rating.</div>
  </form>
</div>



<script>
    var radio_button_clicked = 0;

    function radiobutton_clicked(rb) {
      radio_button_clicked ++;
    }

    function check_form(event) {
      console.log(document.getElementById("pi").value);
      document.getElementById("ratingselect").style.display = "none";

      if (radio_button_clicked == 0) {
          document.getElementById("ratingselect").style.display="block";
          event.preventDefault();
          return
      }
    }
</script>