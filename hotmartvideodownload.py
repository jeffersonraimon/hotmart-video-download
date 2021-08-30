import requests

print('=-'*30)
print('''
   H O T M A R T  V I D E O  D O W N L O A D
''')
print('=-'*30)

print('''

INSTRUCTIONS: 

FOR .m3u8 FORMAT

1: USE IDM BROWSER EXTENSION TO GET THE VIDEO LINK
2: PASTE THE LINK IN THIS PROGRAM AND DOWNLOAD IT
3: USE VLC TO CONVERT .m3u8 TO YOUR VIDEO FORMAT AND CODEC FAVORITE

''')

print("Type 'q' to quit \n")


while True:

    url = input('Type or paste the video URL: ')

    if url != 'q':

    

            newurl = url.replace('source', 'authsource') #To download the video, we have to chance that word

            r = requests.get(newurl, allow_redirects=True)

            filename = str(input('New video name: '))
        
            open(filename, "wb").write(r.content)

        
    else:
       
        break

