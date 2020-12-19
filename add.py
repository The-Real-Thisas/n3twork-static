from riposte import Riposte
import os
from gtts import gTTS 

print("VERSION: 1.1")
print("Author: Thisas")

audify = Riposte(prompt="▶ ")

@audify.command("version")
def search():
    print("""
    ◤ VERSION: 1.1 ◢

    """)

@audify.command("test")
def test():
    print(""" 
▷ Opening input.txt ( ﾟヮﾟ)
            """)
    file = open("input.txt", "r").read().replace("\n", " ")
    language = 'en'
    myobj = gTTS(text=file, lang=language, slow=False)
    nam = input("Name: ")
    print(""" 
▷ Converting to Audio (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
            """)
    myobj.save(nam + ".mp3")
    print(""" 
▷ Saving the audio in the audio folder (~˘▾˘)~
            """)
    os.system("cp " + nam + ".mp3 audio")
    print(""" 
▷ Fusing the logo and audio ᕙ(⇀‸↼‶)ᕗ
            """)
    os.system("ffmpeg -loop 1 -y -i logo.png -i " + nam + ".mp3 -shortest -pix_fmt yuv420p " + nam + ".mp4  -vf 'pad=ceil(iw/2)*2:ceil(ih/2)*2'")
    print(""" 
▷ Saving the video in the video folder (~˘▾˘)~
            """)
    os.system("mv " + nam + ".mp4 video")
    print(""" 
▷ Cleaning up 〆(・∀・＠)
            """)
    os.system("rm " + nam + ".mp3")
    print(""" 
▸ Yaaa we did it \ (•◡•) /
            """)

@audify.command("exit")
def ext():
    exit()




audify.run()
