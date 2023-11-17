#include <vector>

class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        std::vector<int> tmp(nums1.begin(), nums1.begin() + m); // Copy the first m elements of nums1 to tmp
        int i = 0; // Index for tmp
        int j = 0; // Index for nums2
        int k = 0; // Index for nums1

        while (i < m && j < n) {
            if (tmp[i] <= nums2[j]) {
                nums1[k] = tmp[i];
                i++;
            } else {
                nums1[k] = nums2[j];
                j++;
            }
            k++;
        }

        // Copy the remaining elements from tmp or nums2 if any
        while (i < m) {
            nums1[k] = tmp[i];
            i++;
            k++;
        }

        while (j < n) {
            nums1[k] = nums2[j];
            j++;
            k++;
        }
    }
};
