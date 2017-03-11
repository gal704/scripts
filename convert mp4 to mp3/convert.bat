mkdir newfiles 2>null
for %%a in ("*.mp4") do ffmpeg -i "%%a" "newfiles\%%~na.mp3"
pause
REM ffmpeg -i filename.mp4 filename.mp3