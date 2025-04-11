Advanced CLI Toolchain
=====================

Core Functionality
-----------------
The CLI module delivers production-ready automation for Python environment management and application deployment, showcasing enterprise-grade system integration capabilities.

Technical Highlights
-------------------
- **Environment Management**: Complete virtual environment control (destructive rebuild with automatic dependency installation via ``-v/--venv``)
- **Dependency Analysis**: Comprehensive import detection including hidden dependencies (``-fi/--find-imports``)
- **Executable Packaging**: Single-file standalone executable generation with PyInstaller integration (``-e/--exe``)
- **Automated Deployment**: End-to-end dependency resolution and installation (``-i/--install-imports``)
- **Interactive Help**: Complete feature documentation (``-h/--help``)

Command Reference
----------------
.. code-block:: text

   nr            Initialize toolchain
   nr -e  {file.py}                  Generate Windows executable with embedded environment
   nr -fi {file.py}                  Detect all required imports
   nr -i  {file.py}                  Install detected dependencies
   nr -v                             Rebuild virtual environment with current requirements
   nr -v -ad {folders} -e {file.py}: Combine commands to run all operations together
   nr -h                             Display complete command reference

Implementation Notes
--------------------
Demonstrated technical competencies:
- The .exe ('nr -e') is self-contained and requires neither Python nor external dependencies
- Advanced argument parsing architectures
- Cross-platform subprocess management
- Environment isolation techniques
- Production-grade error handling
- Automated dependency resolution