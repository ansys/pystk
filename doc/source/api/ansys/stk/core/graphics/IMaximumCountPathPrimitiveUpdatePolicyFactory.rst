IMaximumCountPathPrimitiveUpdatePolicyFactory
=============================================

.. py:class:: IMaximumCountPathPrimitiveUpdatePolicyFactory

   object
   
   path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Construct a default update policy. This is equivalent to constructing a policy with maximum count set to 0 and a remove location of Front.
            * - :py:meth:`~initialize_with_parameters`
              - Initialize a policy with the specified maximumCount and removeLocation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IMaximumCountPathPrimitiveUpdatePolicyFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IMaximumCountPathPrimitiveUpdatePolicy"

    Construct a default update policy. This is equivalent to constructing a policy with maximum count set to 0 and a remove location of Front.

    :Returns:

        :obj:`~"IMaximumCountPathPrimitiveUpdatePolicy"`

.. py:method:: initialize_with_parameters(self, maximumCount:int, removeLocation:"PATH_PRIMITIVE_REMOVE_LOCATION") -> "IMaximumCountPathPrimitiveUpdatePolicy"

    Initialize a policy with the specified maximumCount and removeLocation.

    :Parameters:

    **maximumCount** : :obj:`~int`
    **removeLocation** : :obj:`~"PATH_PRIMITIVE_REMOVE_LOCATION"`

    :Returns:

        :obj:`~"IMaximumCountPathPrimitiveUpdatePolicy"`

