# Mr.Robot
<p align="center">
  <a href="https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/">
    <img  src="/github/ressources/mrobot.png"
      width="284" border="0" alt="Mr.Robot">
  </a>
</p>  
  
_This is my final project of TSTI2D._

Project available at : https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/

## Why ?  
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
  
## Process
### Repartition
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
### Components
So I choose these components for the realization of the robot :
  
- Raspberry Pi 4 B board - 2 GB
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
  
### Diagrams, visualization and schematics
You can find below some realizations graphic that I have made.
![diagram1](https://user-images.githubusercontent.com/106342136/172487064-a080fab4-54a2-4cb8-98e7-dfe3582bc39a.png)
![diagram2](https://user-images.githubusercontent.com/106342136/172487186-51a61364-4810-4f8d-96e6-c503cb613883.png)
  
Here is a global diagram : [global_diagram.pdf](https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/files/8856730/global_diagram.pdf)
### Assembly
First, you need to assemble the frame. You can find all the necessary informations in this documentation : [pj2-robot05-manual-2152.pdf](https://github.com/lionrayonnant/Mr.Robot-Robot-Livreur/files/8856761/pj2-robot05-manual-2152.pdf)
Now you should have something like this : ![robot_view1](github/ressources/robot_view1.JPG)
![robot_view1 2](github/ressources/robot_view1.2.JPG)


  
  
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
