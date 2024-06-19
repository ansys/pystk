IFigureOfMeritUncertainties
===========================

.. py:class:: IFigureOfMeritUncertainties

   object
   
   Receiver range uncertainty (for Navigation Accuracy FOM).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~receiver_range`
            * - :py:meth:`~asset_list`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritUncertainties


Property detail
---------------

.. py:property:: receiver_range
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritUncertainties.receiver_range
    :type: float

    Receiver range uncertainty value.

.. py:property:: asset_list
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritUncertainties.asset_list
    :type: IAgFmAssetListCollection

    Get list of assets for specifying range uncertainty.


