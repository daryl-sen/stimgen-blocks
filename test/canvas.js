var canvas = document.getElementById("canvas");

var c = canvas.getContext('2d');


// create black background
c.fillStyle = "gray";
c.fillRect(0,0,900,500);

c.fillStyle = "green";
c.fillRect(10,5,870,480);

// c.fillStyle = "red";
// c.fillRect();

createGrid(900/3,900/3,900,500/5,500/5,500,"red");













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
