IAntennaContourLevel
====================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourLevel

   object
   
   IAgAntennaContourLevel Interface for an antenna contour level.

.. py:currentmodule:: IAntennaContourLevel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevel.value`
              - Get the contour level value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevel.color`
              - Gets or sets the contour level color.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourLevel.line_style`
              - Select the line style, displayed for the contour level, from the AgELineStyle enumeration.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourLevel


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevel.value
    :type: float

    Get the contour level value.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevel.color
    :type: agcolor.Color

    Gets or sets the contour level color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IAntennaContourLevel.line_style
    :type: LINE_STYLE

    Select the line style, displayed for the contour level, from the AgELineStyle enumeration.


