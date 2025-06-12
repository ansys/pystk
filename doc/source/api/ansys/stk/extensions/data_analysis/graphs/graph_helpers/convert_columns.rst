convert_columns
===============

.. py:function:: convert_columns(dataframe: ~pandas.DataFrame, numerical_column_list: list[str], date_column_list: list[str]) -> ~pandas.DataFrame
    :canonical: ansys.stk.extensions.data_analysis.graphs.graph_helpers.convert_columns

    Convert numerical and time columns in a pandas dataframe.



    :Parameters:

        **dataframe** : :obj:`~pandas.DataFrame`
        The dataframe containing the data.

        **numerical_column_list** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with numerical values.

        **date_column_list** : :obj:`~list` of :obj:`~str`
        The list of dataframe columns with time values.



    :Returns:

        :obj:`~pandas.DataFrame`
        The dataframe with converted columns.


.. py:currentmodule:: convert_columns


Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.graphs.graph_helpers import convert_columns


