Title: Pottery Faceter
Date: 2026-05-31
Slug: pottery-faceter
Category: projects
Tags: modeling,3dprinting,ceramics
Summary:          

####Concept
I have been making ceramic teapots at a local makerspace, and I like the look of pottery that has been thrown and then faceted on the sides by dragging a wire through part of the clay wall. You can make a lot of interesting organic shapes doing this freehand, but I wondered if I could make a device that allowed repeated, consistent slices around a piece such that it made an equilateral n-gon of arbitrary n. It would have multiple adjustable positioning pivots that then allowed a wire to travel along a track in a repeatable way while rotating around the piece. Some requirements:
    
<ol>
  <li>Can mount to the side of a banding wheel, and be able to rotate around it</li>
  <li>Has an adjustable distance to the piece</li>
  <li>Has an adjustable angle and height for the slicing track</li>
</ol>

####Process
Using Fusion360, I started by making a copy of the banding wheel that I was trying to fit the faceter onto. Then I made a mount with a rounded lip that could sit right on the edge of the wheel. A screw hole in the center would let me attach the next piece.
<br>
<img src="{static}/images/pottery_faceter/slicer_banding.jpg" width="300">

The next piece has a vertical track that lets the slicer track move up and down and also pivot the angle. It attaches to the mount via a horizontal track.
<br>
<img src="{static}/images/pottery_faceter/slicer_pivot.jpg" width="300">

Each side of the vertical track will hold a piece, both of which then create the final track the actual wire will travel through.
<br>
<img src="{static}/images/pottery_faceter/slicer_track.jpg" width="300">

The wire will be strung across a bow-shaped piece that has a handle to make it easier to direct.
<br>
<img src="{static}/images/pottery_faceter/slicer_slicer.jpg" width="300">

Fully assembled, it looks like this:
<br>
<img src="{static}/images/pottery_faceter/slicer_fusion_assembled.jpg" width="300">

All the tracks and slots were designed to fit some small machine screws I bought. I 3D printed it in PLA and this is the result:
<br>
<img src="{static}/images/pottery_faceter/slicer_assembled.jpg" width="300">


I made a 7-sided polygon template to print out and place on the wheel and guide placement.
PICTURE HERE

Here is my first attempt:
<br>
<img src="{static}/images/pottery_faceter/slicer_firstsetup.jpg" width="300">


And the result:
<br>
<img src="{static}/images/pottery_faceter/slicer_firsttry.jpg" width="300">

Pretty good!

After this test, I made two modifications. The first was to shorten the arms of the bow-shaped slicer piece and also increase the infill % when printing it, because the PLA was bending under the tension of the wire. The second was to increase the length of the horizontal track that connects to the mount, because the wire couldn't reach very thin pieces in the center of the wheel.