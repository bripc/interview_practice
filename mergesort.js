(function () {
    'use strict';
    print("Yay mergesort!");
    
    var items = [9, 3, 4, 0, 2, 1, 5, 8];
    print("Items before sort:", items);
    
    function mergeLists(left, right) {
        var sorted = [];
        
        while (left.length && right.length) {
            if (left[0] <= right[0]) {
                sorted.push(left.shift());
            } else {
                sorted.push(right.shift());
            }
        }
        
        // we know the mini lists are already sorted so we are just appending them
        while (left.length) {
            sorted.push(left.shift());
        }
        while (right.length) {
            sorted.push(right.shift());
        }
        return sorted;
    }
    
    function mergesort(list) {
        // if the list is now one item
        if (list.length === 1) {
            return list;
        }
        var middle = Math.floor(list.length / 2),
            left = list.slice(0, middle),
            right = list.slice(middle, list.length);
        left = mergesort(left);
        right = mergesort(right);
        
        return mergeLists(left, right);
    }
    
    print("Final sort:", mergesort(items));
}());
