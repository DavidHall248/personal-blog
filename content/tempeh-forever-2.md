Title: Tempeh Forever: The Incubator
Date: 2028-08-02
Slug: tempeh-forever-2
Category: projects
Tags: raspberrypi,fermentation
Summary: Blah blah blah

####The Incubator

I used a pi pico 4W as the controller. It connects to a MAX31865 PT1000 temperature probe, which returns temperature over SPI. When the temperature is too low, a transistor drives a relay, which turns on my heating element, which is an old incandescent lightbulb. When the temperature hits the target, the heat relay turns off. When the temperature gets too high, a separate relay will turn on a fan that circulates air through incubator to cool it back down. 

![Alt text]({static}/images/tempeh_circuit_diagram.png)


Data is sent via MQTT to a raspberry pi running as an MQTT broker, which is then sent to a SQL server hosted by Neon.


Rhizopus oligosporus needs to be grown at around 95°F. The simple approach to achieving the right temperature is to use a temperature probe and heating element, and to turn on the heating element when the temperature is too low, and turn it off when it is too high. One issue with this is that heat often takes time to propagate through a space, so you can overshoot the temperature if you turn it off only when the correct temperature is detected. One solution is to use what is called a PID (proportional-integral-derivative) controller. These use an algorithm that estimate what effect on temperature having the heat element on for a given unit of time has, and they constantly self-adjust. For example, it could estimate that having the heating element on for 20 seconds increases the system temperature by one degree. Then when you need to increase the temperature, you know exactly how long to keep the heat on. These are the gold standard for high precision temperature control. For now, I'm going to completely ignore that and go with the simple approach.

For my incubator, I am going to use a raspberry pi pico that is powering a temperature probe, an LCD screen, and a relay that controls the heating element.

