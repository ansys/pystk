IStereoscopic
=============

.. py:class:: ansys.stk.core.graphics.IStereoscopic

   object
   
   Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

.. py:currentmodule:: IStereoscopic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IStereoscopic.display_mode`
            * - :py:attr:`~ansys.stk.core.graphics.IStereoscopic.projection_mode`
            * - :py:attr:`~ansys.stk.core.graphics.IStereoscopic.projection_distance`
            * - :py:attr:`~ansys.stk.core.graphics.IStereoscopic.eye_separation_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IStereoscopic


Property detail
---------------

.. py:property:: display_mode
    :canonical: ansys.stk.core.graphics.IStereoscopic.display_mode
    :type: STEREOSCOPIC_DISPLAY_MODE

    Gets or sets the stereoscopic display mode for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

.. py:property:: projection_mode
    :canonical: ansys.stk.core.graphics.IStereoscopic.projection_mode
    :type: STEREO_PROJECTION_MODE

    Gets or sets whether the type of stereo projection that will be used.

.. py:property:: projection_distance
    :canonical: ansys.stk.core.graphics.IStereoscopic.projection_distance
    :type: float

    Gets or sets the projection distance. If projection mode is set to eStkGraphicsStereoProjectionAutomatic, the value of this property will be ignored.

.. py:property:: eye_separation_factor
    :canonical: ansys.stk.core.graphics.IStereoscopic.eye_separation_factor
    :type: float

    Gets or sets the eye separation factor.


