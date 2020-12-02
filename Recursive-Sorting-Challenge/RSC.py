def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order."""
    result = []
    i1, i2 = 0, 0
    while i1 < len(items1) and i2 < len(items2):
        if items1[i1] < items2[i2]:
            result.append(items1[i1])
            i1 += 1
        else:
            result.append(items2[i2])
            i2 += 1
    if i1 == len(items1):
        result.extend(items2[i2:])
    else:
        result.extend(items1[i1:])
    return result


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order."""
    if len(items) < 2:
        return items

    mid = len(items) // 2

    left = items[:mid]
    right = items[mid:]

    items[:] = merge(merge_sort(left), merge_sort(right))
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot"""
    i = (low-1)
    pivot = items[high]

    for j in range(low, high):

        if items[j] <= pivot:

            i = i+1
            items[i], items[j] = items[j], items[i]

    items[i+1], items[high] = items[high], items[i+1]
    return (i+1)


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range."""
    if len(items) == 1:
        return items
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1

    if low < high:

        pi = partition(items, low, high)

        quick_sort(items, low, pi-1)
        quick_sort(items, pi+1, high)
    return items