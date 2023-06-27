'''Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). 
Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are
 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while 
 value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.'''


class Solution:
    def findPath(self, m, n):                               # Method to initialize all the parameters we need
        self.n = n                                          # and call the backtracking method
        self.start = (0, 0)
        self.finish = (n-1, n-1)
        path = ''
        self.paths = []
        i, j = self.start

        if m[0][0] == 0:
            return -1

        self.solve(m, path, i, j)

        return self.paths


    def solve(self, m, path, i, j):                         # Backtracking method to check every posibillity in a maze
        if i == self.finish[0] and j == self.finish[1]:     # If a path has reached the finish, we save it
            self.paths.append(path)
            return True

        moves = self.checkVecinity(i, j, m)                 # Moves will store the possible moves

        if moves != None:
            for move in moves:                              # We iterate every move
                path += move                                # Adding the move to path
                m[i][j] = 0                                 # Turning the current position to 0 to avoid returning at it in the future

                if move == 'U':
                    i -= 1                                  # We move
                    self.solve(m, path, i, j)
                    i += 1                                  # After all the possibilities we want to undo so we can check for other moves

                if move == 'D':
                    i += 1
                    self.solve(m, path, i, j)
                    i -= 1

                if move == 'L':
                    j -= 1
                    self.solve(m, path, i, j)
                    j += 1

                if move == 'R':
                    j += 1
                    self.solve(m, path, i, j)
                    j -= 1

                path = path[:-1]                            # Undoing the changes we made at lines 34, 35
                m[i][j] = 1


    def checkVecinity(self, x, y, arr):             # Method to check the possible moves from m[i][j]
        posMoves = []

        if x != 0:
            if arr[x - 1][y] != 0:
                posMoves.append('U')

        if x != self.n - 1:
            if arr[x + 1][y] != 0 :
                posMoves.append('D')

        if y != 0:
            if arr[x][y - 1] != 0:
                posMoves.append('L')

        if y != self.n - 1:
            if arr[x][y + 1] != 0:
                posMoves.append('R')

        return posMoves
        

ob = Solution()

print(ob.findPath([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]], 4))

