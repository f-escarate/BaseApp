<script>
    import Entry from '../../components/Entry.svelte';
    import { Button } from 'flowbite-svelte'
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

<div class='flex flex-col'>
    {#if entries.length > 0}
        <h1 class='text-4xl font-bold'>Your Entries</h1>
        {#each entries as entry}
            <Entry entry_data={entry} />
            <Button class='md:col-span-2 w-[50%] mx-auto h-full' color="blue" href={`/editEntry/${entry.id}/`}>Edit entry</Button>
        {/each}
    {:else}
        <h1 class='text-4xl font-bold'>No entry found :c</h1>
    {/if}
</div>