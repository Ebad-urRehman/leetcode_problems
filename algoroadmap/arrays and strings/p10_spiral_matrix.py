class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix[0]), len(matrix)
        UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
        size = m*n
        array = []
        current_direction = RIGHT

        # walls
        up_wall = 0
        down_wall = m
        right_wall = n
        left_wall = -1


        while len(array) != size:
            if current_direction == RIGHT:
                for i in range(left_wall+1, right_wall):
                    array.append(matrix[up_wall][i])
                right_wall -= 1
                current_direction = DOWN
            elif current_direction == DOWN:
                for i in range(up_wall+1, down_wall):
                    array.append(matrix[i][right_wall])
                down_wall -= 1
                current_direction = LEFT
            elif current_direction == LEFT:
                for i in range(right_wall-1, left_wall, -1):
                    array.append(matrix[down_wall][i])
                left_wall += 1
                current_direction = UP
            elif current_direction == UP:
                for i in range(down_wall-1, up_wall, -1):
                    array.append(matrix[i][left_wall])
                up_wall += 1
                current_direction = RIGHT
        return array