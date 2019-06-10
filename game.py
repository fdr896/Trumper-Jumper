import pygame as pg
from random import randint
pg.init()


disp_w = 1200
disp_h = 1000
win = pg.display.set_mode((disp_w, disp_h))
pg.display.set_caption('TRUMPER JUMPER')
dark = pg.Surface((1200, 1000), flags=pg.SRCALPHA)
dark.fill((90, 90, 90, 0))


clock = pg.time.Clock()
fps = 40


bg = pg.image.load('static/bg.png')


mob = pg.image.load('Donald/idle.png')

mob_width = mob.get_width()
mob_height = mob.get_height()

mob_right_sprites = []
for i in range(1, 7):
	mob_right_sprites.append(pg.image.load('Donald/right_' + str(i) + '.png'))
mob_left_sprites = []
for i in range(1, 7):
	mob_left_sprites.append(pg.image.load('Donald/left_' + str(i) + '.png'))


x_start = disp_w // 2 - 200
y_start = disp_h // 2
x = x_start
y = y_start
speed = 7
R = 50
jump_count = 0
is_started = 0
direction = 1
y_speed = 3
up = 40
down = disp_h - 35
left = 30
right = disp_w - 10
_count = 0
side = randint(0, 1)
bad_side = 1 - side
let_h = 100
let_bad_h = 100
let_w = 10
score = 0
game_over = False
pause = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
cur_h = randint(2 * R, disp_h - 3 * let_h)
bad_h = randint(2 * R, disp_h - 2 * let_bad_h)



