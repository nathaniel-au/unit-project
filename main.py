@namespace
class SpriteKind:
    Enemy2 = SpriteKind.create()

def on_overlap_tile(sprite, location):
    info.player1.change_score_by(1)
    info.player2.change_score_by(1)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    tiles.set_tile_at(location, sprites.castle.tile_grass1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

p1Distance = 0
p2Distance = 0
Enemies: List[Sprite] = []
scene.set_background_color(7)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
player1 = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
player2 = sprites.create(img("""
        . . . . . f f 4 4 f f . . . . . 
            . . . . f 5 4 5 5 4 5 f . . . . 
            . . . f e 4 5 5 5 5 4 e f . . . 
            . . f b 3 e 4 4 4 4 e 3 b f . . 
            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
            . f 3 3 e b 3 e e 3 b e 3 3 f . 
            . f 3 3 f f e e e e f f 3 3 f . 
            . f b b f b f e e f b f b b f . 
            . f b b e 1 f 4 4 f 1 e b b f . 
            f f b b f 4 4 4 4 4 4 f b b f f 
            f b b f f f e e e e f f f b b f 
            . f e e f b d d d d b f e e f . 
            . . e 4 c d d d d d d c 4 e . . 
            . . e f b d b d b d b b f e . . 
            . . . f f 1 d 1 d 1 d f f . . . 
            . . . . . f f b b f f . . . . .
    """),
    SpriteKind.player)
controller.player1.move_sprite(player1)
controller.player2.move_sprite(player2)
info.player1.set_life(3)
info.player2.set_life(3)
info.player1.set_score(0)
info.player2.set_score(0)
scene.camera_follow_sprite(player1)
mySprite = sprites.create(img("""
        . . . . c c c c c c . . . . . . 
            . . . c 6 7 7 7 7 6 c . . . . . 
            . . c 7 7 7 7 7 7 7 7 c . . . . 
            . c 6 7 7 7 7 7 7 7 7 6 c . . . 
            . c 7 c 6 6 6 6 c 7 7 7 c . . . 
            . f 7 6 f 6 6 f 6 7 7 7 f . . . 
            . f 7 7 7 7 7 7 7 7 7 7 f . . . 
            . . f 7 7 7 7 6 c 7 7 6 f c . . 
            . . . f c c c c 7 7 6 f 7 7 c . 
            . . c 7 2 7 7 7 6 c f 7 7 7 7 c 
            . c 7 7 2 7 7 c f c 6 7 7 6 c c 
            c 1 1 1 1 7 6 f c c 6 6 6 c . . 
            f 1 1 1 1 1 6 6 c 6 6 6 6 f . . 
            f 6 1 1 1 1 1 6 6 6 6 6 c f . . 
            . f 6 1 1 1 1 1 1 6 6 6 f . . . 
            . . c c c c c c c c c f . . . .
    """),
    SpriteKind.enemy)
mySprite.set_position(142, 16)

def on_on_update():
    pass
game.on_update(on_on_update)

def on_update_interval():
    global Enemies, p2Distance, p1Distance
    player2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    Enemies = sprites.all_of_kind(SpriteKind.enemy)
    for value in Enemies:
        p2Distance = Math.sqrt((value.x - player2.x) ** 2 + (value.y - player2.y) ** 2)
        p1Distance = Math.sqrt((value.x - player1.x) ** 2 + (value.y - player1.y) ** 2)
        if p1Distance > p2Distance:
            value.follow(player2, 50)
        else:
            value.follow(player1, 50)
        if value.overlaps_with(player2):
            value.follow(player2, 0)
        if value.overlaps_with(player1):
            value.follow(player1, 0)
game.on_update_interval(100, on_update_interval)