const fs = require("fs");
const {
  convertStringToPoint,
  getLineSegmentPoints,
  plotPoint,
} = require("./lines");

function readData(dataFile) {
  return new Promise((resolve, reject) => {
    fs.readFile(dataFile, "utf-8", (err, data) => {
      if (err) {
        reject(err.message);
      }
      const lineData = data.split("\n");
      resolve(lineData);
    });
  });
}

(async function () {
  const data = await readData("./data.txt");
  const grid = {};
  const allPoints = [];

  data.forEach((line) => {
    const [start, end] = line.split("->");
    const startPoint = convertStringToPoint(start);
    const endPoint = convertStringToPoint(end);
    const points = getLineSegmentPoints(startPoint, endPoint);
    if (points) {
      // don't add any lines that aren't vertical or horizontal
      allPoints.push(...points);
    }
  });

  // console.log(allPoints);
  allPoints.forEach((point) => plotPoint(point, grid));
  let numIntersections = 0;

  Object.keys(grid).forEach((p) => {
    if (grid[p] >= 2) {
      numIntersections += 1;
    }
  });
  console.log(numIntersections);
})();
