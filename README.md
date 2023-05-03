# AutoFisher
This code allows you to automate fishing in a game. This fishing game is simple, you have a yellow line and if it goes to the blue rectangle u have to press the big white cercle. you do this until you have catch a fish. 

![image](https://user-images.githubusercontent.com/89668373/235968973-0640f012-e329-4bd7-9109-8625d89d81c7.png)

First of all, it requires the necessary libraries, such as OpenCV for image processing, pyautogui for click-and-key simulation, and keyboard for key detection.

Then, it loads a reference image (template) that corresponds to the appearance of the yellow line on the blue square. It also defines the dimensions of the game (x, y, w, h).

At each iteration, the program takes a screenshot of the specified play area and milks it to detect the presence of the yellow line on the blue square. If the result is greater than or equal to 0.8 (which means the yellow line is on the blue square), the program simulates a click on the fishing button (the big white circle).
![image](https://user-images.githubusercontent.com/89668373/235973652-5d2ff4db-44ce-4bf5-b573-a24a65c082c3.png)





