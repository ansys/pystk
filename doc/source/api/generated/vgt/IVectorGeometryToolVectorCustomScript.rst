IVectorGeometryToolVectorCustomScript
=====================================

.. py:class:: IVectorGeometryToolVectorCustomScript

   object
   
   Customized vector components defined with respect to reference axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_axes`
            * - :py:meth:`~script_file`
            * - :py:meth:`~initialization_script_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCustomScript.reference_axes
    :type: "IAgCrdnAxesRefTo"

    Specify a reference axes.

.. py:property:: script_file
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCustomScript.script_file
    :type: str

    Specify a script file.

.. py:property:: initialization_script_file
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorCustomScript.initialization_script_file
    :type: str

    Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.


