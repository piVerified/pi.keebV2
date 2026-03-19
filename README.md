![oled](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/thumbnail.png?raw=true)

# pi.keeb

meet pi.keeb my first hardware project, all thanks to the nice peeps at the Hack CLub, this macro pad acts as multi action keypad, can launch apps, turn up and down the volume and all other normal macro pad stuff. Heavily inspired by the [Treasure type 9 design](https://treasuretypes.com/products/type9), with a touch of functionality!
---
Demo: [https://github.com/piVerified/pi.keeb/blob/main/assets/cpmpressed-est.mov](https://youtu.be/ANN9QJmfbyw)

---
# Features

1. Six total keys that can be mapped to do anything, in my use case i have mapped 

|    copy     | paste |
| :---------: | :---: |
| calculatior | edge  |
|   Spotify   |       |
2. The encoder is for Volume UP, Volume Down And defn
3. The Oled Display shows the pi x hackclub logo!
## BOM

![oled](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/pi%20keeb%20manual.png?raw=true)

1. white blank DSA keycaps 6x
2. Knob Enclosure -> I'll print it on my own!
3. MX-Style switches 6x
4. 0.91 inch OLED display 1x
5. through-hole 1N4148 Diodes 7x
6. EC11 Rotary encoder 1x
7. PCB
8. unsoldered Seeed XIAO RP2040
9. 3d printed keyboard case
## Fusion 360

### 1. Assembled

|                                         Top                                         |                                         Side                                          |
| :---------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![Top view](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/top.png?raw=true) | ![Side VIew](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/side.png?raw=true) |
### 2. Case

|                                           Top                                           |                                           Side                                            |
| :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: |
| ![Top view](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/caseTOp.png?raw=true) | ![Side VIew](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/caseside.png?raw=true) |

---
## KiCAD


|                                       Schematic                                        |
| :------------------------------------------------------------------------------------: |
| ![Schematic](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/schem.png?raw=true) |
|                                          PCB                                           |
|  ![Schematic](https://github.com/TreakeeOG/pi.keeb/blob/main/assets/pcb.png?raw=true)  |

---
# Softwares Used

* KiCAD -> PCB Design
* Fusion 360 -> Case design
* Blender -> Thumbnail image
* Photopea -> For editing the thumbnail and other graphics

---
# Bibliography

> This project would not have been possible without the help of the amazing people of the internet, the blueprint guide and a bit of AI
>
>I used ai to find out more about the Controller learn about key matrix, how to code QMK for my keyboard and some basic information (i wanted to be completely transparent about the use of ai in this project)
