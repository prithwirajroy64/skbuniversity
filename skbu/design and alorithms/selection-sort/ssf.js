const fs = require("fs");

function selectionSort(arr) {
  let n = arr.length;

  for (let i = 0; i < n; i++) {
    let min = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    if (i !== min) {
      let temp = arr[i];
      arr[i] = arr[min];
      arr[min] = temp;
    }
  }
  return arr;
}

fs.readFile("data.txt", "utf-8", (err, data) => {
  if (err) {
    console.error("Error reading files: ", err);
    return;
  }
  const arr = data.split("\n").map(Number);
  console.log("Sorted array: ", selectionSort(arr));
});
