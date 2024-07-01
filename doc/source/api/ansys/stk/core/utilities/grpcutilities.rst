The ``grpcutilities`` module
============================

.. py:module:: ansys.stk.core.utilities.grpcutilities

Summary
-------

.. tab-set::

    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:class:`~GrpcCallBatcher`
              - A class used to batch together API calls to optimize performance.



Description
-----------

Optimize performance of gRPC communications.

GrpcCallBatcher may be used to reduce the number of remote communications
by batching together API commands that do not require return values.

.. py:currentmodule:: ansys.stk.core.utilities.grpcutilities

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     GrpcCallBatcher<grpcutilities/GrpcCallBatcher>


