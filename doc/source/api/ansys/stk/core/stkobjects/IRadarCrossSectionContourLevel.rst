IRadarCrossSectionContourLevel
==============================

.. py:class:: ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel

   object
   
   IAgRadarCrossSectionContourLevel Interface for an radar cross section contour level.

.. py:currentmodule:: IRadarCrossSectionContourLevel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.value`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.line_style`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRadarCrossSectionContourLevel


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.value
    :type: float

    Get the contour level value.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.color
    :type: agcolor.Color

    Gets or sets the contour level color.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IRadarCrossSectionContourLevel.line_style
    :type: LINE_STYLE

    Select the line style, displayed for the contour level, from the AgELineStyle enumeration.


