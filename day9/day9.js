const fs = require("fs");

function readData(dataFile) {
  const data = fs.readFileSync(dataFile, "utf-8").split("\n");
  const heightMap = data.map((row) =>
    row.split("").map((num) => parseInt(num))
  );
  return heightMap;
}

function calcAdjacentValues(heightMap, point) {
  const { row, col } = point;
  let up, down, left, right;

  // check up
  if (row > 0) {
    up = getHeightMapValue(heightMap, { row: row - 1, col });
  } else {
    up = Infinity;
  }

  // down
  if (row < heightMap.length - 1) {
    down = getHeightMapValue(heightMap, { row: row + 1, col });
  } else {
    down = Infinity;
  }

  // left
  if (col > 0) {
    left = getHeightMapValue(heightMap, { row, col: col - 1 });
  } else {
    left = Infinity;
  }

  // right
  if (col < heightMap[0].length) {
    right = getHeightMapValue(heightMap, { row, col: col + 1 });
  } else {
    right = Infinity;
  }

  return { up, down, left, right };
}

function getHeightMapValue(heightMap, point) {
  // console.log(point.row, point.col);
  const { row, col } = point;
  return heightMap[row][col];
}

function checkForLowest(heightMap, point) {
  const val = heightMap[point.row][point.col]; // the actual point value
  const around = calcAdjacentValues(heightMap, point);

  // check if val is less than all the surrounding points
  if (
    val >= around.up ||
    val >= around.down ||
    val >= around.left ||
    val >= around.right
  ) {
    return false;
  }
  return true;
}

const heightMap = readData("data.txt");
const numCols = heightMap[0].length;
const numRows = heightMap.length;

// console.log(heightMap);
// console.log(numRows, numCols);

// const d = calcAdjacentValues(heightMap, { row: 0, col: 0 });
// console.log(d);
let sum = 0;

for (let row = 0; row < numRows; row++) {
  for (let col = 0; col < numCols; col++) {
    if (checkForLowest(heightMap, { row, col })) {
      sum += heightMap[row][col] + 1;
    }
  }
}
console.log(sum);
