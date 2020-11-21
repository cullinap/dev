package main

import (
    "fmt"

)

func main() {

    var k = 2
    centroids := make(map[int]int)
    var X = [6][2]int {{1,2}, {1,8}, {5,8}, {8,8}, {1,1}, {9,11}}

    // assign first two values of X to centroids
    for i := 0; i < k; i++ {
        centroids[i] = {i,i}
    }

    for key, value := range centroids {
        fmt.Println("key:", key, "value: ", value)
    }
}
