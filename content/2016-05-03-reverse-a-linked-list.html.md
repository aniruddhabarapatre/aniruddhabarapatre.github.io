---
title: Reverse a Linked List
date: 2016-05-03 18:58 EDT
tags: CS, Data structures, Linked List
Category: Blog
---

Algorithm and Data structures have been one of my weak point for quite some time now. And after working for more than 6 years a lot of these are forgotten. Past few days have been brushing up my skills and will be documenting here.

Starting with Linked list, here's how to reverse a linked list.

Assume that we have linked list 1 → 2 → 3, we would like to change it to 1 ← 2 ← 3.

A simpler way to come up with solution is by iterative way. We can traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!

```ruby
# Time complexity: O(n)
# Space complexity: O(1)

def reverse(head_of_list)
  current = head_of_list
  previous = nil
  next_node = nil

  # until we have 'fallen off' the end of the list
  while current

    # copy a pointer to the next element
    # before we overwrite current.next
    next_node = current.next

    # reverse the 'next' pointer
    current.next = previous

    # step forward in the list
    previous = current
    current = next_node
  end

  return previous
end
```
