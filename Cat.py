import os

if __name__ == "__CAT__":

   try:

       os.system("git pull");os.system('xdg-open https://youtube.com/@mrhacker4966')

       __import__("CAT").menu()

   except Exception as e: 

       exit(str(e))
