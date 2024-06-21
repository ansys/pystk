IRFFilterModel
==============

.. py:class:: ansys.stk.core.stkobjects.IRFFilterModel

   object
   
   Provide access to the properties and methods defining an RF filter model.

.. py:currentmodule:: IRFFilterModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.upper_bandwidth_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.lower_bandwidth_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.bandwidth`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRFFilterModel.insertion_loss`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRFFilterModel


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.name
    :type: str

    Gets the filter model name.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.type
    :type: RF_FILTER_MODEL_TYPE

    Gets the filter model type enumeration.

.. py:property:: upper_bandwidth_limit
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.upper_bandwidth_limit
    :type: float

    Gets or sets the upper bandwidth limit.

.. py:property:: lower_bandwidth_limit
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.lower_bandwidth_limit
    :type: float

    Gets or sets the lower bandwidth limit.

.. py:property:: bandwidth
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.bandwidth
    :type: float

    Gets the filter bandwidth.

.. py:property:: insertion_loss
    :canonical: ansys.stk.core.stkobjects.IRFFilterModel.insertion_loss
    :type: float

    Gets or sets the insertion loss.


