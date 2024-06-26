IGlobeImageOverlay
==================

.. py:class:: ansys.stk.core.graphics.IGlobeImageOverlay

   object
   
   A globe overlay that shows an image.

.. py:currentmodule:: IGlobeImageOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.translucency`
              - Gets or sets the translucency value for the image. The translucency is between 0 and 1, where 0 is fully opaque and 1 is invisible.
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.use_altitude_based_translucency`
              - Gets or sets whether to use altitude to determine the translucency value for the image or not. If <see langword='false' />, the translucency value is used...
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_lower_translucency`
              - Gets or sets the lower translucency value for the image when use altitude based translucency is set to <see langword='true' />...
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_upper_translucency`
              - Gets or sets the upper translucency value for the image when use altitude based translucency is set to <see langword='true' />...
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_lower_altitude`
              - Gets or sets the lower altitude bound used to calculate translucency for the image when use altitude based translucency is set to <see langword='true' />...
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_upper_altitude`
              - Gets or sets the upper altitude bound used to calculate translucency for the image when use altitude based translucency is set to <see langword='true' />...
            * - :py:attr:`~ansys.stk.core.graphics.IGlobeImageOverlay.more_than_one_image_globe_overlay_supported`
              - Gets whether or not the video card allows for more than one image globe overlay globe image overlay to be added.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGlobeImageOverlay


Property detail
---------------

.. py:property:: translucency
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.translucency
    :type: float

    Gets or sets the translucency value for the image. The translucency is between 0 and 1, where 0 is fully opaque and 1 is invisible.

.. py:property:: use_altitude_based_translucency
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.use_altitude_based_translucency
    :type: bool

    Gets or sets whether to use altitude to determine the translucency value for the image or not. If <see langword='false' />, the translucency value is used...

.. py:property:: altitude_based_translucency_lower_translucency
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_lower_translucency
    :type: float

    Gets or sets the lower translucency value for the image when use altitude based translucency is set to <see langword='true' />...

.. py:property:: altitude_based_translucency_upper_translucency
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_upper_translucency
    :type: float

    Gets or sets the upper translucency value for the image when use altitude based translucency is set to <see langword='true' />...

.. py:property:: altitude_based_translucency_lower_altitude
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_lower_altitude
    :type: float

    Gets or sets the lower altitude bound used to calculate translucency for the image when use altitude based translucency is set to <see langword='true' />...

.. py:property:: altitude_based_translucency_upper_altitude
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.altitude_based_translucency_upper_altitude
    :type: float

    Gets or sets the upper altitude bound used to calculate translucency for the image when use altitude based translucency is set to <see langword='true' />...

.. py:property:: more_than_one_image_globe_overlay_supported
    :canonical: ansys.stk.core.graphics.IGlobeImageOverlay.more_than_one_image_globe_overlay_supported
    :type: bool

    Gets whether or not the video card allows for more than one image globe overlay globe image overlay to be added.


