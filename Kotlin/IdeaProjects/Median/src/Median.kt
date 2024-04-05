class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        val n = nums1.size
        val m = nums2.size
        val ans = DoubleArray(n+m)
        var i = 0
        var j = 0
        var index = 0
        while(i < n && j< m){
            if(nums1[i] < nums2[j]){
                ans[index++] = nums1[i++].toDouble()
            } else {
                ans[index++] = nums2[j++].toDouble()
            }
        }

        while(i < n) ans[index++] = nums1[i++].toDouble()
        while(j < m) ans[index++] = nums2[j++].toDouble()
        val mid = (n+m)/2

        if ((n+m) %2 ==0){
            return (ans[mid] + ans[mid-1])/2.0
        }

        return ans[mid]
    }
}
//https://leetcode.com/problems/median-of-two-sorted-arrays/