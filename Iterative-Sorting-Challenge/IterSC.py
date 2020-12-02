def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because it can loop through all items in the list
    Memory usage: O(1) Only declares a single counter variable
    """
    i = 1
    while i < len(items):

        if items[i] < items[i - 1]:
            return False
        i += 1
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n**2) because it passes through n/2 (on average) elements
        n-1 times, which simplifies to n elements n times, n**2
    Memory usage: O(1), as only a boolean and two integers are declared
    """
    for k in range(len(items) - 1):

        swapped = False

        for i in range(len(items) - 1 - j):

            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True

        if not swapped:
            return items
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n**2) As it loops through the whole array for each element
    Memory usage: O(1) Sorting is done in place on the array
    """
    for i in range(len(items)):

        ind = items.index(min(items[i:]), i)

        items[ind], items[i] = items[i], items[ind]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n**2) It can iterate through all elements on each loop
    Memory usage: O(1) Sorting is done in place, only ints declared
    """
    for i in range(1, len(items)):

        k = i
        while items[k] < items[k - 1] and k > 0:
            items[k], items[k - 1] = items[k - 1], items[k]
            k -= 1
    return items