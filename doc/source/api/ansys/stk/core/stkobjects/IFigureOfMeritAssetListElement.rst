IFigureOfMeritAssetListElement
==============================

.. py:class:: IFigureOfMeritAssetListElement

   object
   
   Asset list item (for Navigation Accuracy FOM).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~method_type`
            * - :py:meth:`~method`
            * - :py:meth:`~asset`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritAssetListElement


Property detail
---------------

.. py:property:: method_type
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritAssetListElement.method_type
    :type: FIGURE_OF_MERIT_NAVIGATION_ACCURACY_METHOD_TYPE

    Type of method used to specify range uncertainty.

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritAssetListElement.method
    :type: IAgFmNAMethod

    Range uncertainty method.

.. py:property:: asset
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritAssetListElement.asset
    :type: str

    Asset used in specifying range uncertainty.


