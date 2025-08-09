Graphics3DVaporTrail
====================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DVaporTrail

   Vapor trail attributes.

.. py:currentmodule:: Graphics3DVaporTrail

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.attachment_point_name`
              - The name of the point on the object's model where the vapor trail will be attached.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.available_attachment_points`
              - Get a list of available attach points.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.color`
              - Color of the vapor trail.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.density`
              - Vapor density for a puff. A higher number produces denser looking vapor.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.display_interval`
              - Define a display interval of the vapor trail in the 3D window.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.image_filename`
              - Image file used to display the vapor trail.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.maximum_number_of_puffs`
              - Maximum number of puffs trailing the vapor source. A higher number represents a longer vapor trail. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.radius`
              - True scale size for a puff. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.use_attach_point`
              - If the model file for the object has attach points, use this attribute and the AttachPointName attribute to specify the point where the vapor trail should be attached. Otherwise the vapor trail will be attached to the center of the model.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DVaporTrail.visible`
              - Control whether to display the vapor trail in the 3D window.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DVaporTrail


Property detail
---------------

.. py:property:: attachment_point_name
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.attachment_point_name
    :type: str

    The name of the point on the object's model where the vapor trail will be attached.

.. py:property:: available_attachment_points
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.available_attachment_points
    :type: list

    Get a list of available attach points.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.color
    :type: Color

    Color of the vapor trail.

.. py:property:: density
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.density
    :type: float

    Vapor density for a puff. A higher number produces denser looking vapor.

.. py:property:: display_interval
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.display_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Define a display interval of the vapor trail in the 3D window.

.. py:property:: image_filename
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.image_filename
    :type: str

    Image file used to display the vapor trail.

.. py:property:: maximum_number_of_puffs
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.maximum_number_of_puffs
    :type: int

    Maximum number of puffs trailing the vapor source. A higher number represents a longer vapor trail. Dimensionless.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.radius
    :type: float

    True scale size for a puff. Uses Distance Dimension.

.. py:property:: use_attach_point
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.use_attach_point
    :type: bool

    If the model file for the object has attach points, use this attribute and the AttachPointName attribute to specify the point where the vapor trail should be attached. Otherwise the vapor trail will be attached to the center of the model.

.. py:property:: visible
    :canonical: ansys.stk.core.stkobjects.Graphics3DVaporTrail.visible
    :type: bool

    Control whether to display the vapor trail in the 3D window.


