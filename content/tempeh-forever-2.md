Title: Tempeh Forever
Date: 2025-11-02
Slug: tempeh-forever-2
Category: projects
Tags: raspberrypi,fermentation
Summary: Blah blah blah

####Beans
My doctor told me recently that I probably wasn't eating enough fiber, and suggested that I eat more beans. I eat a lot of rice and beans, but I would really like more options. There is a very good local brand of tempeh that I like to eat, but it's expensive enough that it is usually just a special treat. So I wondered if I could just make my own tempeh.

####Tempeh
I conceived of this project as a manic solution to multiple goals at once. I am interested food fermentation, data analysis, and low-cost embedded systems. I imagined a system that would produce tempeh in a relatively procedural and predictable way, and then give me a dataset that explained the progress. Here are the steps:
1. A tempeh incubator with a temperature control device that would toggle a heating element to maintain the correct temperature. Data regarding the toggling of the element and also ongoing temperature/humidity information would flow to...
2. An MQTT broker that accepts information from the control device and uploads it to...
3. An online SQL server for storage, which can then be queried with...
4. A Python visualization.

####The Controller
I used a pi pico 4W as the incubator controller. It connects to a MAX31865 PT1000 temperature probe, which returns temperature over SPI. When the temperature is too low, a transistor drives a relay, which turns on the heating element, which is an old incandescent lightbulb. When the temperature hits the target, the heat relay turns off. When the temperature gets too high, a separate relay will turn on a fan that circulates air through incubator to cool it back down. A small OLED screen displays target temperature, actual temperature, and the status of wifi and MQTT. Two buttons next to the screen let me increase and decrease the target temperature. A third button lets me toggle MQTT transfer, in case I am debugging and don't want data uploaded.

![Alt text]({static}/images/tempeh_circuit_diagram.png)

Break Break

<figure>
  <img src="{static}/images/tempeh_circuit_diagram.png" style="width:60%">
  <figcaption>Tidy circuit diagram</figcaption>
</figure>

<figure>
  <img src="{static}/images/incubator_wires.png" style="width:60%">
  <figcaption>Circuit IRL</figcaption>
</figure>

####Assembly
The incubator controller is housed in an old tin I had. I connected the relays to a standard power outlet so my heating and cooling devices could be switched out if needed, and the screen is built into the lid. 

I 3D printed several parts, mostly for aesthetics, and these include:
-The plate for the OLED screen and buttons
-The bushing for the power cable and temperature probe to pass through
-The mount for the power outlets
-The cylinder that holds the cooling fan

The box I am using for the incubator itself is an old Tupperware. The tray of beans rests on paracord I strung at mid-height. The tray is a stainless steel baking pan that I drilled a grid of holes into to improve airflow. I put the lightbulb at the bottom, then the tray, then I put the temperature probe on top of the tray, place the lid, place the fan column, and then wrap everything in towels and turn it on.

####MQTT
MQTT is a lightweight messaging protocol often used in IoT devices that works via a system of topics and subscriptions. To send data, I am subscribing to three topics:
tempeh/events/heat - Messaged when the heat is toggled
tempeh/events/fan - Messaged when the fan is toggled
tempeh/measurements - Messaged every minute with current incubator temperature

Data are sent from the pico to a separate raspberry pi that acts as an MQTT broker. The data is read from the MQTT message, converted into a SQL INSERT query, and then sent to a Neon server. I had to use the MQTT broker because I couldn't find a reliable/compact SQL library for picos. 

####Everything together!!

Attempt 1: I soaked garbanzo beans for ~12 hours, and then tried to massage the hulls off because the tempeh mold can't penetrate hulls. I couldn't really get the hulls off and none of the methods mentioned online helped at all. So I made hummus!!

Attempt 2: This time I used 2 lb. of chana dal from an Indian market because it comes already hulled and split. I cooked them, without soaking, until they were slightly less than al dente, which was ~18 minutes. I let them cool and dry, then added 3 Tbsp. of tempeh starter. I put it in the tray, then sealed the tray with foil and poked holes in the foil for airflow. I put it in the incubator at 90 F. About 9 hours later, I notice the lightbulb has been on in the incubator for a very long time. The controller screen appears frozen, and I realize the controller has glitched and stopped running with the lightbulb on. When I restart the controller, it reads 140 degrees. I let it keep running overnight out of curiosity, even though 140 is definitely enough to kill the mold, and it looked like this in the morning:

OVERHEATED PHOTO HERE

A sample of the tempeh around the edges that had not been heat sterilized tasted fine, but I still didn't really consider it safe to eat.

Attempt 3: To avoid glitching, I added more error handling in the controller and also a watchdog timer, which reboots the pico if communication is lost, and then repeated the steps in attempt #2. After ~23 hours, even though the controller was working, the temperature had reached 114 degrees. This happened because the fermentation generates its own heat and the mold had cooked itself to death. The tempeh smelled earthy, sweet, and correct, but certain parts that were touching the baking sheet had the telltale mucilage of bacterial contamination, probably Bacillus subtilis. This happens when there is too much standing water and not enough airflow. Also, tempeh should typically ferment for around 36 hours and because this tempeh had overheated itself early, there was low mycelial density between the grains, and the tempeh was floppy.

Attempt 4: To improve airflow at the bottom of the pan I drilled a grid of holes into the baking sheet. To give the incubator a way to reduce heat, I added a cooling fan. I drilled holes in the bottom of the box, and added a fan column on top of the lid, which the fan sat on top of. I then rewired the controller and outlets to have a second relay that could toggle the fan independently of the heater. Then I edited the code to have a temperature maximum that would turn the fan on, and added an MQTT topic to record these events. When the temperature was under 90, the heat would turn on. When it was above 95, the fan would turn on. Then I repeated the process, and made what I would consider my first decent batch of tempeh:

####Data Analysis



####Conclusion
I am pretty pleased with the tempeh that came out of attempt 4. I made quite a few tempeh reubens. I think I could cook the beans a little more without risking structural degradation. 






Rhizopus oligosporus needs to be grown at around 95°F. The simple approach to achieving the right temperature is to use a temperature probe and heating element, and to turn on the heating element when the temperature is too low, and turn it off when it is too high. One issue with this is that heat often takes time to propagate through a space, so you can overshoot the temperature if you turn it off only when the correct temperature is detected. One solution is to use what is called a PID (proportional-integral-derivative) controller. These use an algorithm that estimate what effect on temperature having the heat element on for a given unit of time has, and they constantly self-adjust. For example, it could estimate that having the heating element on for 20 seconds increases the system temperature by one degree. Then when you need to increase the temperature, you know exactly how long to keep the heat on. These are the gold standard for high precision temperature control. For now, I'm going to completely ignore that and go with the simple approach.

For my incubator, I am going to use a raspberry pi pico that is powering a temperature probe, an LCD screen, and a relay that controls the heating element.






