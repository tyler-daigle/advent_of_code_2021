const {
  getLineSegmentPoints,
  convertPointToString,
  convertStringToPoint,
  calcSlope,
  plotPoint,
} = require("../lines");

test("getLineSegmentPoints() should return the correct points for 0,9 -> 5,9 - A horizontal line.", () => {
  const testPoints = ["0,9", "1,9", "2,9", "3,9", "4,9", "5,9"];
  const actualPoints = testPoints.map((p) => convertStringToPoint(p));
  const points = getLineSegmentPoints({ x: 0, y: 9 }, { x: 5, y: 9 });

  expect(points).toEqual(actualPoints);
});

// test("Test 8,0 -> 0,8", () => {
//   const testPoints = ["0,9", "1,9", "2,9", "3,9", "4,9", "5,9"];
//   const actualPoints = testPoints.map((p) => convertStringToPoint(p));
//   const points = getLineSegmentPoints({ x: 0, y: 9 }, { x: 5, y: 9 });

//   expect(points).toEqual(actualPoints);
// });

test("Get the points for a vertical line", () => {
  const testPoints = ["7,0", "7,1", "7,2", "7,3", "7,4"];
  const actualPoints = testPoints.map((p) => convertStringToPoint(p));
  const points = getLineSegmentPoints({ x: 7, y: 0 }, { x: 7, y: 4 });
  expect(points).toEqual(actualPoints);
});

test("calcSlope() of (0,9) and (5,9) should return 0", () => {
  const slope = calcSlope({ x: 0, y: 9 }, { x: 5, y: 9 });
  expect(slope).toBe(0);
});

test("calcSlope() of 8,0 and 0,8 should be 1", () => {
  expect(calcSlope({ x: 8, y: 0 }, { x: 0, y: 8 })).toBe(1);
});

test('convertStringToPoint() should convert "0,9" to a point object', () => {
  const pt = convertStringToPoint("0,9");
  expect(pt).toEqual({ x: 0, y: 9 });
});

test('convertPointToString should convert {x: 1, y:1} to "1,1"', () => {
  const st = convertPointToString({ x: 1, y: 1 });
  expect(st).toBe("1,1");
});

test("Plotting Points {x:0,y:0} twice and making sure it is marked twice", () => {
  const grid = {};
  const point = { x: 0, y: 0 };
  plotPoint(point, grid);
  plotPoint(point, grid);

  const pStr = convertPointToString(point);
  expect(grid[pStr]).toEqual(2);
});
