IAnalysisWorkbenchContext
=========================

.. py:class:: ansys.stk.core.vgt.IAnalysisWorkbenchContext

   object
   
   The interface represents a context associated with a VGT component. All VGT components are associated with a valid context. A context can represent a VGT instance or a VGT template.

.. py:currentmodule:: IAnalysisWorkbenchContext

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchContext.is_template`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchContext


Property detail
---------------

.. py:property:: is_template
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchContext.is_template
    :type: bool

    Returns whether the current instance is a VGT template.


