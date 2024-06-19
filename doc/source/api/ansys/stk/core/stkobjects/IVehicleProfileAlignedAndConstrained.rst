IVehicleProfileAlignedAndConstrained
====================================

.. py:class:: IVehicleProfileAlignedAndConstrained

   IVehicleAttitudeProfile
   
   Aligned and Constrained attitude profile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aligned_vector`
            * - :py:meth:`~constrained_vector`
            * - :py:meth:`~displayed_aligned_vector_type`
            * - :py:meth:`~displayed_constrained_vector_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleProfileAlignedAndConstrained


Property detail
---------------

.. py:property:: aligned_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileAlignedAndConstrained.aligned_vector
    :type: IAgVeVector

    Get the aligned vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.

.. py:property:: constrained_vector
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileAlignedAndConstrained.constrained_vector
    :type: IAgVeVector

    Get the constrained vector pair. Vectors dependent on the satellite's body axes are invalid for this attitude profile; all other vectors are valid choices.

.. py:property:: displayed_aligned_vector_type
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileAlignedAndConstrained.displayed_aligned_vector_type
    :type: DIRECTION_TYPE

    Aligned vector type displayed on GUI.

.. py:property:: displayed_constrained_vector_type
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileAlignedAndConstrained.displayed_constrained_vector_type
    :type: DIRECTION_TYPE

    Constrained vector type displayed on GUI.


