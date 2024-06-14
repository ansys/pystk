IStateCalcDeltaFromMaster
=========================

.. py:class:: IStateCalcDeltaFromMaster

   object
   
   Properties for a Rel Mean Mean Anomaly calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~calc_object_name`
            * - :py:meth:`~reference_selection`
            * - :py:meth:`~reference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcDeltaFromMaster


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaFromMaster.calc_object_name
    :type: str

    Gets or sets the calculation object of interest.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaFromMaster.reference_selection
    :type: "CALC_OBJECT_REFERENCE"

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDeltaFromMaster.reference
    :type: "IAgLinkToObject"

    Get the reference object.


