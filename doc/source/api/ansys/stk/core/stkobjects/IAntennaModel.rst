IAntennaModel
=============

.. py:class:: IAntennaModel

   object
   
   Provide access to the properties and methods defining an antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`
            * - :py:meth:`~design_frequency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IAntennaModel.name
    :type: str

    Gets the antenna model name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IAntennaModel.type
    :type: ANTENNA_MODEL_TYPE

    Gets the antenna model type enumeration.

.. py:property:: design_frequency
    :canonical: ansys.stk.core.stkobjects.IAntennaModel.design_frequency
    :type: float

    Gets the antenna design frequency.


