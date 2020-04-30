# youtube-dl2kodi

# options
youtube-dl2 -f <video.mp4>
 -f file path of the youtube-dl output file

# example
~~~~
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' \
--continue --ignore-errors --write-info-json --write-thumbnail --write-sub \ 
--add-metadata  --embed-thumbnail \
--output '%(uploader)s/S00E00 %(title)s (%(upload_date)s)[%(id)s].%(ext)s' \ 
--exec 'youtube-dl2kodi.py -f {}' \
https://www.youtube.com/playlist?list=PLKocZwBnFDxNAoxyxZ0w7mum35YY4v0nb 
~~~~
