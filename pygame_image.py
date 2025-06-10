import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True,False)
    bg_img12 = pg.image.load("fig/pg_bg.jpg")
    koukaton3_img = pg.image.load("fig/3.png")
    koukaton3_img = pg.transform.flip(koukaton3_img,True,False)
    koukaton3_rct = koukaton3_img.get_rect()
    koukaton3_rct.center = 300, 200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, [-tmr + 1600, 0])
        screen.blit(bg_img12, [-tmr + 3200, 0])
        screen.blit(koukaton3_img,koukaton3_rct)
        if tmr > 3199:
            tmr = 0 
        if key_lst[pg.K_UP]:
            koukaton3_rct.move_ip((0,-1))
        elif key_lst[pg.K_DOWN]:
            koukaton3_rct.move_ip((0,+1))
        elif key_lst[pg.K_RIGHT]:
            koukaton3_rct.move_ip((+1,0))
        elif key_lst[pg.K_LEFT]:
            koukaton3_rct.move_ip((-1,0))
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()