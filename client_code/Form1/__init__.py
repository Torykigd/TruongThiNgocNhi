from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  import anvil.server

  def sort_button_click(self, **event_args):
   numbers = self.text_box_numbers.text
        algorithm = self.dropdown_algorithm.selected_value
        
        sorted_numbers = anvil.server.call('sort_numbers', numbers, algorithm)
        
        self.label_sorted_numbers.text = ", ".join(map(str, sorted_numbers))
    

    