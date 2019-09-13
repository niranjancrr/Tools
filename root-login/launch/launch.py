import webbrowser
import sys

def main():
    ip = sys.argv[1]
  
    try: 
        url = 'https://' + str(ip)
        webbrowser.open(url)
    except: 
        print "Failed launching APIC UI. Please check"

if __name__ == '__main__':
    main()
