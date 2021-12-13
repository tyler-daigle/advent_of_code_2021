const fs = require("fs");

function readData(dataFile) {
  const data = fs.readFileSync(dataFile, "utf-8").split("\n");
  return data;
}

function validateCode(line) {
  const chunks = [];
  const opening = "[({<";
  const expected = { "{": "}", "[": "]", "(": ")", "<": ">" };
  for (let bracket of line) {
    if (opening.includes(bracket)) {
      chunks.push(bracket);
    } else {
      switch (bracket) {
        case "]": {
          const open = chunks.pop();
          if (open !== "[") {
            return { valid: false, found: bracket, expected: expected[open] };
          }
          break;
        }

        case ")": {
          const open = chunks.pop();
          if (open !== "(") {
            return { valid: false, found: bracket, expected: expected[open] };
          }
          break;
        }

        case "}": {
          const open = chunks.pop();
          if (open !== "{") {
            return { valid: false, found: bracket, expected: expected[open] };
          }
          break;
        }

        case ">": {
          const open = chunks.pop();
          if (open !== "<") {
            return { valid: false, found: bracket, expected: expected[open] };
          }
          break;
        }
      }
    }
  }

  return { valid: true };
}

function completeLine(line) {
  const brackets = { "{": "}", "[": "]", "(": ")", "<": ">" };
  const openers = Object.keys(brackets);
  const closers = Object.values(brackets);
  const chunks = [];

  for (let ch of line) {
    if (openers.includes(ch)) {
      chunks.push(ch);
    } else {
      // doesn't matter what the character is since this line is already validated
      chunks.pop();
    }
  }

  let s = "";
  chunks.forEach((bracket) => {
    s += brackets[bracket];
  });

  return s.split("").reverse().join("");
}

function calcScore(errors) {
  let score = 0;

  errors.forEach((error) => {
    switch (error.found) {
      case ")":
        score += 3;
        break;
      case "]":
        score += 57;
        break;
      case "}":
        score += 1197;
        break;
      case ">":
        score += 25137;
        break;
    }
  });

  return score;
}

function calcSecondScore(line) {
  let score = 0;

  for (let ch of line) {
    score *= 5;
    switch (ch) {
      case ")":
        score += 1;
        break;
      case "]":
        score += 2;
        break;
      case "}":
        score += 3;
        break;
      case ">":
        score += 4;
        break;
    }
  }
  return score;
}
const data = readData("data.txt");
const errors = [];
const goodLines = [];
data.forEach((line) => {
  const result = validateCode(line);
  if (result.valid === false) {
    errors.push(result);
  } else {
    goodLines.push(line);
  }
});

const scores = [];
goodLines.forEach((line) => {
  const score = calcSecondScore(completeLine(line));
  scores.push(score);
});

scores.sort((a, b) => {
  if (a < b) return -1;
  if (a > b) return 1;
  return 0;
});

console.log(scores[Math.floor(scores.length / 2)]);

// const secondScore = calcSecondScore(completeLine("[({(<(())[]>[[{[]{<()<>>"));
// console.log(secondScore);

// console.log(`There are ${errors.length} errors.`);
// console.log(calcScore(errors));
