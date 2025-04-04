Advanced CLI Toolchain
=====================

Core Functionality
-----------------
The Neri CLI module provides enterprise-grade automation for Python environment management and application deployment, demonstrating advanced system integration capabilities.

Technical Highlights
-------------------
- **Cross-platform virtual environment control** (destructive rebuilds with ``-v`` flag)
- **Smart dependency resolution** (including hidden imports via ``-fi``)
- **Self-contained executable generation** (PyInstaller integration via ``-e``)
- **Automated package installation** (dependency detection + install via ``-i``)

Command Reference
----------------
.. code-block:: text

   nr          : Base command
   nr -e       : Generate Windows .exe with embedded dependencies
   nr -fi      : Advanced import detection
   nr -i       : Install detected requirements
   nr -v       : Rebuild virtual environment
   nr -h       : Display full command reference

Implementation Notes
--------------------
This toolchain demonstrates:
1. Complex argument parsing architectures
2. Subprocess management best practices
3. Cross-platform compatibility layers
4. Production-grade error handling