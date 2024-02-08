<script>
    import { onMount } from 'svelte';
    export let entry_data;
    const HOST = 'http://localhost:8000';
    let image;

    onMount(async () => {
        const response = await fetch(`${HOST}/get_image/${entry_data.id}`, {
            method: 'GET',
            headers: {
                'Content-Type': `image/${entry_data.image}`
            }
        });
        image = URL.createObjectURL(await response.blob());
    });
</script>

<div class='m-4 p-8 bg-blue-300 flex justify-between max-h-[300px] md:w-[85%]'>
    <div class='flex flex-col justify-between'>
        <h1 class='text-4xl font-semibold'>{entry_data.title}</h1>
        <p class='m-2'>{entry_data.description}</p>
        <p class="text-xs font-bold">Fecha {entry_data.date}</p>
    </div>
    <img class='w-1/2 object-contain' src={image} alt={entry_data.id} />
</div>