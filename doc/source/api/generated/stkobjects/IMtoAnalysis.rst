IMtoAnalysis
============

.. py:class:: IMtoAnalysis

   object
   
   MTO spatial state info.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~range`
            * - :py:meth:`~field_of_view`
            * - :py:meth:`~visibility`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMtoAnalysis


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.position
    :type: "IAgMtoAnalysisPosition"

    Returns a spatial state of the mto at specified time.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.range
    :type: "IAgMtoAnalysisRange"

    Returns the range from an Mto track to another object.

.. py:property:: field_of_view
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.field_of_view
    :type: "IAgMtoAnalysisFieldOfView"

    Returns the field of view from an Mto track to a sensor.

.. py:property:: visibility
    :canonical: ansys.stk.core.stkobjects.IMtoAnalysis.visibility
    :type: "IAgMtoAnalysisVisibility"

    Returns the visibility from an Mto track to another object.


