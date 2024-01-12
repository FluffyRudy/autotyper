from src import mac, linux
import platform
import sys

def main():
    if len(sys.argv) < 3:
        print("Must provide input file, output file(no extension)")
        sys.exit()
    print(sys.argv)
    print("Press enter to continue:")
    if platform.system() == 'Linux':
        out = linux.Autotyper(*sys.argv[1:])
    elif platform.system() == "Darwin":
        out = mac.Autotyper(*sys.argv[1:])
    else:
        print("Unknow system")
        sys.exit()

    try:
        out.run()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()