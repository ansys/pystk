ISensorPointing3DModel
======================

.. py:class:: ansys.stk.core.stkobjects.ISensorPointing3DModel

   object
   
   IAgSnPt3DModel Interface for a sensor with pointing along one of the available elements of a 3D model.

.. py:currentmodule:: ISensorPointing3DModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointing3DModel.attach_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointing3DModel.available_elements`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointing3DModel


Property detail
---------------

.. py:property:: attach_name
    :canonical: ansys.stk.core.stkobjects.ISensorPointing3DModel.attach_name
    :type: str

    Name of the element of the 3D model along which the sensor points.

.. py:property:: available_elements
    :canonical: ansys.stk.core.stkobjects.ISensorPointing3DModel.available_elements
    :type: list

    Get the available elements of the 3D model.


