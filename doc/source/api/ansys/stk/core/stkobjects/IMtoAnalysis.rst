IMtoAnalysis
============

.. py:class:: ansys.stk.core.stkobjects.IMtoAnalysis

   object
   
   MTO spatial state info.

.. py:currentmodule:: IMtoAnalysis

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysis.position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysis.range`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysis.field_of_view`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMtoAnalysis.visibility`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoAnalysis


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.position
    :type: IMtoAnalysisPosition

    Returns a spatial state of the mto at specified time.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.range
    :type: IMtoAnalysisRange

    Returns the range from an Mto track to another object.

.. py:property:: field_of_view
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.field_of_view
    :type: IMtoAnalysisFieldOfView

    Returns the field of view from an Mto track to a sensor.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.visibility
    :type: IMtoAnalysisVisibility

    Returns the visibility from an Mto track to another object.


