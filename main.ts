function EnemyFollowing (Enemy: Sprite) {
    p2Distance = Math.sqrt((Enemy.x - player2.x) ** 2 + (Enemy.y - player2.y) ** 2)
    p1Distance = Math.sqrt((Enemy.x - player1.x) ** 2 + (Enemy.y - player1.y) ** 2)
    if (p1Distance > p2Distance) {
        Enemy.follow(player2, 50)
    } else {
        Enemy.follow(player1, 50)
    }
    if (Enemy.overlapsWith(player2)) {
        Enemy.follow(player2, 0)
    }
    if (Enemy.overlapsWith(player1)) {
        Enemy.follow(player1, 0)
    }
}
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    info.player1.changeScoreBy(1)
    info.player2.changeScoreBy(1)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    tiles.setTileAt(location, sprites.castle.tileGrass1)
})
let Enemies: Sprite[] = []
let p1Distance = 0
let p2Distance = 0
let player2: Sprite = null
let player1: Sprite = null
scene.setBackgroundColor(7)
tiles.setCurrentTilemap(tilemap`level1`)
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
controller.player1.moveSprite(player1)
controller.player2.moveSprite(player2)
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
let player1Health = statusbars.create(20, 4, StatusBarKind.Health)
player1Health.setColor(3, 2)
player1Health.value = 100
player1Health.attachToSprite(player1, -22, 0)
let player2Health = statusbars.create(20, 4, StatusBarKind.Health)
player2Health.setColor(3, 2)
player2Health.value = 100
player2Health.attachToSprite(player2, -22, 0)
game.onUpdateInterval(100, function () {
    player2.setFlag(SpriteFlag.StayInScreen, true)
    Enemies = sprites.allOfKind(SpriteKind.Enemy)
    for (let value of Enemies) {
        EnemyFollowing(value)
    }
})
