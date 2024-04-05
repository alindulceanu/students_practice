class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var maxLength = 0
        var start = 0
        val charIndexMap = mutableMapOf<Char, Int>()

        for (end in s.indices) {
            val currentChar = s[end]
            if (charIndexMap.containsKey(currentChar)) {
                start = maxOf(start, charIndexMap[currentChar]!! + 1)
            }
            charIndexMap[currentChar] = end
            maxLength = maxOf(maxLength, end - start + 1)
        }
        return maxLength
    }
}

//https://leetcode.com/problems/longest-substring-without-repeating-characters/