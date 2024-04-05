fun main() {
    val test = true
    val name = "Xulescu"
    val friend = "One for $name, one for me."
    val random = "One for you, one for me."
    var line: String

    if (test == true)
        line = friend
    else
        line = random
    println(line)
}
//https://exercism.org/tracks/kotlin/exercises/two-fer