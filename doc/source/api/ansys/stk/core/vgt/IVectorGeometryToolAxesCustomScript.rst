IVectorGeometryToolAxesCustomScript
===================================

.. py:class:: IVectorGeometryToolAxesCustomScript

   object
   
   Customized axes offset with respect to a set of reference Axes.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_axes`
            * - :py:meth:`~filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.reference_axes
    :type: IAgCrdnAxesRefTo

    Specify a reference axes.

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.filename
    :type: str

    Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.


