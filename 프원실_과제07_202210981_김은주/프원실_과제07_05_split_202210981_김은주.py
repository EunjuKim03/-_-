# -*- coding: utf-8 -*-
"""프원실_과제07_05_Split_202210981_김은주.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CChDTalKzTb-IQCwbBQdxFL6v0SwxmCv
"""

#과제(5). 1번과제에서 만든 함수를 이용하며, 메인에서 split()함수를 이용하여 여러 값을 한줄로 입력받아 평균을 출력할 수 있는 프로그램을 완성하시오.
def average(nums):
    total = 0
    for num in nums:
      total += int(num)
    return total / len(nums)

def main():
  numbers=input("숫자를 입력하세요").split(",")
  nums1=numbers[0]
  nums2=numbers[1]
  nums3=numbers[2]

  nums = [nums1, nums2, nums3]

  print("숫자들의 평균은"+str(average(nums)))

if __name__=="__main__":
  main()