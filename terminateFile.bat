@echo off

taskkill /F /IM explorer.exe /IM winword.exe /IM excel.exe /IM chrome.exe /IM iexplore.exe

Start explorer.exe

shutdown -s -t 15