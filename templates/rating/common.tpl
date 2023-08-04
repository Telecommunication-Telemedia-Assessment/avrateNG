    <input type="hidden" value="{{stimuli_file}}" id="stimuli_file" name="stimuli_file" />
    <input type="hidden" value="{{stimuli_idx}}" id="stimuli_idx" name="stimuli_idx" />

    <input type="hidden" value="-1" id="ww" name="ww" /> <!-- window width while playing -->
    <input type="hidden" value="-1" id="wh" name="wh" /> <!-- window height while playing -->
    <input type="hidden" value="-1" id="wz" name="wz" /> <!-- window zoom factor while playing -->
    <input type="hidden" value="-1" id="start_timestamp" name="start_timestamp" /> <!-- when was the page rendered -->
    <input type="hidden" value="1" id="pi" name="pi" /> <!-- play iterations (counter how often the play button was hit) -->

<script type="text/javascript">

function page_loaded() {
    var timestamp = new Date().toUTCString();
    document.getElementById("start_timestamp").value = timestamp;
}

page_loaded();
</script>