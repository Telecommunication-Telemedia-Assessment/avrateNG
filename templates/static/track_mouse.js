
var time = 100; // set update time in ms
var cursorX;
var cursorY;
var position = {
    posX: [],
    posY:[]
    };
document.onmousemove = function(e){
    cursorX = e.pageX;
    cursorY = e.pageY;
}
setInterval(checkCursor, time);
function checkCursor(){
    position.posX.push(cursorX);
    position.posY.push(cursorY);

}

function log_position(){
    var pos_string = JSON.stringify(position);
    document.getElementById("mouse_track").value = pos_string;

}


