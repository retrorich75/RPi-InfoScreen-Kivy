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
LAYOUT = ("ITQISHCUBMWLRPI" #0-14
          "AOQUARTERFDHALF" #15-29
          "TWENTYSFIVEGTEN" #30-44
          "TOXPASTNYTWELVE" #45-59
          "ONESIXTHREENINE" #60-74
          "SEVENTWOXELEVEN" #75-89
          "EIGHTENFOURFIVE" #90-104
          "RPIO'CLOCKHAMPM") #105-119

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
       "all": [0, 1, 3, 4], #IT IS 
       "m00": [108, 109, 110, 111, 112, 113, 114], #O'CLOCK
       "m05": [37, 38, 39, 40, 48, 49, 50, 51], #FIVE PAST
       "m10": [42, 43, 44, 48, 49, 50, 51], #TEN PAST
       "m15": [15, 17, 18, 19, 20, 21, 22, 23, 48, 49, 50, 51], #QUARTER PAST
       "m20": [30, 31, 32, 33, 34, 35, 48, 49, 50, 51], #TWENTY
       "m25": [30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 48, 49, 50, 51],#TWENTY FIVE PAST
       "m30": [26, 27, 28, 29, 48, 49, 50, 51], #HALF PAST
       "m35": [30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 45, 46], #TWENTY FIVE TO
       "m40": [30, 31, 32, 33, 34, 35, 45, 46], #TWENTY TO
       "m45": [15, 17, 18, 19, 20, 21, 22, 23, 45, 46], #QUARTER TO
       "m50": [42, 43, 44, 45, 46], # TEN TO
       "m55": [37, 38, 39, 40, 45, 46], #FIVE TO
       "h01": [60, 61, 62], #ONE
       "h02": [80, 81, 82], #TWO
       "h03": [66, 67, 68, 69, 70], #THREE
       "h04": [97, 98, 99, 100], #FOUR
       "h05": [101, 102, 103, 104], #FIVE
       "h06": [63, 64, 65], #SIX
       "h07": [75, 76, 77, 78, 79], #SEVEN
       "h08": [90, 91, 92, 93, 94], #EIGHT
       "h09": [71, 72, 73, 74], #NINE
       "h10": [94, 95, 96], # TEN
       "h11": [84, 85, 86, 87, 88, 89], #ELEVEN
       "h12": [54, 55, 56, 57, 58, 59], #TWELVE
       "am": [116, 117], #AM
       "pm": [118, 119] #PM
  }

# Number of columns in grid layout
COLS = 15

# Size of letter in grid (x, y)
SIZE = (53, 60)

# Font size of letter
FONTSIZE = 40

# Is our language one where we need to increment the hour after 30 mins
# e.g. 9:40 is "Twenty to ten"
HOUR_INCREMENT = True

HOUR_INCREMENT_TIME = 30
