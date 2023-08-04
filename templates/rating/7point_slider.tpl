<div class="col-12" id="ratingform" >

<h5>{{question}}</h5>

  % route = f"save_rating?stimuli_idx={stimuli_idx}" if not train else "training/" + str(stimuli_idx + 1)
  <form id="form1" action="/{{route}}" method="post">

    <div>
      <div style="z-index:100; position: relative;">
      <input
          type="range"
          class="form-range slider7p"
          name="range_7point_slider"
          id="range_7point_slider"
          min="1"
          max="7"
          value="4"
          step="0.07"
          oninput="slider_change(this)"
          onchange="slider_change(this)"
        />
      </div>
      <div style="z-index:10; position: relative;">
      <table class="ticks">
          <td class="ticklabel"><div class="tick"> </div></td>
        % for i in range(1, 3):
          <td class="ticklabel"><div class="tickNone"> </div></td>
        % end
        % for i in range(3, 30-2):
          <td class="ticklabel" >
            % if i % 5 == 0:
              <div class="tick2"> </div>
            % else:
              <div class="tick"> </div>
            % end
          </td>
        % end
        % for i in range(30-2, 30):
          <td class="ticklabel"><div class="tickNone"> </div></td>
        % end
        <td class="ticklabel"><div class="tick"> </div></td>

      </table>


      <table class="textlabels">
        <td class="textlabel">Extremly <br> bad</td>
        <td class="textlabel">Bad</td>
        <td class="textlabel">Poor</td>
        <td class="textlabel">Fair</td>
        <td class="textlabel">Good</td>
        <td class="textlabel">Excellent</td>
        <td class="textlabel">Ideal</td>
      </table>
      </div>
    </div>
    <style type="text/css">

      .ticks {
        width: 86%;
        height: 15px;
        margin-left: 7%;
        text-align: center;
        margin-top: -20px;
        margin-bottom: 0.5em;
      }
      .tick {
        display: inline-block;
        width:3px;
        height: 15px; background-color: black;
        margin-left: -1px;
        top: 0px;
      }
      .tickNone {
        display: inline-block;
        width:1px;
        height: 5px; background-color: none;
        margin-left: -0.5px;
        top: 0px;
      }
      .tick2 {
        display: inline-block;
        width:5px;
        height: 25px; background-color: black;
        margin-left: -2px;
        top: 0px;
      }
      .ticklabel {
        width: {{100/35}}%;
      }
      .slider7p {
        width:  86%;
        margin-left: 7%;
        margin-right: 7%;
      }
      .labels {
        width: 86%;
        text-align: center;
        margin-left: 7%;
        margin-top: -0.5em;
        margin-bottom: 0.5em;
      }
      .label {
        width: {{100/7}}%;
        height: 1em;
      }
      .textlabels {
        width: 100%;
        text-align: center;
      }
      .textlabel {
        /*border: 1px solid black;;*/
        width: {{100/7}}%;
      }
    </style>

    <div style="margin-bottom:2em; margin-top:1em">
    Rating: <input type="number" id="label_range_7point_slider" style="width:5em" onchange="update_slider(this, 'range_7point_slider')" required>
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