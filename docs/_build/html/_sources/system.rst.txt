System Operations
=================

The ``System`` class provides functionalities for system operations such as PDF extraction, directory creation, and message display.

Example usage:

.. code-block:: python

   from neri_library import System

   # Extract text from a PDF
   text = System.extract_pdf("path/to/file.pdf")

   # Create default directories
   System.create_dirs()

   # Display a message on the screen
   System.show_message("Hello, world!")

Key Features:
- **extract_pdf**: Extracts text from PDF files.
- **create_dirs**: Creates default or custom directories.
- **show_message**: Displays a dialog box with a message.

For more details, refer to the full documentation of the ``System`` class.