IVmExternalFile
===============

.. py:class:: ansys.stk.core.stkobjects.IVmExternalFile

   object
   
   IAgVmExternalFile Interface for volume external file.

.. py:currentmodule:: IVmExternalFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmExternalFile.reload`
              - Reload volume external file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVmExternalFile.filename`
              - Path and file name of volume external file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmExternalFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVmExternalFile.filename
    :type: str

    Path and file name of volume external file.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVmExternalFile.reload

    Reload volume external file.

    :Returns:

        :obj:`~None`

