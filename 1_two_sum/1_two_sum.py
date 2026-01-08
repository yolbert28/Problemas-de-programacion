from typing import List


def two_sum(nums: List[int], target: int):
    
    if len(nums) < 2:
        print("La lista de números es invalida por tener una longitud incorrecta, debe tener al menos 2 números")
        return 
    
    print("La lista de números ingresada es: ", nums)
    print("El número objetivo es: ", target)
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                print("\nSe hallo un resultado que coincide con el objetivo: ",[i,j])
                return
    print("\nLa suma de los números no coincide con el objetivo")
                
     
# Valores de prueba
# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,2]
# target = 6

nums = [3]
target = 6

two_sum(nums, target)