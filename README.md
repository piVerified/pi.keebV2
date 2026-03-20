![oled](https://github.com/piVerified/pi.keebV2/blob/main/assets/pi.keebv2%20banner.jpg)

# pi.keeb V2

Introducing pi.keebV2 better, more compact and stable version of pi.keeb, this one introduces shortcuts that is very helpfull for live streaming or recording by youreself! Heavily inspired by the [Treasure type 9 design](https://treasuretypes.com/products/type9)
---
Demo: SOON!
---
# Features

1. nine total keys that are mapped to streaming and recording specific use case. 

|    record   | pause | terminate |
| :---------: | :---: | :-------: |
|   go live   | clip  | scrrenshot|
|   stream    |  mute |     -     |


## BOM

1. white blank DSA keycaps 9x -> Self sourced
2. MX-Style switches 9x -> Self sourced
3. through-hole 1N4148 Diodes 9x -> Self sourced
4. PCB -> linked in STASIS
5. ESP32-C3 -> Linked in stasis
6. 3d printed case + plate -> linked in stasis
7. 4X M3X6 screws -> linked in stasis

##3D

### 1. case + plate

|                                         Top                                         |                                         Side                                          |
| :---------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![Top view](https://github.com/piVerified/pi.keebV2/blob/main/assets/top.png) | ![Side VIew](https://github.com/piVerified/pi.keebV2/blob/main/assets/side.png) |
### 2. Assembeld

|                                           Top                                           |                                           Side                                            |
| :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: |
| ![Top view](https://github.com/piVerified/pi.keebV2/blob/main/assets/top1.png) | ![Side VIew](https://github.com/piVerified/pi.keebV2/blob/main/assets/side1.png) |

---
## KiCAD


|                                       Schematic                                        |
| :------------------------------------------------------------------------------------: |
| ![Schematic](https://github.com/piVerified/pi.keebV2/blob/main/assets/Screenshot%202026-03-19%20204305.png) |
|                                          PCB                                           |
|  ![Schematic](https://github.com/piVerified/pi.keebV2/blob/main/assets/Screenshot%202026-03-19%20204412.png)  |

---
# Softwares Used

* KiCAD -> PCB Design
* Fusion 360 -> Case design
* Blender -> Thumbnail image
* Photopea -> For editing the thumbnail and other graphics
---
# BOM


| Name | Purpose | Cost Per Item (USD) | Quantity | Total (USD) | Distributor | Link |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Type C Cable** | Debugging | $1.50 | 1 | $1.50 | Amazon | [View Item](https://www.amazon.in/HAMMER-Braided-Chraging-Compatible-Enabled/dp/B0F9F9CRQK?source=ps-sl-shoppingads-lpcontext&th=1) |
| **PCB** | Main circuitry | $2.05 | 5 | $10.25 | Robu | [View Item](https://robu.in/cart/) |
| **Enclosure + Plate** | Component housing | $1.00 | 1 | $1.00 | #printingLegion | [View Item](https://hackclub.enterprise.slack.com/archives/C095YP8GLKT) |
| **M3X6 Screws** | To screw the PCB | $0.05 | 50 | $2.50 | Only Screws | [View Item](https://onlyscrews.in/products/chhd-m3-x-6mm-pack-of-22?variant=48458858889529) |
| **ESP32-C3 Mini** | Microcontroller | $4.02 | 1 | $4.02 | Amazon | [View Item](https://www.amazon.in/ESP32-Mini-Development-Board-Compatibility/dp/B0GQC8T6HV/260-5280188-7733568?pd_rd_w=WFsq0&content-id=amzn1.sym.e84a26b2-5470-42e6-b7fa-162e7bb17185&pf_rd_p=e84a26b2-5470-42e6-b7fa-162e7bb17185&pf_rd_r=KPN97KBDS1VZR7RX0Y6P&pd_rd_wg=9SVMn&pd_rd_r=f36e5fa7-8011-4993-8ceb-c25d20907ea4&pd_rd_i=B0GQC8T6HV&psc=1) |
| **TOTAL** | | | | **$19.27** | | |


> **Note:** For the **M3X6 screws**, bulk ordering being more cost-effective! I've calculated the total based on the quantity of 50.


---
# Bibliography

> The enourmose library of macropad inspired me to make a better version of my maccropad. Thanks to the peeps of hackclub and specially STASIS.
>
>I used ai to find out more about the Controller learn about key matrix, how to code QMK for my keyboard and some basic information (i wanted to be completely transparent about the use of ai in this project)
