IComponentDirectory
===================

.. py:class:: IComponentDirectory

   object
   
   Manages all components.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_components`
              - Return the specified components.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IComponentDirectory



Method detail
-------------

.. py:method:: get_components(self, eComponent:"COMPONENT") -> "IComponentInfoCollection"

    Return the specified components.

    :Parameters:

    **eComponent** : :obj:`~"COMPONENT"`

    :Returns:

        :obj:`~"IComponentInfoCollection"`

