---
title: Merge two sorted lists
date: 2016-07-01 21:36 EDT
tags: CS, Data structures, Linked List
Category: Blog
---

*Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.*

For this we create a dummy head before the new list so that we don't have to deal with cases for initializing head of new list. Then new list's head could be returned as dummy head's next node.

```ruby
# Time complexity: O(n)

def merge_two_lists(l1, l2)
  dummyhead = Node.new(0)
  p = dummyhead

  while(!l1.nil? && !l2.nil?)
    if (l1.val < l2.val)
      p.next = l1
      l1 = l1.next
    else
      p.next = l2
      l2 = l2.next
    end
    p = p.next
  end

  if (!l1.nil?)
    p.next = l1
  end

  if (!l2.nil?)
    p.next = l2
  end
  dummyhead.next
end
```
