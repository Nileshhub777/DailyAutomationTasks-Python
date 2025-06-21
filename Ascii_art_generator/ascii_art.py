from pyfiglet import Figlet
def generate_ascii_art():
    # Choose a font style
    fonts = Figlet().getFonts()
    print("Available fonts:", ", ".join(fonts[:5]), ".....and more!")

    # Input text and font
    text = input("Enter the text to be converted to the  ASCII art: ")
    font = input("Enter the font style or press the Enter key for the default : ").strip()

    if font not in fonts:
        print("Invalid or there was no font selected. Using the default font.")
        font = "Standard"

    # Generate ASCII art
    figlet = Figlet(font=font)
    ascii_art = figlet.renderText(text)
    print("\nYour Converted ASCII Art:\n")
    print(ascii_art)


# Run the generator
generate_ascii_art()
