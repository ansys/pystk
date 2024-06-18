IDisplaySystemGeocentric
========================

.. py:class:: IDisplaySystemGeocentric

   IDisplaySystem
   
   Properties for a geocentric launch coordinate system.

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
            * - :py:meth:`~radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IDisplaySystemGeocentric


Property detail
---------------

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeocentric.latitude
    :type: typing.Any

    Gets or sets the latitude of the launch location. Uses Angle Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeocentric.longitude
    :type: typing.Any

    Gets or sets the longitude of the launch location. Uses Angle Dimension.

.. py:property:: radius
    :canonical: ansys.stk.core.stkobjects.astrogator.IDisplaySystemGeocentric.radius
    :type: float

    Gets or sets the radius of the launch location. Uses Distance Dimension.


