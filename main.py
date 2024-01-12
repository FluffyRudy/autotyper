from src import mac, linux 
import platform

def main():
    if platform.system() == 'Linux':
        out = linux.Autotyper('main.py', title='autotype')
    elif platform.system() == "Darwin":
        out = mac.Autotyper("main.py", title="autotype")
    else:
        print("Unknow system")
        import sys
        sys.exit()

    try:
        out.run()
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()