<script>
    import Entry from '../../components/Entry.svelte';
    import { onMount } from 'svelte';
    import { HOST } from '$lib/constants';
    import Cookies from 'js-cookie';
    let entries = [];

    onMount(async () => {
        const response = await fetch(`${HOST}/get_items/own/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${Cookies.get('token')}`
            }
        });
        entries = await response.json();
        
    });

</script>
<div class='mx-auto w-[75%] my-5 h-full p-4 space-y-4'>
    <div class='flex flex-col'>
        {#if entries.length > 0}
            <h1 class='text-4xl font-bold'>Your Entries</h1>
            {#each entries as entry}
                <Entry entry_data={entry} />
            {/each}
        {:else}
            <h1 class='text-4xl font-bold'>No entry found :c</h1>
        {/if}
    </div>
</div>