var canvas = document.getElementById("canvas");

var c = canvas.getContext('2d');


// create black background
c.fillStyle = "black";
c.fillRect(0,0,1280,1024);



// needed variables

// var stim_width
// var stim_height
// var half_width
// var canvas_padding
// var xpos_restriction
// var ypos_restriction
// var pos_variance
// var colors


// create first stim
  // left half
  c.fillStyle = "red";
  c.fillRect(100, 245, 150, 50);
  // right half
  c.fillStyle = "blue";
  c.fillRect(250, 245, 150, 50); // x pos is x pos from left half + half_width

// create second stim
  // left half
  c.fillStyle = "blue";
  c.fillRect(132, 421, 150, 50);
  // right half
  c.fillStyle = "green";
  c.fillRect(282, 421, 150, 50);

// create second stim
  // left half
  c.fillStyle = "yellow";
  c.fillRect(76, 576, 150, 50);
  // right half
  c.fillStyle = "red";
  c.fillRect(226, 576, 150, 50);











createGrid(1200/3,1200/3,1200,1024/5,1024/5,1024,"white");

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

// var img = canvas.toDataURL("image/png");
// document.write('<img src="'+img+'"/>');
