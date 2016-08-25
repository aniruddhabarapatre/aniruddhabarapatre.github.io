---
title: Matrix Spiral Print
date: 2016-05-11 21:46 EDT
tags: CS, Data structures, Array
Category: Blog
---

*Given a 2D array (matrix), print all elements in a clockwise (spiral) manner*

```ruby
# Time complexity: O(n*m)
# Space complexity: O(1)

def matrix_spiral matx
  topRow = 0
  btmRow = m-1
  leftCol = 0
  rightCol = n-1

  while (topRow <= btmRow && leftCol <= rightCol):
    # print the next top row
    (leftCol..rightCol).each do |i|
      print matx[topRow][i]
    end
    topRow++

    # print the next right hand side column
    (topRow..btmRow).each do |i|
      print matx[i][rightCol]
    end
    rightCol--

    # print the next bottom row
    if (topRow <= btmRow)
      (rightCol..leftCol).each do |i|
        print matx[btmRow][i]
      end
      btmRow--
    end

    # print the next left hand side column
    if (leftCol <= rightCol)
      (btmRow..topRow).each do |i|
        print matx[i][leftCol]
      end
      leftCol++
    end
  end
end
```
