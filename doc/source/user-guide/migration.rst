Migrate to PySTK
################

This topic provides details on migrating your code to PySTK.

.. raw:: html

    <div class="migration-search-bar">
        <input id="migration-search-bar" type="text" placeholder="Search...">
    </div>


.. rst-class:: migration-table

.. include:: ../_static/migration-tables/agi.stk12.graphics.rst


.. raw:: html

    <script>
        // Select the search bar
        const searchBar = document.getElementById('migration-search-bar');
        const table = document.getElementsByClassName('migration-table')[0]; // Fix for getElementsByClassName
        if (table) {
            const tbody = table.querySelector('tbody'); // Ensure tbody exists before accessing
    
            // Add an event listener to handle input
            searchBar.addEventListener('input', () => {
                const query = searchBar.value.trim().toLowerCase();
                console.log(query);
    
                if (tbody) {
                    const rows = tbody.getElementsByTagName('tr'); // Fix for getElementsByTagName
    
                    for (let row of rows) {
                        const cells = row.getElementsByTagName('td'); // Fix for getElementsByTagName
                        let match = false;
    
                        for (let cell of cells) {
                            if (cell.textContent.toLowerCase().includes(query)) {
                                match = true;
                                break;
                            }
                        }
    
                        row.style.display = match ? '' : 'none';
                    }
                }
            });
        }
    </script>
