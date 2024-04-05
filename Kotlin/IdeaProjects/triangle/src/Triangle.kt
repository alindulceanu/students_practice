class Triangle {
    var a: Int = 0
    var b: Int = 0
    var c: Int = 0

    fun inputValues() {
        print("Write the value of a here: ")
        a = readLine()!!.toInt()

        print("Write the value of b here: ")
        b = readLine()!!.toInt()

        print("Write the value of c here: ")
        c = readLine()!!.toInt()

        println("You have entered this for a: $a")
        println("You have entered this for b: $b")
        println("You have entered this for c: $c")
    }

    fun printTriangleType() {
        if (a == b && a == c)
            println("The triangle is equilateral")
        else if (a == b && a != c || a != b && a == c || b == c && a != b)
            println("The triangle is isosceles")
        else if (a != b && a != c && b != c)
            println("The triangle is scalene")
    }
}

fun main(args: Array<String>) {
    val triangle = Triangle()
    triangle.inputValues()
    triangle.printTriangleType()
}
