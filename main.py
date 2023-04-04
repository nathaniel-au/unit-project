# This function allows the enemies to follow the closest player
def EnemyFollowing(Enemy: Sprite):
    global p2Distance, p1Distance
    p2Distance = Math.sqrt((Enemy.x - player2.x) ** 2 + (Enemy.y - player2.y) ** 2)
    p1Distance = Math.sqrt((Enemy.x - player1.x) ** 2 + (Enemy.y - player1.y) ** 2)
    if p1Distance > p2Distance:
        return player2
    else:
        return player1
# This allows the player to destroy the enemy and also animates the player while doing it

def on_a_pressed():
    sprites.destroy(chosen_enemy)
    animation.run_image_animation(player1,
        [img("""
                ..............ffffff....
                        .............f2feeeeff..
                        ............f222feeeeff.
                        .......cc...feeeeffeeef.
                        .......cdc.fe2222eeffff.
                        .......cddcf2effff222ef.
                        ........cddcffeeefffffff
                        .........cddce44fbe44eff
                        ..........cdceddf14d4eef
                        ..........cccdeddd4eeef.
                        ...........edd4e44eeff..
                        ............ee442222f...
                        .............f2e2222f...
                        .............f554444f...
                        ..............ffffff....
                        ................fff.....
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        ..............fff.......
                        .............f2fffff....
                        ...........ff22eeeeeff..
                        ..........ff222eeeeeeff.
                        ..........feeeefffeeeef.
                        .........fe2222eeefffff.
                        .........f2efffff222efff
                        ..cc.....fffeeefffffffff
                        ..cdcc...fee44fbbe44efef
                        ..ccddcc..feddfbb4d4eef.
                        ....cdddceefddddd4eeef..
                        .....ccdcddee2222222f...
                        ......cccdd44e544444f...
                        .........eeeeffffffff...
                        .............ff...fff...
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ...............ff.......
                        .............ff2ffff....
                        ............ff2feeeeff..
                        ...........ff22feeeeeff.
                        ...........feeeeffeeeef.
                        ..........fe2222eefffff.
                        ..........f2effff222efff
                        ..........fffeeeffffffff
                        ..........fee44fbe44efef
                        ...........feddfb4d4eef.
                        ..........c.eeddd4eeef..
                        ....ccccccceddee2222f...
                        .....dddddcedd44e444f...
                        ......ccccc.eeeefffff...
                        ..........c...ffffffff..
                        ...............ff..fff..
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ..............ffffff....
                        .............f2feeeeff..
                        ............f222feeeeff.
                        ............feeeeffeeef.
                        ...........fe2222eeffff.
                        ...........f2effff222ef.
                        ...........fffeeefffffff
                        ...........fee44fbe44eff
                        ............feddf14d4eef
                        .............fdddd4eeef.
                        .............fe444eddf..
                        .............ccc22eddf..
                        .............cdc22fee...
                        ............cddc4444f...
                        ...........cddcfffff....
                        ..........cddc..fff.....
                        ..........cdc...........
                        ..........cc............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        100,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# This creates the chests that give you points

def on_overlap_tile(sprite, location):
    info.player1.change_score_by(1)
    info.player2.change_score_by(1)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    tiles.set_tile_at(location, sprites.castle.tile_grass1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

# This ends the game if the players health reaches 0

def on_on_zero(status):
    game.game_over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

# This block of code stores the overlapped enemy into a variable, and also depletes the players health when they overlap an enemy.

def on_on_overlap(sprite2, otherSprite):
    global chosen_enemy
    chosen_enemy = otherSprite
    player1Health.value += -1
    player2Health.value += -1
    animation.run_image_animation(otherSprite,
        [img("""
                . . . . c c c c c c c . . . . . 
                        . . . c 6 7 7 7 7 7 6 c . . . . 
                        . . c 6 7 c 6 6 6 6 c 7 c . . . 
                        . . c 7 7 6 f 6 6 f 6 7 6 c . . 
                        . . c 7 7 7 7 7 7 7 7 7 7 c . . 
                        . . f 7 7 7 6 1 f f 1 8 7 f . . 
                        . . f 7 7 7 f 1 f f 1 f 6 f . . 
                        . . f 6 7 7 f 2 2 2 2 f f . . . 
                        . . c f 6 7 7 2 2 2 2 f c c . . 
                        . c 7 7 c c 7 7 7 7 7 7 7 7 c . 
                        c 7 7 7 6 c f 7 7 7 7 1 1 1 7 c 
                        c c 6 6 6 c c f 6 7 1 1 1 1 1 f 
                        . . c 6 6 6 c 6 6 1 1 1 1 1 1 f 
                        . . c 6 6 6 6 6 6 1 1 1 1 1 6 f 
                        . . . c 6 6 6 6 1 1 1 1 1 6 f . 
                        . . . . c c c c c c c c f f . .
            """),
            img("""
                . . . c c c c c c c . . . . . . 
                        . . c 7 f f 6 6 f f c . . . . . 
                        . c 6 7 6 6 6 6 6 6 7 c . . . . 
                        . c 7 7 7 7 7 7 7 7 7 7 c . . . 
                        . c 7 7 7 6 1 f f 1 8 7 c . . . 
                        . f 7 7 7 f 1 f f 1 f 6 f . . . 
                        . f 7 7 7 f 2 2 2 2 f 6 f . . . 
                        . f 6 7 7 f 2 2 2 2 f 6 c c . . 
                        . . c f 7 7 2 2 2 2 7 7 7 7 c . 
                        . c 7 7 c c 7 7 7 7 7 1 1 1 7 c 
                        c 7 7 7 6 c f 7 7 7 1 1 1 1 1 f 
                        c c 6 6 6 c c f 6 1 1 1 1 1 1 f 
                        . . c 6 6 6 c 6 6 1 1 1 1 1 6 f 
                        . . c 6 6 6 6 6 6 1 1 1 1 1 6 f 
                        . . . c 6 6 6 6 6 1 1 1 1 6 f . 
                        . . . . c c c c c c c c f f . .
            """),
            img("""
                . . . c c c c c c c . . . . . . 
                        . . c 7 f f 6 6 f f c . . . . . 
                        . c 6 7 6 6 6 6 6 6 7 c . . . . 
                        . c 7 7 7 7 7 7 7 7 7 7 c . . . 
                        . c 7 7 7 6 1 f f 1 8 7 c . . . 
                        . f 7 7 7 f 1 f f 1 f 6 f . . . 
                        . f 7 7 7 f 2 2 2 2 f 6 f . . . 
                        . f 6 7 7 f 2 2 2 2 f 6 c c . . 
                        . . c f 7 7 2 2 2 2 7 7 7 7 c . 
                        . c 7 7 c c 7 7 7 7 7 1 1 1 7 c 
                        c 7 7 7 6 c f 7 7 7 1 1 1 1 1 f 
                        c c 6 6 6 c c f 6 1 1 1 1 1 1 f 
                        . . c 6 6 6 c 6 6 1 1 1 1 1 6 f 
                        . . c 6 6 6 6 6 6 1 1 1 1 1 6 f 
                        . . . c 6 6 6 6 6 1 1 1 1 6 f . 
                        . . . . c c c c c c c c f f . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        c c c c c . . . . . . . . . . . 
                        c 6 7 7 7 c c . . . . . . . . . 
                        . c c 7 7 7 c c . . . . . . . . 
                        . . . c 7 7 6 c . . . . . . . . 
                        . . . c 6 6 6 c . . . . . . . . 
                        . . c c 6 6 6 c c c c c c . . . 
                        . c 6 6 6 c c 6 7 7 7 7 6 c . . 
                        c c 6 6 6 c 7 7 7 7 7 7 7 7 c . 
                        c 6 6 6 c 6 7 7 7 7 7 7 7 7 6 c 
                        c 6 6 6 c 7 7 7 c 6 6 6 6 c 7 c 
                        c 6 6 6 f 7 7 7 c c 6 6 c c 7 f 
                        c 6 6 6 f 7 7 7 6 f 6 6 f 6 7 f 
                        . c c 6 6 f 6 7 c 1 f f c 1 c . 
                        . . . c c c c c c c c c c c c .
            """),
            img("""
                c c c c c . . . . . . . . . . . 
                        c 6 7 7 7 c c . . . . . . . . . 
                        . c c 7 7 7 c c . . . . . . . . 
                        . . . c 7 7 6 c . . . . . . . . 
                        . . . c 6 6 6 c . . . . . . . . 
                        . . c c 6 6 6 c . . . . . . . . 
                        . c c 6 6 6 c c c c c c c . . . 
                        . c 6 6 6 c c 6 7 7 7 7 6 c . . 
                        c c 6 6 6 c 7 7 7 7 7 7 7 7 c . 
                        c 6 6 6 c 6 7 7 7 7 7 7 7 7 6 c 
                        c 6 6 6 c 7 7 7 c 6 6 6 6 c 7 c 
                        c 6 6 6 f 7 7 7 c c 6 6 c c 7 f 
                        c 6 6 6 f 7 7 7 6 f 6 6 f 6 7 f 
                        . c 6 6 f 6 7 7 7 7 7 7 7 7 f . 
                        . c c 6 6 f 6 7 c 1 f f c 1 c . 
                        . . . c c c c c c c c c c c c .
            """),
            img("""
                c c c c c . . . . . . . . . . . 
                        c 6 7 7 7 c c . . . . . . . . . 
                        . c c 7 7 7 c c . . . . . . . . 
                        . . . c 7 7 6 c . . . . . . . . 
                        . . . c 6 6 6 c . . . . . . . . 
                        . . c c 6 6 6 c . . . . . . . . 
                        . c c 6 6 6 c c c c c c c . . . 
                        . c 6 6 6 c c 6 7 7 7 7 6 c . . 
                        c c 6 6 6 c 7 7 7 7 7 7 7 7 c . 
                        c 6 6 6 c 6 7 7 7 7 7 7 7 7 6 c 
                        c 6 6 6 c 7 7 7 c 6 6 6 6 c 7 c 
                        c 6 6 6 f 7 7 7 c c 6 6 c c 7 f 
                        c 6 6 6 f 7 7 7 6 f 6 6 f 6 7 f 
                        . c 6 6 f 6 7 7 7 7 7 7 7 7 f . 
                        . c c 6 6 f 6 7 c 1 f f c 1 c . 
                        . . . c c c c c c c c c c c c .
            """)],
        100,
        False)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# This block chain creates the players, map, and enemy
Snake: Sprite = None
Enemies: List[Sprite] = []
chosen_enemy: Sprite = None
p1Distance = 0
p2Distance = 0
player2Health: StatusBarSprite = None
player1Health: StatusBarSprite = None
player2: Sprite = None
player1: Sprite = None
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
animation.run_image_animation(player1,
    [img("""
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
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . f f e 2 f f f f f f 2 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f b f 4 4 f b f e f . . 
                . . f e 4 1 f d d f 1 4 e f . . 
                . . . f e 4 d d d d 4 e f e . . 
                . . f e f 2 2 2 2 e d d 4 e . . 
                . . e 4 f 2 2 2 2 e d d e . . . 
                . . . . f 4 4 5 5 f e e . . . . 
                . . . . f f f f f f f . . . . . 
                . . . . f f f . . . . . . . . .
        """),
        img("""
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
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f e e 2 2 2 2 2 2 e f f . . 
                . f f e 2 f f f f f f 2 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f b f 4 4 f b f e f . . 
                . . f e 4 1 f d d f 1 4 e f . . 
                . . e f e 4 d d d d 4 e f . . . 
                . . e 4 d d e 2 2 2 2 f e f . . 
                . . . e d d e 2 2 2 2 f 4 e . . 
                . . . . e e f 5 5 4 4 f . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . f f f . . . .
        """)],
    500,
    True)
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
animation.run_image_animation(player2,
    [img("""
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
        img("""
            . . . . . . . f f . . . . . . . 
                . . . . . f f 4 4 f f . . . . . 
                . . . . f 5 4 5 5 4 5 f . . . . 
                . . . f e 4 5 5 5 5 4 e f . . . 
                . . f b 3 e 4 4 4 4 e 3 b f . . 
                . f e 3 3 3 3 3 3 3 3 3 3 e f . 
                . f 3 3 e b 3 e e 3 b e 3 3 f . 
                . f b 3 f f e e e e f f 3 b f . 
                f f b b f b f e e f b f b b f f 
                f b b b e 1 f 4 4 f 1 e b b b f 
                . f b b e e 4 4 4 4 4 f b b f . 
                . . f 4 4 4 e d d d b f e f . . 
                . . f e 4 4 e d d d d c 4 e . . 
                . . . f e e d d b d b b f e . . 
                . . . f f 1 d 1 d 1 1 f f . . . 
                . . . . . f f f b b f . . . . .
        """),
        img("""
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
        img("""
            . . . . . . . f f . . . . . . . 
                . . . . . f f 4 4 f f . . . . . 
                . . . . f 5 4 5 5 4 5 f . . . . 
                . . . f e 4 5 5 5 5 4 e f . . . 
                . . f b 3 e 4 4 4 4 e 3 b f . . 
                . f e 3 3 3 3 3 3 3 3 3 3 e f . 
                . f 3 3 e b 3 e e 3 b e 3 3 f . 
                . f b 3 f f e e e e f f 3 b f . 
                f f b b f b f e e f b f b b f f 
                f b b b e 1 f 4 4 f 1 e b b b f 
                . f b b f 4 4 4 4 4 e e b b f . 
                . . f e f b d d d e 4 4 4 f . . 
                . . e 4 c d d d d e 4 4 e f . . 
                . . e f b b d b d d e e f . . . 
                . . . f f 1 1 d 1 d 1 f f . . . 
                . . . . . f b b f f f . . . . .
        """)],
    100,
    True)
controller.player1.move_sprite(player1, 100, 100)
controller.player2.move_sprite(player2, 100, 100)
info.player1.set_life(3)
info.player2.set_life(3)
info.player1.set_score(0)
info.player2.set_score(0)
scene.camera_follow_sprite(player1)
player1Health = statusbars.create(20, 4, StatusBarKind.health)
player1Health.set_color(3, 2)
player1Health.value = 100
player1Health.attach_to_sprite(player1, -22, 0)
player2Health = statusbars.create(20, 4, StatusBarKind.health)
player2Health.set_color(3, 2)
player2Health.value = 100
player2Health.attach_to_sprite(player2, -22, 0)
# This block chain creates an enemy array, and uses that array to limit the amount of enemies. This also programs the enemies so that they follow the players.

def on_update_interval():
    global Enemies, Snake
    player2.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    Enemies = sprites.all_of_kind(SpriteKind.enemy)
    # This programs the enemies to follow the player
    for value in Enemies:
        value.follow(EnemyFollowing(value), randint(70, 90))
        if value.overlaps_with(player2):
            value.follow(player2, 0)
        if value.overlaps_with(player1):
            value.follow(player1, 0)
        EnemyFollowing(value)
    # This creates multiple enemies and also limits the amount of enemies in the game
    while len(Enemies) < 7:
        Snake = sprites.create(img("""
                . . . . . . c c c c c c . . . . 
                            . . . . . c 6 7 7 7 7 6 c . . . 
                            . . . . c 7 7 7 7 7 7 7 7 c . . 
                            . . . c 6 7 7 7 7 7 7 7 7 6 c . 
                            . . . c 7 7 7 c 6 6 6 6 c 7 c . 
                            . . . f 7 7 7 6 f 6 6 f 6 7 f . 
                            . . . f 7 7 7 7 7 7 7 7 7 7 f . 
                            . . c f 6 7 7 c 6 7 7 7 7 f . . 
                            . c 7 7 f 6 7 7 c c c c f . . . 
                            c 7 7 7 7 f c 6 7 7 7 2 7 c . . 
                            c c 6 7 7 6 c f c 7 7 2 7 7 c . 
                            . . c 6 6 6 c c f 6 7 1 1 1 1 c 
                            . . f 6 6 6 6 c 6 6 1 1 1 1 1 f 
                            . . f c 6 6 6 6 6 1 1 1 1 1 6 f 
                            . . . f 6 6 6 1 1 1 1 1 1 6 f . 
                            . . . . f c c c c c c c c c . .
            """),
            SpriteKind.enemy)
        Snake.set_position(randint(0, scene.screen_width()),
            randint(0, scene.screen_height()))
        animation.run_image_animation(Snake,
            [img("""
                    . . . . . . c c c c c c . . . . 
                                . . . . . c 6 7 7 7 7 6 c . . . 
                                . . . . c 7 7 7 7 7 7 7 7 c . . 
                                . . . c 6 7 7 7 7 7 7 7 7 6 c . 
                                . . . c 7 7 7 c 6 6 6 6 c 7 c . 
                                . . . f 7 7 7 6 f 6 6 f 6 7 f . 
                                . . . f 7 7 7 7 7 7 7 7 7 7 f . 
                                . . c f 6 7 7 c 6 7 7 7 7 f . . 
                                . c 7 7 f 6 7 7 c c c c f . . . 
                                c 7 7 7 7 f c 6 7 7 7 2 7 c . . 
                                c c 6 7 7 6 c f c 7 7 2 7 7 c . 
                                . . c 6 6 6 c c f 6 7 1 1 1 1 c 
                                . . f 6 6 6 6 c 6 6 1 1 1 1 1 f 
                                . . f c 6 6 6 6 6 1 1 1 1 1 6 f 
                                . . . f 6 6 6 1 1 1 1 1 1 6 f . 
                                . . . . f c c c c c c c c c . .
                """),
                img("""
                    . . . . . . . c c c c c c . . . 
                                . . . . . . c 6 7 7 7 7 6 c . . 
                                . . . . . c 7 7 7 7 7 7 7 7 c . 
                                . . . . c 6 7 7 7 7 7 7 7 7 6 c 
                                . . . . c 7 7 7 c 6 6 6 6 c 7 c 
                                . . . . f 7 7 7 6 f 6 6 f 6 7 f 
                                . . . . f 7 7 7 7 7 7 7 7 7 7 f 
                                . . . . f 6 7 7 c 6 7 7 7 7 f . 
                                . . c c c f 6 7 7 c c c c f . . 
                                . c 7 7 7 c c f 7 7 7 2 6 c . . 
                                c 7 7 7 7 6 f c 7 7 2 7 7 6 c . 
                                c c c 6 6 6 c 6 6 7 1 1 1 1 c . 
                                . . c 6 6 6 6 6 6 1 1 1 1 1 c . 
                                . . c 6 6 6 6 6 1 1 1 1 1 6 c . 
                                . . c c 6 6 7 1 1 1 1 1 6 c . . 
                                . . . c c c c c c c c c c . . .
                """)],
            500,
            True)
game.on_update_interval(100, on_update_interval)
