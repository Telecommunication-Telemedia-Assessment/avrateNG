




<style>

.slider {
  width: 100% !important;
}


</style>

<div class="col-12" id="ratingform" >



<h5>Please rate the quality.</h5>

    <style type="text/css">
    .slider::-webkit-slider-thumb  {
      background: #28a745;
    }
    .slider::-moz-range-thumb {
      background: #28a745;
    }
    .slider::-ms-thumb {
      background: #28a745;
    }
    </style>


  % route = f"save_rating?stimuli_idx={stimuli_idx}" if not train else "training/" + str(stimuli_idx + 1)
  <form id="form1" action="/{{route}}" method="post">

<%



groups = [
    {
        "group": "Quality",
        "adjectives": ["audio", "video"]
    },
    {
        "group": "Are audio and video quality matching?",
        "adjectives": ["matching"]
    },

]


%>

    <table class="table table-sm">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col"></th>
          <th scope="col"></th>
          <th scope="col">not</th>
          <th scope="col" style="text-align:center">applicable</th>
          <th scope="col">very</th>
        </tr>
      </thead>
      <tbody>
        % for g in groups:

            <tr><th colspan="5">{{g["group"]}}</th></tr>
            % for adj in g["adjectives"]:
              % adj_key = g["group"] + adj.replace(" ", "_")
            <tr>
              <td style="width:5%"></td>
              <td style="width:15%" >{{adj}} </td>
              <td style="width:15%" ><input type="number" id="label_range_{{adj_key}}" style="width:3em" onchange="update_slider(this, 'range_{{adj_key}}')" required></td>

              <td style="width:8em">0</td>
              <td style="width:50%">
                <input
                    type="range"
                    class="form-range slider"
                    name="range_{{adj_key}}"
                    id="range_{{adj_key}}"
                    min="0"
                    max="100"
                    value="50"
                    step="1"
                    oninput="slider_change(this)"
                    onchange="slider_change(this)"
                />

              </td>
              <td style="width:8em">100</th>
            </tr>
            % end
        %end
      </tbody>
    </table>

    % include('templates/rating/common.tpl', stimuli_file=stimuli_file)


    <button type="submit" id="submitButton" class="btn btn-success btn-block" onclick="check_form(event)">submit</button>
    % if dev:
      <button type="submit" class="btn btn-success" formnovalidate>skip (for dev)</button>
    % end

    <div id="playonce" class="btn alert-danger" style="display:none;cursor:default; margin-top: 0.5em; margin-bottom: 0.5em" disabled>Please play the stimuli at least once.</div>
  </form>
</div>



<script>
    var slidersChanged = {};
    // initialize sliders
    for (const slider of document.querySelectorAll('input.slider')) {
        slidersChanged[slider.getAttribute("name")] = 0;
    }
    function update_slider(input, range_id) {
        var slider = document.getElementById(range_id);
        slider.value = input.value
    }

    function slider_change(slider) {
        console.log("change");
        const label = document.getElementById("label_" + slider.getAttribute("name"));
        //label.textContent = slider.value;
        label.value = slider.value;

        slidersChanged[slider.getAttribute("name")] = 1;
        var check = Object.values(slidersChanged).every(e => e > 0);

        if (check) {
            document.getElementById("submitButton").disabled = false;
        }
    }
    function display_rating(){
        document.getElementById("ratingform").style.display="block";
    }

    function check_form(event) {
      console.log(document.getElementById("pi").value);
      if (document.getElementById("pi").value == 0) {
          document.getElementById("playonce").style.display="block";
          event.preventDefault();
          return
      }
    }
</script>