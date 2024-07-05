IVectorGeometryToolAxesCustomScript
===================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript

   object
   
   Customized axes offset with respect to a set of reference Axes.

.. py:currentmodule:: IVectorGeometryToolAxesCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.filename`
              - Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCustomScript.filename
    :type: str

    Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.


