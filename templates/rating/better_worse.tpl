<div class="col-12" id="ratingform" >

<h5>{{question}}</h5>


  % route = f"save_rating?stimuli_idx={stimuli_idx}" if not train else "training/" + str(stimuli_idx + 1)
  <form id="form1" action="/{{route}}" method="post">

      <div class="col-lg-6">
        <button id="submitButton" name="submit" value="better" class="btn-lg btn-success btn-block" onclick="check_form(event)">Better</button>
      </div>
      <div class="col-lg-6">
        <button id="submitButton" name="submit" value="worse" class="btn-lg btn-danger btn-block" onclick="check_form(event)">Worse</button>
      </div>

    % include('templates/rating/common.tpl', stimuli_file=stimuli_file)


    % if dev:
      <button type="submit" class="btn btn-success" formnovalidate>skip (for dev)</button>
    % end

    <div id="ratingselect" class="btn alert-danger" style="display:none;cursor:default; margin-top: 0.5em; margin-bottom: 0.5em" disabled>Please select a rating.</div>
  </form>
</div>



<script>

    function check_form(event) {
      console.log(document.getElementById("pi").value);
      document.getElementById("ratingselect").style.display = "none";

    }
</script>