def draw_mob():
	global _count
	if direction == 0:
		win.blit(mob, (x, y))
	elif direction == 1:
		win.blit(mob_right_sprites[_count // 5], (x - 25, y - 30))
		_count = (_count + 1) % 30
	else:
		win.blit(mob_left_sprites[_count // 5], (x - 25, y - 30))
		_count = (_count + 1) % 30



def render_text(text, font, sz, color):
    font = pg.font.SysFont(font, sz)
    text = font.render(text, 1, color)
    return text



def get_width(text, font, sz):
    font = pg.font.SysFont(font, sz)
    text = font.render(text, 1, BLACK)
    return text.get_width()



def get_height(text, font, sz):
    font = pg.font.SysFont(font, sz)
    text = font.render(text, 1, BLACK)
    return text.get_height()



def draw_text_center(text, font, sz, color, y_cnt):
    _text = render_text(text, font, sz, color)
    width = get_width(text, font, sz)
    x_cnt = (disp_w - width) // 2

    win.blit(_text, (x_cnt, y_cnt))



def draw_text(text, font, sz, color, x_cnt, y_cnt):
    _text = render_text(text, font, sz, color)

    win.blit(_text, (x_cnt, y_cnt))



def get_random_height(let_h):
    fst = 0
    if 2 * R < y - R // 2 - let_h:
        fst = randint(2 * R, y - R // 2 - let_h)
    
    scd = 0
    if y + R // 2 < disp_h - 3 * let_h:
        scd = randint(y + R // 2, disp_h - 3 * let_h)
    
    if not fst:
        return scd
    if not scd:
        return fst
    return [fst, scd][randint(0, 1)]



def print_rules(text, level, font_color):
        global score

        font = 'jelle'
        _score = 'SCORE: ' + str(score)
        symbols_in_line = get_width(_score, font, 60)
        rules = text.split(' ')
        for i in range(len(rules)):
            rules[i] += ' '
        
        cur_x = (disp_w - symbols_in_line) // 2
        cur_y = disp_h // 2 - 425 + get_height(_score, font, 60)
        cur_len = 0
        
        draw_text('RULES:', font, 30, font_color, cur_x, cur_y)
        
        for word in rules:
            wid = get_width(word, font, 30)
            if wid + cur_len <= symbols_in_line and word[0] != '-':
                cur_len += wid 
                draw_text(word, font, 30, font_color, cur_x, cur_y)
                cur_x += wid
            else:
                cur_len = wid
                cur_x = (disp_w - symbols_in_line) // 2
                cur_y += 30 + 5 * (word[0] == '-')
                draw_text(word, 'jelle', 30, font_color, cur_x, cur_y)
                cur_x += wid



run = True

while run:
    clock.tick(fps)

    if not game_over:
        cur_x = [0, disp_w - let_w][side]
        bad_x = [0, disp_w - let_w][bad_side]

        win.blit(bg, (0, 0))

        pg.draw.rect(win, (255, 0, 0), (0, 0, disp_w, 20))
        pg.draw.rect(win, (255, 0, 0), (0, disp_h - 20, disp_w, 20))

        _score = 'SCORE: ' + str(score)
        _speed = 'SPEED: ' + str(speed)
        draw_text(_speed, 'jelle', 30, WHITE, 1075, 30)
        draw_text_center(_score, 'jelle', 60, (255, 255, 0), 50)

        pg.draw.rect(win, (0, 255, 0), (cur_x, cur_h, let_w, let_h))
        pg.draw.rect(win, (255, 0, 0), (bad_x, bad_h, let_w, let_bad_h))
        pg.draw.circle(win, (255, 200, 0), (x, y), 50)
        draw_mob()

        if pause:
            win.blit(dark, (0, 0), special_flags=pg.BLEND_RGB_SUB)
            draw_text("Press Space or Up-arrow to play", 'jelle', 30, WHITE, 20, 30)
            print_rules("-Use Left-arrow and Right-arrow to change direction of ball`s movement -Use Up-arrow or Space to jump -Hit green rectangles -Don`t touch red surface and rectangles -Press 'Esc' to close the game", score, WHITE)
        else:
            draw_text("Press 'f' to pause", 'jelle', 30, WHITE, 20, 30)
    else:
        pg.draw.rect(win, (0, 0, 0), (0, 0, disp_w, disp_h))
        bad_message = 'GAME OVER'
        play_again = "(Press Space or Up-arrow to play again)"
        draw_text_center(bad_message, 'jelle', 150, WHITE, 300)
        draw_text_center(play_again, 'jelle', 40, WHITE, 410)
    
    pg.display.flip()

    for event in pg.event.get():
        tp = event.type

        if tp == pg.QUIT:
            run = False
            pg.quit()

    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        run = False
        pg.quit()

    if not game_over:
        if keys[pg.K_f]:
            if pause == False:
                pause = True
    
        if keys[pg.K_UP] or keys[pg.K_SPACE]:
            if pause == True:
                pause = False
    
        if pause == True:
            pass
        else:
            y -= jump_count ** 2 // 2
            y += y_speed
            y_speed += 1
            x += direction * speed

            if side == 0 and x - R <= cur_x + let_w and y in range(cur_h, cur_h + let_h):
                side = randint(0, 1)
                bad_side = 1 - side
                speed += 2
                score += 1
                cur_h = get_random_height(let_h)
                bad_h = get_random_height(let_bad_h)
            if side == 1 and x + R >= cur_x and y in range(cur_h, cur_h + let_h):
                side = randint(0, 1)
                bad_side = 1 - side
                speed += 2
                score += 1
                cur_h = get_random_height(let_h)
                bad_h = get_random_height(let_bad_h)

            if y + R // 2 >= down or y - R // 2 <= up:
                game_over = True
                continue
            
            if side == 1 and x - R <= bad_x + let_w and y in range(bad_h, bad_h + let_bad_h):
                game_over = True
                continue

            if side == 0 and x + R >= bad_x and y in range(bad_h, bad_h + let_bad_h):
                game_over = True
                continue
            
            if keys[pg.K_RIGHT]:
                direction = 1
            if keys[pg.K_LEFT]:
                direction = -1

            if x - R // 2 <= left:
                direction = 1
            if x + R >= right:
                direction = -1



            if not is_started:
                if keys[pg.K_UP] or keys[pg.K_SPACE]:
                    is_started = 1
                    y_speed = 3
                    jump_count = 10
            else:
                jump_count -= 1
                if jump_count == 0:
                    is_started = 0
    else:
        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            game_over = False
            score = 0
            speed = 7
            x = x_start
            y = y_start
            pause = True
