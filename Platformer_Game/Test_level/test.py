# making the level layout using a list
level_map = [
    '                           ',
    '                           ',
    '                           ',
    'XX     XX       XX         ',
    'XX P                       ',
    'XXXX          XX         XX',
    'XXXX        XX             ',
    'XX     X    XXXX   XX  XX  ',
    '       X    XXXX   XX  XXX ',
    '    XXXX  XXXXXX   XX  XXX ',
    'XXXXXXXX  XXXXXX   XX  XXX']

# setting the screens width and height and the tile size
tile_size = 50
screen_width = 1000
screen_height = len(level_map) * tile_size

# print the level height and if i replace the code in the print to
# screen height i can see the screen height
# print(len(level_map))
# print(screen_height)
