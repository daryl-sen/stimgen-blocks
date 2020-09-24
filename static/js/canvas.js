var canvas1 = document.getElementById("canvas1");
canvas1.width = 1280;
canvas1.height = 1024;

var c = canvas1.getContext('2d');





var canvas2 = document.getElementById("canvas2");
canvas2.width = 1280;
canvas2.height = 1024;

var c2 = canvas2.getContext('2d');







// create black background
c.fillStyle = "black";
c.fillRect(0,0,canvas1.width,canvas1.height);

c2.fillStyle = "black";
c2.fillRect(0,0,canvas2.width,canvas2.height);

// show grid
// createGrid(canvas1.width/4,canvas1.width/4,canvas1.width,canvas1.height/4,canvas1.height/4,canvas1.height,"gray");

// show fixation cross
var hfc_width = 100;
var hfc_height = 15;
var vfc_width = 15;
var vfc_height = 100;

c.fillStyle = "white";
hfc_xpos = Math.floor((canvas1.width - hfc_width)/2);
hfc_ypos = Math.floor((canvas1.height - hfc_height)/2);

vfc_xpos = Math.floor((canvas1.width - vfc_width)/2);
vfc_ypos = Math.floor((canvas1.height - vfc_height)/2);

c.fillRect(hfc_xpos, hfc_ypos, hfc_width, hfc_height);
c.fillRect(vfc_xpos, vfc_ypos, vfc_width, vfc_height);

c2.fillStyle = "white";
c2.fillRect(hfc_xpos, hfc_ypos, hfc_width, hfc_height);
c2.fillRect(vfc_xpos, vfc_ypos, vfc_width, vfc_height);












function createGrid(x_start, x_increments, x_max, y_start, y_increments, y_max, grid_color)
{  // Create grid
  var x_start = x_start;
  var x_increments = x_increments;
  var x_max = x_max;

  var y_start = y_start;
  var y_increments = y_increments;
  var y_max = y_max;

  var grid_color = grid_color;
  c.strokeStyle = grid_color;

  // create x grid
  c.beginPath();
  for (var x_pos = x_start; x_pos < x_max; x_pos = x_pos + x_increments)
  {
    c.moveTo(x_pos,0);
    c.lineTo(x_pos,y_max);
  }
  c.stroke();

  // create y grid
  c.beginPath();
  for (var y_pos = y_start; y_pos < y_max; y_pos = y_pos + y_increments)
  {
    c.moveTo(0,y_pos);
    c.lineTo(x_max,y_pos);
  }
  c.stroke();
}

// var img = canvas1.toDataURL("image/png");
// document.write('<img src="'+img+'"/>');
