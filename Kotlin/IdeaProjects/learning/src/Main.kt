fun decimalToBinary(decimal: Int): String {
    var n = decimal
    var binary = ""

    if (n == 0) {
        return "0"
    }

    while (n > 0) {
        val remainder = n % 2
        binary = remainder.toString() + binary
        n /= 2
    }

    return binary
}

fun main() {
    val decimalNumber = 42 // Replace with your decimal number
    val binaryNumber = decimalToBinary(decimalNumber)
    println("Binary representation of $decimalNumber is $binaryNumber")
}
