//  This function allows the enemies to follow the closest player
function EnemyFollowing(Enemy: Sprite): Sprite {
    
    p2Distance = Math.sqrt((Enemy.x - player2.x) ** 2 + (Enemy.y - player2.y) ** 2)
    p1Distance = Math.sqrt((Enemy.x - player1.x) ** 2 + (Enemy.y - player1.y) ** 2)
    if (p1Distance > p2Distance) {
        return player2
    } else {
        return player1
    }
    
}

//  This allows the player to destroy the enemy and also animates the player while doing it
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    sprites.destroy(chosen_enemy)
    animation.runImageAnimation(player1, [img`
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
            `, img`
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
            `, img`
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
            `, img`
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
            `], 100, false)
})
//  This creates the chests that give you points
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    info.player1.changeScoreBy(1)
    info.player2.changeScoreBy(1)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    tiles.setTileAt(location, sprites.castle.tileGrass1)
})
//  This ends the game if the players health reaches 0
statusbars.onZero(StatusBarKind.Health, function on_on_zero(status: StatusBarSprite) {
    game.gameOver(false)
})
//  This block of code stores the overlapped enemy into a variable, and also depletes the players health when they overlap an enemy.
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap(sprite2: Sprite, otherSprite: Sprite) {
    
    chosen_enemy = otherSprite
    pause(500)
    player1Health.value += -1
    player2Health.value += -1
    pause(500)
})
//  This block chain creates the players, map, and enemy
let Enemies : Sprite[] = []
let chosen_enemy : Sprite = null
let p1Distance = 0
let p2Distance = 0
let player2Health : StatusBarSprite = null
let player1Health : StatusBarSprite = null
let player2 : Sprite = null
let player1 : Sprite = null
scene.setBackgroundColor(7)
tiles.setCurrentTilemap(tilemap`
    level1
`)
player1 = sprites.create(img`
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
    `, SpriteKind.Player)
player2 = sprites.create(img`
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
    `, SpriteKind.Player)
controller.player1.moveSprite(player1, 100, 100)
controller.player2.moveSprite(player2, 100, 100)
info.player1.setLife(3)
info.player2.setLife(3)
info.player1.setScore(0)
info.player2.setScore(0)
scene.cameraFollowSprite(player1)
let Snake = sprites.create(img`
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
    `, SpriteKind.Enemy)
Snake.setPosition(142, 16)
player1Health = statusbars.create(20, 4, StatusBarKind.Health)
player1Health.setColor(3, 2)
player1Health.value = 100
player1Health.attachToSprite(player1, -22, 0)
player2Health = statusbars.create(20, 4, StatusBarKind.Health)
player2Health.setColor(3, 2)
player2Health.value = 100
player2Health.attachToSprite(player2, -22, 0)
//  This block chain creates an enemy array, and uses that array to limit the amount of enemies. This also programs the enemies so that they follow the players.
game.onUpdateInterval(100, function on_update_interval() {
    
    player2.setFlag(SpriteFlag.StayInScreen, true)
    Enemies = sprites.allOfKind(SpriteKind.Enemy)
    //  This programs the enemies to follow the player
    for (let value of Enemies) {
        value.follow(EnemyFollowing(value), randint(70, 90))
        if (value.overlapsWith(player2)) {
            value.follow(player2, 0)
        }
        
        if (value.overlapsWith(player1)) {
            value.follow(player1, 0)
        }
        
        EnemyFollowing(value)
    }
    //  This creates multiple enemies and also limits the amount of enemies in the game
    while (Enemies.length < 7) {
        Snake = sprites.create(img`
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
            `, SpriteKind.Enemy)
        Snake.setPosition(randint(0, scene.screenWidth()), randint(0, scene.screenHeight()))
        Enemies = sprites.allOfKind(SpriteKind.Enemy)
    }
})
