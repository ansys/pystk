ComponentDirectory
==================

.. py:class:: ansys.stk.core.stkobjects.ComponentDirectory

   Manages all components.

.. py:currentmodule:: ComponentDirectory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ComponentDirectory.get_components`
              - Return the specified components.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ComponentDirectory



Method detail
-------------

.. py:method:: get_components(self, component: Component) -> ComponentInfoCollection
    :canonical: ansys.stk.core.stkobjects.ComponentDirectory.get_components

    Return the specified components.

    :Parameters:

        **component** : :obj:`~Component`


    :Returns:

        :obj:`~ComponentInfoCollection`

