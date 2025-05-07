from pyfiglet import Figlet
def generate_ascii_art():
    # Choose a font style
    fonts = Figlet().getFonts()
    print("Available fonts:", ", ".join(fonts[:5]), "...and more!")

    # Input text and font
    text = input("Enter the text to be converted to ASCII art: ")
    font = input("Enter the font style or press the Enter key for default : ").strip()

    if font not in fonts:
        print("Invalid or no font was selected. Using the default font.")
        font = "Standard"

    # Generate ASCII art
    figlet = Figlet(font=font)
    ascii_art = figlet.renderText(text)
    print("\nYour ASCII Art:\n")
    print(ascii_art)


# Run the generator
generate_ascii_art()
