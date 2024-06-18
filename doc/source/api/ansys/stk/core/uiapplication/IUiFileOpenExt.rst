IUiFileOpenExt
==============

.. py:class:: IUiFileOpenExt

   object
   
   Access to file open dialog that allows multiple file specifications.

.. py:currentmodule:: ansys.stk.core.uiapplication

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~file_name`
            * - :py:meth:`~filter_description`
            * - :py:meth:`~filter_pattern`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import IUiFileOpenExt


Property detail
---------------

.. py:property:: file_name
    :canonical: ansys.stk.core.uiapplication.IUiFileOpenExt.file_name
    :type: "IAgUiFileOpenExtCollection"

    Gets/sets the multiple file open collection.

.. py:property:: filter_description
    :canonical: ansys.stk.core.uiapplication.IUiFileOpenExt.filter_description
    :type: str

    Gets/sets the file open dialog filter description.

.. py:property:: filter_pattern
    :canonical: ansys.stk.core.uiapplication.IUiFileOpenExt.filter_pattern
    :type: str

    Gets/sets the file open dialog filter pattern.


