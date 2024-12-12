import pygame
import sys
import os

class Mario:
    def __init__(self):
        pygame.init()
        self.ANCHO, self.ALTO = 800, 600
        self.pantalla = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Pantalla de Inicio - Mario Style")

        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        self.ROJO = (255, 0, 0)
        self.AZUL = (0, 0, 255)

        self.fondo = pygame.image.load(os.path.join("mario", "assets", "mario_background.png"))
        self.fondo = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))

        self.personaje = pygame.image.load(os.path.join("mario", "assets", "mario_sprite.png"))
        self.personaje = pygame.transform.scale(self.personaje, (100, 100))
        self.personaje_direction = 0  # 0 for right, 1 for left

        self.boton_normal = pygame.image.load(os.path.join("mario", "assets", "boton_normal.png"))
        self.boton_seleccionado = pygame.image.load(os.path.join("mario", "assets", "boton_seleccionado.png"))
        self.boton_normal = pygame.transform.scale(self.boton_normal, (300, 60))
        self.boton_seleccionado = pygame.transform.scale(self.boton_seleccionado, (300, 60))

        pygame.mixer.music.load(os.path.join("mario", "assets", "mario_theme.mp3"))
        pygame.mixer.music.play(-1)

        self.efecto_sonido = pygame.mixer.Sound(os.path.join("mario", "assets", "clicked_button.mp3"))

        self.titulo_imagen = pygame.image.load(os.path.join("mario", "assets", "mario_title.png"))
        self.titulo_imagen = pygame.transform.scale(self.titulo_imagen, (600, 150))

        self.fuente_menu = pygame.font.Font(pygame.font.match_font('arial'), 40)  # Add this line

        self.opciones = ["Iniciar Juego", "Opciones", "Salir"]
        self.opcion_seleccionada = 0

        self.personaje_x = 100
        self.personaje_y = self.ALTO - 180
        self.salto = False
        self.velocidad_salto = -15
        self.gravedad = 1

        self.ejecutando = True
        self.en_menu = True
        self.movimiento_izquierda = False
        self.movimiento_derecha = False

    def dibujar_menu(self):
        for i, opcion in enumerate(self.opciones):
            if i == self.opcion_seleccionada:
                self.pantalla.blit(self.boton_seleccionado, (self.ANCHO // 2 - 150, 300 + i * 80))
            else:
                self.pantalla.blit(self.boton_normal, (self.ANCHO // 2 - 150, 300 + i * 80))

            texto = self.fuente_menu.render(opcion, True, self.NEGRO if i != self.opcion_seleccionada else self.ROJO)
            self.pantalla.blit(texto, (self.ANCHO // 2 - texto.get_width() // 2, 310 + i * 80))

    def run(self):
        clock = pygame.time.Clock()
        while self.ejecutando:
            self.pantalla.blit(self.fondo, (0, 0))
            if self.en_menu:
                self.pantalla.blit(self.titulo_imagen, (self.ANCHO // 2 - self.titulo_imagen.get_width() // 2, 100))
                self.dibujar_menu()
            else:
                self.update_game()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False
                elif evento.type == pygame.KEYDOWN:
                    if self.en_menu:
                        self.handle_menu_keydown(evento)
                    else:
                        self.handle_game_keydown(evento)
                elif evento.type == pygame.KEYUP:
                    if not self.en_menu:
                        self.handle_game_keyup(evento)
                elif evento.type == pygame.MOUSEBUTTONDOWN and self.en_menu:
                    self.handle_menu_click(evento)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_menu_keydown(self, evento):
        if evento.key == pygame.K_UP:
            self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
            self.efecto_sonido.play()
        elif evento.key == pygame.K_DOWN:
            self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
            self.efecto_sonido.play()
        elif evento.key == pygame.K_RETURN:
            if self.opcion_seleccionada == 0:
                self.en_menu = False
            elif self.opcion_seleccionada == 1:
                print("Opciones seleccionadas")
            elif self.opcion_seleccionada == 2:
                self.ejecutando = False

    def handle_menu_click(self, evento):
        mouse_x, mouse_y = evento.pos
        for i, opcion in enumerate(self.opciones):
            boton_rect = pygame.Rect(self.ANCHO // 2 - 150, 300 + i * 80, 300, 60)
            if boton_rect.collidepoint(mouse_x, mouse_y):
                if i == 0:
                    self.en_menu = False
                elif i == 1:
                    print("Opciones seleccionadas")
                elif i == 2:
                    self.ejecutando = False

    def handle_game_keydown(self, evento):
        if evento.key == pygame.K_SPACE and not self.salto:
            self.salto = True
        elif evento.key == pygame.K_a:
            self.movimiento_izquierda = True
        elif evento.key == pygame.K_d:
            self.movimiento_derecha = True
        elif evento.key == pygame.K_ESCAPE:
            self.en_menu = True

    def handle_game_keyup(self, evento):
        if evento.key == pygame.K_a:
            self.movimiento_izquierda = False
        elif evento.key == pygame.K_d:
            self.movimiento_derecha = False

    def update_game(self):
        if self.salto:
            self.personaje_y += self.velocidad_salto
            self.velocidad_salto += self.gravedad
            if self.personaje_y >= self.ALTO - 180:
                self.personaje_y = self.ALTO - 180
                self.salto = False
                self.velocidad_salto = -15

        if self.movimiento_derecha:
            self.personaje_x += 5
            if self.personaje_direction == 1:
                self.personaje_direction = 0
                self.personaje = pygame.transform.flip(self.personaje, True, False)
        if self.movimiento_izquierda:
            self.personaje_x -= 5
            if self.personaje_direction == 0:
                self.personaje_direction = 1
                self.personaje = pygame.transform.flip(self.personaje, True, False)

        self.pantalla.blit(self.personaje, (self.personaje_x, self.personaje_y))
