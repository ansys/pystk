ILighting
=========

.. py:class:: ILighting

   object
   
   Lighting in the 3D scene.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enabled`
            * - :py:meth:`~ambient_intensity`
            * - :py:meth:`~diffuse_intensity`
            * - :py:meth:`~night_lights_intensity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ILighting


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.graphics.ILighting.enabled
    :type: bool

    Gets or sets whether or not lighting is enabled.

.. py:property:: ambient_intensity
    :canonical: ansys.stk.core.graphics.ILighting.ambient_intensity
    :type: float

    Gets or sets the ambient intensity throughout the scene.

.. py:property:: diffuse_intensity
    :canonical: ansys.stk.core.graphics.ILighting.diffuse_intensity
    :type: float

    Gets or sets the diffuse intensity from the sun.

.. py:property:: night_lights_intensity
    :canonical: ansys.stk.core.graphics.ILighting.night_lights_intensity
    :type: float

    Gets or sets the overall brightness for the night light's image overlay, night overlay.


