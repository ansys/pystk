IDataProviderElement
====================

.. py:class:: IDataProviderElement

   object
   
   Provide methods to access the information about the element (for instance ``x``).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`
            * - :py:meth:`~dimension_name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderElement


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IDataProviderElement.name
    :type: str

    Returns a name of the element.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IDataProviderElement.type
    :type: "DATA_PROVIDER_ELEMENT_TYPE"

    Returns a type of the element.

.. py:property:: dimension_name
    :canonical: ansys.stk.core.stkobjects.IDataProviderElement.dimension_name
    :type: str

    Returns the dimension of the element.


