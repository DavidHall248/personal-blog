Title: Tempeh Forever: Prologue
Date: 2024-07-01
Slug: tempeh-forever-1
Category: projects
Tags: raspberrypi,fermentation
Summary: Recently I have been thinking...

####Background

Recently, I have been thinking about the ecological and economic impact of getting our protein needs met from meat. I have personally landed in many places on the meat-eater to vegan spectrum at different times. Currently, I land about here: my issue with meat-eating is that animals do not actually produce protein, they just rearrange protein from the food they eat and form it into their own muscles and organs. The process of creating protein from nitrogen is performed by plants and bacteria. Then animals are not very efficient about generating meat from the protein they ingest. For example, a chicken will only turn about 60% of the protein it eats into protein available in its own body. From a resource flow perspective, we could just eat soybeans directly, and the intermediate step of having to pass protein from a soybean through an animal before we eat it seems arbitrary and wasteful. But we do it because we like the taste of meat and though often that is enough reason for me to justify the disasters of animal agriculture, sometimes it isn't.

####Beans

My doctor told me recently that I probably wasn't eating enough fiber, and recommended that I eat more beans. Beans are cheap, high in fiber, and also a good source of protein. Members of the bean family, Fabaceae, have a special structure on their roots called a root nodule that houses species of bacteria that can sequester nitrogen, the building block of protein. In many ways beans are the perfect food.

But as much as I love a plate of rice and beans, if I am in any kind of a hurry it becomes much harder to get beans into my body. Where are the convenient bean snacks? Beans have been transformed into many shapes and textures. In Japan alone, beans are boiled into soymilk, curdled into tofu, fermented into natto, and aged into miso and soy sauce. But none of these really help me in my quest to get more beans into my body conveniently.

####Tempeh

Tempeh is an Indonesian bean preparation where beans are partially cooked and then inoculated with spores of a species of mold called Rhizopus oligosporus. Over the course of several days, the mold fills the gaps between the soybeans and you are left with solid cubes. The tempeh can then be sauteed or fried, and then used in dishes as an approximate meat replacement. I am curious about relying more on tempeh as a source of protein in my own diet, but in general it is still treated as an exotic curiosity in the US. A half-pound of tempeh at my local grocery store is $5, putting it on par with if not above the cost per gram of protein as meat. If I want cheap tempeh, I guess I will have to make it myself!!

####Tempeh Forever

I conceived of this project as a somewhat manic solution to multiple goals at once. I am interested food fermentation, data analysis, and low-cost embedded systems. I imagined a system that would produce tempeh in a relatively procedural and predictable way, and then give me a dataset that explained the progress. Here are the steps:
1. A tempeh incubator with a temperature control device that would toggle a heating element to maintain the correct temperature. Data regarding the toggling of the element and also ongoing temperature/humidity information would flow to...
2. An MQTT broker that accepts information from the control device and uploads it to...
3. An online SQL server for storage, which can then be queried with...
4. A Python visualization.

Great!
