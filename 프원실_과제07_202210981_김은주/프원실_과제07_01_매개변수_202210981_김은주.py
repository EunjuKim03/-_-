# -*- coding: utf-8 -*-
"""프원실_과제07_01_매개변수_202210981_김은주.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CChDTalKzTb-IQCwbBQdxFL6v0SwxmCv
"""

#과제(1) 숫자 리스트를 매개변수로 받아서 평균을 구하는 함수를 완성하시오. 함수는 average(nums)
def average(nums):
    total = 0
    for num in nums:
      total += int(num)
    return total / len(nums)

def main():
  nums1=input("숫자를 입력하세요.")
  nums2=input("숫자를 입력하세요.")
  nums3=input("숫자를 입력하세요.")

  nums = [nums1, nums2, nums3]

  print("숫자들의 평균은"+str(average(nums)))

if __name__=="__main__":
  main()