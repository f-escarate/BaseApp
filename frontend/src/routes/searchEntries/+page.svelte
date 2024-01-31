<script>
    import Entry from './Entry.svelte';
    const getEntries = async () => {
        const response = await fetch('http://localhost:8000/get_items/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await response.json();
        console.log(data);
        return data;
    }

</script>
<div class='mx-auto w-[75%] my-5 h-full p-4 space-y-4'>
    <h1 class='text-4xl font-bold'>Search Entries</h1>
    {#await getEntries()}
        <p>Fetching data...</p>
    {:then data}
        <ul>
            {#each data as entry}
                <li>
                    <Entry entry_data={entry} />
                </li>
            {/each}
        </ul>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>