import pygame
from Platformer_Game.tiles.tiles import Tile
from Platformer_Game.Test_level.test import tile_size, screen_width
from Platformer_Game.Player.Player import Player


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    # setting up the level from text.py
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        # iterating over the rows and columns in the list in test.py and making the list into an enumerate object
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                # turing the 'X's and the P into the gray tile and the Player
                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if col == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    # carma movemnt
    def camra_scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        # checking to see wif the player is moving to the left or right and how the camra should move
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    # checking the players collision from the left and right
    def horizontal_collistion(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        # checking to see where the player collided with a tile from the left or right
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    # checking the players collision from the top and bottom
    def vertical_collistion(self):
        player = self.player.sprite
        player.apply_gravity()
        # checking to see where the player collided with a tile from the top or bottom
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.camra_scroll_x()
        # player
        self.player.update()
        self.horizontal_collistion()
        self.vertical_collistion()
        self.player.draw(self.display_surface)
