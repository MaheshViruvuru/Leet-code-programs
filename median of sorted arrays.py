def median_of_sorted_arrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
    n = len(nums1)
    if n % 2 == 0:
        median = (nums1[int(n / 2)] + nums1[int(n / 2) - 1]) / 2
        print(median)
    else:
        median = nums1[n // 2]
        print(median)


nums1 = [1, 2]
nums2 = [3, 4]
median_of_sorted_arrays(nums1, nums2)