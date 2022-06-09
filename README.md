# BEN
<p>
  <a href="https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/">
    <img  src="https://c.tenor.com/dQ7a15SpFMsAAAAi/ben-talking.gif"
      width="284" border="0" alt="Mr.Robot">
  </a>
</p>  
  
_This is my final project of TSTI2D._

Project available at : https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/

# Why ?  
Because it was the project who was attribuated to me. There is the problematic :  
  
**The market for the sale and distribution of grocery-type products is constantly evolution ; exclusively in stores of proximity or by traders until 1955
to 1960, then in department stores (supermarkets then hypermarkets) on the outskirts urban.**
  
And then, the question :
  
**How to deliver everyday groceries in urban areas while minimizing environmental impacts while reducing the effort and time spent by customers ?**
  
This project has two interest :
  
- improve user comfort
- contribute to minimizing environmental impacts by reducing the use of thermal cars personal
  
And finnaly a finality :
  
Préparer technologiquement l’évolution sociétale de la distribution des produits courants de type épicerie.
  
# Process
## Repartition
In this project, we were 5 guys with 1 task each.  
List of the tasks :
  
- [**1**] Study, simulate and carry out the control of the motorization and the detection of possible
obstacles.
- [**2**] Study, simulate and carry out motorization control and displacement counting
actually done.
- [**3**] Study, simulate and carry out the local display to the robot (at a minimum) of the status of the missions and the
energy charge rate.
- [**4**] Study, simulate and carry out remote monitoring of the evolution of the robot and the display of
main parameters on a supervision PC.
- [**5**] Studying, simulating and carrying out the authorization of access to products based on the reading of a
QR Code.
  
My task was the number **1**. So, I have made a lot of research and take some notes before starting. I have search how complete my task by the best way without spend too much money. 
## Components
So I choose these components for the realization of the robot :
  
- Raspberry Pi 4 B board - 2 GB
- 32 GB SD card
- US detection module HC-SR04A
- Official 8 MP RB-CAM-V camera
- External USB battery UPBK10002BK
10000 mAh - 1 x 2.1 A, 1 x 1 A and 1 x 3 A
- Buzzer SV3 8 à 15 Vcc - 88 dB
- Cable 10 cm USBC-0.1
- Box + switch 9V BH9VB
- Chassis Robot05
- Motor kit + FIT0450 encoder
- Hat module 2 DC motors 1.2 A DFR0592
- Base Hat for Raspberry Pi Grove
  
You can also count som male-male cable and some female-male cables and also a bredboard coupled with 2 led (  1 green and 1 red )
  
Here is the list of the component with links for shop them : [Liste composants robot livreur.xlsx](https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/files/8856706/Liste.composants.robot.livreur.xlsx)
  
## Diagrams, visualization and schematics
You can find below some realizations graphic that I have made.
![diagram1](/github/ressources/diagram1.png)
<p align="center">
    <img  src="/github/ressources/diagram2.png"
      width="284" border="0" alt="diagram2">
</p>  
  
Here is a global diagram : [global_diagram.pdf](https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/files/8856730/global_diagram.pdf)
## Assembly
### **{0}** First, you need to assemble the Chassis Robot05.    
You can find all the necessary informations in this documentation : [pj2-robot05-manual-2152.pdf](https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/files/8856761/pj2-robot05-manual-2152.pdf)  
Now you should have something like this :  
  
![robot_view1](github/ressources/robot_view1.png)
  
![robot_view1 2](github/ressources/robot_view1.2.png)
  
### **{1}** Then, you can to screw the RPI4 on the frame.    
Logically, you put the necessary cables from the motors and the incremental encoders to the RPI4.  
You can use the documentation of the motors if you need of : https://wiki.dfrobot.com/Micro_DC_Motor_with_Encoder-SJ01_SKU__FIT0450  

### **{2}** To let the RPI4 have a full controll on the motors, you will need to place the Hat module 2 DC motors 1.2 A DFR0592 on the RPI4.     
You just have to place it on the GPIO Pins.  
Their is the documentation if you need of : https://media.digikey.com/pdf/Data%20Sheets/DFRobot%20PDFs/DFR0592_Web.pdf  
  
<img width="503" alt="image" src="https://user-images.githubusercontent.com/106342136/172494346-6143d6fa-5477-463a-ab3c-0d5bd4670309.png">

### **{3}** After that you can set the Official 8 MP RB-CAM-V camera on.  
Their is the full documentation of this camera : https://www.raspberrypi.com/documentation/accessories/camera.html  
Their is the tutorial to plug the camera on the raspberry pi : https://youtu.be/GImeVqHQzsE  
  
At this point, the robot should look like this :  
  
