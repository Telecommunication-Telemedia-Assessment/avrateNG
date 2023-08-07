<div class="col-12" id="ratingform" >

<h5>{{question}}</h5>
<style type="text/css">
    input[type=range][orient=vertical] {
        writing-mode: bt-lr; /* IE */
        -webkit-appearance: slider-vertical; /* Chromium */
        width: 8px;
        height: 175px;
        padding: 0 5px;
    }
    .slider-container {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 10px;
      text-align: center;
      margin-top: 50px;
    }

    .slider-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .slider-wrapper {
      position: relative;
    }

    .slider-content {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .slider-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .slider-value {
        display: block;
        font-size: 24px;
        margin-top: 10px;
    }
</style>

  % route = f"save_rating?stimuli_idx={stimuli_idx}" if not train else "training/" + str(stimuli_idx + 1)
  <form id="form1" action="/{{route}}" method="post">
    <div class="slider-container">
            <div class="slider-item">
                <div class="slider-wrapper">
                    <button class="play-button btn btn-warning" type="button" onclick="play({{stimuli_idx}}, 'ref')">ref</button>
                    <div class="slider-content">
                        <input type="range" orient="vertical" min="0" max="100" step="1" value="50" class="slider" id="slider_ref" oninput="sliderChange(this)" name="slider_ref" />
                        <span class="slider-value">50</span>
                    </div>
                </div>
            </div>
            <%
            import random
            variants = ["fps24", "fps30", "fps40", "fps60", "fps120"]
            random.shuffle(variants)
            %>
            % for i, v in enumerate(["S1", "S2", "S3", "S4", "S5"]):
            <div class="slider-item">
                <div class="slider-wrapper">
                    <button class="play-button btn btn-primary" type="button" onclick="play({{stimuli_idx}}, '{{variants[i]}}')">{{v}}</button>
                    <div class="slider-content">
                        <input type="range" orient="vertical" min="0" max="100" step="1" value="50" class="slider" id="slider_{{variants[i]}}" oninput="sliderChange(this)" name="slider_{{variants[i]}}" />
                        <span class="slider-value">50</span>
                    </div>
                </div>
            </div>
            % end


        </div>

    % include('templates/rating/common.tpl', stimuli_file=stimuli_file)

    <button type="submit" id="submitButton" class="btn btn-success btn-block" onclick="check_form(event)" disabled>submit</button>


  </form>
</div>



<script>
    var slidersChanged = {};
    // initialize sliders
    for (const slider of document.querySelectorAll('input.slider')) {
        slidersChanged[slider.getAttribute("name")] = 0;
    }

    function sliderChange(slider) {
        slidersChanged[slider.getAttribute("name")] = 1;
        var check = Object.values(slidersChanged).every(e => e > 0);

        if (check) {
            document.getElementById("submitButton").disabled = false;
        }
    }

    const sliders = document.querySelectorAll(".slider");
    const sliderValues = document.querySelectorAll(".slider-value");

    sliders.forEach((slider, index) => {
      slider.addEventListener("input", function() {
        sliderValues[index].textContent = slider.value;
      });
    });
</script>
