class Solution {
    fun countAndSay(n: Int): String {
        fun next(s: String): String {

            var res = ""
            var count: Int
            var i = 0
            while (i<s.length) {
                count = 1
                while (i+1<s.length && s[i]==s[i+1]) {
                    i++
                    count++
                }
                res += "$count${s[i++]}"
            }
            return res
        }
        return generateSequence("1", ::next).take(n).last()

    }
}

//https://leetcode.com/problems/count-and-say/