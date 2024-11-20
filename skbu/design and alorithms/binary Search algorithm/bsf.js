const fs = require("fs");

function binarySearch(arr, target) {
  let l = 0;
  let r = arr.length - 1;

  while (l <= r) {
    let mid = Math.floor((l + r) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      l = mid + 1;
    } else {
      r = mid - 1;
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
  numbers.sort((a, b) => a - b);

  console.log("Numbers from the file:", numbers);
  const target = 77;
  const result = binarySearch(numbers, target);
  if (result != -1) {
    console.log(`Element ${target} found at index: ${result}`);
  } else {
    console.log(`Element not found.`);
  }
});
