const fs = require("fs");

function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;
}

fs.readFile("data.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }
  const numbers = data.split("\n").map(Number);
  console.log("Numbers from the file:", numbers);
  const target = 59;
  const result = linearSearch(numbers, target);
  if (result != -1) {
    console.log(`Element ${target} found at index: ${result}`);
  } else {
    console.log(`Element not found.`);
  }
});