![A99E7CE3-EA6E-456D-961F-D8452D249BF6](https://user-images.githubusercontent.com/106342136/172496409-6143ba47-de84-4574-ab16-8bf3e5b40bc7.jpg)
![FFC60ECD-9BDC-44A2-B54E-8186BE430D75](https://user-images.githubusercontent.com/106342136/172496414-1f30b774-8ce9-414a-a922-1ed4f47b2a45.jpg)

### **{4}** Set the Base Hat for Raspberry Pi Grove.  
You just have to set it on the GPIO Pins.  
Their is the documentation : https://wiki.seeedstudio.com/Grove_Base_Hat_for_Raspberry_Pi/

### **{5}** Add the US detection module HC-SR04A ultrasonic sensors.  
You have to plug them on the hat set just before. Be sure to plug them on the same ports as indicated in the code.
Their is the documentation : https://www.gotronic.fr/pj2-hc-sr04-utilisation-avec-picaxe-1343.pdf

### **{6}** Plug the necessary cables from the RPI4 to the breadboard, add some leds and the buzzer.  
As the pictures below, plug the necessary cables, the leds and the buzzer.  
  
![IMG_3574](https://user-images.githubusercontent.com/106342136/172499657-29e99176-7738-4a2a-a345-f7d6fb3ef40c.png)

![IMG_3577](https://user-images.githubusercontent.com/106342136/172499641-9fe23b89-57cb-4a13-bfd7-6ed22440f9f4.png)

![IMG_3576](https://user-images.githubusercontent.com/106342136/172499687-5a8b5694-ee32-4a2b-889b-d1a97dcc4d29.png)

https://user-images.githubusercontent.com/106342136/172499908-4467ca10-2061-4d7c-924a-72f77053643a.mov


### **{7}** Add the External USB battery UPBK10002BK 10000 mAh - 1 x 2.1 A, 1 x 1 A and 1 x 3 A and the accumulator in the case.
I recommend that you place the external battery as shown above with a rilsan without overtightening.

## Installation
### **{0}** Raspberry  PI4 configuration.
You will see, that very easy. First, you need to grab your 32 GB SD card and plug it in your desktop. Then, launch your favorite web-browser and download the software "Balena Etcher". Their is the link of the official website : https://www.balena.io/etcher/  
  
Once you have install the software, go to https://raspberry-pi.fr/telechargements/ and download the raspbian image. Don't choose the lite version because it will be more difficult to connect at the wifi because it's a version with only the terminal, so their are no graphical part. But if you want you can choose the lite version and connect the raspberry pi at internet with a Ethernet cable during the download of libraries.  
  
Now, launch Balena Etcher, choose your SD card in the devicees detected, choose the raspbian image you just have download and start flashing your SD card. As soon as the flash process is finish, remove the SD card and plug it in the RPI4. If you need more detailled explanations with visuals, check this video : https://www.youtube.com/watch?v=En3C6uccixw  
  
You can boot the RPI4 by link him on a screen, connect the power bank, a keyboard and a mouse. Now you arrived on the desktop menu.
  
![Raspbian_2019 04_application_menu](https://user-images.githubusercontent.com/106342136/172739344-e9a18cfe-bfe3-41be-a416-842959411f61.jpg)
  
On the upper right you can set up your WIFI. Once your WIFI is configurated, update your RPI4 with these commands runs in the terminal :  
  
`sudo apt update`  
`sudo apt upgrade`
  
note : you can contract this recurring commands by adding "&&" between the two commands and adding "-y" to say yes automaticaly.  
  
`sudo apt update && sudo apt upgrade -y`
  
Okay right, now we can start the instalation of my software solution !

### **{1}** Github clone.  
First, go in the files explorer, in the Documents section and create a new folder with the name indulge yourself, for me it's "BEN". Then, you have to go in this folder by the terminal. For it, we gonna use the `ls` and `cd` command. Write `ls` in the terminal. This command list to you the directories presents in the directory were you are actually. You should see this :  
  
![ls-command-home](https://user-images.githubusercontent.com/106342136/172741128-a356e55a-777d-4e2f-a862-462a19ac3924.png)
  
To go in the Documents directory, write `cd Documents/` ps : you can write the begin of the directory and makes TAB to complete his name and btw safe some time. Now, you can clone properly the Github with this command : 
  
`git clone https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur`
  
Now you gonna need to get some libraries.

### **{2}** Libraries.
If you want that the code executes well, you nedd to add this libraries in the project folder.  
### 


You will need to download a last library who **is not included in my repo.**  
This is the **grove.py** library ( to use arduino script on python ).  
  
Make a **git clone** in your project folder with this command line :  
  
`git clone https://github.com/Seeed-Studio/grove.py`
  
## opencv2
  
You need to download opencv2 if you want run the camera.  
Follow the instructions bellow to install it :  
- Write this commands in the terminal :  

`sudo pip3 install opencv-contrib-python==4.5.5.62`  

`sudo apt install libhdf5-dev libhdf5-serial-dev libhdf5-103`  

`sudo apt install libatlas-base-dev`  

`pip3 install numpy --upgrade --ignore-installed`  

`pip3 install pyzbar`  

`pip3 install qrcode`  

Link of the library repo :es: : https://github.com/ComputadorasySensores/Capitulo53

Good luck STI2D !
