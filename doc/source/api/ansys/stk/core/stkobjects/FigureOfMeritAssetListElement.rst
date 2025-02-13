FigureOfMeritAssetListElement
=============================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritAssetListElement

   Asset list item (for Navigation Accuracy FOM).

.. py:currentmodule:: FigureOfMeritAssetListElement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.method_type`
              - Type of method used to specify range uncertainty.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.method`
              - Range uncertainty method.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.asset`
              - Asset used in specifying range uncertainty.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritAssetListElement


Property detail
---------------

.. py:property:: method_type
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.method_type
    :type: FigureOfMeritNavigationAccuracyMethod

    Type of method used to specify range uncertainty.

.. py:property:: method
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.method
    :type: IFigureOfMeritNavigationAccuracyMethod

    Range uncertainty method.

.. py:property:: asset
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritAssetListElement.asset
    :type: str

    Asset used in specifying range uncertainty.


