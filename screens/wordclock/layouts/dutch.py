'''This is a custom layout for the RPi InfoScreen wordclock screen.

    Custom layouts can be created for the screen by creating a new file in the
    "layouts" folder.

    Each layout must have the following variables:
        LAYOUT:   The grid layout. Must be a single string.
        MAP:      The mapping required for various times (see notes below)
        COLS:     The number of columns required for the grid layout
        SIZE:     The size of the individual box containing your letter.
                  Tuple in (x, y) format.
        FONTSIZE: Font size for the letter
'''

# Layout is a single string variable which will be looped over by the parser.
LAYOUT = ("HETGISBNUL"
          "DVIJFTIENV"
          "KWARTXOVER"
          "TVOORHALFJ"
          "ACHTWEEZES"
          "DRIELFTIEN"
          "CZEVENEGEN"
          "VIERTWAALF"
          "EENVIJFUUR")

# Map instructions:
# The clock works by rounding the time to the nearest 5 minutes.
# This means that you need to have settngs for each five minute interval "m00"
# "m00", "m05".
# The clock also works on a 12 hour basis rather than 24 hour:
# "h00", "h01" etc.
# There are three optional parameters:
#   "all": Anything that is always shown regardless of the time e.g. "It is..."
#   "am":  Wording/symbol to indicate morning.
#   "pm":  Wording/symbol to indicate afternoon/evening
MAP = {
       "all": [0, 1, 2, 4, 5], # HET IS
       "m00": [87,88,89], # UUR
       "m05": [11, 12, 13, 14, 26, 27, 28, 29], #VIJF OVER
       "m10": [15, 16, 17, 18, 26, 27, 28, 29], #TIEN OVER
       "m15": [20, 21, 22, 23, 24, 26, 27, 28, 29], #KWART OVER
       "m20": [15, 16, 17, 18, 31, 32 ,33 ,34], #TIEN VOOR
       "m25": [11, 12, 13, 14, 31, 32 ,33 ,34], #VIJF VOOR
       "m30": [35, 36, 37, 38], #HALF
       "m35": [11, 12, 13, 14, 26, 27, 28, 29], #VIJF OVER
       "m40": [15, 16, 17, 18, 26, 27, 28, 29], #TIEN OVER
       "m45": [20, 21, 22, 23, 24, 31, 32 ,33 ,34], #KWART VOOR
       "m50": [15, 16, 17, 18, 31, 32 ,33 ,34], #TIEN VOOR
       "m55": [11, 12, 13, 14, 31, 32 ,33 ,34], #VIJF VOOR
       "h01": [80, 81, 82], #EEN (D)
       "h02": [43, 44, 45, 46], #TWEE (D)
       "h03": [50, 51, 52, 53], #DRIE (D)
       "h04": [70, 71, 72, 73], #VIER (D)
       "h05": [83, 84, 85, 86], #VIJF (D)
       "h06": [47, 48, 49], #ZES (D)
       "h07": [61, 62, 63, 64, 65], #ZEVEN (D)
       "h08": [40, 41, 42, 43], #ACHT (D)
       "h09": [65, 66, 67, 68, 69], #NEGEN (D)
       "h10": [56, 57, 58, 59], #TIEN (D)
       "h11": [53, 54, 55], #ELF (D)
       "h12": [74, 75, 76, 77, 78, 79], #TWAALF (D)
  }

# Number of columns in grid layout
COLS = 10

# Size of letter in grid (x, y)
SIZE = (80, 53)

# Font size of letter
FONTSIZE = 50

# Is our language one where we need to increment the hour after 30 mins
# e.g. 9:40 is "Twenty to ten"
HOUR_INCREMENT = True

HOUR_INCREMENT_TIME = 30
