from pyfiglet import Figlet

def print_fancy_text():
    f = Figlet(font='slant')  # Şekilli yazı tipi
    print(f.renderText('wasetrox'))

if __name__ == "__main__":
    print_fancy_text()
