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

const arr = [1, 2, 4, 6, 7, 8, 11, 13, 16, 23];
const target = 11;
const result = binarySearch(arr, target);

console.log(arr);

if (result != -1) {
  console.log(`Element found at index: ${result}`);
} else {
  console.log(`Element not found.`);
}
