def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Where k is the maximum value, because it loops over a list of n size and one of k size
    Memory usage: O(k) Because it declares an array of size k
    """
    count_list = []

    for num in numbers:
        if len(count_list) < num + 1:
            count_list.extend([0] * (num - len(count_list) + 1))

        count_list[num] += 1

    numbers[:] = []

    for i, v in enumerate(count_list):
        numbers.extend([i] * v)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n+k) where k is the number of buckets, as it loops over each element and each bucket
    Memory usage: O(n+k) as it declares buckets and adds each element to them
    """

    if len(numbers) == 0:
        return


    max_value = max(numbers)
    buckets = [[] * num_buckets]
    print(buckets)


    for num in numbers:
        print(num)
        print(buckets)
        buckets[num * len(buckets) // (max_value + 1)].append(num)

    print(buckets)

    numbers[:] = []

    for bucket in buckets:
        if len(bucket) > 0:
            counting_sort(bucket)
            numbers.extend(bucket)