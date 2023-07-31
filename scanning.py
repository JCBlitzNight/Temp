<!DOCTYPE html>
<html>
    <!-- Your head content here -->
    <body class="bg-gray-100 text-gray-900 px-4 py-8">
        <div class="container mx-auto" x-data="getUsers()">
            <input
                x-ref="searchInput"
                x-model="search"
                x-on:keydown.window.prevent.slash="$refs.searchInput.focus()"
                placeholder="Search for an IP address..."
                type="search"
                class="block w-full rounded bg-gray-200 p-4 mb-4"
            />
            <table x-show="searchResult" class="table-auto border-collapse w-full">
                <thead>
                    <tr>
                        <th class="px-4 py-2 bg-gray-200 text-left">IP Address</th>
                        <th class="px-4 py-2 bg-gray-200 text-left">Country</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border px-4 py-2" x-text="searchResult.ip"></td>
                        <td class="border px-4 py-2" x-text="searchResult.country"></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <script>
            function getUsers() {
                return {
                    search: '',
                    searchResult: null,
                    async findUser() {
                        if (this.search === '') {
                            this.searchResult = null;
                            return;
                        }

                        try {
                            const response = await fetch('data.json'); // Replace 'data.json' with the actual file path
                            if (!response.ok) {
                                throw new Error('Failed to fetch data.');
                            }
                            const data = await response.json();
                            const result = data.find((entry) => entry.ip === this.search);

                            this.searchResult = result || null;
                        } catch (error) {
                            console.error(error);
                        }
                    },
                };
            }
        </script>
    </body>
</html>
