.. container::

   .. container:: separator

      |image0|

   This is my son standing under the Flying Speghetti Monster. This is a
   nice photo, but maybe I want to zoom in on just my son. Further,
   maybe I want to do this on the client-side, not on the server-side.

.. container::

.. container::

   There are a number of reasons I might want to do this. The most
   obvious is displaying a thumbnail that expands into the full photo.
   Rather than load two images, we can load a single one, crop the image
   to get the thumbnail, and expand it into the full image when the user
   wants to see it.

.. container::

.. container::

   We might start by looking into the CSS clip property, but we'd run
   into an immediate problem: the result is just floating in dead-space!
   The image will be clipped as we specify, but this only hides the
   clipped areas and leaves the image otherwise in-place.
   A better solution is to take the original layout of the image and
   reposition and resize it and adjust the clip, so that the region we
   specify by the clip property is expanded to fit the full size of the
   space we gave for the image.
   This means we can define a simple thumbnail CSS class, and specify a
   height and width, then by specifying the portion of the image that
   makes up the thumbnail, they'll be generated and adjusted
   automatically. This is what the clipexpand() plugin does.
   You can see an example usage below. You can grab a copy at the github
   `downloads
   page <http://github.com/ironfroggy/phototagger/downloads>`__ for my
   `phototagger <http://github.com/ironfroggy/phototagger/>`__ app,
   which this grew out of.

.. |image0| image:: http://i.imgur.com/9ptco.jpg
   :width: 212px
   :height: 320px
   :target: http://i.imgur.com/9ptco.jpg
