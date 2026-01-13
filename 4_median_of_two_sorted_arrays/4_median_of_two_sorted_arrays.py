from typing import List


class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        print("Array iniciales: ", nums1,nums2)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
    
    
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        print("x, y: ", x,y)
        print("low, high: ", low,high)

        while low <= high:
            # Partición binaria en el arreglo más corto
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            print("ParticionX, ParticionY: ", partitionX,partitionY)

            # Valores en los bordes de la partición (usamos infinito para bordes)
            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < x else float('inf')
            print("maxLeftX, minRightX: ", maxLeftX,minRightX)

            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = nums2[partitionY] if partitionY < y else float('inf')
            print("maxLeftY, minRightY: ", maxLeftY,minRightY)

            # Verificar si hemos encontrado el punto de corte correcto
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                print(maxLeftX <= minRightY and maxLeftY <= minRightX)
                # Si el total es par
                if (x + y) % 2 == 0:
                    print("par")
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                # Si el total es impar
                else:
                    print("impar")
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                # Estamos muy a la derecha en nums1, movemos a la izquierda
                high = partitionX - 1
            else:
                # Estamos muy a la izquierda en nums1, movemos a la derecha
                low = partitionX + 1
        
        
  
print(Solution().findMedianSortedArrays(nums1=[1,4,7,10,20,30,40,49],nums2=[3,5,9,34]))      
