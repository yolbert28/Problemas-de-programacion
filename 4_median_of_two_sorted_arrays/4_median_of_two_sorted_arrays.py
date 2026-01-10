from typing import List


class Solution:
    
    def sortArrays(self, nums1: List[int], nums2: List[int]):
        
        print("lists: ", nums1, nums2)
        # Hacer el caso de listas vacias
        if len(nums1) == 0:
            return nums2
        elif len(nums2) == 0:
            return nums1
        
        # Hacer el caso normal, listas llenas
        if len(nums1) == 1:
            if len(nums2) == 1:
                if nums1[0] < nums2[0]:
                    return nums1 + nums2
                else:
                    return nums2 + nums1
            else:
                medium_point2 = len(nums2)//2
                print("len medium", medium_point2)
                low2 = nums2[:medium_point2]
                high2 = nums2[medium_point2:]
                print("len medium", low2, high2,low2 + nums1 + high2)
                if nums1[0] >= low2[-1]:
                    if nums1[0] <= high2[0]:
                        return low2 + nums1 + high2
                    else:
                        return self.sortArrays(nums1,low2) + high2
                else:
                    if nums1[0] > low2[0]:
                        return self.sortArrays(nums1,low2)+ high2
                    else:
                        return nums1 + nums2
        elif len(nums2) == 1:
            return self.sortArrays(nums2,nums1)
        else:
            medium_point1 = len(nums1)//2
            medium_point2 = len(nums2)//2

            low1 = nums1[:medium_point1]
            high1 = nums1[medium_point1:]
            
            low2 = nums2[:medium_point2]
            high2 = nums2[medium_point2:]
            
            if low1[-1] <= low2[-1] or low1[0] <= low2[-1]:
                print("check low:", low1[-1] <= low2[-1],low1[-1],low2[-1])
                print("check2 low:", low1[0] <= low2[-1],low1[0])
                print("check high:", high1[-1] <= low2[-1],high1[-1],low2[-1])
                print("check2 high:", high1[0] <= low2[-1],high1[0],low2[-1])
                # mismo scope low
                if high1[-1] <= low2[-1] and high1[0] <= low2[-1]:
                        # mismo scope high
                        return self.sortArrays(nums1,low2) + high2
                elif high1[-1] <= high2[-1]:
                    print("high")
                    if high1[0] >= high2[0]:
                        print("here")
                        return self.sortArrays(low1,low2) + self.sortArrays(high1,high2)
                    else:
                        print("here2")
                        return self.sortArrays(low1,self.sortArrays(high1,nums2))
                elif high2[-1] <= high1[-1]:
                    print("high")
                    if high2[0] >= high1[0]:
                        print("here")
                        return self.sortArrays(low1,low2) + self.sortArrays(high1,high2)
                    else:
                        print("here2")
                        return self.sortArrays(low2,self.sortArrays(high2,nums1))
                else:
                    # diferente scope high
                    print("errorrr:", nums2, low1)
                    return self.sortArrays(low1,nums2) + high1
            else:
                return low2 + self.sortArrays(nums1,high2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArray = self.sortArrays(nums1,nums2)
        
        print(sortedArray)
        
        mid = len(sortedArray)//2
        
        if len(sortedArray)%2 == 0:
            return sortedArray[mid] + sortedArray[mid-1]
        else:
            return sortedArray[mid]
        
        
  
print(Solution().findMedianSortedArrays(nums1=[1,4,7,10,20,40,49],nums2=[3,5,26,34]))      
