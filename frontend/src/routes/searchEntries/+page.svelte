<script>
    import Entry from '../../components/Entry.svelte';
    import { onMount } from 'svelte';
    import { HOST } from '$lib/constants';
    let entries = [];

    onMount(async () => {
        const response = await fetch(`${HOST}/get_items/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        entries = await response.json();
        
    });

</script>

<h1 class='text-4xl font-bold'>Search Entries</h1>
<div class='flex flex-col'>
    {#each entries as entry}
        <Entry entry_data={entry} />
    {/each}
</div>
