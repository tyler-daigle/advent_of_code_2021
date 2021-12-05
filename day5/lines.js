function getLineSegmentPoints(startPoint, endPoint) {
  // for first part calculating slope seems pointless
  // there are only vertical and horizontal lines
  // so if x1 == x2 it is a vertical line - x doesn't change
  // if y1 == y2 it is a horizontal line - y doesn't change

  let xDelta, yDelta; // how much each point moves
  let numPoints = 0;

  if (startPoint.x === endPoint.x) {
    // x stays the same - vertical line - going up

    if (startPoint.y > endPoint.y) {
      let temp = startPoint;
      startPoint = endPoint;
      endPoint = temp;
    }

    xDelta = 0;
    yDelta = 1;
    numPoints = Math.abs(endPoint.y - startPoint.y);
  } else if (startPoint.y === endPoint.y) {
    // y stays the same - horizontal line - going right

    if (startPoint.x > endPoint.x) {
      let temp = startPoint;
      startPoint = endPoint;
      endPoint = temp;
    }

    xDelta = 1;
    yDelta = 0;
    numPoints = Math.abs(endPoint.x - startPoint.x);
  } else {
    // throw "Something is wrong - not horizontal or vertical line";
    // point doesn't matter?
    // return;
    xDelta = yDelta = 1;
    if (startPoint.x > endPoint.x) {
      xDelta = -1;
    } else {
      xDelta = 1;
    }
    if (startPoint.y > endPoint.y) {
      yDelta = -1;
    } else {
      yDelta = 1;
    }
    numPoints = Math.abs(endPoint.x - startPoint.x);
  }

  const points = [{ ...startPoint }];
  let x = xDelta;
  let y = yDelta;

  for (let i = 0; i < numPoints - 1; i++) {
    const pt = { x: startPoint.x + x, y: startPoint.y + y };
    x += xDelta;
    y += yDelta;
    points.push(pt);
  }
  points.push({ ...endPoint });

  return points;
}

function convertStringToPoint(pointString) {
  const [x, y] = pointString.split(",");
  return { x: parseInt(x), y: parseInt(y) };
}

// convert the point object to a string - there is no space between x,y
function convertPointToString(point) {
  return `${point.x},${point.y}`;
}

function calcSlope(point1, point2) {
  // for this challenge it seems like everything is either 0 or 1
  const deltaX = point1.x - point2.x;
  const deltaY = point1.y - point2.y;

  if (deltaY === 0) {
    return 0;
  }

  return Math.abs(deltaX / deltaY);
}

function plotPoint(point, grid) {
  // convert the point to a string
  // add it to the grid and see if something is already there
  // if something is already there add 1 to it, otherwise just
  // set it to 1 the first time the point is plotted
  const pStr = convertPointToString(point);
  if (pStr in grid) {
    grid[pStr] += 1;
  } else {
    grid[pStr] = 1;
  }
  return grid;
}

module.exports = {
  getLineSegmentPoints,
  convertStringToPoint,
  convertPointToString,
  calcSlope,
  plotPoint,
};
