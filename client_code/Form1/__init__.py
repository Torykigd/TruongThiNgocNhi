from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    algorithms = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Merge Sort"]
    self.dropdown_algorithm.items = algorithms

    # Any code you write here will run before the form opens.
  import anvil.server

  def sort_button_click(self, **event_args):
        numbers = self.text_box_numbers.text
        algorithm = self.dropdown_algorithm.selected_value
        sorted_numbers = self.sort_numbers(numbers, algorithm)
        self.label_sorted_numbers.text = ", ".join(map(str, sorted_numbers))
  def sort_numbers(self, numbers, algorithm):
        # Hàm sắp xếp dãy số nguyên dựa trên thuật toán được chọn
        if algorithm == "Insertion Sort":
            sorted_numbers = self.insertion_sort(numbers)
        elif algorithm == "Selection Sort":
            sorted_numbers = self.selection_sort(numbers)
        elif algorithm == "Bubble Sort":
            sorted_numbers = self.bubble_sort(numbers)
        elif algorithm == "Merge Sort":
            sorted_numbers = self.merge_sort(numbers)
        else:
            sorted_numbers = numbers  # Trong trường hợp không có thuật toán nào được chọn
            
        return sorted_numbers
  def dropdown_algorithm_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_algorithm = self.dropdown_algorithm.selected_value
    print("Thuật toán sắp xếp được chọn:", selected_algorithm) 
    
  def insertion_sort(self, arr):
        # Thuật toán Insertion Sort
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr = list(arr)
                arr[j + 1] = arr[j]
                arr = ''.join(arr)
                j -= 1
            arr = list(arr)
            arr[j + 1] = key
            arr = ''.join(arr)
        return arr
  def selection_sort(self, arr):
        # Thuật toán Selection Sort
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr_list = list(arr)
            arr_list[i], arr_list[min_idx] = arr_list[min_idx], arr_list[i]
            arr = ''.join(arr_list)
        return arr

  def bubble_sort(self, arr):
        # Thuật toán Bubble Sort
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr_list = list(arr)
                    arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
                    arr = ''.join(arr_list)
                    
        return arr

  def merge_sort(self, arr):
        # Thuật toán Merge Sort
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr_list = list(arr)
                    arr_list[k] = left_half[i]
                    arr = ''.join(arr_list)
                    i += 1
                else:
                    arr_list = list(arr)
                    arr_list[k] = right_half[j]
                    arr = ''.join(arr_list)
                    j += 1
                k += 1

            while i < len(left_half):
                arr_list = list(arr)
                arr_list[k] = left_half[i]
                arr = ''.join(arr_list)
                i += 1
                k += 1

            while j < len(right_half):
                arr_list = list(arr)
                arr_list[k] = right_half[j]
                arr = ''.join(arr_list)
                j += 1
                k += 1

        return arr