const fs = require("fs");

class LanternFish {
  constructor(initialTimer = 8) {
    this.timer = initialTimer;
  }

  tick(newFishHandler) {
    if (this.timer === 0) {
      newFishHandler();
      this.timer = 6;
    } else {
      this.timer--;
    }
  }
}

function loadData(dataFile) {
  return new Promise((resolve, reject) => {
    fs.readFile(dataFile, "utf-8", (err, data) => {
      if (err) {
        console.log(err);
        reject(err);
      } else {
        const fishData = data.split(",").map((fish) => parseInt(fish));
        resolve(fishData);
      }
    });
  });
}

(async function () {
  const schoolData = await loadData("data.txt");
  const school = Array(9).fill(0);

  schoolData.forEach((fish) => school[fish]++);
  console.log(school);
  const numDays = 256;

  for (let day = 0; day < numDays; day++) {
    console.log(`Day: ${day}`);
    let numNewFish = school[0];
    school.push(numNewFish);
    school.shift();
    school[6] += numNewFish;
  }

  const numFish = school.reduce((acc, curr) => acc + curr);
  console.log(numFish);

  // console.log(schoolData.length);
  // const school = schoolData.map((fishTimer) => new LanternFish(fishTimer));

  // const newFishHandler = () => {
  //   school.push(new LanternFish(8));
  // };
  // const numDays = 256;
  // for (let i = 0; i < numDays; i++) {
  //   console.log(`Day ${i}`);
  //   school.forEach((fish) => fish.tick(newFishHandler));
  // }
  // console.log(school.length);
})();
