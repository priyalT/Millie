import pygame
from sys import exit

def player_animation():
    global millie_surf, millie_index, is_animating, is_sleeping, sleep_start_time, is_eating, eat_start_time, food_active
    current_time = pygame.time.get_ticks()

    if is_animating:
        if current_time - animation_start_time < 5000:
            millie_index += 0.1
            if millie_index >= len(millie_pet):
                millie_index = 0
            millie_surf = millie_pet[int(millie_index)]
            
            if not pet_music.get_num_channels():
                bg_music.stop()
                pet_music.play()
        else:
            is_animating = False
            millie_surf = millie_stand
            
            
            pet_music.stop()
            bg_music.play(-1)

    elif is_sleeping:
        if current_time - sleep_start_time < 5000:
            frame_index = (current_time // 500) % len(millie_sleep)
            millie_surf = millie_sleep[int(frame_index)]

            if not snore_music.get_num_channels():
                snore_music.play()
        else:
            is_sleeping = False
            millie_surf = millie_stand
            snore_music.stop()

    elif is_eating:
        if current_time - eat_start_time < 4000: 
            frame_index = int((current_time - eat_start_time) / 500) % len(millie_eat_list)
            millie_surf = millie_eat_list[frame_index]
            
            if not chew_music.get_num_channels():  
                chew_music.play()
        else:
            is_eating = False  
            food_active = False 
            millie_surf = millie_stand

            chew_music.stop()

pygame.init()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption('Millie!')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

room_surface = pygame.image.load('graphics/Room.jpg').convert()
floor_surface = pygame.image.load('graphics/floor.jpg').convert()
text_surface = test_font.render('Millie!', False, 'Black')

air_surface = pygame.image.load('graphics/air.png').convert_alpha()
air2_surface = pygame.image.load('graphics/air.png').convert_alpha()
air_x_pos = 500
air2_x_pos = 100

millie = pygame.image.load('graphics/Mil/millie_stand.png').convert_alpha()
millie_stand = pygame.transform.scale(millie, (200, 200))
millie_pet_1 = pygame.image.load('graphics/Mil/millie_pet_1.png').convert_alpha()
millie_pet_1 = pygame.transform.scale(millie_pet_1, (200, 200))
millie_pet_2 = pygame.image.load('graphics/Mil/millie_pet_2.png').convert_alpha()
millie_pet_2 = pygame.transform.scale(millie_pet_2, (200, 200))
millie_pet = [millie_pet_1, millie_pet_2]

millie_sleep_1 = pygame.image.load('graphics/Mil/millie_sleep1.png').convert_alpha()
millie_sleep_1 = pygame.transform.scale(millie_sleep_1, (200, 200))
millie_sleep_2 = pygame.image.load('graphics/Mil/millie_sleep2.png').convert_alpha()
millie_sleep_2 = pygame.transform.scale(millie_sleep_2, (200, 200))
millie_sleep_3 = pygame.image.load('graphics/Mil/millie_sleep3.png').convert_alpha()
millie_sleep_3 = pygame.transform.scale(millie_sleep_3, (200, 200))
millie_sleep_4 = pygame.image.load('graphics/Mil/millie_sleep4.png').convert_alpha()
millie_sleep_4 = pygame.transform.scale(millie_sleep_4, (200, 200))
millie_sleep = [millie_sleep_1, millie_sleep_2, millie_sleep_3, millie_sleep_4]

millie_eat = pygame.image.load('graphics/Mil/millie_eat.png').convert_alpha()
millie_eat = pygame.transform.scale(millie_eat, (200, 200))
millie_eat_1 = pygame.image.load('graphics/Mil/millie_eat1.png').convert_alpha()
millie_eat_1 = pygame.transform.scale(millie_eat_1, (200, 200))
millie_eat_2 = pygame.image.load('graphics/Mil/millie_eat2.png').convert_alpha()
millie_eat_2 = pygame.transform.scale(millie_eat_2, (200, 200))
millie_eat_3 = pygame.image.load('graphics/Mil/millie_eat3.png').convert_alpha()
millie_eat_3 = pygame.transform.scale(millie_eat_3, (200, 200))
millie_eat_list = [millie_eat, millie_eat_1, millie_eat_2, millie_eat_3]

food = pygame.image.load('graphics/Mil/food.png').convert_alpha()
food = pygame.transform.scale(food, (100, 100))
food_x_pos, food_y_pos = 200,200  

millie_index = 0
millie_surf = millie_stand

is_animating = False
animation_start_time = 0
is_sleeping = False
sleep_start_time = 0
food_active = False  
is_eating = False  
eat_start_time = 0

bg_music = pygame.mixer.Sound('audio/strawberry-cake-bg.mp3')
bg_music.play(loops=-1)
pet_music = pygame.mixer.Sound('audio/pet.mp3')
chew_music = pygame.mixer.Sound('audio/chewing.mp3')
snore_music = pygame.mixer.Sound('audio/snore.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_animating:
                is_animating = True
                animation_start_time = pygame.time.get_ticks()
            if event.key == pygame.K_SPACE and not is_sleeping:
                is_sleeping = True
                sleep_start_time = pygame.time.get_ticks()
            if event.key == pygame.K_c and not food_active:  
                food_active = True

    if food_active and not is_eating:
        is_eating = True
        eat_start_time = pygame.time.get_ticks()

    player_animation()

    screen.blit(room_surface, (0, 0))
    screen.blit(floor_surface, (0, 350))
    screen.blit(text_surface, (325, 25))

    air_x_pos += 1
    screen.blit(air_surface, (air_x_pos, -300))
    if air_x_pos == 550:
        air_x_pos = 500
    air2_x_pos += 1
    screen.blit(air2_surface, (air2_x_pos, -300))
    if air2_x_pos == 150:
        air2_x_pos = 100

    screen.blit(millie_surf, (250, 150))

    if food_active:  # Draw food if active
        screen.blit(food, (food_x_pos, food_y_pos))

    pygame.display.update()
    clock.tick(60)