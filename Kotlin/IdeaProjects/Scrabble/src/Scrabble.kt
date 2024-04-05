fun main(){

    var word: String = ""
    println("Insert the word for points! : ")
    word = readLine()!!.toString()
    val list1 = listOf("A","E","I","O","U","L","N","R","S","T")
    val list2 = listOf("D","G")
    val list3 = listOf("B","C","M","P")
    val list4 = listOf("F","H","V","W","Y")
    val list5 = listOf("K")
    val list8 = listOf("J","X")
    val list10 = listOf("Q","Z")
    var result = 0

    for (char in word.toUpperCase()) {
        if (char.toString() in list1) {
            result += 1
        } else if (char.toString() in list2) {
            result += 2
        } else if (char.toString() in list3) {
            result += 3
        } else if (char.toString() in list4) {
            result += 4
        } else if (char.toString() in list5) {
            result += 5
        } else if (char.toString() in list8) {
            result += 8
        } else if (char.toString() in list10) {
            result += 10
        }
    }

    println("Total score: $result")
}