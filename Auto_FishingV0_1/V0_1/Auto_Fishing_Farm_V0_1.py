
#import
import time
from time import sleep
import cv2
import pyautogui
import keyboard


#template & dimensions
template = cv2.imread("images/test3.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
#longueur et largeur de notre image
template_w, template_h = template_gray.shape[::-1]

#dimensions du jeu
x, y, w, h = 805, 850, 323, 222


#attente
sleep(3)

#main
print("Appuyez sur <Q> pour arreter le programme")

compt = 1
while keyboard.is_pressed('q') == False:

    

    #screenshot
    pyautogui.screenshot("images/image.png", (x, y, w, y))
    image = cv2.imread("images/image.png")

    
    while True:

        #montre ce que l'ecran voit
        #image_mini = cv2.resize(
         #   src = image,
          #  dsize = (805,850)

        #)
        #cv2.imshow("vision", image_mini)
        #cv2.waitKey(10)        

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        resultat = cv2.matchTemplate(
            image = image_gray,
            templ = template_gray,
            method = cv2.TM_CCOEFF_NORMED
        )

        #min_val = pire resultat correspondant
        #max_val = meilleur résultat correspondant
        #min_loc = coordonnees du pire resultat
        #max_loc = coordonnees du meilleur resultat
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultat)

        #threshold - Permet de toujour determiner le meilleur resultat

        if max_val >= 0.8:
            
            #appuie sur le bouton blanc
            pyautogui.click() #958 998

            #designe un carre rouge pour tester
            image = cv2.rectangle(
                img = image,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + template_w,
                    max_loc[1] + template_h
                ),
                color = (0,0,255),
                thickness = -1 #remplis le rectangle
            )

            if pyautogui.locateOnScreen('images/fishingCircle.png', confidence=0.85, region=(850,930,200,200)) == None:
                
                
                print("Vous avez pechee " + str(compt) + " poissons" )
                time.sleep(3)
                keyboard.press('e')
                keyboard.release("e")
                compt += 1
                time.sleep(1)
                pyautogui.click()
                
        
            
        else:
            
            break

print("Total du nombre de poissons pechee : " + str(compt - 1))        
