

var validData = { // Define valid options here
1:["1", "one", "eins", "very poor"],
2:["2", "two", "zwei", "poor"],
3:["3", "three", "drei", "fair"],
4:["4", "four", "vier", "good"],
5:["5", "five", "fünf", "excellent"],
}

var recognizing = false;
var ignore_onend = true;
talk('Please rate the watched video by saying your answer out loud!')
setTimeout(listen,3000) // Wait until instructions are said

function listen(){ // main function

    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'de';
    recognition.interimResults = false;
    recognition.maxAlternatives = 5;
    recognition.start();
    recognizing = true;

    recognition.onstart = function() {
        recognizing = true;
    }

    recognition.onresult = function(event) { //the event holds the results
        capture = event["results"]["0"]["0"]["transcript"];
        console.log("Captured speech:", capture);

        if (checkCapture(capture)==''){ // Check if capture is not a valid response
            capture = null; // Delete old capture
            talk("Please choose a valid option!");
            return;
            }
        else { // Valid response recognized
            var result = checkCapture(capture) // check for validity and get valid response format
            console.log("Capture is valid. Chosen option is: ", result)
            ignore_onend = false;
            recognition.stop();
            submit_capture(result); // send to server side
        }
    };

    recognition.onend = function(){

        recognizing = false;
        if (ignore_onend) {
            console.log('ignore_end triggered. Listening...')
            listen();
            return;
        }
        else {
            console.log('Recognition stopped')
            
        }
    };

  recognition.onerror = function(event) {
    if (event.error == 'no-speech') {
      
      console.log('info_no_speech');
      ignore_onend = true;
    }
    if (event.error == 'audio-capture') {
      console.log('info_no_microphone');
      ignore_onend = true;
    }
    if (event.error == 'not-allowed') {
      console.log('not-allowed error')
      ignore_onend = true;
    }
  };

};




function talk(text){ // Define what should be said or done when speech could not be recognized properly
    var synth = window.speechSynthesis;
    msg = new SpeechSynthesisUtterance(text);
    msg.lang = 'en-US';
    synth.speak(msg);
}

function checkCapture(capture){ // Check if recognized speech is valid (defined in validData object)
    options = Object.keys(validData);
    matching_Idx = '';
    for (var i in options){
        option = options[i];
        if (validData[option].indexOf(capture.toLowerCase())>=0){
            matching_Idx = option;
            return matching_Idx};
    };
    return matching_Idx
}

function submit_capture(data){ // Give voice feedback over chosen option and submit
    talk("Your answer is:" + data + ". Going to next video...");

    document.getElementById("radio"+data).checked=true;
    document.getElementById("voice").disabled = false; // Only submit value when recognized, else: click button
    setTimeout(function(){document.getElementById("form1").submit();
                          $("#playback").show();
                          $("#content").hide();},3000) // Wait 3s until feedback was given

}

