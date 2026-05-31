Title: Pottery Faceter
Date: 2026-05-31
Slug: pottery-faceter
Category: projects
Tags: modeling,3dprinting,ceramics
Summary:          

####Concept
I have been making ceramic teapots at a local makerspace, and I like the look of pottery that has been thrown and then faceted on the sides by dragging a wire through part of the clay wall. You can make a lot of interesting organic shapes doing this freehand, but I wondered if I could make a device that made it possible to make repeated, consistent slices around a piece such that it made an equilateral n-gon of arbitrary n. It would be something that had multiple adjustable pivots that allowed a wire to travel along a track in a repeatable way while rotating around the piece. Some requirements:
    
<ol>
  <li>Mount to the side of a banding wheel, and be able to rotate around it</li>
  <li>Have an adjustable distance to the piece</li>
  <li>Have an adjustable angle and height for the slicing track</li>
</ol>

####Execution
Using Fusion360, I started by making a copy of the banding wheel that I was trying to fit the faceter onto. Then I made a mount with a rounded lip that could sit right on the edge of the wheel. A screw hole in the center would let me attach the next piece.

<img src="{static}/images/slicer_banding.jpg" width="300">

The next piece has a vertical track that lets the slicer track move up and down and also pivot the angle. It attaches to the mount via a horizontal track.

<img src="{static}/images/slicer_pivot.jpg" width="300">

Each side of the vertical track will hold a piece, both of which then create the final track the actual wire will travel through.

<img src="{static}/images/slicer_track.jpg" width="300">

The wire will be strung across a bow-shaped piece that has a handle to make it easier to direct.

<img src="{static}/images/slicer_slicer.jpg" width="300">

Fully assembled, it looks like this:

<img src="{static}/images/slicer_fusion_assembled.jpg" width="300">

I 3D printed it in PLA and this is the result:

<img src="{static}/images/slicer_assembled.jpg" width="300">
