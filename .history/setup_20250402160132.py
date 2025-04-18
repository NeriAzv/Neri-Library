from setuptools import setup, find_packages

setup(
    name="bcpkgfox",
    version="0.15.112",
    author="Guilherme Neri",
    author_email="guilherme.neri@bcfox.com.br",
    description="Biblioteca BCFOX",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NeriAzv/Neri-Library",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            *[f"{cmd}=neri_library.cli:main" for cmd in [
                "neri_library",
                "nerilibrary",
                "neri-lib",
                "nerilib",
                "nlib",
                "neri",
                "library",
                "nl",
            ]],
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'setuptools',
        'pyperclip',
        'pyinstaller',
        'selenium',
    ],
    extras_require={
        "pynput": [
            'pynput',
        ],
        "screeninfo": [
            'screeninfo',
        ],
        "pywinauto": [
            'pywinauto',
        ],
        "capmonstercloudclient":[
            'capmonstercloudclient',
        ],
        "full": [
            'undetected-chromedriver',
            'webdriver-manager',
            'opencv-python',
            'pygetwindow',
            'pyinstaller',
            'screeninfo',
            'pyscreeze',
            'pyautogui',
            'selenium',
            'requests',
            'pymupdf',
            'Pillow',
            'psutil',
            'pynput',
        ],
    },
)
