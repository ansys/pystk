MaximumCountPathPrimitiveUpdatePolicyFactory
============================================

.. py:class:: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory

   path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

.. py:currentmodule:: MaximumCountPathPrimitiveUpdatePolicyFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory.initialize`
              - Construct a default update policy. This is equivalent to constructing a policy with maximum count set to 0 and a remove location of Front.
            * - :py:attr:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory.initialize_with_parameters`
              - Initialize a policy with the specified maximumCount and removeLocation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MaximumCountPathPrimitiveUpdatePolicyFactory



Method detail
-------------

.. py:method:: initialize(self) -> MaximumCountPathPrimitiveUpdatePolicy
    :canonical: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory.initialize

    Construct a default update policy. This is equivalent to constructing a policy with maximum count set to 0 and a remove location of Front.

    :Returns:

        :obj:`~MaximumCountPathPrimitiveUpdatePolicy`

.. py:method:: initialize_with_parameters(self, maximum_count: int, remove_location: PATH_PRIMITIVE_REMOVE_LOCATION) -> MaximumCountPathPrimitiveUpdatePolicy
    :canonical: ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory.initialize_with_parameters

    Initialize a policy with the specified maximumCount and removeLocation.

    :Parameters:

    **maximum_count** : :obj:`~int`
    **remove_location** : :obj:`~PATH_PRIMITIVE_REMOVE_LOCATION`

    :Returns:

        :obj:`~MaximumCountPathPrimitiveUpdatePolicy`

