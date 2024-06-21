IVehicleGraphics3DBPlaneTemplateDisplayCollection
=================================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection

   object
   
   3D DisplayElements collection for BPlane.

.. py:currentmodule:: IVehicleGraphics3DBPlaneTemplateDisplayCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DBPlaneTemplateDisplayCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleGraphics3DBPlaneTemplateDisplayElement
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DBPlaneTemplateDisplayCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleGraphics3DBPlaneTemplateDisplayElement`


