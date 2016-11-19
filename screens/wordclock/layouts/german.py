# This Python file uses the following encoding: utf-8
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
LAYOUT = (u"ESKISTRFÜNFE" #0-12 extra "u" before each line with Extended Unicode character(s)
          u"XZEHNZWANZIG" #12-23
          u"DREIUVIERTEL" #24-44
          u"XRVORNACHBSE" #36-59
          u"OHALBAELFÜNF" #48-74
          u"EINSELFZWEIX" #60-89
          u"RDREIAEKVIER" #72-83
          u"SECHSNLACHTI" #84-95
          u"DSIEBENZWÖLF" #96-107
          u"ZEHNEUNDUHRE") #108-119

# Map instructions:
# The clock works by rounding the time to the nearest 5 minutes.
# This means that you need to have settings for each five minute interval "m00"
# "m00", "m05".
# The clock also works on a 12 hour basis rather than 24 hour:
# "h00", "h01" etc.
# There are three optional parameters:
#   "all": Anything that is always shown regardless of the time e.g. "It is..."
#   "am":  Wording/symbol to indicate morning.
#   "pm":  Wording/symbol to indicate afternoon/evening
MAP = {
       "all": [0, 1, 3, 4, 5, 116, 117, 118], #ES IST
       "m00": [], #UHR
       "m05": [71, 72, 73, 74, 41, 42, 43, 44],#FUNT NACH
       "m10": [13, 14, 15, 16, 41, 42, 43, 44], #ZEHN NACH
       "m15": [29, 30, 31, 32, 33, 34, 35, 41, 42, 43, 44], #VIERTEL NACH
       "m20": [17, 18, 19, 20, 21, 22, 23, 41, 42, 43, 44], #ZWANZIG NACH
       "m25": [],
       "m30": [49, 50, 51, 52], #HALB
       "m35": [],
       "m40": [],
       "m45": [29, 30, 31, 32, 33, 34, 35, 38, 39, 40], #VIERTEL VOR
       "m50": [38, 39, 40], #ZEHN VOR
       "m55": [7, 8, 9, 10, 38, 39, 40], #FÜNF VOR
       "h01": [60, 61, 62], #EIN(S) is not used for telling the time.
       "h02": [67, 68, 69, 70], #ZWEI
       "h03": [66, 67, 68], #DREI
       "h04": [97, 98, 99, 100], #VIER
       "h05": [56, 57, 58, 59], #FÜNF
       "h06": [84, 85, 86, 87, 88], #SECHS
       "h07": [97, 98, 99, 100, 101, 102], #SIEBEN
       "h08": [91, 92, 93, 94], #ACHT
       "h09": [111, 112, 113, 114], #NEUN
       "h10": [108, 109, 110, 111], #ZEHN
       "h11": [54, 55, 56], #ELF
       "h12": [103, 104, 105, 106, 107], #ZWÖLF
       "am": [],
       "pm": []
  }

# Number of columns in grid layout
COLS = 12

# Size of letter in grid (x, y)
SIZE = (66, 48)

# Font size of letter
FONTSIZE = 40

# Is our language one where we need to increment the hour after 30 mins
# e.g. 9:40 is "Twenty to ten"
HOUR_INCREMENT = True

HOUR_INCREMENT_TIME = 29
