IVisualEffects
==============

.. py:class:: IVisualEffects

   object
   
   Control various post processing effects that can be applied to the scene.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~lens_flare_enabled`
            * - :py:meth:`~vignette_enabled`
            * - :py:meth:`~vignette_strength`


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


