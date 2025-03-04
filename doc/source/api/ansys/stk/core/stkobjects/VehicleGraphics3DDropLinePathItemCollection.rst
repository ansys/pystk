VehicleGraphics3DDropLinePathItemCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection

   Collection of drop lines from the vehicle's orbit or trajectory.

.. py:currentmodule:: VehicleGraphics3DDropLinePathItemCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Examples
--------

Display drop lines in 3D Window

.. code-block:: python

    # Satellite satellite: Satellite object
    orbitDroplines = satellite.graphics_3d.drop_lines.orbit
    wgs84 = orbitDroplines.item(0)  # Droplines to WGS84 surface
    wgs84.show_graphics = True
    wgs84.line_width = LineWidth.WIDTH2
    wgs84.use_2d_color = False
    wgs84.color = Colors.Red


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DDropLinePathItemCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGraphics3DDropLinePathItem
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DDropLinePathItemCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGraphics3DDropLinePathItem`


