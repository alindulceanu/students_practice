import java.security.KeyStore.TrustedCertificateEntry

class Xo {
    private var map : Array<Array<Char>>
    private var turn = true // true = X false = O
    private var endGame = true
    private var validPosition = false
    private var n: Int

    init {
        printMap()
        println("Choose size: ")
        n = readln().toInt()
        map = Array(n) {Array<Char>(n){' '} }
    }

    fun printMap() {
        (0..< n * 4).forEach{print("-")}
        println()
        (0..< n).forEach{i->
            (0..< n).forEach{j->
                print(map[i][j] + " | ")
        }
            println()
            (0..n * 4).forEach{print("-")}
            println()
        }
    }
    fun printPos(){
        (0..< n * 5).forEach{print("-")}
        println()

        var count = 1
        (0..< n).forEach{i->
            (0..< n).forEach{j->
                print(count.toString() + (if(count.toString().length < 2) {"  "} else if ((count.toString().length < 3)) {" "} else " ") + "|" + if((count + 1).toString().length < 2) {" "} else if ((count + 1).toString().length < 3) {" "} else {""})
                count++
            }
            println()
            (0..n * 5).forEach{print("-")}
            println()
        }
    }

    private fun convertPos(pos: Int): Pair<Int, Int>{
        val row = (pos - 1) / n
        val column = (pos - 1) % n
        return Pair(row, column)
    }

    fun set(pos: Int) {
        val (row, col) = convertPos(pos)

        if (map[row][col] == ' ') {
            if (turn)
                map[row][col] = 'X'
            else
                map[row][col] = 'O'

            turn = !turn
            validPosition = true

        } else {
            println("Position already claimed")
            validPosition = false
        }
    }

    private fun checkRules(){
        fun checkLines() {
            var currentCharHor = 'X'
            var currentCharVer = 'X'
            var lengthHor = 1
            var lengthVer = 1

            try {
                (0..<n - 1).forEach { i ->
                    (0..<n - 1).forEach { j ->
                        if (map[i][j] == currentCharHor && map[i][j] != ' ')
                            lengthHor++
                        else {
                            currentCharHor = map[i][j]
                            lengthHor = 1
                        }

                        if (map[j][i] == currentCharVer && map[j][i] != ' ')
                            lengthVer++
                        else {
                            currentCharVer = map[j][i]
                            lengthVer = 1
                        }

                        if (lengthHor >= 5 || lengthVer >= 5) {
                            throw RuntimeException()
                        }
                    }
                }
            }
            catch(e: RuntimeException){
                endGame = false
            }
        }
        checkLines()
    }

    private fun askPosition(){
        validPosition = false
        while(!validPosition) {
            println("move: ")
            val position = readln()

            try {
                set(position.toInt())
            }
            catch(e: Exception){
                println("Only use Integers in between 1 and ${n * n}")
                continue
            }
        }
    }

    fun play(){
        printPos()

        while(endGame){
            askPosition()
            checkRules()

            if (n > 6)
                printPos()

            printMap()
        }

        if (turn)
            println("O won")
        else
            println("X won")
    }
}

fun main(){
    var xD = Xo()
    xD.play()
}