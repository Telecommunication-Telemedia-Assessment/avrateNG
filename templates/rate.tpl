% rebase('templates/skeleton.tpl', title=title)


<h3 class="mt-5">{{"Training" if get("train", False) else "Rating"}}</h3>

<script type="text/javascript">
  function get_request(url) {
    const Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }
  }

  function play(stimuli_idx, sub_index) {
    console.log("play: stimuli_idx:" + stimuli_idx + " sub_index:" + sub_index );
    get_request("/play/" + stimuli_idx + "/" + sub_index);
    setTimeout(
      ()=> {
        document.getElementById("rating_template").style.display = "block";
      },
      2000  // 1 second delay to show the main rating form
    );
  }

  //play("{{stimuli_idx}}", "ref");
</script>

<div class="row" id="rating_template" style="padding-top: 1em;">
% include('templates/' + rating_template, stimuli_idx=stimuli_idx, stimuli_file=stimuli_file, train=get("train", False), question=question)
</div>

% include('templates/progress_bar.tpl', stimuli_done=stimuli_done, stimuli_count=stimuli_count)

