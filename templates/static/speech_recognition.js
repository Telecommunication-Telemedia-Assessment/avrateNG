

var validData = { // Define valid options here
1:["1", "one", "eins", "very poor"],
2:["2", "two", "zwei", "poor"],
3:["3", "three", "drei", "fair"],
4:["4", "four", "vier", "good"],
5:["5", "five", "fünf", "excellent"],
}


window.onload = function listen(){ // main function
    
    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'de';
    recognition.interimResults = false;
    recognition.maxAlternatives = 5;
    recognition.start();
    

    recognition.onresult = function(event) { //the event holds the results
        if (typeof(event.results) === "undefined") { //Something went wrong…
            console.log("event.results triggert -> Error")
            recognition.stop();
            return;
        }
        else {
            capture = event["results"]["0"]["0"]["transcript"];
            console.log("Captured speech:", capture);
            return capture
        };
    
    }; 

    recognition.onend = function(){ 
        //capture = "good" // Debug: This should be the result from the recognition

        if (typeof(capture) === "undefined" || capture == null){ // No Result from speech recognition -> Try Again!
            synthError(); // Wird etwas oft getriggert...
            listen();
        }
        else{ // Valid Speech was recognized
            if (checkCapture(capture)==''){ // Check if capture is not a valid response
                capture = null; // Delete old capture
                synthError();
                listen();
            }
            else { // Valid response recognized
                var result = checkCapture(capture) // check for validity and get valid response format
                console.log("Capture is valid. Chosen option is: ", result)
                recognition.stop();
                submit_capture(result); // send to server side
            }
            console.log(capture)
            return capture
        };
    };
    
};


function synthError(){ // Define what should be said or done when speech could not be recognized properly
    var synth = window.speechSynthesis;
    msg = new SpeechSynthesisUtterance("Please say that again!");
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
    var synth = window.speechSynthesis;
    msg = new SpeechSynthesisUtterance("Your answer is:" + data + ". Going to next video...");
    msg.lang = 'en-US';
    synth.speak(msg);

    //document.getElementById("voice").value = data; // not really needed, since the buttons get checked
    document.getElementById("radio"+data).checked=true;

    document.getElementById("voice").disabled = false; // Only submit value when recognized, else: click button
    setTimeout(function(){document.getElementById("form1").submit();},4000) // Wait 4s until feedback was given
    
}
 
