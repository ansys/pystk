IDurationPathPrimitiveUpdatePolicyFactory
=========================================

.. py:class:: IDurationPathPrimitiveUpdatePolicyFactory

   object
   
   path primitive update policy that removes points from remove location after a given duration.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Construct a default update policy. This is equivalent to constructing a policy with duration set to 0 and a remove location of Front.
            * - :py:meth:`~initialize_with_parameters`
              - Initialize a policy with the specified duration and removeLocation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDurationPathPrimitiveUpdatePolicyFactory



Method detail
-------------

.. py:method:: initialize(self) -> IDurationPathPrimitiveUpdatePolicy
    :canonical: ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicyFactory.initialize

    Construct a default update policy. This is equivalent to constructing a policy with duration set to 0 and a remove location of Front.

    :Returns:

        :obj:`~IDurationPathPrimitiveUpdatePolicy`

.. py:method:: initialize_with_parameters(self, duration: float, removeLocation: PATH_PRIMITIVE_REMOVE_LOCATION) -> IDurationPathPrimitiveUpdatePolicy
    :canonical: ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicyFactory.initialize_with_parameters

    Initialize a policy with the specified duration and removeLocation.

    :Parameters:

    **duration** : :obj:`~float`
    **removeLocation** : :obj:`~PATH_PRIMITIVE_REMOVE_LOCATION`

    :Returns:

        :obj:`~IDurationPathPrimitiveUpdatePolicy`

