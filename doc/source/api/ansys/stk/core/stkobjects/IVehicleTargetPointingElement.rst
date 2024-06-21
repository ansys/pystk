IVehicleTargetPointingElement
=============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleTargetPointingElement

   object
   
   Target pointing data for target pointing attitude.

.. py:currentmodule:: IVehicleTargetPointingElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.reset_constrained_vector_reference`
              - Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.target`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.aligned_vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector_reference`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.available_constrained_vectors`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTargetPointingElement.intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTargetPointingElement


Property detail
---------------

.. py:property:: target
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.target
    :type: ILinkToObject

    Get a reference to the targeted object.

.. py:property:: aligned_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.aligned_vector
    :type: IDirection

    Get the aligned vector.

.. py:property:: constrained_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector
    :type: IDirection

    Get the constrained vector.

.. py:property:: constrained_vector_reference
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.constrained_vector_reference
    :type: str

    Gets or sets the reference for the constrained vector.

.. py:property:: available_constrained_vectors
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.available_constrained_vectors
    :type: list

    Returns the available constrained vectors.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.latitude
    :type: float

    Get the LLA position's latitude. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.longitude
    :type: float

    Get the LLA position's longitude. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.altitude
    :type: float

    Get the LLA position's altitude. Uses Distance Dimension.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.intervals
    :type: IVehicleTargetPointingIntervalCollection

    Returns a list of scheduled time intervals for the current target.


Method detail
-------------






.. py:method:: reset_constrained_vector_reference(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleTargetPointingElement.reset_constrained_vector_reference

    Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    :Returns:

        :obj:`~bool`






