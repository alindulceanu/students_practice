//https://leetcode.com/problems/isomorphic-strings/description/?envType=daily-question&envId=2024-04-02
// Runtime: Beats 93.08% of users with kotlin
// Memory: 36.29 MB beats 99.69% of users with kotlin
class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        var chrList = hashMapOf<Char, Char>()

        for (i in 0..s.length - 1) {
            if (chrList.containsKey(t[i])) {
                if (chrList.get(t[i]) != s[i]) {
                    return false
                }
            } else if(chrList.containsValue(s[i])){
                return false
            }
            else{
                chrList[t[i]] = s[i]
            }
        }
        return true
    }
}

fun main() {
    val xd = Solution()

    print(xd.isIsomorphic("foo", "bar"))
}

