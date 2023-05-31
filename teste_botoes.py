import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.is_clicked = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_clicked = True
                # Aqui você pode adicionar a resposta desejada quando o botão for pressionado

# Exemplo de uso
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

button1 = Button(50, 50, 100, 50, "Botão 1")
button2 = Button(200, 50, 100, 50, "Botão 2")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button1.handle_event(event)
        button2.handle_event(event)

    screen.fill((255, 255, 255))
    button1.draw(screen)
    button2.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
