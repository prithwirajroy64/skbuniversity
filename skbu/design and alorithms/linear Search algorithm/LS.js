function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
      return i;
    }
  }
  return -1;
}

const arr = [2, 4, 5, 1, 7, 32, 21];
const target = 7;

const result = linearSearch(arr, target);
if (result != -1) {
  console.log(`Element found at index: ${result}`);
} else {
  console.log(`Element not found.`);
}
