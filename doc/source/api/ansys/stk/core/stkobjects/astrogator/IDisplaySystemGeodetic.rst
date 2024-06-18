IDisplaySystemGeodetic
======================

.. py:class:: IDisplaySystemGeodetic

   IDisplaySystem
   
   Properties for a geodetic launch coordinate system.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~latitude`
            * - :py:meth:`~longitude`
            * - :py:meth:`~altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDisplaySystemGeodetic


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeodetic.latitude
    :type: typing.Any

    Gets or sets the latitude of the launch location. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeodetic.longitude
    :type: typing.Any

    Gets or sets the longitude of the launch location. Uses Angle Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeodetic.altitude
    :type: float

    Gets or sets the altitude of the launch location. Uses Distance Dimension.


