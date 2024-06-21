IGraphics3DVaporTrail
=====================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DVaporTrail

   object
   
   Configure the vapor trail 3D attributes.

.. py:currentmodule:: IGraphics3DVaporTrail

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.max_num_of_puffs`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.density`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.radius`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.use_attach_point`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.attach_point_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.image_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.available_attach_points`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DVaporTrail.display_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DVaporTrail


Property detail
---------------

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.visible
    :type: bool

    Controls whether to display the vapor trail in the 3D window.

.. py:property:: max_num_of_puffs
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.max_num_of_puffs
    :type: int

    Maximum number of puffs trailing the vapor source. A higher number represents a longer vapor trail. Dimensionless.

.. py:property:: density
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.density
    :type: float

    Vapor density for a puff. A higher number produces denser looking vapor.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.radius
    :type: float

    True scale size for a puff. Uses Distance Dimension.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.color
    :type: agcolor.Color

    Color of the vapor trail.

.. py:property:: use_attach_point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.use_attach_point
    :type: bool

    If the model file for the object has attach points, use this attribute and the AttachPointName attribute to specify the point where the vapor trail should be attached. Otherwise the vapor trail will be attached to the center of the model.

.. py:property:: attach_point_name
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.attach_point_name
    :type: str

    The name of the point on the object's model where the vapor trail will be attached.

.. py:property:: image_file
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.image_file
    :type: str

    Image file used to display the vapor trail.

.. py:property:: available_attach_points
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.available_attach_points
    :type: list

    Gets a list of available attach points.

.. py:property:: display_interval
    :canonical: ansys.stk.core.stkobjects.IGraphics3DVaporTrail.display_interval
    :type: ITimeToolEventIntervalSmartInterval

    Defines a display interval of the vapor trail in the 3D window.


