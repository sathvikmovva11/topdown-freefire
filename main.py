@namespace
class SpriteKind:
    background_objects = SpriteKind.create()

def on_up_repeated():
    roy_player.y += -5
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        roy_player,
        100,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    roy_player.x += 5
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_down_repeated():
    roy_player.y += 5
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    roy_player.x += -5
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

projectile: Sprite = None
roy_player: Sprite = None
info.set_score(0)
info.set_life(3)
scene.set_background_color(13)
tree_2 = sprites.create(img("""
        ................86..................
            ...........6688867886...............
            ...........8666877688868............
            ............868777767768............
            .........688667777776688............
            ........67767777777778666...........
            .........6776667767666868...........
            ..........866667667677688...........
            .........8666666666667778...........
            ........667766666666666676..........
            .......67766667666776667776.........
            ......886667776676777666688.........
            .....67766777667767777666768........
            ....6776666666777667776666776.......
            .....8667776667766676677776776......
            ......8777666666667776777776688.....
            ....6887766776677677777777776776....
            ..8866666677767777777777766666778...
            .86666666777667767777766666776668...
            ..88677666666777677677666667776668..
            ..86776677666666666666667776666668..
            886666677766667666666776677766668...
            6668666676667766767767766677666668..
            88866666666777677677667666666776668.
            .86668866666766776776666667766666668
            .86688666666666776666667667776666688
            .668866666666666666666677666666688..
            ..8866686666666666677667776666668...
            ...866886666666666677667776666668...
            ...86886668666666667666666666888....
            ....88866886686666666666666668......
            ......86886668666866668666868.......
            ......88866688668866688866888.......
            ........8888888688888ce868..........
            ..............e88e88.ec.8...........
            ...............eeee..e..............
            ...............ceef.ce..............
            ...............ceefcec..............
            ...............feefce...............
            ...............fceeec...............
            ...............ffceec...............
    """),
    SpriteKind.background_objects)
rock = sprites.create(img("""
        . . . . . c c b b b . . . . . . 
            . . . . c b d d d d b . . . . . 
            . . . . c d d d d d d b b . . . 
            . . . . c d d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . c c c c b b b b d d d b b b . 
            . c d d b c b b b b b b b b d b 
            c b b d d d b b b b b d d b d b 
            c c b b d d d d d d d b b b d c 
            c b c c c b b b b b b b d d c c 
            c c b b c c c c b d d d b c c b 
            . c c c c c c c c c c c b b b b 
            . . c c c c c b b b b b b b c . 
            . . . . . . c c b b b b c c . . 
            . . . . . . . . c c c c . . . .
    """),
    SpriteKind.background_objects)
rock_2 = sprites.create(img("""
        . . . . . c c b b b . . . . . . 
            . . . . c b d d d d b . . . . . 
            . . . . c d d d d d d b b . . . 
            . . . . c d d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . c c c c b b b b d d d b b b . 
            . c d d b c b b b b b b b b d b 
            c b b d d d b b b b b d d b d b 
            c c b b d d d d d d d b b b d c 
            c b c c c b b b b b b b d d c c 
            c c b b c c c c b d d d b c c b 
            . c c c c c c c c c c c b b b b 
            . . c c c c c b b b b b b b c . 
            . . . . . . c c b b b b c c . . 
            . . . . . . . . c c c c . . . .
    """),
    SpriteKind.background_objects)
rock_3 = sprites.create(img("""
        . . . . . c c b b b . . . . . . 
            . . . . c b d d d d b . . . . . 
            . . . . c d d d d d d b b . . . 
            . . . . c d d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . . . c b b d d d d d d d b . . 
            . c c c c b b b b d d d b b b . 
            . c d d b c b b b b b b b b d b 
            c b b d d d b b b b b d d b d b 
            c c b b d d d d d d d b b b d c 
            c b c c c b b b b b b b d d c c 
            c c b b c c c c b d d d b c c b 
            . c c c c c c c c c c c b b b b 
            . . c c c c c b b b b b b b c . 
            . . . . . . c c b b b b c c . . 
            . . . . . . . . c c c c . . . .
    """),
    SpriteKind.background_objects)
tree = sprites.create(img("""
        ........................
            ...........88...........
            ..........8668..........
            .........886688.........
            .........866668.........
            ........86666668........
            ......886666666688......
            .....86666666666668.....
            .....88666666666688.....
            .....86666666666668.....
            ....8668866666888668....
            ....8888668886686888....
            .....86868868868668.....
            ....866888668888868.....
            ....8688886888888888....
            ....8886688888866888....
            ....8666888868886668....
            ...866688686686886668...
            ..8666666666686666668...
            .866866666666666666668..
            .8886666666666666666868.
            .8866666666666666666688.
            ..886686668668666686668.
            ..8688668886688686688668
            .86688688686866888688888
            8668868866888866888868..
            88886686688888868688668.
            .8888888888888888668868.
            .8866688668868868868688.
            .86668866688668666666688
            866666666686666666666668
            88866686666666666866688.
            ..88886686666666668888..
            .....86886686668868.....
            ......8886888668888.....
            .........88ee88.........
            .........feeeef.........
            .........feeeef.........
            ........feeefeef........
            ........fefeffef........
    """),
    SpriteKind.background_objects)
roy_player = sprites.create(img("""
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
ghost = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ..........ffff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
tree_2.set_position(116, 38)
rock_2.set_position(103, 55)
tree.set_position(16, 97)
rock.set_position(34, 43)
rock_3.set_position(73, 81)
roy_player.set_position(43, 100)
ghost.set_position(155, -5)
ghost.follow(roy_player)
if projectile.overlaps_with(ghost):
    info.change_score_by(1)
    ghost.set_position(151, randint(0, 112))

def on_forever():
    music.play_melody("E B C5 A B G A F ", 200)
    roy_player.set_bounce_on_wall(True)
forever(on_forever)
