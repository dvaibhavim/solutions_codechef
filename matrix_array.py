# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:00:56 2020

@author: lenovo
"""

def rotate( matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        
        for i in range(length // 2):  # layer
            print(i,"i")
            k = length - i - 1
            print(k,"k")
            for r in range(i, length - i - 1):  # offset in layer
                j = length - r - 1
                print(j,"j",r)
                matrix[r][i], matrix[k][r] = matrix[k][r], matrix[r][i]
                matrix[k][r], matrix[j][k] = matrix[j][k], matrix[k][r]
                matrix[j][k], matrix[i][j] = matrix[i][j], matrix[j][k]
        return matrix
    
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate([[1]]))
print(rotate([[1,2],[3,4]]))