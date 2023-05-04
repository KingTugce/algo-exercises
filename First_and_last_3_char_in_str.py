s = "MillionerTugce"
# option 1
if len(s) < 6:
    print("empty string")

else: 
    new_string = s[:3] + s[len(s)-3:]
    print(new_string)

# option 2
s = "amazing"

num_char = 3

if len(s) < num_char*2:
    print("")
