import os

if __name__ == "__main__":

   try:

       os.system("git pull");os.system('xdg-open https://www.facebook.com/Captain.TaRikuL.420')

       __import__("SIX").menu()

   except Exception as e: 

       exit(str(e))
