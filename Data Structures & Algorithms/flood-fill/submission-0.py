class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        vis = set()
        def dfs(i: int, j: int, c: int) -> None:
            # Base cases:
            if (i < 0 or i >= len(image) or
                j < 0 or j >= len(image[0]) or
                (i,j) in vis or
                image[i][j] != c):
                return
            
            image[i][j] = color
            vis.add((i,j))

            # Top, Bottom, Left, Right:
            dfs(i - 1, j, c)
            dfs(i + 1, j, c)
            dfs(i, j - 1, c)
            dfs(i, j + 1, c)
        
        dfs(sr, sc, image[sr][sc])
        return image

        # image = [
        #     [2,2,2],
        #     [2,2,0],
        #     [2,0,1]
        # ]
        # sr = 1, sc = 1, color = 2
        # dfs(1,1,1)