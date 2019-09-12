<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="Max" >
    <title>{{title}}</title>
    % include('templates/header.tpl')
    <script>
      // this script is reponsible for engaging the wait screen during playback
      $(document).ready(function(){
        $("#demographics").submit(function(){
          $("#playback").show();
          $("#content").hide();
          $("#footer").hide();
        });
      });
    </script>

    <style>
      .input-group-addon {
        width: 150px;
      }
      .input-group {
        width: 100%;
      }
    </style>
  </head>

<!-- this template contains the text input fields for the demographic user info.
When creating custom forms stick to this structure and add or remove the custom fields.
Don't change the form attributes "action" and "method"-->

  <body>
    <div id="playback"></div>
    <div class="container" id="content">
      <div class="row">
        <h3>Please fill in the following fields before we start:<br><br></h3>
      </div>

      <form id="demographics" action="/save_demographics" method="post">

        <!-- this form was developed by John Dumke and Margaret Pinson -->
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">What is your age?</span>
          <select name="userAgeRange" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="< 18">&lt; 18</option>
            <option value="18 to 24">18 to 24</option>
            <option value="25 to 29">25 to 29</option>
            <option value="30 to 39">30 to 39</option>
            <option value="40 to 49">40 to 49</option>
            <option value="50 to 59">50 to 59</option>
            <option value="60 to 69">60 to 69</option>
            <option value="70+">70+</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">What is your gender?</span>
          <select name="userGender" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">How good is your vision?</span>
          <select name="userEyeQuality" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Excellent(5)">Excellent</option>
            <option value="Good(4)">Good</option>
            <option value="Fair(3)">Fair</option>
            <option value="Poor(2)">Poor</option>
            <option value="Bad(1)">Bad</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">How good is your hearing?</span>
          <select name="userEarQuality" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Excellent(5)">Excellent</option>
            <option value="Good(4)">Good</option>
            <option value="Fair(3)">Fair</option>
            <option value="Poor(2)">Poor</option>
            <option value="Bad(1)">Bad</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">Which option best describes your environment?</span>
          <select name="userRoomQuality" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Alone in a Quiet Room">Alone in a Quiet Room</option>
            <option value="Some Noise and Distractions">Some Noise and Distractions</option>
            <option value="Significant Noise and Distractions">Significant Noise and Distractions</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">What type of device are you now using?</span>
          <select name="userComputerType" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Phone">Phone</option>
            <option value="Tablet">Tablet</option>
            <option value="Laptop">Laptop</option>
            <option value="Desktop">Desktop</option>
          </select>
        </div>
        <br>
        <div class="input-group input-group-lg">
          <span class="input-group-addon" id="sizing-addon2" style="width: 350px; white-space: nowrap; padding-top: 10px;">What are you using to listen to this test?</span>
          <select name="userAudioDevice" class="form-control" required>
            <option value="">&nbsp;</option>
            <option value="Speakers">Speakers</option>
            <option value="Earbuds">Earbuds</option>
            <option value="Headphones">Headphones</option>
          </select>
        </div>
        <br>

        <div class="form-group">
          <textarea class="form-control" rows="5" id="comment" name="comment" placeholder="Comments"></textarea>
        </div>
        <div class="col-lg-2">
          <button type="submit" class="btn-lg btn-success">OK</button>
        </div>
      </form>

      <div class="container" id="footer">
        % include('templates/footer.tpl')
      </div>
    </div>
  </body>
</html>