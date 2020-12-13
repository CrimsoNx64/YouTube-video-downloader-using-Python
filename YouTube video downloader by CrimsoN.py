
#   _____      _                     _   _ 
#  / ____|    (_)                   | \ | |
# | |     _ __ _ _ __ ___  ___  ___ |  \| |
# | |    | '__| | '_ ` _ \/ __|/ _ \| . ` |
# | |____| |  | | | | | | \__ \ (_) | |\  |
#  \_____|_|  |_|_| |_| |_|___/\___/|_| \_|
                                            
#YouTube video downloader

import webbrowser#allows Pyhton to access your browser

videolink=input("enter YouTube url / link you want to download: ")

videolink=videolink[:12]+"ss"+videolink[12:]#adds "ss" which makes the video downloadable
webbrowser.open(videolink)#opens the new link
