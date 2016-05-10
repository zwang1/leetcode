__author__ = 'zhengyiwang'
def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0
    n  = len(matrix)
    m = len(matrix[0])
    hori = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    ver = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(m):
            if matrix[i][j] == "1":
                hori[i][j] = 1
                ver[i][j] = 1
                if j > 0:
                    hori[i][j] = hori[i][j - 1] + 1
                if i > 0:
                    ver[i][j] = ver[i - 1][j] + 1
    area = [[0 for j in range(m)] for i in range(n)]
    maxarea = 0
    for i in range(n):
        for j in range(m):
            cur = max(hori[i][j], ver[i][j])
            if i > 0 and j > 0:
                a = min (hori[i - 1][j - 1] + 1, hori[i][j])
                b = min (ver[i - 1][j - 1] + 1, ver[i][j])
                cur = max(cur, a * b)
            area[i][j] = cur
            maxarea = max(maxarea, cur)
    return maxarea

print maximalRectangle(["01101","11010","01110","11110","11111","00000"])
