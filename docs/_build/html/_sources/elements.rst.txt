Element Manipulation
====================

The ``Elements`` class provides functionalities for manipulating web page elements using Selenium. It includes methods for finding elements, waiting for conditions, and interacting with elements.

Example usage:

.. code-block:: python

   from neri_library import Elements

   # Find an element on the page
   element = Elements.find_element_with_wait("xpath", "//div[@class='example']")

   # Wait until an element is clickable
   clickable_element = Elements.wait_for_element_be_clickable("id", "button")

Key Features:
- **find_element_with_wait**: Finds an element on the page with a wait time.
- **wait_for_element_be_clickable**: Waits until an element is clickable.
- **move_mouse_smoothly**: Moves the mouse smoothly to an element.

For more details, refer to the full documentation of the ``Elements`` class.