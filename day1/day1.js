function twosum(arr) {
    let tmp = {};

    for (let i=0; i<arr.length; i++) {
        let targetVal = 2020 - arr[i];
        tmp[targetVal] = arr[i];
    };

    for (let i=0; i<arr.length; i++) {
        if (tmp[arr[i]]) {
            return arr[i] * tmp[arr[i]];
        };
    };
};

function threesum(arr) {
    let sortedArr = arr.sort((a,b) => a-b);

    for (let left=0; left<arr.length - 2; left++) {
        let mid = left + 1;
        let right = arr.length - 1;

        while (mid < right) {
            let sum = arr[left] + arr[mid] + arr[right];

            if (sum === 2020) {
                return arr[left] * arr[mid] * arr[right];
            };

            if (sum < 2020) {
                mid++;
            } else if (sum > 2020) {
                right--;
            }
        };
    };

    return null;
};
