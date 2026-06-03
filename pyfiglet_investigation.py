

import pyfiglet
f = pyfiglet.figlet_format("Welcome Aidan", font="slant")
print(f)

f = pyfiglet.Figlet()

font_list = f.getFonts()

print (font_list)
print (len(font_list))


for font in font_list:
    f = pyfiglet.figlet_format(f"{font}", font=font)
    print(f)
