import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0
    tmr_kk = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        
        tmr_bgx = tmr % 3200
        screen.blit(bg_img2, [-tmr_bgx, 0])
        screen.blit(bg_img, [1600-tmr_bgx,0])
        screen.blit(bg_img2,[3200-tmr_bgx,0])
        
        if tmr % 100==1:
            tmr_kk=(tmr_kk+1)%2
        


        screen.blit(kk_imgs[tmr_kk], [300,200])
        
        pg.display.update()
        clock.tick(100)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()