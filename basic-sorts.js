function bubbleSort(array) {
  let swaps;
  while (swaps !== 0) {
    swaps = 0;
    for (let i = 0; i < array.length; i++) {
      if (array[i] > array[i + 1]) {
        let element1 = array[i];
        let element2 = array[i + 1];
        array[i] = element2;
        array[i + 1] = element1;
        swaps += 1;
        console.log(array);
      }
    }
  }
  return array;
}

console.log(bubbleSort([2, 1, 3, 24, 100, 6, 88, 13]));
