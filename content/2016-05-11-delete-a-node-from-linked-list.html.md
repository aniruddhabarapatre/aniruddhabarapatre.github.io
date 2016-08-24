---
title: Delete a node from Linked List
date: 2016-05-11 08:18 EDT
tags: CS, Data structures, Linked List
Category: Blog
---

*Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.*

We can traverse the list from the beginning until we encounter the node to delete. But in this situation, we don't know where the head of the list is, we only have a reference to the node to delete.

The usual way of deleting a node node from a linked list is to modify the next pointer of the node before it, to point to the node after it.

So we take the `@value` and `@next` from the input node's next node and copy them into the input node. Now the input node's previous node effectively skips the input node's old value!

```ruby
# Time complexity: O(1)
# Space complexity: O(1)

def delete_node(node_to_delete)
  # Getting next node which we want to move to
  next_node = node_to_delete.next

  if next_node
    # Replace value and pointer with next_node's value
    # and pointer
    node_to_delete.value = next_node.value
    node_to_delete.next = next_node.next

  else
    raise "Can't delete the last node."
  end
end
```
