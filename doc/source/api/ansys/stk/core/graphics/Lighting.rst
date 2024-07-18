Lighting
========

.. py:class:: ansys.stk.core.graphics.Lighting

   Bases: 

   Lighting in the 3D scene.

.. py:currentmodule:: Lighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.Lighting.enabled`
              - Gets or sets whether or not lighting is enabled.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.ambient_intensity`
              - Gets or sets the ambient intensity throughout the scene.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.diffuse_intensity`
              - Gets or sets the diffuse intensity from the sun.
            * - :py:attr:`~ansys.stk.core.graphics.Lighting.night_lights_intensity`
              - Gets or sets the overall brightness for the night light's image overlay, night overlay.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import Lighting


Property detail
---------------

.. py:property:: enabled
    :canonical: ansys.stk.core.graphics.Lighting.enabled
    :type: bool

    Gets or sets whether or not lighting is enabled.

.. py:property:: ambient_intensity
    :canonical: ansys.stk.core.graphics.Lighting.ambient_intensity
    :type: float

    Gets or sets the ambient intensity throughout the scene.

.. py:property:: diffuse_intensity
    :canonical: ansys.stk.core.graphics.Lighting.diffuse_intensity
    :type: float

    Gets or sets the diffuse intensity from the sun.

.. py:property:: night_lights_intensity
    :canonical: ansys.stk.core.graphics.Lighting.night_lights_intensity
    :type: float

    Gets or sets the overall brightness for the night light's image overlay, night overlay.


