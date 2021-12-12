function setSquare(segment, squareNum, status) {
  const square = segment.getElementsByClassName("grid-square")[squareNum];
  if (status === "on") {
    square.classList.remove("segment-off");
    square.classList.add("segment-on");
  } else {
    square.classList.remove("segment-on");
    square.classList.add("segment-off");
  }
}

function createGrid(width = 6, height = 7) {
  const table = document.createElement("table");
  for (let row = 0; row < height; row++) {
    const tr = document.createElement("tr");
    tr.classList.add("grid-row");
    table.appendChild(tr);
    for (let col = 0; col < width; col++) {
      const td = document.createElement("td");
      td.classList.add("grid-square");
      // td.innerText = row * width + col;
      td.id = row * width + col;
      tr.appendChild(td);
    }
  }
  return table;
}

function setSegment(segment, segmentChar, status) {
  const segments = {
    a: [1, 2, 3, 4],
    b: [6, 12],
    c: [11, 17],
    d: [19, 20, 21, 22],
    e: [24, 30],
    f: [29, 35],
    g: [37, 38, 39, 40],
  };
  segments[segmentChar].forEach((squareNum) =>
    setSquare(segment, squareNum, status)
  );
}

const grid = document.getElementById("grid");
const numSegments = 4;
const segments = [];
for (let i = 0; i < numSegments; i++) {
  segments.push(createGrid());
}
segments.forEach((segment) => grid.appendChild(segment));

const data = "cdfeb fcadb cdfeb cdbaf".split(" ");
data.forEach((d, index) => {
  d.split("").forEach((char) => {
    setSegment(segments[index], char, "on");
  });
});
// "dab".split("").forEach((ch) => setSegment(segments[0], ch, "on"));
// // setSegment(segments[0], "a", "on");
