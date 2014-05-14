import sys, pygame
from itertools import chain

#external code 
def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped
 
 
def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)


#start of code
pygame.init()

#File information
file1 = open('questions.txt', 'r')
file2 = open('answers.txt', 'r')

questions = file1.readlines()
answers = file2.readlines()

size = width, height = 1024, 768
speed = [2, 2]
black = 0, 0, 0
white = 255,255,255
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("arial", 15)

#Define Variables
question = True
questionNumber = 0
questionDisplay = ''

#Game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
	elif event.type == pygame.KEYDOWN:
		if event.key == pygame.K_n or event.key == pygame.K_RIGHT:			
			if question: 
				questionDisplay = questions[questionNumber].strip()
				question = False
			else: 		
				questionDisplay = answers[questionNumber].strip()
				question = True
				if questionNumber + 1 < len(questions):
					questionNumber += 1
				else:
					print('You have reached the end of the list, do you want to enter random Mode?')
					print("Hint, you can do this at any time by pressing 'r'")
		elif event.key == pygame.K_p or event.key == pygame.K_LEFT:
			if question:
				if questionNumber > 0:questionNumber -= 1
				question = False
				questionDisplay = questions[questionNumber].strip()
			else:
				question = True
				questionDisplay = questions[questionNumber].strip()


    # render text
    label = myfont.render(questionDisplay, 1, white)
    #Draw screen
    screen.fill(black)
    screen.blit(label, (10, 10))

    pygame.display.flip()
