@echo off
cd docs
call make clean
call make html
xcopy /E /I /Y _build\html\ ..\DOCS\