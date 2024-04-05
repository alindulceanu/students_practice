fun main(){
    val firstDna = "GAGCCTACTAACGGGAT"
    val secondDna = "CATCGTAATGACGGCCT"
    var counter = 0

    for (i in 0 until firstDna.length)
        if (firstDna[i] != secondDna[i])
            counter ++

    println("The hamming distance is $counter")
}

//https://exercism.org/tracks/kotlin/exercises/hamming