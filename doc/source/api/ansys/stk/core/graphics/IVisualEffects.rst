IVisualEffects
==============

.. py:class:: ansys.stk.core.graphics.IVisualEffects

   object
   
   Control various post processing effects that can be applied to the scene.

.. py:currentmodule:: IVisualEffects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IVisualEffects.lens_flare_enabled`
              - Gets or sets whether or not the lens flare effect is enabled.
            * - :py:attr:`~ansys.stk.core.graphics.IVisualEffects.vignette_enabled`
              - Gets or sets whether or not the vignette effect is enabled. This simulates light being blocked by the lens hood, resulting in a slight darkening at the perimeter of the 3D Window.
            * - :py:attr:`~ansys.stk.core.graphics.IVisualEffects.vignette_strength`
              - Sets the strength of the vignette effect, values between [0.001 and 5.0], with larger values resulting in more pronounced darkening around the perimeter of the 3D window.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IVisualEffects


Property detail
---------------

.. py:property:: lens_flare_enabled
    :canonical: ansys.stk.core.graphics.IVisualEffects.lens_flare_enabled
    :type: bool

    Gets or sets whether or not the lens flare effect is enabled.

.. py:property:: vignette_enabled
    :canonical: ansys.stk.core.graphics.IVisualEffects.vignette_enabled
    :type: bool

    Gets or sets whether or not the vignette effect is enabled. This simulates light being blocked by the lens hood, resulting in a slight darkening at the perimeter of the 3D Window.

.. py:property:: vignette_strength
    :canonical: ansys.stk.core.graphics.IVisualEffects.vignette_strength
    :type: float

    Sets the strength of the vignette effect, values between [0.001 and 5.0], with larger values resulting in more pronounced darkening around the perimeter of the 3D window.


