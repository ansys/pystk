IStateCalcDriftRateFactor
=========================

.. py:class:: IStateCalcDriftRateFactor

   object
   
   Properties for a DriftRateFactor calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~drift_rate_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcDriftRateFactor


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDriftRateFactor.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: drift_rate_model
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDriftRateFactor.drift_rate_model
    :type: GEO_STATIONARY_DRIFT_RATE_MODEL

    Gets or sets the gravity model used to compute drift rate.


