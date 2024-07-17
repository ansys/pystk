AreaTypeEllipse
===============

.. py:class:: ansys.stk.core.stkobjects.AreaTypeEllipse

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAreaTypeData`

   Class defining the AreaTarget AreaType in terms of MajorAxis, MinorAxis and Bearing.

.. py:currentmodule:: AreaTypeEllipse

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypeEllipse.semi_major_axis`
              - Semimajor axis, i.e. half the length of the ellipse's long axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypeEllipse.semi_minor_axis`
              - Semiminor axis, i.e. half the length of the ellipse's short axis. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AreaTypeEllipse.bearing`
              - The angle, measured in an easterly direction, between the major axis of the ellipse and the local North direction. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AreaTypeEllipse


Property detail
---------------

.. py:property:: semi_major_axis
    :canonical: ansys.stk.core.stkobjects.AreaTypeEllipse.semi_major_axis
    :type: float

    Semimajor axis, i.e. half the length of the ellipse's long axis. Uses Distance Dimension.

.. py:property:: semi_minor_axis
    :canonical: ansys.stk.core.stkobjects.AreaTypeEllipse.semi_minor_axis
    :type: float

    Semiminor axis, i.e. half the length of the ellipse's short axis. Uses Distance Dimension.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.AreaTypeEllipse.bearing
    :type: typing.Any

    The angle, measured in an easterly direction, between the major axis of the ellipse and the local North direction. Uses Angle Dimension.


