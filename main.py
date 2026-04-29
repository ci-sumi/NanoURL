
import pyshorteners
#pyshorteners is a package which bridges the 3rd party Url shortener service"
#  pyfiglet converts normal text to ASCII Art
from pyfiglet import figlet_format
def main():
    print("Hello from nanourl!")
    print(figlet_format("NanoURL"))
def shorten_url_pyshorteners(long_url):
    try:
        #Create an Instance of Shortener class
        s=pyshorteners.Shortener()
        #Shorten the URL using TinyUrl
        shorten_url=s.tinyurl.short(long_url)
        return shorten_url
    except Exception as e:
        return f"Error occured{e}"
    
if __name__ == "__main__":
    main()
    # shorten_url_pyshorteners()
    long_url=input("Enter the URL to shorten using pyshorteners: ")
    if long_url.strip()=="":
        print("Invalid URL")
        exit()
    shorten_url=shorten_url_pyshorteners(long_url)
    print(f"ShortenedURL: {shorten_url}")
