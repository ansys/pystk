ILLAPosition
============

.. py:class:: ansys.stk.core.stkobjects.ILLAPosition

   Interface to set and retrieve the LLA position type.

.. py:currentmodule:: ILLAPosition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAPosition.convert_to`
              - Change the position representation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAPosition.assign`
              - Assign a new position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAPosition.assign_geocentric`
              - Assign the position using geocentric representation. Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Rad uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAPosition.assign_geodetic`
              - Assign the position using geodetic representation.  Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Alt uses Distance Dimension.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAPosition.type`
              - Returns the position type currently being used.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILLAPosition


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.ILLAPosition.type
    :type: LLA_POSITION_TYPE

    Returns the position type currently being used.


Method detail
-------------

.. py:method:: convert_to(self, type: LLA_POSITION_TYPE) -> ILLAPosition
    :canonical: ansys.stk.core.stkobjects.ILLAPosition.convert_to

    Change the position representation.

    :Parameters:

    **type** : :obj:`~LLA_POSITION_TYPE`

    :Returns:

        :obj:`~ILLAPosition`


.. py:method:: assign(self, pPos: ILLAPosition) -> None
    :canonical: ansys.stk.core.stkobjects.ILLAPosition.assign

    Assign a new position.

    :Parameters:

    **pPos** : :obj:`~ILLAPosition`

    :Returns:

        :obj:`~None`

.. py:method:: assign_geocentric(self, lat: float, lon: float, rad: float) -> None
    :canonical: ansys.stk.core.stkobjects.ILLAPosition.assign_geocentric

    Assign the position using geocentric representation. Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Rad uses Distance Dimension.

    :Parameters:

    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **rad** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_geodetic(self, lat: float, lon: float, alt: float) -> None
    :canonical: ansys.stk.core.stkobjects.ILLAPosition.assign_geodetic

    Assign the position using geodetic representation.  Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Alt uses Distance Dimension.

    :Parameters:

    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

